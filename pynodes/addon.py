import bpy
from bpy.types import Node, NodeFrame, NodeLink, NodeSocket, Context, NodeTree, Panel, Operator


class PYNODES_PT_MAIN(Panel):
    bl_label = "Arrange Nodes"
    bl_space_type = "NODE_EDITOR"
    bl_region_type = "UI"
    bl_category = "Pynodes"

    def draw(self, context):

        layout = self.layout
        btree: NodeTree = context.space_data.edit_tree

        if btree is not None:

            col = layout.column()
            row = col.row(align=False)
            row.operator('node.pynodes_arrange', icon="PREFERENCES")
            row.label(text=btree.name, icon="NODETREE")

            layout.label(text="Node Margin:", icon="SEQ_STRIP_DUPLICATE")
            row = layout.row(align=True)
            row.prop(context.scene, 'nodemargin_x', text="X")
            row.prop(context.scene, 'nodemargin_y', text="Y")

            layout.label(text="Frame Margin:", icon="SEQ_STRIP_META")
            row = layout.row(align=True)
            row.prop(context.scene, 'framemargin_x', text="X")
            row.prop(context.scene, 'framemargin_y', text="Y")

            layout.label(text="Columns Center Order:")
            row = layout.row(align=True)
            row.prop(context.scene, 'node_center1', text="L → R", toggle=True)
            row.prop(context.scene, 'node_center2', text="L ← R", toggle=True)

            layout.label(text="Options:")
            col = layout.column(align=True)
            col.prop(context.scene, 'only_selected_frame', text="Only Selected Frame", toggle=True)
            col.prop(context.scene, 'reverse_single_link_sequence', text="Reverse Single Sequence", toggle=True)

            layout.separator()
            # node = btree.nodes.active
            node = context.active_node
            if node is not None and node.select:
                col = layout.column(align=True)
                if node.bl_idname == "NodeFrame":
                    split = col.split(factor=0.33, align=True)
                    box = split.box()
                    box.scale_y = 0.5
                    box.label(text=f"{node.bl_label}", icon="NODE")
                    split.prop(node, "label", text="")
                else:
                    box = col.box()
                    box.scale_y = 0.5
                    name = node.bl_label
                    if node.type == 'GROUP':
                        name = node.node_tree.name
                    if node.bl_idname == 'ShaderNodeMath':
                        name = node.operation.title()
                    box.label(text=f"{name}", icon="NODE")
                row = col.row(align=True)
                box = row.box()
                box.scale_y = 0.5
                box.label(text="Location", icon="ORIENTATION_VIEW")
                row.prop(node, 'location', text="X", index=0)
                row.prop(node, 'location', text="Y", index=1)
                row = col.row(align=True)
                box = row.box()
                box.scale_y = 0.5
                box.label(text="Dimension", icon="OBJECT_HIDDEN")
                row.prop(node, 'width', text="W")
                row.prop(node, 'dimensions', text="H", index=1)

                row = col.row(align=True)
                row.operator('node.options_toggle', text="Options", icon="HIDE_OFF")
                row.operator('node.hide_socket_toggle', text="Sockets", icon="HIDE_OFF")

                for input in node.inputs:
                    layout.row().label(text=f"{input.name} ({input.bl_idname})")

                for output in node.outputs:
                    layout.row().label(text=f"{output.name} ({output.bl_idname})")

        layout.separator()
        layout.row().operator('outliner.orphans_purge_recursive', icon="CANCEL")


# class PYNODES_PT_UTILS(Panel):
#     bl_label = "Utils"
#     bl_space_type = "NODE_EDITOR"
#     bl_region_type = "UI"
#     bl_category = "Pynodes"

#     def draw(self, context):
#         layout = self.layout
#         layout.row().operator('outliner.orphans_purge_recursive', icon="CANCEL")


class PYNODES_OT_ARRANGE(Operator):
    '''Arrange all nodes, deepest frame first, columns by columns from left to right'''
    bl_idname = 'node.pynodes_arrange'
    bl_label = 'Arrange'

    def execute(self, context):
        arrange(self, context)
        return {'FINISHED'}

    def invoke(self, context, value):
        arrange(self, context)
        return {'FINISHED'}

    @ classmethod
    def poll(cls, context: Context):
        space = context.space_data
        return space and (space.type == 'NODE_EDITOR') and space.edit_tree and not space.edit_tree.library


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

    @ property
    def height_with_offset(self):
        return self.height + self.offset


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

    # btree = get_active_tree(context)
    btree = context.space_data.edit_tree

    if btree is None:
        return

    margin_x, margin_y = context.scene.nodemargin_x, context.scene.nodemargin_y
    frame_margin_x, frame_margin_y = context.scene.framemargin_x, context.scene.framemargin_y
    node_center1 = context.scene.node_center1
    node_center2 = context.scene.node_center2
    only_selected_frame = context.scene.only_selected_frame
    reverse_single_link_sequence = context.scene.reverse_single_link_sequence

    arrange_tree(btree, margin_x, margin_y, frame_margin_x, frame_margin_y, node_center1, node_center2, only_selected_frame, reverse_single_link_sequence)


def arrange_tree(btree: NodeTree, margin_x=40, margin_y=20, frame_margin_x=10, frame_margin_y=10, node_center1=True, node_center2=True, only_selected_frame=False, reverse_single_link_sequence=False):
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

    frames_level_dict: dict[NodeFrame, int] = {}
    for frame, level in frames_level:
        frames_level_dict[frame] = level

    # A dict to record all frames and the deepest level it contains
    frames_deepest_level: dict[NodeFrame, int] = {}
    for frame, level in frames_level:
        if frame not in frames_deepest_level:
            frames_deepest_level[frame] = level
        if frame.parent is not None:
            frames_deepest_level[frame.parent] = max(frames_deepest_level[frame], frames_deepest_level.setdefault(frame.parent, 0))

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
                        if node_to_add is not None and node_to_add != node:
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
        frame_padding_x, frame_padding_y = 30, 30
        current_has_frame = previsous_has_frame = False
        for x_index, col in enumerate(cols):
            current_has_frame = col.has_frame
            if x_index == 0:
                if current_has_frame and frame is not None:
                    x -= frame_padding_x
            else:
                if current_has_frame:
                    x -= frame_margin_x + frame_padding_x
                elif previsous_has_frame:
                    x -= frame_margin_x
                else:
                    x -= margin_x

            y = 0
            current_is_frame = previsous_is_frame = False
            for y_index, node in enumerate(col.nodes):
                current_is_frame = is_frame(node)
                w, h = node.dimensions
                if w > col.width:
                    col.width = w
                if y_index == 0:
                    if current_is_frame:
                        node.location = (x, y)
                        if bpy.app.version >= (3, 6, 0):
                            padding_top = frame_padding_y + (10 if node.label != "" else 0)
                        else:
                            padding_top = frame_padding_y
                        y_offset = h - padding_top
                        col.height += y_offset
                        y -= y_offset
                    else:
                        if w > 140:
                            node.location = (x + 140 - w, y)
                        else:
                            node.location = (x, y)
                        col.height += h
                        y -= h
                else:  # y_index > 0
                    if current_is_frame:
                        if bpy.app.version >= (3, 6, 0):
                            padding_top = frame_padding_y + (10 if node.label != "" else 0)
                        else:
                            padding_top = frame_padding_y
                        y -= frame_margin_y + padding_top
                        node.location = (x, y)
                        y -= h - padding_top
                        col.height += frame_margin_y + h
                    else:
                        if previsous_is_frame:
                            y -= frame_margin_y
                            if w > 140:
                                node.location = (x + 140 - w, y)
                            else:
                                node.location = (x, y)
                            y -= h
                            col.height += frame_margin_y + h
                        else:
                            y -= margin_y
                            if w > 140:
                                node.location = (x + 140 - w, y)
                            else:
                                node.location = (x, y)
                            y -= h
                            col.height += margin_y + h

                previsous_is_frame = current_is_frame
            x -= col.width
            if current_has_frame:
                x += frame_padding_x
            previsous_has_frame = current_has_frame
        '''
        # Code for debug
        for i, col in enumerate(cols):
            for j, node in enumerate(col.nodes):
                if j == 0:
                    node.label = f"{col.width:3.0f} {col.height:3.0f}"
                else:
                    node.label = f"{node.dimensions[0]:3.0f} {node.dimensions[1]:3.0f}"
        '''

        # If a child node is too tall, then don't aligin center
        for node in child_nodes:
            if not is_frame(node) and node.dimensions[1] >= 500:
                return

        diff_shreshold_factor = 0.66

        # Center from left columns to right columns
        if node_center1:
            for i, col in reversed(list(enumerate(cols))):
                if i == len(cols) - 1:
                    continue
                current_height = col.height + col.offset
                pre_height = cols[i + 1].height + cols[i + 1].offset
                if cols[i + 1].offset > 0 and cols[i + 1].offset + cols[i + 1].height / 2 - col.height / 2 < cols[i + 1].height * (1 - diff_shreshold_factor):
                    continue
                if cols[i + 1].offset == 0 and current_height > pre_height * diff_shreshold_factor:
                    continue
                # col.offset + col.height / 2 + offset_y = cols[i + 1].offset + cols[i + 1].height / 2
                offset_y = cols[i + 1].offset + cols[i + 1].height / 2 - col.height / 2
                if offset_y < 0:
                    continue
                else:
                    col.offset += offset_y
                for j, node in enumerate(col.nodes):
                    x, y = node.location
                    node.location = (x, y - offset_y)

        # Center from right columns to left columns
        if node_center2:
            for i, col in enumerate(cols):
                if i == 0:
                    continue
                current_height = col.height + col.offset
                pre_height = cols[i - 1].height + cols[i - 1].offset
                if current_height > pre_height * diff_shreshold_factor:
                    continue
                # col.offset + col.height / 2 + offset_y = cols[i - 1].offset + cols[i - 1].height / 2
                offset_y = cols[i - 1].offset + cols[i - 1].height / 2 - (col.offset + col.height / 2)
                if offset_y < 0:
                    continue
                else:
                    col.offset += offset_y
                for j, node in enumerate(col.nodes):
                    x, y = node.location
                    node.location = (x, y - offset_y)

        # If for every column, there is only one node, then staggering in height.
        offset_y = 20 + margin_y
        if margin_x <= 0 and all(len(col.nodes) <= 1 for col in cols):
            for i, col in enumerate(cols):
                for node in col.nodes:
                    x, y = node.location
                    if not reverse_single_link_sequence:
                        node.location = (x, -i * offset_y)
                    else:
                        node.location = (x, -(len(cols) - i) * offset_y)
        elif margin_x <= 0:
            for i, col in reversed(list(enumerate(cols))):
                if i == len(cols) - 1:
                    continue
                if len(cols[i + 1].nodes) == 1 and not is_frame(cols[i + 1].nodes[0])\
                        and len(col.nodes) == 1 and not is_frame(col.nodes[0]):
                    for node in col.nodes:
                        x = node.location.x
                        y = cols[i + 1].nodes[0].location.y
                        if not reverse_single_link_sequence:
                            node.location = (x, y - offset_y)
                        else:
                            node.location = (x, y + offset_y)

    if only_selected_frame:
        has_frame_selected = False
        for frame, _ in frames_level:
            if frame.select == True:
                has_frame_selected = True
                arrange_frame(frame)
        if not has_frame_selected:
            arrange_frame()
    else:
        # Arrange all frames, deepest first
        for frame, _ in frames_level:
            arrange_frame(frame)
        # Arrange root tree
        arrange_frame()


def register():
    bpy.types.Scene.nodemargin_x = bpy.props.IntProperty(default=-140, min=-140, update=arrange)
    bpy.types.Scene.nodemargin_y = bpy.props.IntProperty(default=20, update=arrange)
    bpy.types.Scene.framemargin_x = bpy.props.IntProperty(default=10, update=arrange)
    bpy.types.Scene.framemargin_y = bpy.props.IntProperty(default=10, update=arrange)
    bpy.types.Scene.node_center1 = bpy.props.BoolProperty(default=True, description="Center each column from left to right", update=arrange)
    bpy.types.Scene.node_center2 = bpy.props.BoolProperty(default=True, description="Center each column from right to left", update=arrange)
    bpy.types.Scene.only_selected_frame = bpy.props.BoolProperty(default=False, description="Only arrange selected frame, if no frame selected, arrange the root tree", update=arrange)
    bpy.types.Scene.reverse_single_link_sequence = bpy.props.BoolProperty(default=False, description="Reverse single link staggered sequence", update=arrange)


def unregister():
    del bpy.types.Scene.nodemargin_x
    del bpy.types.Scene.nodemargin_y
    del bpy.types.Scene.framemargin_x
    del bpy.types.Scene.framemargin_y
    del bpy.types.Scene.node_center1
    del bpy.types.Scene.node_center2
    del bpy.types.Scene.only_selected_frame
    del bpy.types.Scene.reverse_single_link_sequence
