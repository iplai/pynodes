import bpy, collections, itertools, json
from bpy.types import Node, NodeFrame, NodeLink, NodeSocket, Context, NodeTree, Panel, Operator


def get_active_tree(context: Context) -> NodeTree | None:
    tree = context.space_data.node_tree
    if tree is None:
        return
    if tree.nodes.active is not None:
        while tree.nodes.active != context.active_node:
            tree = tree.nodes.active.node_tree
    return tree


def get_group_output_node(tree: NodeTree):
    for node in tree.nodes:
        node: bpy.types.NodeGroupOutput
        if node.bl_idname == 'NodeGroupOutput' and node.is_active_output == True:
            return node


class PYNODES_PT_MAIN(Panel):
    bl_label = "Pynodes"
    bl_space_type = "NODE_EDITOR"
    bl_region_type = "UI"
    bl_category = "Pynodes"

    def draw(self, context):

        layout = self.layout
        layout.row().operator('node.pynodes_arrange')

        row = layout.row()
        row.label(text="Node Margin")
        row.prop(context.scene, 'nodemargin_x', text="X")
        row.prop(context.scene, 'nodemargin_y', text="Y")

        row = layout.row()
        row.label(text="Frame Margin")
        row.prop(context.scene, 'framemargin_x', text="X")
        row.prop(context.scene, 'framemargin_y', text="Y")

        # get current active tree
        btree = get_active_tree(context)
        if btree is None:
            return

        node = btree.nodes.active
        if node is not None and node.select:
            # layout.row().label(text=f"{node.bl_idname = }")
            row = layout.row()
            row.label(text="Node Info")
            row = layout.row()
            row.label(text="Location")
            row.prop(node, 'location', text="X", index=0)
            row.prop(node, 'location', text="Y", index=1)
            row = layout.row()
            row.label(text="Dimension")
            row.prop(node, 'width', text="W")
            row.prop(node, 'dimensions', text="H", index=1)

        layout.row().operator('outliner.orphans_purge_recursive')


class PYNODES_OT_SHOW_ARRANGE(Operator):
    '''Test'''
    bl_idname = 'node.pynodes_arrange'
    bl_label = 'Arrange'

    def execute(self, context):
        arrange(self, context)
        return {'FINISHED'}


class PYNODES_OT_PURGE(Operator):
    """Clear all orphaned data-blocks without any users from the file"""
    bl_idname = 'outliner.orphans_purge_recursive'
    bl_label = 'Purge Orphan'

    def execute(self, context):
        bpy.ops.outliner.orphans_purge(do_recursive=True)
        return {'FINISHED'}


class Column:
    def __init__(self):
        self.nodes: list[Node] = []
        self.height = 0

    @property
    def frame_count(self):
        return len([node for node in self.nodes if is_frame(node)])


def is_frame(node: Node):
    return node.bl_idname == 'NodeFrame'


def is_linked_output(node: Node):
    for output in node.outputs:
        if output.is_linked:
            return True
    return False


def is_linked_input(node: Node):
    for input in node.inputs:
        if input.is_linked:
            return True
    return False


def match_frame_node(node: Node | None, frame_child_nodes: list[Node]):
    while node is not None:
        if node in frame_child_nodes:
            return node
        node = node.parent
    return None


def arrange(self, context: Context):
    btree = get_active_tree(context)

    margin_x, margin_y = context.scene.nodemargin_x, context.scene.nodemargin_y
    frame_margin_x, frame_margin_y = context.scene.framemargin_x, context.scene.framemargin_y

    arrange_tree(btree, margin_x, margin_y, frame_margin_x, frame_margin_y)


def arrange_tree(btree: NodeTree, margin_x=60, margin_y=20, frame_margin_x=0, frame_margin_y=40):

    frames_level: list[tuple(NodeFrame, int)] = []
    for node in btree.nodes:
        if is_frame(node):
            frame: NodeFrame = node
            level = 0
            while frame.parent is not None:
                level += 1
                frame = frame.parent
            frames_level.append((node, level))
    frames_level.sort(key=lambda x: x[1], reverse=True)

    frame_child_nodes: dict[NodeFrame, list[Node]] = {}
    for node in btree.nodes:
        if node.parent is not None:
            frame_child_nodes.setdefault(node.parent, []).append(node)

    frame_all_nodes: dict[NodeFrame, list[Node]] = {}
    for frame, _ in frames_level:
        frame_all_nodes[frame] = []
        for child_frame, nodes in frame_all_nodes.items():
            if child_frame.parent == frame:
                frame_all_nodes[frame].extend(nodes)
        frame_all_nodes[frame].extend([node for node in frame_child_nodes[frame] if not is_frame(node)])

    frame_input_nodes: dict[NodeFrame, list[Node]] = {}
    frame_input_sockets: dict[NodeFrame, list[NodeSocket]] = {}

    def get_frame_input_sockets(input_node: Node, current_frame_nodes: list[Node]):
        input_sockets: list[NodeSocket] = []
        for input in input_node.inputs:
            link: NodeLink
            for link in input.links:
                if link.from_node not in current_frame_nodes:
                    if input not in input_sockets:
                        input_sockets.append(input)
        return input_sockets

    for frame, level in frames_level:
        input_nodes = []
        for node in frame_child_nodes.get(frame, []):
            if is_frame(node):
                input_nodes.extend(frame_input_nodes.get(node, []))
            else:
                if is_linked_input(node):
                    input_nodes.append(node)
        input_sockets = []
        input_nodes_valid = []
        for node in input_nodes:
            sockets = get_frame_input_sockets(node, frame_all_nodes.get(frame, []))
            if sockets:
                input_nodes_valid.append(node)
            input_sockets.extend(sockets)
        frame_input_sockets[frame] = input_sockets
        frame_input_nodes[frame] = input_nodes_valid

    frame_output_nodes: dict[NodeFrame, list[Node]] = {}

    def linked_to_outer_frame(output_node: Node, current_frame_nodes: list[Node]):
        for output in output_node.outputs:
            link: NodeLink
            for link in output.links:
                if link.to_node not in current_frame_nodes:
                    return True
        return False

    for frame, level in frames_level:
        output_nodes = []
        for node in frame_child_nodes.get(frame, []):
            if is_frame(node):
                output_nodes.extend(frame_output_nodes.get(node, []))
            else:
                if is_linked_output(node):
                    output_nodes.append(node)

        frame_output_nodes[frame] = [node for node in output_nodes if linked_to_outer_frame(node, frame_all_nodes.get(frame, []))]

    root_child_nodes = [node for node in btree.nodes if node.parent == None]

    def arrange_frame(frame: NodeFrame = None):

        if frame is not None:
            child_nodes = frame_child_nodes.get(frame, [])
            output_nodes: list[Node] = []
            for node in child_nodes:
                if is_frame(node):
                    child_frame = node
                    if any(a in frame_output_nodes[frame] for a in frame_output_nodes[child_frame]) or not frame_output_nodes[child_frame]:
                        output_nodes.append(node)
                else:
                    if node in frame_output_nodes[frame] or not is_linked_output(node):
                        output_nodes.append(node)
        else:
            child_nodes = root_child_nodes
            output_nodes = []
            for node in child_nodes:
                if is_frame(node):
                    child_frame = node
                    for frame_output_node in frame_output_nodes[child_frame]:
                        if not is_linked_output(frame_output_node):
                            output_nodes.append(child_frame)
                            break
                else:
                    if not is_linked_output(node):
                        output_nodes.append(node)
        remain_nodes = [node for node in child_nodes if node not in output_nodes]
        remain_nodes_col_index = {node: 1 for node in remain_nodes}
        cols = [Column() for _ in range(len(remain_nodes) + 2)]
        cols[0].nodes.extend(output_nodes)

        index = 0
        while True:
            # print(frame.name if frame is not None else "Root", index, [node.name for node in cols[index].nodes])
            if len(cols[index].nodes) == 0:
                break
            for node in cols[index].nodes:
                if is_frame(node):
                    input_sockets = frame_input_sockets[node]
                    # print('\tInput Sockets', [input.name for input in input_sockets])
                else:
                    input_sockets = [input for input in node.inputs if input.is_linked]
                for input in input_sockets:
                    link: NodeLink
                    for link in input.links:
                        node_to_add = match_frame_node(link.from_node, remain_nodes)
                        if node_to_add is not None:
                            remain_nodes_col_index[node_to_add] = index + 1
                            if node_to_add not in cols[index + 1].nodes:
                                cols[index + 1].nodes.append(node_to_add)
            index += 1

            for i, col in enumerate(cols):
                if i == 0:
                    continue
                for node in col.nodes.copy():
                    if i < remain_nodes_col_index[node]:
                        col.nodes.remove(node)

        x = 0
        for col in cols:
            y = 0
            max_w = 0
            frame_margined = False
            for node in col.nodes:
                w, h = node.dimensions
                if is_frame(node):
                    w -= 30
                    y -= frame_margin_y
                    if not frame_margined:
                        x -= frame_margin_x
                        frame_margined = True
                if w > max_w:
                    max_w = w
                if w > 140 and not is_frame(node):
                    node.location = (x - (w - 140), y)
                else:
                    node.location = (x, y)
                y -= h
                y -= margin_y
            col.height = -y
            x -= max_w
            x -= margin_x

        max_col_height = max(col.height for col in cols)
        for i, col in enumerate(cols):
            for j, node in enumerate(col.nodes):
                x, y = node.location
                node.location = (x, y - (max_col_height - col.height) / 2)

    for frame, _ in frames_level:
        arrange_frame(frame)

    arrange_frame()


def register():
    bpy.types.Scene.nodemargin_x = bpy.props.IntProperty(default=60, update=arrange)
    bpy.types.Scene.nodemargin_y = bpy.props.IntProperty(default=20, update=arrange)
    bpy.types.Scene.framemargin_x = bpy.props.IntProperty(default=0, update=arrange)
    bpy.types.Scene.framemargin_y = bpy.props.IntProperty(default=0, update=arrange)


def unregister():
    del bpy.types.Scene.nodemargin_x
    del bpy.types.Scene.nodemargin_y
    del bpy.types.Scene.framemargin_x
    del bpy.types.Scene.framemargin_y
