:py:mod:`pynodes.core`
======================

.. py:module:: pynodes.core

.. autodoc2-docstring:: pynodes.core
   :parser: myst
   :allowtitles:

Module Contents
---------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`NodeWraper <pynodes.core.NodeWraper>`
     - .. autodoc2-docstring:: pynodes.core.NodeWraper
          :parser: myst
          :summary:
   * - :py:obj:`SocketWraper <pynodes.core.SocketWraper>`
     - .. autodoc2-docstring:: pynodes.core.SocketWraper
          :parser: myst
          :summary:
   * - :py:obj:`Socket <pynodes.core.Socket>`
     - .. autodoc2-docstring:: pynodes.core.Socket
          :parser: myst
          :summary:
   * - :py:obj:`Tree <pynodes.core.Tree>`
     - .. autodoc2-docstring:: pynodes.core.Tree
          :parser: myst
          :summary:
   * - :py:obj:`Group <pynodes.core.Group>`
     - .. autodoc2-docstring:: pynodes.core.Group
          :parser: myst
          :summary:
   * - :py:obj:`Frame <pynodes.core.Frame>`
     - .. autodoc2-docstring:: pynodes.core.Frame
          :parser: myst
          :summary:
   * - :py:obj:`Script <pynodes.core.Script>`
     - .. autodoc2-docstring:: pynodes.core.Script
          :parser: myst
          :summary:

Functions
~~~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`new_node <pynodes.core.new_node>`
     - .. autodoc2-docstring:: pynodes.core.new_node
          :parser: myst
          :summary:
   * - :py:obj:`new_link <pynodes.core.new_link>`
     - .. autodoc2-docstring:: pynodes.core.new_link
          :parser: myst
          :summary:
   * - :py:obj:`update_modifier <pynodes.core.update_modifier>`
     - .. autodoc2-docstring:: pynodes.core.update_modifier
          :parser: myst
          :summary:
   * - :py:obj:`convert_param_name <pynodes.core.convert_param_name>`
     - .. autodoc2-docstring:: pynodes.core.convert_param_name
          :parser: myst
          :summary:
   * - :py:obj:`get_param_name <pynodes.core.get_param_name>`
     - .. autodoc2-docstring:: pynodes.core.get_param_name
          :parser: myst
          :summary:
   * - :py:obj:`dispath_tree <pynodes.core.dispath_tree>`
     - .. autodoc2-docstring:: pynodes.core.dispath_tree
          :parser: myst
          :summary:
   * - :py:obj:`tree <pynodes.core.tree>`
     - .. autodoc2-docstring:: pynodes.core.tree
          :parser: myst
          :summary:
   * - :py:obj:`frame <pynodes.core.frame>`
     - .. autodoc2-docstring:: pynodes.core.frame
          :parser: myst
          :summary:
   * - :py:obj:`reload <pynodes.core.reload>`
     - .. autodoc2-docstring:: pynodes.core.reload
          :parser: myst
          :summary:

Data
~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`Param <pynodes.core.Param>`
     - .. autodoc2-docstring:: pynodes.core.Param
          :parser: myst
          :summary:
   * - :py:obj:`RT <pynodes.core.RT>`
     - .. autodoc2-docstring:: pynodes.core.RT
          :parser: myst
          :summary:

API
~~~

.. py:class:: NodeWraper(bnode: bpy.types.Node)
   :canonical: pynodes.core.NodeWraper

   .. autodoc2-docstring:: pynodes.core.NodeWraper
      :parser: myst

   .. rubric:: Initialization

   .. autodoc2-docstring:: pynodes.core.NodeWraper.__init__
      :parser: myst

   .. py:property:: outputs
      :canonical: pynodes.core.NodeWraper.outputs

      .. autodoc2-docstring:: pynodes.core.NodeWraper.outputs
         :parser: myst

   .. py:property:: inputs
      :canonical: pynodes.core.NodeWraper.inputs

      .. autodoc2-docstring:: pynodes.core.NodeWraper.inputs
         :parser: myst

   .. py:property:: color
      :canonical: pynodes.core.NodeWraper.color

      .. autodoc2-docstring:: pynodes.core.NodeWraper.color
         :parser: myst

   .. py:property:: label
      :canonical: pynodes.core.NodeWraper.label
      :type: str

      .. autodoc2-docstring:: pynodes.core.NodeWraper.label
         :parser: myst

   .. py:method:: plug_inputs(inputs_all: list[tuple])
      :canonical: pynodes.core.NodeWraper.plug_inputs

      .. autodoc2-docstring:: pynodes.core.NodeWraper.plug_inputs
         :parser: myst

   .. py:method:: __setitem__(key: str, value)
      :canonical: pynodes.core.NodeWraper.__setitem__

      .. autodoc2-docstring:: pynodes.core.NodeWraper.__setitem__
         :parser: myst

.. py:class:: SocketWraper(bsocket: bpy.types.NodeSocket)
   :canonical: pynodes.core.SocketWraper

   .. autodoc2-docstring:: pynodes.core.SocketWraper
      :parser: myst

   .. rubric:: Initialization

   .. autodoc2-docstring:: pynodes.core.SocketWraper.__init__
      :parser: myst

   .. py:property:: default_value
      :canonical: pynodes.core.SocketWraper.default_value

      .. autodoc2-docstring:: pynodes.core.SocketWraper.default_value
         :parser: myst

.. py:class:: Socket(bsocket: bpy.types.NodeSocket)
   :canonical: pynodes.core.Socket

   Bases: :py:obj:`pynodes.core.SocketWraper`

   .. autodoc2-docstring:: pynodes.core.Socket
      :parser: myst

   .. rubric:: Initialization

   .. autodoc2-docstring:: pynodes.core.Socket.__init__
      :parser: myst

   .. py:attribute:: bl_idname
      :canonical: pynodes.core.Socket.bl_idname
      :value: 'NodeSocket'

      .. autodoc2-docstring:: pynodes.core.Socket.bl_idname
         :parser: myst

   .. py:property:: node
      :canonical: pynodes.core.Socket.node

      .. autodoc2-docstring:: pynodes.core.Socket.node
         :parser: myst

   .. py:method:: __call__(name: str)
      :canonical: pynodes.core.Socket.__call__

      .. autodoc2-docstring:: pynodes.core.Socket.__call__
         :parser: myst

   .. py:method:: __setitem__(key: str, value)
      :canonical: pynodes.core.Socket.__setitem__

      .. autodoc2-docstring:: pynodes.core.Socket.__setitem__
         :parser: myst

   .. py:property:: name
      :canonical: pynodes.core.Socket.name

      .. autodoc2-docstring:: pynodes.core.Socket.name
         :parser: myst

   .. py:method:: link_tree_output(index: int = None)
      :canonical: pynodes.core.Socket.link_tree_output

      .. autodoc2-docstring:: pynodes.core.Socket.link_tree_output
         :parser: myst

   .. py:method:: func_ret_to_tree_output()
      :canonical: pynodes.core.Socket.func_ret_to_tree_output

      .. autodoc2-docstring:: pynodes.core.Socket.func_ret_to_tree_output
         :parser: myst

   .. py:property:: linked_to_group_output
      :canonical: pynodes.core.Socket.linked_to_group_output

      .. autodoc2-docstring:: pynodes.core.Socket.linked_to_group_output
         :parser: myst

   .. py:method:: Input(default=None, name=None, min=None, max=None, description=None, bl_idname=None)
      :canonical: pynodes.core.Socket.Input
      :classmethod:

      .. autodoc2-docstring:: pynodes.core.Socket.Input
         :parser: myst

   .. py:property:: Float
      :canonical: pynodes.core.Socket.Float

      .. autodoc2-docstring:: pynodes.core.Socket.Float
         :parser: myst

   .. py:property:: Integer
      :canonical: pynodes.core.Socket.Integer

      .. autodoc2-docstring:: pynodes.core.Socket.Integer
         :parser: myst

   .. py:property:: Boolean
      :canonical: pynodes.core.Socket.Boolean

      .. autodoc2-docstring:: pynodes.core.Socket.Boolean
         :parser: myst

   .. py:property:: Vector
      :canonical: pynodes.core.Socket.Vector

      .. autodoc2-docstring:: pynodes.core.Socket.Vector
         :parser: myst

   .. py:property:: Color
      :canonical: pynodes.core.Socket.Color

      .. autodoc2-docstring:: pynodes.core.Socket.Color
         :parser: myst

   .. py:property:: Geometry
      :canonical: pynodes.core.Socket.Geometry

      .. autodoc2-docstring:: pynodes.core.Socket.Geometry
         :parser: myst

   .. py:property:: Mesh
      :canonical: pynodes.core.Socket.Mesh

      .. autodoc2-docstring:: pynodes.core.Socket.Mesh
         :parser: myst

   .. py:property:: Points
      :canonical: pynodes.core.Socket.Points

      .. autodoc2-docstring:: pynodes.core.Socket.Points
         :parser: myst

   .. py:property:: Volume
      :canonical: pynodes.core.Socket.Volume

      .. autodoc2-docstring:: pynodes.core.Socket.Volume
         :parser: myst

   .. py:property:: Instances
      :canonical: pynodes.core.Socket.Instances

      .. autodoc2-docstring:: pynodes.core.Socket.Instances
         :parser: myst

   .. py:property:: Curve
      :canonical: pynodes.core.Socket.Curve

      .. autodoc2-docstring:: pynodes.core.Socket.Curve
         :parser: myst

   .. py:property:: String
      :canonical: pynodes.core.Socket.String

      .. autodoc2-docstring:: pynodes.core.Socket.String
         :parser: myst

   .. py:property:: Object
      :canonical: pynodes.core.Socket.Object

      .. autodoc2-docstring:: pynodes.core.Socket.Object
         :parser: myst

   .. py:property:: Collection
      :canonical: pynodes.core.Socket.Collection

      .. autodoc2-docstring:: pynodes.core.Socket.Collection
         :parser: myst

   .. py:property:: Texture
      :canonical: pynodes.core.Socket.Texture

      .. autodoc2-docstring:: pynodes.core.Socket.Texture
         :parser: myst

   .. py:property:: Material
      :canonical: pynodes.core.Socket.Material

      .. autodoc2-docstring:: pynodes.core.Socket.Material
         :parser: myst

   .. py:property:: Image
      :canonical: pynodes.core.Socket.Image

      .. autodoc2-docstring:: pynodes.core.Socket.Image
         :parser: myst

   .. py:property:: Shader
      :canonical: pynodes.core.Socket.Shader

      .. autodoc2-docstring:: pynodes.core.Socket.Shader
         :parser: myst

.. py:class:: Tree(node_tree: bpy.types.NodeTree)
   :canonical: pynodes.core.Tree

   .. autodoc2-docstring:: pynodes.core.Tree
      :parser: myst

   .. rubric:: Initialization

   .. autodoc2-docstring:: pynodes.core.Tree.__init__
      :parser: myst

   .. py:attribute:: tree
      :canonical: pynodes.core.Tree.tree
      :type: pynodes.core.Tree
      :value: None

      .. autodoc2-docstring:: pynodes.core.Tree.tree
         :parser: myst

   .. py:property:: group_input_node
      :canonical: pynodes.core.Tree.group_input_node

      .. autodoc2-docstring:: pynodes.core.Tree.group_input_node
         :parser: myst

   .. py:property:: group_output_node
      :canonical: pynodes.core.Tree.group_output_node

      .. autodoc2-docstring:: pynodes.core.Tree.group_output_node
         :parser: myst

   .. py:property:: tree_output_node
      :canonical: pynodes.core.Tree.tree_output_node

      .. autodoc2-docstring:: pynodes.core.Tree.tree_output_node
         :parser: myst

   .. py:property:: is_embedded
      :canonical: pynodes.core.Tree.is_embedded

      .. autodoc2-docstring:: pynodes.core.Tree.is_embedded
         :parser: myst

   .. py:property:: cur_frame
      :canonical: pynodes.core.Tree.cur_frame

      .. autodoc2-docstring:: pynodes.core.Tree.cur_frame
         :parser: myst

   .. py:method:: new_node(bl_idname: str, properties: list[tuple] = None, inputs: list[tuple] = None)
      :canonical: pynodes.core.Tree.new_node

      .. autodoc2-docstring:: pynodes.core.Tree.new_node
         :parser: myst

   .. py:method:: new_group_node(node_tree: bpy.types.NodeTree)
      :canonical: pynodes.core.Tree.new_group_node

      .. autodoc2-docstring:: pynodes.core.Tree.new_group_node
         :parser: myst

   .. py:method:: new_link(bsocket_from: bpy.types.NodeSocket, bsocket_to: bpy.types.NodeSocket)
      :canonical: pynodes.core.Tree.new_link

      .. autodoc2-docstring:: pynodes.core.Tree.new_link
         :parser: myst

   .. py:method:: new_input(type='NodeSocketGeometry', name='Geometry')
      :canonical: pynodes.core.Tree.new_input

      .. autodoc2-docstring:: pynodes.core.Tree.new_input
         :parser: myst

   .. py:method:: new_output(type='NodeSocketGeometry', name='Geometry')
      :canonical: pynodes.core.Tree.new_output

      .. autodoc2-docstring:: pynodes.core.Tree.new_output
         :parser: myst

   .. py:method:: frame(label='Layout')
      :canonical: pynodes.core.Tree.frame

      .. autodoc2-docstring:: pynodes.core.Tree.frame
         :parser: myst

.. py:class:: Group(bnode: bpy.types.Node)
   :canonical: pynodes.core.Group

   Bases: :py:obj:`pynodes.core.NodeWraper`

   .. autodoc2-docstring:: pynodes.core.Group
      :parser: myst

   .. rubric:: Initialization

   .. autodoc2-docstring:: pynodes.core.Group.__init__
      :parser: myst

   .. py:method:: __call__(**kwargs)
      :canonical: pynodes.core.Group.__call__

      .. autodoc2-docstring:: pynodes.core.Group.__call__
         :parser: myst

   .. py:method:: __getitem__(name: str)
      :canonical: pynodes.core.Group.__getitem__

      .. autodoc2-docstring:: pynodes.core.Group.__getitem__
         :parser: myst

   .. py:method:: __setitem__(name: str, value)
      :canonical: pynodes.core.Group.__setitem__

      .. autodoc2-docstring:: pynodes.core.Group.__setitem__
         :parser: myst

.. py:class:: Frame(bnode: bpy.types.Node)
   :canonical: pynodes.core.Frame

   Bases: :py:obj:`pynodes.core.NodeWraper`

   .. autodoc2-docstring:: pynodes.core.Frame
      :parser: myst

   .. rubric:: Initialization

   .. autodoc2-docstring:: pynodes.core.Frame.__init__
      :parser: myst

   .. py:attribute:: bl_idname
      :canonical: pynodes.core.Frame.bl_idname
      :value: 'NodeFrame'

      .. autodoc2-docstring:: pynodes.core.Frame.bl_idname
         :parser: myst

.. py:class:: Script(bnode: bpy.types.Node)
   :canonical: pynodes.core.Script

   Bases: :py:obj:`pynodes.core.NodeWraper`

   .. autodoc2-docstring:: pynodes.core.Script
      :parser: myst

   .. rubric:: Initialization

   .. autodoc2-docstring:: pynodes.core.Script.__init__
      :parser: myst

   .. py:attribute:: bl_idname
      :canonical: pynodes.core.Script.bl_idname
      :value: 'ShaderNodeScript'

      .. autodoc2-docstring:: pynodes.core.Script.bl_idname
         :parser: myst

   .. py:method:: __setitem__(key: str | int, value)
      :canonical: pynodes.core.Script.__setitem__

      .. autodoc2-docstring:: pynodes.core.Script.__setitem__
         :parser: myst

   .. py:method:: __getitem__(key: str | int)
      :canonical: pynodes.core.Script.__getitem__

      .. autodoc2-docstring:: pynodes.core.Script.__getitem__
         :parser: myst

   .. py:property:: fac
      :canonical: pynodes.core.Script.fac

      .. autodoc2-docstring:: pynodes.core.Script.fac
         :parser: myst

   .. py:property:: height
      :canonical: pynodes.core.Script.height

      .. autodoc2-docstring:: pynodes.core.Script.height
         :parser: myst

   .. py:property:: color
      :canonical: pynodes.core.Script.color

      .. autodoc2-docstring:: pynodes.core.Script.color
         :parser: myst

   .. py:property:: vector
      :canonical: pynodes.core.Script.vector

      .. autodoc2-docstring:: pynodes.core.Script.vector
         :parser: myst

.. py:function:: new_node(bl_idname: str, properties: list[tuple] = None, inputs: list[tuple] = None)
   :canonical: pynodes.core.new_node

   .. autodoc2-docstring:: pynodes.core.new_node
      :parser: myst

.. py:function:: new_link(bsocket_from: bpy.types.NodeSocket, bsocket_to: bpy.types.NodeSocket)
   :canonical: pynodes.core.new_link

   .. autodoc2-docstring:: pynodes.core.new_link
      :parser: myst

.. py:function:: update_modifier(default_value, input: bpy.types.NodeSocketInterface)
   :canonical: pynodes.core.update_modifier

   .. autodoc2-docstring:: pynodes.core.update_modifier
      :parser: myst

.. py:data:: Param
   :canonical: pynodes.core.Param
   :value: None

   .. autodoc2-docstring:: pynodes.core.Param
      :parser: myst

.. py:data:: RT
   :canonical: pynodes.core.RT
   :value: None

   .. autodoc2-docstring:: pynodes.core.RT
      :parser: myst

.. py:function:: convert_param_name(name: str)
   :canonical: pynodes.core.convert_param_name

   .. autodoc2-docstring:: pynodes.core.convert_param_name
      :parser: myst

.. py:function:: get_param_name(param: inspect.Parameter) -> str
   :canonical: pynodes.core.get_param_name

   .. autodoc2-docstring:: pynodes.core.get_param_name
      :parser: myst

.. py:function:: dispath_tree(func: typing.Callable)
   :canonical: pynodes.core.dispath_tree

   .. autodoc2-docstring:: pynodes.core.dispath_tree
      :parser: myst

.. py:function:: tree(func: typing.Callable[pynodes.core.Param, pynodes.core.RT]) -> typing.Callable[pynodes.core.Param, pynodes.core.RT]
   :canonical: pynodes.core.tree

   .. autodoc2-docstring:: pynodes.core.tree
      :parser: myst

.. py:function:: frame(label='Layout')
   :canonical: pynodes.core.frame

   .. autodoc2-docstring:: pynodes.core.frame
      :parser: myst

.. py:function:: reload()
   :canonical: pynodes.core.reload

   .. autodoc2-docstring:: pynodes.core.reload
      :parser: myst
