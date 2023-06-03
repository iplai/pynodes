import bpy, collections, itertools
from bpy.types import Node, NodeSocket, Context, NodeTree, Panel, Operator
from nodeitems_utils import node_categories_iter, NodeItemCustom


def get_nodes_from_category(category_name, context):
    for category in node_categories_iter(context):
        if category.name == category_name:
            return sorted(category.items(context), key=lambda node: node.label)
    raise RuntimeError(f"Unknown Category {category_name}")


def get_first_enabled_output(node: Node):
    for output in node.outputs:
        if output.enabled:
            return output
    else:
        return node.outputs[0]


def is_visible_socket(socket: NodeSocket):
    return not socket.hide and socket.enabled and socket.type != 'CUSTOM'


def node_mid_pt(node: bpy.types.Node, axis):
    if axis == 'x':
        d = node.location.x + (node.dimensions.x / 2)
    elif axis == 'y':
        d = node.location.y - (node.dimensions.y / 2)
    else:
        d = 0
    return d


def abs_node_location(node: Node):
    abs_location = node.location
    if node.parent is None:
        return abs_location
    return abs_location + abs_node_location(node.parent)


def get_active_tree(context: Context):
    tree: bpy.types.NodeTree = context.space_data.node_tree
    if tree is None:
        return
    if tree.nodes.active is not None:
        while tree.nodes.active != context.active_node:
            tree = tree.nodes.active.node_tree
    return tree


def get_group_output_node(tree: NodeTree):
    for node in tree.nodes:
        if node.type == 'GROUP_OUTPUT' and node.is_active_output == True:
            return node


class values:
    average_y = 0
    x_last = 0
    margin_x = 100
    margin_y = 20
    mat_name = ""


class NA_PT_NodePanel(Panel):
    bl_label = "Node Arrange"
    bl_space_type = "NODE_EDITOR"
    bl_region_type = "UI"
    bl_category = "Pynodes"

    def draw(self, context):
        btree = get_active_tree(context)

        if btree is None:
            return

        layout = self.layout

        row = layout.row()
        row.operator('node.arrange')
        row.operator('node.arrange2')

        row = layout.row()
        row.label(text="Margin")
        row.prop(context.scene, 'node_center', text="Center nodes")
        row = layout.row()
        row.prop(context.scene, 'nodemargin_x', text="X")
        row.prop(context.scene, 'nodemargin_y', text="Y")

        # row = layout.row()

        row = layout.row()
        row.label(text=btree.bl_idname)

        # row = layout.row()
        # row.label(text=f"is_embedded_data: {btree.is_embedded_data}")

        row = layout.row()
        node = btree.nodes.active
        if node is not None and node.select:
            row.label(text=node.bl_idname)
            row = layout.row()
            row.label(text="Location")
            row = layout.row()
            row.prop(node, 'location', text="X", index=0)
            row.prop(node, 'location', text="Y", index=1)
            row = layout.row()
            row.prop(node, 'width', text="Node width")
            row = layout.row()
            row.prop(node, 'dimensions', text="Node height", index=1)

        row = layout.row()
        row.operator('pynodes.select_unlinked')
        row.operator('outliner.orphans_purge_recursive')


class NA_OT_NodeButton(Operator):
    '''Arrange Connected Nodes/Arrange All Nodes'''
    bl_idname = 'node.arrange'
    bl_label = 'Arrange 1'

    def execute(self, context):
        nodemargin(self, context)
        btree: NodeTree = bpy.context.space_data.node_tree
        btree.nodes.update()
        bpy.ops.node.view_all()
        return {'FINISHED'}

    def invoke(self, context, value):
        values.mat_name = bpy.context.space_data.node_tree
        nodemargin(self, context)
        return {'FINISHED'}


class NA_OT_NodeButton2(Operator):
    '''Arrange Connected Nodes/Arrange All Nodes'''
    bl_idname = 'node.arrange2'
    bl_label = 'Arrange 2'

    def execute(self, context):
        btree: NodeTree = bpy.context.space_data.node_tree
        from pynodes import arrange
        arrange.arrange(btree)
        bpy.ops.node.view_all()
        return {'FINISHED'}


class NA_OT_NodeButtonOdd(Operator):
    """Select Unlinked Nodes"""
    bl_idname = 'pynodes.select_unlinked'
    bl_label = 'Select Unlinked'

    def execute(self, context):
        values.mat_name = bpy.context.space_data.node_tree
        nodes_iterate(context.space_data.node_tree, False)
        return {'FINISHED'}


class PurgeOrphanRecursive(Operator):
    """Clear all orphaned data-blocks without any users from the file"""
    bl_idname = 'outliner.orphans_purge_recursive'
    bl_label = 'Purge Orphan'

    def execute(self, context):
        bpy.ops.outliner.orphans_purge(do_recursive=True)
        return {'FINISHED'}


def nodemargin(self, context: Context):

    values.margin_x = context.scene.nodemargin_x
    values.margin_y = context.scene.nodemargin_y

    btree: NodeTree = context.space_data.node_tree

    # first arrange nodegroups
    n_groups = []
    for i in btree.nodes:
        if i.type == 'GROUP':
            n_groups.append(i)

    while n_groups:
        j = n_groups.pop(0)
        nodes_iterate(j.node_tree)
        for i in j.node_tree.nodes:
            if i.type == 'GROUP':
                n_groups.append(i)

    nodes_iterate(btree)

    # arrange nodes + this center nodes together
    if context.scene.node_center:
        nodes_center(btree)


class NA_OT_ArrangeNodesOp(bpy.types.Operator):
    bl_idname = 'node.arrange_nodetree'
    bl_label = 'Nodes Private Op'

    mat_name: bpy.props.StringProperty()
    margin_x: bpy.props.IntProperty(default=120)
    margin_y: bpy.props.IntProperty(default=120)

    def nodemargin2(self, context):
        mat = None
        mat_found = bpy.data.materials.get(self.mat_name)
        if self.mat_name and mat_found:
            mat = mat_found
            # print(mat)

        if not mat:
            return
        else:
            values.mat_name = self.mat_name
            scn = context.scene
            scn.nodemargin_x = self.margin_x
            scn.nodemargin_y = self.margin_y
            nodes_iterate(mat)
            if scn.node_center:
                nodes_center(mat)

    def execute(self, context):
        self.nodemargin2(context)
        return {'FINISHED'}


def outputnode_search(ntree):
    outputnodes = []
    for node in ntree.nodes:
        if not node.outputs:
            for input in node.inputs:
                if input.is_linked:
                    outputnodes.append(node)
                    break

    if not outputnodes:
        print("No output node found")
        return None
    return outputnodes


###############################################################
def nodes_iterate(ntree, arrange=True):

    nodeoutput = outputnode_search(ntree)
    if nodeoutput is None:
        # print ("nodeoutput is None")
        return None
    a = []
    a.append([])
    for i in nodeoutput:
        a[0].append(i)

    level = 0

    while a[level]:
        a.append([])

        for node in a[level]:
            inputlist = [i for i in node.inputs if i.is_linked]

            if inputlist:

                for input in inputlist:
                    for nlinks in input.links:
                        node1 = nlinks.from_node
                        a[level + 1].append(node1)

            else:
                pass

        level += 1

    del a[level]
    level -= 1

    # remove duplicate nodes at the same level, first wins
    for x, nodes in enumerate(a):
        a[x] = list(collections.OrderedDict(zip(a[x], itertools.repeat(None))))

    # remove duplicate nodes in all levels, last wins
    top = level
    for row1 in range(top, 1, -1):
        for col1 in a[row1]:
            for row2 in range(row1 - 1, 0, -1):
                for col2 in a[row2]:
                    if col1 == col2:
                        a[row2].remove(col2)
                        break

    """
    for x, i in enumerate(a):
        print (x)
        for j in i:
            print (j)
        #print()
    """
    """
    # add node frames to nodelist
    frames = []
    print ("Frames:")
    print ("level:", level)
    print ("a:",a)
    for row in range(level, 0, -1):

        for i, node in enumerate(a[row]):
            if node.parent:
                print ("Frame found:", node.parent, node)
                #if frame already added to the list ?
                frame = node.parent
                #remove node
                del a[row][i]
                if frame not in frames:
                    frames.append(frame)
                    # add frame to the same place than node was
                    a[row].insert(i, frame)

    pprint.pprint(a)
    """
    # return None
    ########################################

    if not arrange:
        nodelist = [j for i in a for j in i]
        nodes_odd(ntree, nodelist=nodelist)
        return None

    ########################################

    levelmax = level + 1
    level = 0
    values.x_last = 0

    while level < levelmax:

        values.average_y = 0
        nodes = [x for x in a[level]]
        # print ("level, nodes:", level, nodes)
        nodes_arrange(nodes, level)

        level = level + 1

    return None


###############################################################
def nodes_odd(ntree, nodelist):

    nodes = ntree.nodes
    for i in nodes:
        i.select = False

    a = [x for x in nodes if x not in nodelist]
    # print ("odd nodes:",a)
    for i in a:
        i.select = True


def nodes_arrange(nodelist, level):

    parents = []
    for node in nodelist:
        parents.append(node.parent)
        node.parent = None
        bpy.context.space_data.node_tree.nodes.update()

    # print ("nodes arrange def")
    # node x positions

    widthmax = max([x.dimensions.x for x in nodelist])
    xpos = values.x_last - (widthmax + values.margin_x) if level != 0 else 0
    # print ("nodelist, xpos", nodelist,xpos)
    values.x_last = xpos

    # node y positions
    x = 0
    y = 0

    for node in nodelist:

        if node.hide:
            hidey = (node.dimensions.y / 2) - 8
            y = y - hidey
        else:
            hidey = 0

        node.location.y = y
        y = y - values.margin_y - node.dimensions.y + hidey

        node.location.x = xpos  # if node.type != "FRAME" else xpos + 1200

    y = y + values.margin_y

    center = (0 + y) / 2
    values.average_y = center - values.average_y

    # for node in nodelist:

    # node.location.y -= values.average_y

    for i, node in enumerate(nodelist):
        node.parent = parents[i]


def nodetree_get(mat):

    return mat.node_tree.nodes


def nodes_center(ntree):

    bboxminx = []
    bboxmaxx = []
    bboxmaxy = []
    bboxminy = []

    for node in ntree.nodes:
        if not node.parent:
            bboxminx.append(node.location.x)
            bboxmaxx.append(node.location.x + node.dimensions.x)
            bboxmaxy.append(node.location.y)
            bboxminy.append(node.location.y - node.dimensions.y)

    # print ("bboxminy:",bboxminy)
    bboxminx = min(bboxminx)
    bboxmaxx = max(bboxmaxx)
    bboxminy = min(bboxminy)
    bboxmaxy = max(bboxmaxy)
    center_x = (bboxminx + bboxmaxx) / 2
    center_y = (bboxminy + bboxmaxy) / 2
    '''
    print ("minx:",bboxminx)
    print ("maxx:",bboxmaxx)
    print ("miny:",bboxminy)
    print ("maxy:",bboxmaxy)

    print ("bboxes:", bboxminx, bboxmaxx, bboxmaxy, bboxminy)
    print ("center x:",center_x)
    print ("center y:",center_y)
    '''

    for node in ntree.nodes:

        if not node.parent:
            node.location.x -= center_x
            node.location.y += -center_y


def register():
    bpy.types.Scene.nodemargin_x = bpy.props.IntProperty(default=60, update=nodemargin)
    bpy.types.Scene.nodemargin_y = bpy.props.IntProperty(default=20, update=nodemargin)
    bpy.types.Scene.node_center = bpy.props.BoolProperty(default=False, update=nodemargin)


def unregister():
    del bpy.types.Scene.nodemargin_x
    del bpy.types.Scene.nodemargin_y
    del bpy.types.Scene.node_center
