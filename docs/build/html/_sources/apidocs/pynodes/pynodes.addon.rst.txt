:py:mod:`pynodes.addon`
=======================

.. py:module:: pynodes.addon

.. autodoc2-docstring:: pynodes.addon
   :parser: myst
   :allowtitles:

Module Contents
---------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`values <pynodes.addon.values>`
     - .. autodoc2-docstring:: pynodes.addon.values
          :parser: myst
          :summary:
   * - :py:obj:`NA_PT_NodePanel <pynodes.addon.NA_PT_NodePanel>`
     -
   * - :py:obj:`NA_OT_NodeButton <pynodes.addon.NA_OT_NodeButton>`
     - .. autodoc2-docstring:: pynodes.addon.NA_OT_NodeButton
          :parser: myst
          :summary:
   * - :py:obj:`NA_OT_NodeButton2 <pynodes.addon.NA_OT_NodeButton2>`
     - .. autodoc2-docstring:: pynodes.addon.NA_OT_NodeButton2
          :parser: myst
          :summary:
   * - :py:obj:`NA_OT_NodeButtonOdd <pynodes.addon.NA_OT_NodeButtonOdd>`
     - .. autodoc2-docstring:: pynodes.addon.NA_OT_NodeButtonOdd
          :parser: myst
          :summary:
   * - :py:obj:`PurgeOrphanRecursive <pynodes.addon.PurgeOrphanRecursive>`
     - .. autodoc2-docstring:: pynodes.addon.PurgeOrphanRecursive
          :parser: myst
          :summary:
   * - :py:obj:`NA_OT_ArrangeNodesOp <pynodes.addon.NA_OT_ArrangeNodesOp>`
     -

Functions
~~~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`get_nodes_from_category <pynodes.addon.get_nodes_from_category>`
     - .. autodoc2-docstring:: pynodes.addon.get_nodes_from_category
          :parser: myst
          :summary:
   * - :py:obj:`get_first_enabled_output <pynodes.addon.get_first_enabled_output>`
     - .. autodoc2-docstring:: pynodes.addon.get_first_enabled_output
          :parser: myst
          :summary:
   * - :py:obj:`is_visible_socket <pynodes.addon.is_visible_socket>`
     - .. autodoc2-docstring:: pynodes.addon.is_visible_socket
          :parser: myst
          :summary:
   * - :py:obj:`node_mid_pt <pynodes.addon.node_mid_pt>`
     - .. autodoc2-docstring:: pynodes.addon.node_mid_pt
          :parser: myst
          :summary:
   * - :py:obj:`abs_node_location <pynodes.addon.abs_node_location>`
     - .. autodoc2-docstring:: pynodes.addon.abs_node_location
          :parser: myst
          :summary:
   * - :py:obj:`get_active_tree <pynodes.addon.get_active_tree>`
     - .. autodoc2-docstring:: pynodes.addon.get_active_tree
          :parser: myst
          :summary:
   * - :py:obj:`get_group_output_node <pynodes.addon.get_group_output_node>`
     - .. autodoc2-docstring:: pynodes.addon.get_group_output_node
          :parser: myst
          :summary:
   * - :py:obj:`nodemargin <pynodes.addon.nodemargin>`
     - .. autodoc2-docstring:: pynodes.addon.nodemargin
          :parser: myst
          :summary:
   * - :py:obj:`outputnode_search <pynodes.addon.outputnode_search>`
     - .. autodoc2-docstring:: pynodes.addon.outputnode_search
          :parser: myst
          :summary:
   * - :py:obj:`nodes_iterate <pynodes.addon.nodes_iterate>`
     - .. autodoc2-docstring:: pynodes.addon.nodes_iterate
          :parser: myst
          :summary:
   * - :py:obj:`nodes_odd <pynodes.addon.nodes_odd>`
     - .. autodoc2-docstring:: pynodes.addon.nodes_odd
          :parser: myst
          :summary:
   * - :py:obj:`nodes_arrange <pynodes.addon.nodes_arrange>`
     - .. autodoc2-docstring:: pynodes.addon.nodes_arrange
          :parser: myst
          :summary:
   * - :py:obj:`nodetree_get <pynodes.addon.nodetree_get>`
     - .. autodoc2-docstring:: pynodes.addon.nodetree_get
          :parser: myst
          :summary:
   * - :py:obj:`nodes_center <pynodes.addon.nodes_center>`
     - .. autodoc2-docstring:: pynodes.addon.nodes_center
          :parser: myst
          :summary:
   * - :py:obj:`register <pynodes.addon.register>`
     - .. autodoc2-docstring:: pynodes.addon.register
          :parser: myst
          :summary:
   * - :py:obj:`unregister <pynodes.addon.unregister>`
     - .. autodoc2-docstring:: pynodes.addon.unregister
          :parser: myst
          :summary:

API
~~~

.. py:function:: get_nodes_from_category(category_name, context)
   :canonical: pynodes.addon.get_nodes_from_category

   .. autodoc2-docstring:: pynodes.addon.get_nodes_from_category
      :parser: myst

.. py:function:: get_first_enabled_output(node: bpy.types.Node)
   :canonical: pynodes.addon.get_first_enabled_output

   .. autodoc2-docstring:: pynodes.addon.get_first_enabled_output
      :parser: myst

.. py:function:: is_visible_socket(socket: bpy.types.NodeSocket)
   :canonical: pynodes.addon.is_visible_socket

   .. autodoc2-docstring:: pynodes.addon.is_visible_socket
      :parser: myst

.. py:function:: node_mid_pt(node: bpy.types.Node, axis)
   :canonical: pynodes.addon.node_mid_pt

   .. autodoc2-docstring:: pynodes.addon.node_mid_pt
      :parser: myst

.. py:function:: abs_node_location(node: bpy.types.Node)
   :canonical: pynodes.addon.abs_node_location

   .. autodoc2-docstring:: pynodes.addon.abs_node_location
      :parser: myst

.. py:function:: get_active_tree(context: bpy.types.Context)
   :canonical: pynodes.addon.get_active_tree

   .. autodoc2-docstring:: pynodes.addon.get_active_tree
      :parser: myst

.. py:function:: get_group_output_node(tree: bpy.types.NodeTree)
   :canonical: pynodes.addon.get_group_output_node

   .. autodoc2-docstring:: pynodes.addon.get_group_output_node
      :parser: myst

.. py:class:: values
   :canonical: pynodes.addon.values

   .. autodoc2-docstring:: pynodes.addon.values
      :parser: myst

   .. py:attribute:: average_y
      :canonical: pynodes.addon.values.average_y
      :value: 0

      .. autodoc2-docstring:: pynodes.addon.values.average_y
         :parser: myst

   .. py:attribute:: x_last
      :canonical: pynodes.addon.values.x_last
      :value: 0

      .. autodoc2-docstring:: pynodes.addon.values.x_last
         :parser: myst

   .. py:attribute:: margin_x
      :canonical: pynodes.addon.values.margin_x
      :value: 100

      .. autodoc2-docstring:: pynodes.addon.values.margin_x
         :parser: myst

   .. py:attribute:: margin_y
      :canonical: pynodes.addon.values.margin_y
      :value: 20

      .. autodoc2-docstring:: pynodes.addon.values.margin_y
         :parser: myst

   .. py:attribute:: mat_name
      :canonical: pynodes.addon.values.mat_name
      :value: <Multiline-String>

      .. autodoc2-docstring:: pynodes.addon.values.mat_name
         :parser: myst

.. py:class:: NA_PT_NodePanel
   :canonical: pynodes.addon.NA_PT_NodePanel

   Bases: :py:obj:`bpy.types.Panel`

   .. py:attribute:: bl_label
      :canonical: pynodes.addon.NA_PT_NodePanel.bl_label
      :value: 'Node Arrange'

      .. autodoc2-docstring:: pynodes.addon.NA_PT_NodePanel.bl_label
         :parser: myst

   .. py:attribute:: bl_space_type
      :canonical: pynodes.addon.NA_PT_NodePanel.bl_space_type
      :value: 'NODE_EDITOR'

      .. autodoc2-docstring:: pynodes.addon.NA_PT_NodePanel.bl_space_type
         :parser: myst

   .. py:attribute:: bl_region_type
      :canonical: pynodes.addon.NA_PT_NodePanel.bl_region_type
      :value: 'UI'

      .. autodoc2-docstring:: pynodes.addon.NA_PT_NodePanel.bl_region_type
         :parser: myst

   .. py:attribute:: bl_category
      :canonical: pynodes.addon.NA_PT_NodePanel.bl_category
      :value: 'Pynodes'

      .. autodoc2-docstring:: pynodes.addon.NA_PT_NodePanel.bl_category
         :parser: myst

   .. py:method:: draw(context)
      :canonical: pynodes.addon.NA_PT_NodePanel.draw

.. py:class:: NA_OT_NodeButton
   :canonical: pynodes.addon.NA_OT_NodeButton

   Bases: :py:obj:`bpy.types.Operator`

   .. autodoc2-docstring:: pynodes.addon.NA_OT_NodeButton
      :parser: myst

   .. py:attribute:: bl_idname
      :canonical: pynodes.addon.NA_OT_NodeButton.bl_idname
      :value: 'node.arrange'

      .. autodoc2-docstring:: pynodes.addon.NA_OT_NodeButton.bl_idname
         :parser: myst

   .. py:attribute:: bl_label
      :canonical: pynodes.addon.NA_OT_NodeButton.bl_label
      :value: 'Arrange 1'

      .. autodoc2-docstring:: pynodes.addon.NA_OT_NodeButton.bl_label
         :parser: myst

   .. py:method:: execute(context)
      :canonical: pynodes.addon.NA_OT_NodeButton.execute

   .. py:method:: invoke(context, value)
      :canonical: pynodes.addon.NA_OT_NodeButton.invoke

.. py:class:: NA_OT_NodeButton2
   :canonical: pynodes.addon.NA_OT_NodeButton2

   Bases: :py:obj:`bpy.types.Operator`

   .. autodoc2-docstring:: pynodes.addon.NA_OT_NodeButton2
      :parser: myst

   .. py:attribute:: bl_idname
      :canonical: pynodes.addon.NA_OT_NodeButton2.bl_idname
      :value: 'node.arrange2'

      .. autodoc2-docstring:: pynodes.addon.NA_OT_NodeButton2.bl_idname
         :parser: myst

   .. py:attribute:: bl_label
      :canonical: pynodes.addon.NA_OT_NodeButton2.bl_label
      :value: 'Arrange 2'

      .. autodoc2-docstring:: pynodes.addon.NA_OT_NodeButton2.bl_label
         :parser: myst

   .. py:method:: execute(context)
      :canonical: pynodes.addon.NA_OT_NodeButton2.execute

.. py:class:: NA_OT_NodeButtonOdd
   :canonical: pynodes.addon.NA_OT_NodeButtonOdd

   Bases: :py:obj:`bpy.types.Operator`

   .. autodoc2-docstring:: pynodes.addon.NA_OT_NodeButtonOdd
      :parser: myst

   .. py:attribute:: bl_idname
      :canonical: pynodes.addon.NA_OT_NodeButtonOdd.bl_idname
      :value: 'pynodes.select_unlinked'

      .. autodoc2-docstring:: pynodes.addon.NA_OT_NodeButtonOdd.bl_idname
         :parser: myst

   .. py:attribute:: bl_label
      :canonical: pynodes.addon.NA_OT_NodeButtonOdd.bl_label
      :value: 'Select Unlinked'

      .. autodoc2-docstring:: pynodes.addon.NA_OT_NodeButtonOdd.bl_label
         :parser: myst

   .. py:method:: execute(context)
      :canonical: pynodes.addon.NA_OT_NodeButtonOdd.execute

.. py:class:: PurgeOrphanRecursive
   :canonical: pynodes.addon.PurgeOrphanRecursive

   Bases: :py:obj:`bpy.types.Operator`

   .. autodoc2-docstring:: pynodes.addon.PurgeOrphanRecursive
      :parser: myst

   .. py:attribute:: bl_idname
      :canonical: pynodes.addon.PurgeOrphanRecursive.bl_idname
      :value: 'outliner.orphans_purge_recursive'

      .. autodoc2-docstring:: pynodes.addon.PurgeOrphanRecursive.bl_idname
         :parser: myst

   .. py:attribute:: bl_label
      :canonical: pynodes.addon.PurgeOrphanRecursive.bl_label
      :value: 'Purge Orphan'

      .. autodoc2-docstring:: pynodes.addon.PurgeOrphanRecursive.bl_label
         :parser: myst

   .. py:method:: execute(context)
      :canonical: pynodes.addon.PurgeOrphanRecursive.execute

.. py:function:: nodemargin(self, context: bpy.types.Context)
   :canonical: pynodes.addon.nodemargin

   .. autodoc2-docstring:: pynodes.addon.nodemargin
      :parser: myst

.. py:class:: NA_OT_ArrangeNodesOp
   :canonical: pynodes.addon.NA_OT_ArrangeNodesOp

   Bases: :py:obj:`bpy.types.Operator`

   .. py:attribute:: bl_idname
      :canonical: pynodes.addon.NA_OT_ArrangeNodesOp.bl_idname
      :value: 'node.arrange_nodetree'

      .. autodoc2-docstring:: pynodes.addon.NA_OT_ArrangeNodesOp.bl_idname
         :parser: myst

   .. py:attribute:: bl_label
      :canonical: pynodes.addon.NA_OT_ArrangeNodesOp.bl_label
      :value: 'Nodes Private Op'

      .. autodoc2-docstring:: pynodes.addon.NA_OT_ArrangeNodesOp.bl_label
         :parser: myst

   .. py:attribute:: mat_name
      :canonical: pynodes.addon.NA_OT_ArrangeNodesOp.mat_name
      :type: bpy.props.StringProperty()
      :value: None

      .. autodoc2-docstring:: pynodes.addon.NA_OT_ArrangeNodesOp.mat_name
         :parser: myst

   .. py:attribute:: margin_x
      :canonical: pynodes.addon.NA_OT_ArrangeNodesOp.margin_x
      :type: bpy.props.IntProperty(default=120)
      :value: None

      .. autodoc2-docstring:: pynodes.addon.NA_OT_ArrangeNodesOp.margin_x
         :parser: myst

   .. py:attribute:: margin_y
      :canonical: pynodes.addon.NA_OT_ArrangeNodesOp.margin_y
      :type: bpy.props.IntProperty(default=120)
      :value: None

      .. autodoc2-docstring:: pynodes.addon.NA_OT_ArrangeNodesOp.margin_y
         :parser: myst

   .. py:method:: nodemargin2(context)
      :canonical: pynodes.addon.NA_OT_ArrangeNodesOp.nodemargin2

      .. autodoc2-docstring:: pynodes.addon.NA_OT_ArrangeNodesOp.nodemargin2
         :parser: myst

   .. py:method:: execute(context)
      :canonical: pynodes.addon.NA_OT_ArrangeNodesOp.execute

.. py:function:: outputnode_search(ntree)
   :canonical: pynodes.addon.outputnode_search

   .. autodoc2-docstring:: pynodes.addon.outputnode_search
      :parser: myst

.. py:function:: nodes_iterate(ntree, arrange=True)
   :canonical: pynodes.addon.nodes_iterate

   .. autodoc2-docstring:: pynodes.addon.nodes_iterate
      :parser: myst

.. py:function:: nodes_odd(ntree, nodelist)
   :canonical: pynodes.addon.nodes_odd

   .. autodoc2-docstring:: pynodes.addon.nodes_odd
      :parser: myst

.. py:function:: nodes_arrange(nodelist, level)
   :canonical: pynodes.addon.nodes_arrange

   .. autodoc2-docstring:: pynodes.addon.nodes_arrange
      :parser: myst

.. py:function:: nodetree_get(mat)
   :canonical: pynodes.addon.nodetree_get

   .. autodoc2-docstring:: pynodes.addon.nodetree_get
      :parser: myst

.. py:function:: nodes_center(ntree)
   :canonical: pynodes.addon.nodes_center

   .. autodoc2-docstring:: pynodes.addon.nodes_center
      :parser: myst

.. py:function:: register()
   :canonical: pynodes.addon.register

   .. autodoc2-docstring:: pynodes.addon.register
      :parser: myst

.. py:function:: unregister()
   :canonical: pynodes.addon.unregister

   .. autodoc2-docstring:: pynodes.addon.unregister
      :parser: myst
