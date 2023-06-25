import bpy
from bpy.types import Node, NodeFrame, NodeLink, NodeSocket, Context, NodeTree, Panel, Operator


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

        layout.row().prop(context.scene, 'nodecenter', text="Column Center")

        # get current active tree
        btree = get_active_tree(context)
        if btree is not None:
            Tree = btree.name
            # layout.row().label(text=f"{Tree = }")

            # node = btree.nodes.active
            node = context.active_node
            if node is not None and node.select:
                Node = node.bl_idname
                # layout.row().label(text=f"{Node = }")
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
        bpy.ops.node.view_all()
        return {'FINISHED'}

    def invoke(self, context, value):
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
    """Represent a column in blender node editor"""

    def __init__(self):
        self.nodes: list[Node] = []
        self.width = 0
        self.height = 0
        self.offset = 0
        self.has_frame = False

    @property
    def height_with_offset(self):
        return self.height + self.offset

    # @property
    # def frame_count(self):
    #     return len([node for node in self.nodes if is_frame(node)])


def get_active_tree(context: Context) -> NodeTree | None:
    tree = context.space_data.node_tree
    if tree is None:
        return
    if tree.nodes.active is not None:
        while tree.nodes.active != context.active_node:
            tree = tree.nodes.active.node_tree
    return tree


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

    if btree is None:
        return

    margin_x, margin_y = context.scene.nodemargin_x, context.scene.nodemargin_y
    frame_margin_x, frame_margin_y = context.scene.framemargin_x, context.scene.framemargin_y
    column_center = context.scene.nodecenter

    arrange_tree(btree, margin_x, margin_y, frame_margin_x, frame_margin_y, column_center)


def arrange_tree(btree: NodeTree, margin_x=60, margin_y=20, frame_margin_x=10, frame_margin_y=10, column_center=True):
    # A list to record all frames and their level
    frames_level: list[tuple(NodeFrame, int)] = []
    for node in btree.nodes:
        if is_frame(node):
            frame: NodeFrame = node
            level = 0
            while frame.parent is not None:
                level += 1
                frame = frame.parent
            frames_level.append((node, level))
    # Sort frames by level, deepest first
    frames_level.sort(key=lambda x: x[1], reverse=True)

    # A dict to record all direct child nodes in each frame including both frames and nodes
    frame_child_nodes: dict[NodeFrame, list[Node]] = {}
    for node in btree.nodes:
        if node.parent is not None:
            frame_child_nodes.setdefault(node.parent, []).append(node)

    # A dict to record all descendant nodes in each frame only excluding frames
    frame_all_nodes: dict[NodeFrame, list[Node]] = {}
    for frame, _ in frames_level:
        frame_all_nodes[frame] = []
        for child_frame, nodes in frame_all_nodes.items():
            if child_frame.parent == frame:
                frame_all_nodes[frame].extend(nodes)
        frame_all_nodes[frame].extend([node for node in frame_child_nodes[frame] if not is_frame(node)])

    # A dict to record all input nodes that have link from other frames in each frame
    frame_input_nodes: dict[NodeFrame, list[Node]] = {}

    # A dict to record all the corresponding input sockets
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

    # Evaluate the input node and input sockets for each frame
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

    # A dict to record all output nodes that have link to other frames in each frame
    frame_output_nodes: dict[NodeFrame, list[Node]] = {}

    def linked_to_outer_frame(output_node: Node, current_frame_nodes: list[Node]):
        for output in output_node.outputs:
            link: NodeLink
            for link in output.links:
                if link.to_node not in current_frame_nodes:
                    return True
        return False

    # Evaluate the output node for each frame
    for frame, level in frames_level:
        output_nodes = []
        for node in frame_child_nodes.get(frame, []):
            if is_frame(node):
                output_nodes.extend(frame_output_nodes.get(node, []))
            else:
                if is_linked_output(node):
                    output_nodes.append(node)

        frame_output_nodes[frame] = [node for node in output_nodes if linked_to_outer_frame(node, frame_all_nodes.get(frame, []))]

    # Get all the root nodes of the tree
    # The root tree can also be treated as a frame
    root_child_nodes = [node for node in btree.nodes if node.parent == None]

    def arrange_frame(frame: NodeFrame = None):
        # Arrange a frame or root tree(frame is None)

        if frame is not None:
            # Evaluate ouput nodes of current frame
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
            # Evaluate ouput nodes of root tree
            child_nodes = root_child_nodes
            output_nodes = []
            for node in child_nodes:
                if is_frame(node):
                    child_frame = node
                    if not frame_output_nodes[child_frame]:
                        output_nodes.append(child_frame)
                else:
                    if not is_linked_output(node):
                        output_nodes.append(node)
        remain_nodes = [node for node in child_nodes if node not in output_nodes]
        # Record the colume index of the remain nodes, then remove the lower index for duplicate nodes
        remain_nodes_col_index = {node: 1 for node in remain_nodes}
        cols = [Column() for _ in range(len(remain_nodes) + 2)]
        cols[0].nodes.extend(output_nodes)

        # Arrange the nodes to columns
        index = 0
        while True:
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
                    for link in reversed(input.links):
                        node_to_add = match_frame_node(link.from_node, remain_nodes)
                        if node_to_add is not None:
                            remain_nodes_col_index[node_to_add] = index + 1
                            if node_to_add not in cols[index + 1].nodes:
                                cols[index + 1].nodes.append(node_to_add)
            index += 1
            # Remove duplicate nodes
            for i, col in enumerate(cols):
                if i == 0:
                    continue
                for node in col.nodes.copy():
                    if i < remain_nodes_col_index[node]:
                        col.nodes.remove(node)

        # Init has_frame for all columns
        for col in cols:
            for node in col.nodes:
                if is_frame(node):
                    col.has_frame = True
                    break

        # Arrange the location of nodes in columns
        x = 0
        for x_index, col in enumerate(cols):
            y = 0
            for y_index, node in enumerate(col.nodes):
                current_is_frame = is_frame(node)
                w, h = node.dimensions
                if w > col.width:
                    col.width = w
                if not current_is_frame and w > 140:
                    node.location = (x + 140 - w, y)
                else:
                    node.location = (x, y)
                y -= h
                col.height += h
                if current_is_frame:
                    if y_index == 0:
                        col.height -= 30
                    if y_index == len(col.nodes) - 1:
                        col.height -= 30
                if y_index == len(col.nodes) - 1:
                    break
                next_is_frame = is_frame(col.nodes[y_index + 1])
                if current_is_frame:
                    if y_index == 0:
                        col.height -= 30
                    if next_is_frame:
                        y -= frame_margin_y
                        col.height += frame_margin_y
                    else:
                        y -= frame_margin_y - 30
                        col.height += frame_margin_y - 30
                else:
                    if next_is_frame:
                        y -= frame_margin_y + 30
                        col.height += frame_margin_y + 30
                    else:
                        y -= margin_y
                        col.height += margin_y
            if x_index == len(cols) - 1:
                break
            x -= col.width
            if col.has_frame:
                if cols[x_index + 1].has_frame:
                    x -= frame_margin_x
                else:
                    x -= -30 + frame_margin_x
            else:
                if cols[x_index + 1].has_frame:
                    x -= 30 + frame_margin_x
                else:
                    x -= margin_x

        # for i, col in enumerate(cols):
        #     for j, node in enumerate(col.nodes):
        #         if j == 0:
        #             node.label = f"{col.width:3.0f} {col.height:3.0f}"
        #         else:
        #             node.label = f"{node.dimensions[0]:3.0f} {node.dimensions[1]:3.0f}"

        # Arrange the location to the center of columns
        if not column_center:
            return

        for node in child_nodes:
            if not is_frame(node) and node.dimensions[1] >= 500:
                return

        diff_shreshold_factor = 0.66

        # Center from left columns to right columns
        for i, col in reversed(list(enumerate(cols))):
            if i == len(cols) - 1:
                continue
            if col.height < cols[i + 1].height:
                col.offset = cols[i + 1].offset
            if col.height < cols[i + 1].height * diff_shreshold_factor:
                col.offset += (cols[i + 1].height - col.height) / 2
            if col.offset == 0:
                continue
            for j, node in enumerate(col.nodes):
                if j == 0 and node.bl_idname.startswith("GeometryNode"):
                    break
                x, y = node.location
                node.location = (x, y - col.offset)

        # Center from right columns to left columns
        for i, col in enumerate(cols):
            if i == 0:
                continue
            if col.offset != 0:
                continue
            if cols[i - 1].offset != 0 and col.height <= cols[i - 1].height:
                col.offset = cols[i - 1].offset
            if col.height < cols[i - 1].height * diff_shreshold_factor:
                col.offset += (cols[i - 1].height - col.height) / 2
            if col.offset == 0:
                continue
            for j, node in enumerate(col.nodes):
                # if j == 0 and node.bl_idname.startswith("GeometryNode"):
                #     break
                x, y = node.location
                node.location = (x, y - col.offset)

    # Arrange all frames, deepest first
    for frame, _ in frames_level:
        arrange_frame(frame)
    # Arrange root tree
    arrange_frame()


def register():
    bpy.types.Scene.nodemargin_x = bpy.props.IntProperty(default=40, min=-140, update=arrange)
    bpy.types.Scene.nodemargin_y = bpy.props.IntProperty(default=20, update=arrange)
    bpy.types.Scene.framemargin_x = bpy.props.IntProperty(default=10, update=arrange)
    bpy.types.Scene.framemargin_y = bpy.props.IntProperty(default=10, update=arrange)
    bpy.types.Scene.nodecenter = bpy.props.BoolProperty(default=True, update=arrange)


def unregister():
    del bpy.types.Scene.nodemargin_x
    del bpy.types.Scene.nodemargin_y
    del bpy.types.Scene.framemargin_x
    del bpy.types.Scene.framemargin_y
    del bpy.types.Scene.nodecenter
