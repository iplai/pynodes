:py:mod:`pynodes.scene`
=======================

.. py:module:: pynodes.scene

.. autodoc2-docstring:: pynodes.scene
   :parser: myst
   :allowtitles:

Module Contents
---------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`ObjType <pynodes.scene.ObjType>`
     -
   * - :py:obj:`O <pynodes.scene.O>`
     -
   * - :py:obj:`Mod <pynodes.scene.Mod>`
     -
   * - :py:obj:`Mat <pynodes.scene.Mat>`
     -
   * - :py:obj:`Key <pynodes.scene.Key>`
     - .. autodoc2-docstring:: pynodes.scene.Key
          :parser: myst
          :summary:
   * - :py:obj:`Tree <pynodes.scene.Tree>`
     - .. autodoc2-docstring:: pynodes.scene.Tree
          :parser: myst
          :summary:

API
~~~

.. py:class:: ObjType
   :canonical: pynodes.scene.ObjType

   Bases: :py:obj:`enum.Enum`

   .. py:method:: __matmul__(name: str)
      :canonical: pynodes.scene.ObjType.__matmul__

      .. autodoc2-docstring:: pynodes.scene.ObjType.__matmul__
         :parser: myst

.. py:class:: O
   :canonical: pynodes.scene.O

   Bases: :py:obj:`pynodes.scene.ObjType`

   .. py:attribute:: plane
      :canonical: pynodes.scene.O.plane
      :value: 'bpy.ops.mesh.primitive_plane_add()'

      .. autodoc2-docstring:: pynodes.scene.O.plane
         :parser: myst

   .. py:attribute:: cube
      :canonical: pynodes.scene.O.cube
      :value: 'bpy.ops.mesh.primitive_cube_add()'

      .. autodoc2-docstring:: pynodes.scene.O.cube
         :parser: myst

   .. py:attribute:: ico_sphere
      :canonical: pynodes.scene.O.ico_sphere
      :value: 'bpy.ops.mesh.primitive_ico_sphere_add()'

      .. autodoc2-docstring:: pynodes.scene.O.ico_sphere
         :parser: myst

   .. py:attribute:: monkey
      :canonical: pynodes.scene.O.monkey
      :value: None

      .. autodoc2-docstring:: pynodes.scene.O.monkey
         :parser: myst

   .. py:attribute:: circle
      :canonical: pynodes.scene.O.circle
      :value: None

      .. autodoc2-docstring:: pynodes.scene.O.circle
         :parser: myst

   .. py:attribute:: cone
      :canonical: pynodes.scene.O.cone
      :value: None

      .. autodoc2-docstring:: pynodes.scene.O.cone
         :parser: myst

   .. py:attribute:: nurbs_path
      :canonical: pynodes.scene.O.nurbs_path
      :value: None

      .. autodoc2-docstring:: pynodes.scene.O.nurbs_path
         :parser: myst

.. py:class:: Mod
   :canonical: pynodes.scene.Mod

   Bases: :py:obj:`pynodes.scene.ObjType`

   .. py:attribute:: geometry_nodes
      :canonical: pynodes.scene.Mod.geometry_nodes
      :value: 'NODES'

      .. autodoc2-docstring:: pynodes.scene.Mod.geometry_nodes
         :parser: myst

   .. py:attribute:: bevel
      :canonical: pynodes.scene.Mod.bevel
      :value: 'BEVEL'

      .. autodoc2-docstring:: pynodes.scene.Mod.bevel
         :parser: myst

   .. py:attribute:: subdivision
      :canonical: pynodes.scene.Mod.subdivision
      :value: 'SUBSURF'

      .. autodoc2-docstring:: pynodes.scene.Mod.subdivision
         :parser: myst

.. py:class:: Mat
   :canonical: pynodes.scene.Mat

   Bases: :py:obj:`pynodes.scene.ObjType`

   .. py:attribute:: slots
      :canonical: pynodes.scene.Mat.slots
      :value: None

      .. autodoc2-docstring:: pynodes.scene.Mat.slots
         :parser: myst

.. py:class:: Key(type: pynodes.scene.ObjType, name: str)
   :canonical: pynodes.scene.Key

   .. autodoc2-docstring:: pynodes.scene.Key
      :parser: myst

   .. rubric:: Initialization

   .. autodoc2-docstring:: pynodes.scene.Key.__init__
      :parser: myst

   .. py:method:: __eq__(__o: object) -> bool
      :canonical: pynodes.scene.Key.__eq__

   .. py:method:: __hash__() -> int
      :canonical: pynodes.scene.Key.__hash__

.. py:class:: Tree(data: dict[pynodes.scene.ObjType | pynodes.scene.Key | bpy.types.Object, dict])
   :canonical: pynodes.scene.Tree

   .. autodoc2-docstring:: pynodes.scene.Tree
      :parser: myst

   .. rubric:: Initialization

   .. autodoc2-docstring:: pynodes.scene.Tree.__init__
      :parser: myst

   .. py:method:: __getitem__(key)
      :canonical: pynodes.scene.Tree.__getitem__

      .. autodoc2-docstring:: pynodes.scene.Tree.__getitem__
         :parser: myst

   .. py:method:: load(clear_animation=True)
      :canonical: pynodes.scene.Tree.load

      .. autodoc2-docstring:: pynodes.scene.Tree.load
         :parser: myst

   .. py:method:: parse_modifier(k: pynodes.scene.Key, v: dict[str], obj: bpy.types.Object)
      :canonical: pynodes.scene.Tree.parse_modifier

      .. autodoc2-docstring:: pynodes.scene.Tree.parse_modifier
         :parser: myst

   .. py:method:: parse_mat_slots(obj: bpy.types.Object, material_names: list[str])
      :canonical: pynodes.scene.Tree.parse_mat_slots

      .. autodoc2-docstring:: pynodes.scene.Tree.parse_mat_slots
         :parser: myst
