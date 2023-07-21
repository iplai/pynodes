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

   * - :py:obj:`PYNODES_PT_MAIN <pynodes.addon.PYNODES_PT_MAIN>`
     -
   * - :py:obj:`PYNODES_OT_ARRANGE <pynodes.addon.PYNODES_OT_ARRANGE>`
     - .. autodoc2-docstring:: pynodes.addon.PYNODES_OT_ARRANGE
          :parser: myst
          :summary:
   * - :py:obj:`PYNODES_OT_PURGE <pynodes.addon.PYNODES_OT_PURGE>`
     - .. autodoc2-docstring:: pynodes.addon.PYNODES_OT_PURGE
          :parser: myst
          :summary:
   * - :py:obj:`PYNODES_OT_RELOAD <pynodes.addon.PYNODES_OT_RELOAD>`
     - .. autodoc2-docstring:: pynodes.addon.PYNODES_OT_RELOAD
          :parser: myst
          :summary:
   * - :py:obj:`PYNODES_OT_select_all_reroute <pynodes.addon.PYNODES_OT_select_all_reroute>`
     - .. autodoc2-docstring:: pynodes.addon.PYNODES_OT_select_all_reroute
          :parser: myst
          :summary:
   * - :py:obj:`Column <pynodes.addon.Column>`
     - .. autodoc2-docstring:: pynodes.addon.Column
          :parser: myst
          :summary:

Functions
~~~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`get_active_tree <pynodes.addon.get_active_tree>`
     - .. autodoc2-docstring:: pynodes.addon.get_active_tree
          :parser: myst
          :summary:
   * - :py:obj:`is_frame <pynodes.addon.is_frame>`
     - .. autodoc2-docstring:: pynodes.addon.is_frame
          :parser: myst
          :summary:
   * - :py:obj:`is_linked_output <pynodes.addon.is_linked_output>`
     - .. autodoc2-docstring:: pynodes.addon.is_linked_output
          :parser: myst
          :summary:
   * - :py:obj:`is_linked_input <pynodes.addon.is_linked_input>`
     - .. autodoc2-docstring:: pynodes.addon.is_linked_input
          :parser: myst
          :summary:
   * - :py:obj:`match_frame_node <pynodes.addon.match_frame_node>`
     - .. autodoc2-docstring:: pynodes.addon.match_frame_node
          :parser: myst
          :summary:
   * - :py:obj:`arrange <pynodes.addon.arrange>`
     - .. autodoc2-docstring:: pynodes.addon.arrange
          :parser: myst
          :summary:
   * - :py:obj:`arrange_tree <pynodes.addon.arrange_tree>`
     - .. autodoc2-docstring:: pynodes.addon.arrange_tree
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

Data
~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`dev <pynodes.addon.dev>`
     - .. autodoc2-docstring:: pynodes.addon.dev
          :parser: myst
          :summary:

API
~~~

.. py:data:: dev
   :canonical: pynodes.addon.dev
   :value: True

   .. autodoc2-docstring:: pynodes.addon.dev
      :parser: myst

.. py:class:: PYNODES_PT_MAIN
   :canonical: pynodes.addon.PYNODES_PT_MAIN

   Bases: :py:obj:`bpy.types.Panel`

   .. py:attribute:: bl_label
      :canonical: pynodes.addon.PYNODES_PT_MAIN.bl_label
      :value: 'Arrange Nodes'

      .. autodoc2-docstring:: pynodes.addon.PYNODES_PT_MAIN.bl_label
         :parser: myst

   .. py:attribute:: bl_space_type
      :canonical: pynodes.addon.PYNODES_PT_MAIN.bl_space_type
      :value: 'NODE_EDITOR'

      .. autodoc2-docstring:: pynodes.addon.PYNODES_PT_MAIN.bl_space_type
         :parser: myst

   .. py:attribute:: bl_region_type
      :canonical: pynodes.addon.PYNODES_PT_MAIN.bl_region_type
      :value: 'UI'

      .. autodoc2-docstring:: pynodes.addon.PYNODES_PT_MAIN.bl_region_type
         :parser: myst

   .. py:attribute:: bl_category
      :canonical: pynodes.addon.PYNODES_PT_MAIN.bl_category
      :value: 'Pynodes'

      .. autodoc2-docstring:: pynodes.addon.PYNODES_PT_MAIN.bl_category
         :parser: myst

   .. py:method:: draw(context)
      :canonical: pynodes.addon.PYNODES_PT_MAIN.draw

.. py:class:: PYNODES_OT_ARRANGE
   :canonical: pynodes.addon.PYNODES_OT_ARRANGE

   Bases: :py:obj:`bpy.types.Operator`

   .. autodoc2-docstring:: pynodes.addon.PYNODES_OT_ARRANGE
      :parser: myst

   .. py:attribute:: bl_idname
      :canonical: pynodes.addon.PYNODES_OT_ARRANGE.bl_idname
      :value: 'node.pynodes_arrange'

      .. autodoc2-docstring:: pynodes.addon.PYNODES_OT_ARRANGE.bl_idname
         :parser: myst

   .. py:attribute:: bl_label
      :canonical: pynodes.addon.PYNODES_OT_ARRANGE.bl_label
      :value: 'Arrange'

      .. autodoc2-docstring:: pynodes.addon.PYNODES_OT_ARRANGE.bl_label
         :parser: myst

   .. py:method:: execute(context)
      :canonical: pynodes.addon.PYNODES_OT_ARRANGE.execute

   .. py:method:: invoke(context, value)
      :canonical: pynodes.addon.PYNODES_OT_ARRANGE.invoke

   .. py:method:: poll(context: bpy.types.Context)
      :canonical: pynodes.addon.PYNODES_OT_ARRANGE.poll
      :classmethod:

.. py:class:: PYNODES_OT_PURGE
   :canonical: pynodes.addon.PYNODES_OT_PURGE

   Bases: :py:obj:`bpy.types.Operator`

   .. autodoc2-docstring:: pynodes.addon.PYNODES_OT_PURGE
      :parser: myst

   .. py:attribute:: bl_idname
      :canonical: pynodes.addon.PYNODES_OT_PURGE.bl_idname
      :value: 'outliner.orphans_purge_recursive'

      .. autodoc2-docstring:: pynodes.addon.PYNODES_OT_PURGE.bl_idname
         :parser: myst

   .. py:attribute:: bl_label
      :canonical: pynodes.addon.PYNODES_OT_PURGE.bl_label
      :value: 'Purge Orphan'

      .. autodoc2-docstring:: pynodes.addon.PYNODES_OT_PURGE.bl_label
         :parser: myst

   .. py:method:: execute(context)
      :canonical: pynodes.addon.PYNODES_OT_PURGE.execute

.. py:class:: PYNODES_OT_RELOAD
   :canonical: pynodes.addon.PYNODES_OT_RELOAD

   Bases: :py:obj:`bpy.types.Operator`

   .. autodoc2-docstring:: pynodes.addon.PYNODES_OT_RELOAD
      :parser: myst

   .. py:attribute:: bl_idname
      :canonical: pynodes.addon.PYNODES_OT_RELOAD.bl_idname
      :value: 'node.pynodes_reload'

      .. autodoc2-docstring:: pynodes.addon.PYNODES_OT_RELOAD.bl_idname
         :parser: myst

   .. py:attribute:: bl_label
      :canonical: pynodes.addon.PYNODES_OT_RELOAD.bl_label
      :value: 'Reload PyNodes'

      .. autodoc2-docstring:: pynodes.addon.PYNODES_OT_RELOAD.bl_label
         :parser: myst

   .. py:method:: execute(context)
      :canonical: pynodes.addon.PYNODES_OT_RELOAD.execute

.. py:class:: PYNODES_OT_select_all_reroute
   :canonical: pynodes.addon.PYNODES_OT_select_all_reroute

   Bases: :py:obj:`bpy.types.Operator`

   .. autodoc2-docstring:: pynodes.addon.PYNODES_OT_select_all_reroute
      :parser: myst

   .. py:attribute:: bl_idname
      :canonical: pynodes.addon.PYNODES_OT_select_all_reroute.bl_idname
      :value: 'node.pynodes_select_all_reroute'

      .. autodoc2-docstring:: pynodes.addon.PYNODES_OT_select_all_reroute.bl_idname
         :parser: myst

   .. py:attribute:: bl_label
      :canonical: pynodes.addon.PYNODES_OT_select_all_reroute.bl_label
      :value: 'Select all Reroute Nodes'

      .. autodoc2-docstring:: pynodes.addon.PYNODES_OT_select_all_reroute.bl_label
         :parser: myst

   .. py:method:: execute(context)
      :canonical: pynodes.addon.PYNODES_OT_select_all_reroute.execute

.. py:class:: Column()
   :canonical: pynodes.addon.Column

   .. autodoc2-docstring:: pynodes.addon.Column
      :parser: myst

   .. rubric:: Initialization

   .. autodoc2-docstring:: pynodes.addon.Column.__init__
      :parser: myst

   .. py:property:: height_with_offset
      :canonical: pynodes.addon.Column.height_with_offset

      .. autodoc2-docstring:: pynodes.addon.Column.height_with_offset
         :parser: myst

.. py:function:: get_active_tree(context: bpy.types.Context) -> bpy.types.NodeTree | None
   :canonical: pynodes.addon.get_active_tree

   .. autodoc2-docstring:: pynodes.addon.get_active_tree
      :parser: myst

.. py:function:: is_frame(node: bpy.types.Node)
   :canonical: pynodes.addon.is_frame

   .. autodoc2-docstring:: pynodes.addon.is_frame
      :parser: myst

.. py:function:: is_linked_output(node: bpy.types.Node)
   :canonical: pynodes.addon.is_linked_output

   .. autodoc2-docstring:: pynodes.addon.is_linked_output
      :parser: myst

.. py:function:: is_linked_input(node: bpy.types.Node)
   :canonical: pynodes.addon.is_linked_input

   .. autodoc2-docstring:: pynodes.addon.is_linked_input
      :parser: myst

.. py:function:: match_frame_node(node: bpy.types.Node | None, frame_child_nodes: list[bpy.types.Node])
   :canonical: pynodes.addon.match_frame_node

   .. autodoc2-docstring:: pynodes.addon.match_frame_node
      :parser: myst

.. py:function:: arrange(self, context: bpy.types.Context)
   :canonical: pynodes.addon.arrange

   .. autodoc2-docstring:: pynodes.addon.arrange
      :parser: myst

.. py:function:: arrange_tree(btree: bpy.types.NodeTree, margin_x=40, margin_y=20, frame_margin_x=10, frame_margin_y=10, node_center1=True, node_center2=True, only_selected_frame=False, reverse_single_link_sequence=False)
   :canonical: pynodes.addon.arrange_tree

   .. autodoc2-docstring:: pynodes.addon.arrange_tree
      :parser: myst

.. py:function:: register()
   :canonical: pynodes.addon.register

   .. autodoc2-docstring:: pynodes.addon.register
      :parser: myst

.. py:function:: unregister()
   :canonical: pynodes.addon.unregister

   .. autodoc2-docstring:: pynodes.addon.unregister
      :parser: myst
