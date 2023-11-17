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

            row = layout.row(align=True)
            row.label(text="Options:")
            row.prop(context.scene, 'only_selected_frame', text="Frame", icon="MENU_PANEL", toggle=True)
            row.prop(context.scene, 'reverse_single_link_sequence', text="Reverse", icon="DECORATE_OVERRIDE", toggle=True)

            layout.row().operator("node.pynodes_select_all_reroute", icon="DECORATE_KEYFRAME")


class PYNODES_PT_node_info(Panel):
    bl_label = "Node Info"
    bl_space_type = "NODE_EDITOR"
    bl_region_type = "UI"
    bl_category = "Pynodes"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):

        layout = self.layout
        btree: NodeTree = context.space_data.edit_tree

        if btree is not None:
            node = context.active_node
            if node is not None and node.select:
                row = layout.row(align=False)
                row.alignment = "LEFT"
                if node.bl_idname == "NodeFrame":
                    row.operator("wm.call_panel", icon="NODE", text=node.label or "Frame (Click to Rename)", emboss=False).name = "TOPBAR_PT_name"
                elif node.bl_idname == "ShaderNodeValToRGB":
                    name = node.bl_label
                    # split = row.split(factor=0.6666, align=True)
                    row.operator("pynodes.copy_node_bl_idname", text=name, emboss=False, icon="NODE").node_bl_idname = node.bl_idname
                    row.operator("node.pynodes_copy_color_ramp", emboss=False)
                else:
                    name = node.bl_label
                    if node.type == 'GROUP':
                        name = node.node_tree.name
                    elif node.bl_idname in ['ShaderNodeMath', 'ShaderNodeVectorMath', 'FunctionNodeCompare']:
                        name = name + " → " + node.operation.replace("_", " ").title()
                    # row.label(text=name, icon="NODE")
                    row.operator("pynodes.copy_node_bl_idname", text=name, emboss=False, icon="NODE").node_bl_idname = node.bl_idname
                row = layout.row(align=True)
                row.label(text="Location", icon="ORIENTATION_VIEW")
                row.prop(node, 'location', text="X", index=0)
                row.prop(node, 'location', text="Y", index=1)
                row = layout.row(align=True)
                row.label(text="Dimension", icon="OBJECT_HIDDEN")
                row.prop(node, 'width', text="W")
                row.prop(node, 'dimensions', text="H", index=1)

                row = layout.row(align=True)
                icon = "HIDE_OFF" if node.show_options else "HIDE_ON"
                row.operator('node.options_toggle', text="Options", icon=icon)
                icon = "HIDE_OFF"
                for input in node.inputs:
                    if input.enabled and input.hide:
                        icon = "HIDE_ON"
                row.operator('node.hide_socket_toggle', text="Sockets", icon=icon)
                icon = "MUTE_IPO_OFF" if node.mute else "MUTE_IPO_ON"
                row.operator('node.mute_toggle', text="Mute", icon=icon)

                if node.inputs:
                    layout.row().label(text="Input Sockets:")
                    col = layout.column(align=True)
                    for i, input in enumerate(node.inputs):
                        row = col.row(align=True)
                        row.prop(input, 'hide', icon_only=True, icon='HIDE_ON' if not input.enabled or input.hide else 'HIDE_OFF')
                        box = row.box()
                        box.scale_y = 0.5
                        name = input.identifier
                        if node.type in ['GROUP', "GROUP_INPUT", "GROUP_OUTPUT", 'REPEAT_INPUT', 'REPEAT_OUTPUT', 'SIMULATION_INPUT', 'SIMULATION_OUTPUT'] and input.name:
                            name = f"{input.name}"
                        box.label(text=f"{i:>02}│ {name}")
                        row.prop(input, "enabled", icon_only=True, invert_checkbox=True, icon="LAYER_ACTIVE" if input.enabled else "BLANK1")

                if node.outputs:
                    layout.row().label(text="Output Sockets:")
                    col = layout.column(align=True)
                    for i, output in enumerate(node.outputs):
                        row = col.row(align=True)
                        row.prop(output, 'hide', icon_only=True, icon='HIDE_ON' if not output.enabled or output.hide else 'HIDE_OFF')
                        box = row.box()
                        box.scale_y = 0.5
                        name = output.identifier
                        if node.type in ['GROUP', "GROUP_INPUT", "GROUP_OUTPUT", 'REPEAT_INPUT', 'REPEAT_OUTPUT', 'SIMULATION_INPUT', 'SIMULATION_OUTPUT'] and output.name:
                            name = f"{output.name}"
                        box.label(text=f"{i:>02}│ {name}")
                        row.prop(output, "enabled", icon_only=True, invert_checkbox=True, icon="LAYER_ACTIVE" if output.enabled else "BLANK1")


class PYNODES_OT_ARRANGE(Operator):
    '''Arrange all nodes, deepest frame first, columns by columns from left to right'''
    bl_idname = 'node.pynodes_arrange'
    bl_label = 'Arrange'

    def execute(self, context):
        arrange(self, context)
        return {'FINISHED'}

    def invoke(self, context, value):
        return self.execute(context)

    @classmethod
    def poll(cls, context: Context):
        space = context.space_data
        return space and (space.type == 'NODE_EDITOR') and space.edit_tree and not space.edit_tree.library


class PYNODES_OT_RELOAD(Operator):
    """Reload pynodes module"""
    bl_idname = 'node.pynodes_reload'
    bl_label = 'Reload PyNodes'

    def execute(self, context):
        from .core import reload
        reload()
        print("Pynodes: Reloaded")
        return {'FINISHED'}


class PYNODES_OT_copy_color_ramp(Operator):
    """Copy color ramp to clipboard as python list"""
    bl_idname = 'node.pynodes_copy_color_ramp'
    bl_label = 'Copy'

    def execute(self, context):
        from .colors import srgb_to_hex_string, linear_to_srgb
        node: bpy.types.ShaderNodeValToRGB = context.active_node
        color_ramp = node.color_ramp
        colors = []
        for element in color_ramp.elements:
            colors.append((round(element.position, 3), srgb_to_hex_string(*[linear_to_srgb(c) for c in element.color[:3]])))
        context.window_manager.clipboard = repr(colors)
        return {'FINISHED'}


class PYNODES_OT_select_all_reroute(Operator):
    """Select all reroute nodes"""
    bl_idname = 'node.pynodes_select_all_reroute'
    bl_label = 'Select all Reroute Nodes'

    def execute(self, context):
        btree: NodeTree = context.space_data.edit_tree
        for node in btree.nodes:
            bl_idname = node.bl_idname
            node.hide = False
            if bl_idname in ["ShaderNodeMath", "ShaderNodeVectorMath", "FunctionNodeCompare"]:
                node.show_options = False
            if node.width < 140:
                node.width = 140
            if node.bl_idname == 'NodeReroute':
                node.select = True
            else:
                node.select = False
        return {'FINISHED'}


class PYNODES_OT_toggle_editor(Operator):
    """Toggle between Geometry and Shader Editor"""
    bl_idname = 'screen.toggle_editor'
    bl_label = 'Toggle Editor'

    def execute(self, context):
        if context.area.type != "NODE_EDITOR":
            context.area.type = "NODE_EDITOR"
        editor: bpy.types.SpaceNodeEditor = context.area.spaces.active
        editor.tree_type = "ShaderNodeTree" if editor.tree_type == "GeometryNodeTree" else "GeometryNodeTree"
        # bpy.ops.node.view_all()
        return {'FINISHED'}


class PYNODES_OT_copy_node_bl_idname(Operator):
    """Copy bl_idname of selected node to clipboard"""
    bl_idname = 'pynodes.copy_node_bl_idname'
    bl_label = 'Copy bl_idname of selected node to clipboard'

    node_bl_idname: bpy.props.StringProperty(name='node_bl_idname', default='')

    def execute(self, context):
        context.window_manager.clipboard = self.node_bl_idname
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
    scale = 1 / context.preferences.view.ui_scale

    arrange_tree(btree, margin_x, margin_y, frame_margin_x, frame_margin_y, node_center1, node_center2, only_selected_frame, reverse_single_link_sequence, scale)


def arrange_tree(btree: NodeTree, margin_x=40, margin_y=20, frame_margin_x=10, frame_margin_y=10, node_center1=True, node_center2=True, only_selected_frame=False, reverse_single_link_sequence=False, scale=1):
    # Hide Vector input sockets with default value to save spaces
    for bnode in btree.nodes:
        if bnode.bl_idname == "ShaderNodeMapping":
            continue
        for bsocket in bnode.inputs:
            if bsocket.is_linked or bsocket.display_shape == "DIAMOND" or bsocket.enabled == False or bsocket.hide_value == True:
                continue
            if bsocket.bl_idname in ['NodeSocketVector', 'NodeSocketVectorTranslation', "NodeSocketVectorEuler"]:
                if tuple(bsocket.default_value) == (0, 0, 0) and "_" not in bsocket.identifier:
                    bsocket.hide = True
            if bsocket.name == "Scale" and bsocket.bl_idname in ['NodeSocketVectorXYZ']:
                if tuple(bsocket.default_value) == (1, 1, 1):
                    bsocket.hide = True

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
        try:
            frame_all_nodes[frame].extend([node for node in frame_child_nodes[frame] if not is_frame(node)])
        except KeyError:
            pass

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

    def arrange_frame(frame: NodeFrame = None, scale=1):
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
            if len(cols[index].nodes) == 0 or index == len(remain_nodes):
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

        diff_shreshold_factor = 0.66

        # Center from left columns to right columns
        if node_center1:
            for i, col in reversed(list(enumerate(cols))):
                if i == len(cols) - 1:
                    continue
                # If a child node of previous column is too tall, then don't aligin center
                if any(node.dimensions[1] >= 500 for node in cols[i + 1].nodes if not is_frame(node)):
                    offset_y = cols[i + 1].offset
                else:
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
                # If a child node of previous column is too tall, then don't aligin center
                if any(node.dimensions[1] >= 500 for node in cols[i - 1].nodes if not is_frame(node)):
                    continue
                for node in cols[i - 1].nodes:
                    if not is_frame(node) and node.dimensions[1] >= 500:
                        continue
                current_height = col.height + col.offset
                pre_height = cols[i - 1].height + cols[i - 1].offset
                if current_height > pre_height:
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

        for node in child_nodes:
            x, y = node.location
            node.location = (x * scale, y * scale)

    if only_selected_frame:
        has_frame_selected = False
        for frame, _ in frames_level:
            if frame.select == True:
                has_frame_selected = True
                arrange_frame(frame, scale)
        if not has_frame_selected:
            arrange_frame(scale=scale)
    else:
        # Arrange all frames, deepest first
        for frame, _ in frames_level:
            arrange_frame(frame, scale)
        # Arrange root tree
        arrange_frame(scale=scale)


def register():
    default_nodemargin_x = 40
    bpy.types.Scene.nodemargin_x = bpy.props.IntProperty(default=default_nodemargin_x, min=-140, update=arrange)
    bpy.types.Scene.nodemargin_y = bpy.props.IntProperty(default=20, update=arrange)
    bpy.types.Scene.framemargin_x = bpy.props.IntProperty(default=10, update=arrange)
    bpy.types.Scene.framemargin_y = bpy.props.IntProperty(default=10, update=arrange)
    bpy.types.Scene.node_center1 = bpy.props.BoolProperty(default=True, description="Center each column from left to right", update=arrange)
    bpy.types.Scene.node_center2 = bpy.props.BoolProperty(default=True, description="Center each column from right to left", update=arrange)
    bpy.types.Scene.only_selected_frame = bpy.props.BoolProperty(default=False, name="Only Arrange Selected Frame", description="Only arrange selected frame, if no frame selected, arrange the root tree", update=arrange)
    bpy.types.Scene.reverse_single_link_sequence = bpy.props.BoolProperty(default=False, name="Reverse Single Link Sequence", description="Reverse single link staggered sequence", update=arrange)


def unregister():
    del bpy.types.Scene.nodemargin_x
    del bpy.types.Scene.nodemargin_y
    del bpy.types.Scene.framemargin_x
    del bpy.types.Scene.framemargin_y
    del bpy.types.Scene.node_center1
    del bpy.types.Scene.node_center2
    del bpy.types.Scene.only_selected_frame
    del bpy.types.Scene.reverse_single_link_sequence
