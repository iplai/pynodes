from bpy.types import Node, NodeFrame, NodeTree, NodeLink, ShaderNodeFloatCurve

from .dimensions import NODE_DIMS

frames = {}


def init_frames(btree: NodeTree):
    global frames
    frames.clear()
    for node in btree.nodes:
        if is_frame(node):
            frame = node
            frames[node.name] = {
                "nodes": [node for node in btree.nodes if node.parent == frame],
                "in_nodes": get_frame_in_nodes(btree, frame),
                "out_nodes": get_frame_out_nodes(btree, frame),
                "all_nodes": get_frame_all_nodes(btree, frame),
            }


def group_dim(node: Node):
    """Custom group dimensions"""

    w = 140
    h = 32 + 22 * len(node.outputs)

    if node.bl_idname in ["GeometryNodeGroup", "ShaderNodeGroup"]:
        h += 30

    if node.bl_idname in ["ShaderNodeScript"]:
        w = node.width
        h += 60

    if node.inputs:
        for input in node.inputs:
            h += 22
            if input.bl_idname[:16] == "NodeSocketVector" and not bool(input.links) and not input.hide_value:
                h += 60

    return [w, h]


def node_dim(node: Node):
    if node.bl_idname in ["GeometryNodeGroup", "ShaderNodeGroup", "NodeGroupInput", "NodeGroupOutput", "ShaderNodeScript"]:
        return group_dim(node)

    info: dict = NODE_DIMS.get(node.bl_idname)

    nd: list[int] = list(info["dimensions"])

    params_enum: dict[str, tuple[str]] = info.get("params_enum")

    if params_enum is not None:
        indexes = []
        for param_name, param_values in params_enum.items():
            value = getattr(node, param_name)
            indexes.append(param_values.index(value))
        dimension_key = f"dimensions_{'_'.join(str(i) for i in indexes)}"
        if dimension_key in info:
            nd: list[int] = list(info[dimension_key])

    if not node.bl_idname in ["NodeReroute"]:
        for sock in node.inputs:
            if sock.enabled and (not sock.hide_value) and bool(sock.links) and sock.bl_idname[:16] == "NodeSocketVector":
                nd[1] -= 60

    h = nd[1]

    if node.bl_idname == "ShaderNodeTexImage":
        h = 277

    if node.bl_idname == "ShaderNodeFloatCurve":
        float_curve: ShaderNodeFloatCurve = node
        curve = float_curve.mapping.curves[0]
        for point in curve.points:
            if point.select:
                h += 25
                break

    return [nd[0], h]


class Column:
    def __init__(self):
        self.nodes: list[Node] = []
        self.height = 0


def is_linked_to(a: Node | NodeFrame, b: Node | NodeFrame):
    global frames
    from_nodes: list[Node] = []
    to_nodes: list[Node] = []
    if is_frame(a):
        out_nodes = frames[a.name]['out_nodes']
        if not out_nodes:
            out_nodes = frames[a.name]['all_nodes']
        from_nodes.extend(out_nodes)
    else:
        from_nodes.append(a)
    if is_frame(b):
        to_nodes.extend(frames[b.name]['all_nodes'])
    else:
        to_nodes.append(b)
    for node in from_nodes:
        for output in node.outputs:
            link: NodeLink
            for link in output.links:
                if link.to_node in to_nodes:
                    return True
    return False


def is_linked_to_col(node: Node, col: Column):
    return any(is_linked_to(node, i) for i in col.nodes)


def is_in_frame(node: Node, frame: NodeFrame):
    nd = node
    for _ in range(10):
        if nd.parent is None:
            return False
        if nd.parent == frame:
            return True
        nd = nd.parent
    return False


def is_frame(node: Node):
    return node.bl_idname == "NodeFrame"


def is_frame_out_node(node: Node, frame: NodeFrame):
    if is_frame(node):
        return False
    for output in node.outputs:
        link: NodeLink
        for link in output.links:
            if link.to_node.parent == frame:
                return False
    return True


def get_frame_out_nodes(btree: NodeTree, frame: NodeFrame):
    nodes: list[Node] = []
    for node in btree.nodes:
        if not node.parent == frame:
            continue
        if is_frame_out_node(node, frame):
            nodes.append(node)
    return nodes


def is_frame_in_node(node: Node, frame: NodeFrame):
    if is_frame(node):
        return False
    for input in node.inputs:
        link: NodeLink
        for link in input.links:
            if link.from_node.parent == frame:
                return False
    return True


def get_frame_in_nodes(btree: NodeTree, frame: NodeFrame):
    nodes: list[Node] = []
    for node in btree.nodes:
        if not node.parent == frame:
            continue
        if is_frame_in_node(node, frame):
            nodes.append(node)
    return nodes


def get_frame_all_nodes(btree: NodeTree, frame: NodeFrame):
    nodes: list[Node] = []
    for node in btree.nodes:
        if not is_frame(node) and is_in_frame(node, frame):
            nodes.append(node)
    return nodes


def has_output_link(node: Node):
    global frames
    if is_frame(node):
        return any(has_output_link(node) for node in frames[node.name]['out_nodes'])
    for output in node.outputs:
        if output.is_linked:
            return True
    return False


def build_cols(nodes: list[Node], parent: NodeFrame = None):
    global frames
    cols = [Column()]
    nodes_remain: list[Node] = []
    if parent is None:
        for node in nodes:
            if not has_output_link(node):
                cols[0].nodes.append(node)
            else:
                nodes_remain.append(node)
    else:
        for node in nodes:
            if node in frames[parent.name]['out_nodes']:
                cols[0].nodes.append(node)
            else:
                nodes_remain.append(node)

    def new_column():
        new_col = Column()
        for node in nodes_remain.copy():
            if is_linked_to_col(node, cols[-1]):
                new_node = node
                nodes_remain.remove(new_node)
                new_col.nodes.append(new_node)
                for col in cols:
                    for old_node in col.nodes.copy():
                        if is_linked_to(old_node, new_node):
                            col.nodes.remove(old_node)
                            nodes_remain.append(old_node)
        for node in new_col.nodes.copy():
            if is_linked_to_col(node, new_col):
                nodes_remain.append(node)
                new_col.nodes.remove(node)
        if new_col.nodes:
            return new_col
        else:
            return None
    while (col := new_column()) is not None:
        cols.append(col)
    return cols


def arrange_frame(btree: NodeTree, frame: NodeFrame):
    global frames
    cols = build_cols(frames[frame.name]["nodes"], parent=frame)
    sepx, sepy = 60, 30
    dx = 0
    frame_height = 0
    max_frame_count = 0
    for i, col in enumerate(cols):
        frame_count = 0
        dy = -20
        max_width = 0
        for j, node in enumerate(col.nodes):
            if is_frame(node):
                w, h, c = arrange_frame(btree, node)
                frame_count += 1
                node.location = (dx - 30, dy)
            else:
                w, h = node_dim(node)
                node.location = (dx - w, dy)
            if w > max_width:
                max_width = w
            dy -= h
            dy -= sepy
        col.height = -dy
        dx -= max_width
        dx -= sepx
        if -dy > frame_height:
            frame_height = -dy
        if frame_count > max_frame_count:
            max_frame_count = frame_count
    max_col_height = max(col.height for col in cols)
    for i, col in enumerate(cols):
        for j, node in enumerate(col.nodes):
            x, y = node.location
            node.location = (x, y - (max_col_height - col.height) / 2)
    return -dx, frame_height + 10 * max_frame_count, max_frame_count


def arrange(btree: NodeTree, **kwargs):
    """Arrange a tree"""
    init_frames(btree)
    cols = build_cols([node for node in btree.nodes if node.parent is None])
    sepx, sepy = 60, 30
    dx = 0
    for i, col in enumerate(cols):
        dy = 0
        max_width = 0
        for j, node in enumerate(col.nodes):
            if is_frame(node):
                w, h, c = arrange_frame(btree, node)
                node.location = (dx - 30, dy - c * 15)
                # node.label = f"{node.label} {i} {j}"
            else:
                w, h = node_dim(node)
                node.location = (dx - w, dy)
                # node.label = f"{node.name.split('.')[0]} {i} {j}"
            if w > max_width:
                max_width = w
            dy -= h
            dy -= sepy
        col.height = -dy
        dx -= max_width
        dx -= sepx
    max_col_height = max(col.height for col in cols)
    for i, col in enumerate(cols):
        for j, node in enumerate(col.nodes):
            x, y = node.location
            node.location = (x, y - (max_col_height - col.height) / 2)
