import bpy, mathutils, contextlib, sys
from bpy.types import Node, NodeSocket, NodeSocketInterface, NodeTree, NodeLink, NodeGroup


class NodeWraper:
    def __init__(self, bnode: Node) -> None:
        self.bnode = bnode
        self._outputs = None
        self._inputs = None

    @property
    def outputs(self):
        if self._outputs is None:
            self._outputs = [Socket(output) for output in self.bnode.outputs]
        return self._outputs

    @property
    def inputs(self):
        if self._inputs is None:
            self._inputs = [Socket(input) for input in self.bnode.inputs]
        return self._inputs

    @property
    def color(self):
        return self.bnode.color

    @color.setter
    def color(self, color: str | mathutils.Color | list[float] | tuple[float]):
        self.bnode.use_custom_color = True
        if isinstance(color, str):
            from . import colors
            color = colors.hex_color_to_rgb(color)
        if not isinstance(color, mathutils.Color):
            color = mathutils.Color(color)
        self.bnode.color = color

    @property
    def label(self) -> str:
        return self.bnode.label

    @label.setter
    def label(self, label: str):
        self.bnode.label = label

    def plug_inputs(self, inputs_all: list[tuple]):
        frame = Tree.tree.cur_frame
        if frame is not None:
            frame_input_node = None
            for node in Tree.tree.btree.nodes:
                if node.bl_idname == "NodeGroupInput" and node.parent == frame:
                    frame_input_node = node
                    break

            for i, input in enumerate(inputs_all):
                data, default_value = input
                if isinstance(data, Socket) and Tree.tree._group_input_node is not None and data.node.bnode == Tree.tree.group_input_node.bnode:
                    if frame_input_node is None:
                        frame_input_node = Tree.tree.btree.nodes.new("NodeGroupInput")
                        frame_input_node.parent = frame
                        frame_input_node.select = False
                    index = 0
                    for j, output in enumerate(Tree.tree.group_input_node.outputs):
                        if output.bsocket == data.bsocket:
                            index = j
                            break
                    else:
                        index = -2
                        # raise RuntimeError("Can't find output socket of NodeGroupInput")
                    inputs_all[i] = Socket(frame_input_node.outputs[index]), default_value
        bnode = self.bnode
        for i, input in enumerate(inputs_all):
            data, default_value = input
            if data is None:
                continue
            socket_to = SocketWraper(bnode.inputs[i])
            if isinstance(data, Socket):
                new_link(data.bsocket, socket_to.bsocket)
                continue
            if isinstance(data, (list, tuple)):
                if len(data) == 3:
                    if any(isinstance(a, Socket) for a in data) or socket_to.bsocket.display_shape == "DIAMOND":
                        from .datasocks import CombineXYZ
                        socket = CombineXYZ(*data)
                        new_link(socket.bsocket, socket_to.bsocket)
                        continue
                if len(data) == 4:
                    if any(isinstance(a, Socket) for a in data) or socket_to.bsocket.display_shape == "DIAMOND":
                        if isinstance(Tree.tree.btree, bpy.types.GeometryNodeTree):
                            from .datasocks import CombineColor
                        else:
                            from .datasocks import ShaderNodeCombineColor as CombineColor
                        socket = CombineColor(*data)
                        new_link(socket.bsocket, socket_to.bsocket)
                        continue
            if data != default_value:
                socket_to.default_value = data
                continue

    def __setitem__(self, key: str, value):
        for input in self.inputs:
            if input.bsocket.name == key.replace('_', " ").title():
                if isinstance(value, Socket):
                    new_link(value.bsocket, input.bsocket)
                else:
                    input.default_value = value
                break
        else:
            try:
                setattr(self.bnode, key, value)
            except Exception as e:
                print(e, f"Cannot set item of the node of socket {self.bnode.name}", f"{key = }", f"{value = }", sep='\n')


class SocketWraper:
    def __init__(self, bsocket: NodeSocket) -> None:
        self.bsocket = bsocket

    @property
    def default_value(self):
        return getattr(self.bsocket, "default_value")

    @default_value.setter
    def default_value(self, value):
        bsocket = self.bsocket
        bnode = bsocket.node
        if bsocket.bl_label in ["Vector", "Color"]:
            if not hasattr(value, "__len__") and isinstance(value, (int, float)):
                value = (value,) * len(self.default_value)
            elif bsocket.bl_label == "Color" and type(value) == str and value.startswith("#"):
                from .colors import hex_color_to_rgba
                value = hex_color_to_rgba(value)
        elif bsocket.bl_label == "Material":
            if type(value) == str:
                if bpy.data.materials.get(value) is None:
                    bpy.data.materials.new(value)
                value = bpy.data.materials[value]
            else:
                assert isinstance(value, bpy.types.Material)
        elif bsocket.bl_label == "Image":
            if type(value) == str:
                if bpy.data.images.get(value) is None:
                    bpy.data.images.new(value)
                value = bpy.data.images[value]
            else:
                assert isinstance(value, bpy.types.Image)
        elif bsocket.bl_label == "Float":
            if isinstance(value, str):
                if value.startswith("#"):
                    value = value[1:].strip()
                fcurve = self.bsocket.driver_add("default_value")
                fcurve.driver.type = "SCRIPTED"
                fcurve.driver.expression = value
                return
        try:
            setattr(bsocket, "default_value", value)
        except Exception as e:
            print("Cannot set default_value", e, f"{bnode.name = }", f"{bsocket.name = }", f"{value = }", sep="\n")


class Socket(SocketWraper):
    """Base class of datasocks and geosocks, represents an output socket"""
    bl_idname = "NodeSocket"

    def __init__(self, bsocket: NodeSocket) -> None:
        super().__init__(bsocket)
        self._node = None
        self._name = None

    @property
    def node(self):
        if self._node is None:
            self._node = NodeWraper(self.bsocket.node)
        return self._node

    def __call__(self, name: str):
        self._name = name
        return self

    def __setitem__(self, key: str, value):
        self.node[key] = value

    @property
    def name(self):
        if self._name is not None:
            return self._name
        base_class_names = [self.__class__.__name__]
        for cls in self.__class__.__bases__:
            if cls is Socket:
                continue
            if issubclass(cls, Socket):
                base_class_names.append(cls.__name__)
        if self.bsocket.name not in base_class_names:
            return self.bsocket.name
        return base_class_names[0]

    @name.setter
    def name(self, value: str):
        self._name = value

    def link_tree_output(self, index: int = None):
        if not Tree.tree.is_embedded:
            if self.linked_to_group_output:
                return
            Tree.tree.new_output(self.bsocket.__class__.__name__, self.name)
            Tree.tree.new_link(self.bsocket, Tree.tree.group_output_node.bnode.inputs[-2])
            Tree.tree.group_output_node._inputs = None
            return
        else:
            for i, input in enumerate(Tree.tree.tree_output_node.inputs):
                if not input.bsocket.is_linked:
                    if index is None or i == index:
                        Tree.tree.new_link(self.bsocket, input.bsocket)
                        break
            else:
                raise RuntimeError("Cannot link the return value of the function to the material ouput node!")

    def func_ret_to_tree_output(self):
        index = None
        if self.bsocket.name == "Volume":
            index = 1
        if self.bsocket.name == "Displacement":
            index = 2
        self.link_tree_output(index)

    @property
    def linked_to_group_output(self):
        link: NodeLink
        for link in self.bsocket.links:
            if link.to_node.bl_idname == "NodeGroupOutput":
                return True
        return False

    @classmethod
    def Input(cls, default=None, name=None, min=None, max=None, description=None, bl_idname=None):
        if name is None:
            name = cls.__name__
        input = Tree.tree.new_input(cls.bl_idname if bl_idname is None else bl_idname, name)
        if default != None:
            if input.bl_socket_idname == "NodeSocketMaterial":
                if type(default) == str:
                    mat_name = default
                    default = bpy.data.materials.get(mat_name)
                    if default is None:
                        default = bpy.data.materials.new(mat_name)
            if Tree.tree.btree.bl_idname == "GeometryNodeTree":
                update_modifier(default, input)
            input.default_value = default
        if min is not None:
            input.min_value = min
        if max is not None:
            input.max_value = max
        if description is not None:
            input.description = description
        socket = cls(Tree.tree.group_input_node.bnode.outputs[-2])
        socket.name = name
        return socket

    @property
    def Float(self):
        from .datasocks import Float
        return Float(self.bsocket)

    @property
    def Integer(self):
        from .datasocks import Integer
        return Integer(self.bsocket)

    @property
    def Boolean(self):
        from .datasocks import Boolean
        return Boolean(self.bsocket)

    @property
    def Vector(self):
        from .datasocks import Vector
        return Vector(self.bsocket)

    @property
    def Color(self):
        from .datasocks import Color
        return Color(self.bsocket)

    @property
    def Geometry(self):
        from .geosocks import Geometry
        return Geometry(self.bsocket)

    @property
    def Mesh(self):
        from .geosocks import Mesh
        return Mesh(self.bsocket)

    @property
    def Points(self):
        from .geosocks import Points
        return Points(self.bsocket)

    @property
    def Volume(self):
        from .geosocks import Volume
        return Volume(self.bsocket)

    @property
    def Instances(self):
        from .geosocks import Instances
        return Instances(self.bsocket)

    @property
    def Curve(self):
        from .geosocks import Curve
        return Curve(self.bsocket)

    @property
    def String(self):
        from .datasocks import String
        return String(self.bsocket)

    @property
    def Object(self):
        from .datasocks import Object
        return Object(self.bsocket)

    @property
    def Collection(self):
        from .datasocks import Collection
        return Collection(self.bsocket)

    @property
    def Texture(self):
        from .datasocks import Texture
        return Texture(self.bsocket)

    @property
    def Material(self):
        from .datasocks import Material
        return Material(self.bsocket)

    @property
    def Image(self):
        from .datasocks import Image
        return Image(self.bsocket)

    @property
    def Shader(self):
        from .datasocks import Shader
        return Shader(self.bsocket)


class Tree:
    tree: "Tree"

    def __init__(self, node_tree: NodeTree) -> None:
        Tree.tree = self
        self.btree = node_tree
        node_tree.nodes.clear()
        node_tree.inputs.clear()
        node_tree.outputs.clear()
        self.frames: list[Frame] = []
        self._group_input_node = None
        self._group_output_node = None
        self._tree_output_node = None

    @property
    def group_input_node(self):
        if self._group_input_node is None:
            self._group_input_node = self.new_node("NodeGroupInput")
        return self._group_input_node

    @property
    def group_output_node(self):
        if self._group_output_node is None:
            self._group_output_node = self.new_node("NodeGroupOutput")
        return self._group_output_node

    @property
    def tree_output_node(self):
        # TODO
        btree: bpy.types.ShaderNodeTree = self.btree
        obj_type = btree.bl_icon.split("_")[-1].lower().title()
        bl_idname = f"ShaderNodeOutput{obj_type}"
        if obj_type == "Scene":
            bl_idname = "CompositorNodeComposite"
        if self._tree_output_node is None:
            self._tree_output_node = self.new_node(bl_idname)
        return self._tree_output_node

    @property
    def is_embedded(self):
        """True if self.btree is the node_tree of a material object"""
        return self.btree.is_embedded_data

    @property
    def cur_frame(self):
        """Get the current layout for the newly created nodes."""
        if self.frames:
            return self.frames[-1].bnode
        else:
            return None

    def new_node(self, bl_idname: str, properties: list[tuple] = None, inputs: list[tuple] = None):
        bnode = self.btree.nodes.new(bl_idname)
        bnode.select = False
        bnode.parent = self.cur_frame

        node = NodeWraper(bnode)
        if properties is not None:
            for name, value, default_value in properties:
                if value != default_value:
                    setattr(bnode, name, value)
                    # TODO
        if inputs is not None:
            node.plug_inputs(inputs)

        return node

    def new_group_node(self, node_tree: NodeTree):
        node = self.new_node(self.btree.bl_idname.replace("Tree", "Group"))
        bnode: NodeGroup = node.bnode
        bnode.node_tree = node_tree
        return node

    def new_link(self, bsocket_from: NodeSocket, bsocket_to: NodeSocket):
        link = self.btree.links.new(bsocket_from, bsocket_to)
        return link

    def new_input(self, type="NodeSocketGeometry", name="Geometry"):
        return self.btree.inputs.new(type, name)

    def new_output(self, type="NodeSocketGeometry", name="Geometry"):
        return self.btree.outputs.new(type, name)

    @contextlib.contextmanager
    def frame(self, label="Layout"):
        frame = Frame(self.new_node(Frame.bl_idname).bnode)
        frame.label = label
        self.frames.append(frame)
        yield frame
        frame = self.frames.pop()


class Group(NodeWraper):
    def __init__(self, bnode: Node) -> None:
        super().__init__(bnode)

    def __call__(self, **kwargs):
        inputs = []
        for input in self.bnode.inputs:
            value = kwargs.get(input.name, kwargs.get(input.name.lower()))
            inputs.append((value, None))
        self.plug_inputs(inputs)
        return self

    def __getitem__(self, name: str):
        name = name.replace(" ", "_")
        try:
            output = self.bnode.outputs[name.title()]
        except KeyError:
            output = self.bnode.outputs[name]
        return Socket(output)

    def __setitem__(self, name: str, value):
        return self.__call__(**{name: value})


class Frame(NodeWraper):
    bl_idname = "NodeFrame"


class Script(NodeWraper):
    bl_idname = "ShaderNodeScript"

    def __setitem__(self, key: str | int, value):
        if type(key) == int:
            input = self.inputs[key]
            if isinstance(value, Socket):
                new_link(value.bsocket, input.bsocket)
            else:
                input.default_value = value
            return

        for input in self.inputs:
            if input.bsocket.name.lower().replace(" ", "_") == key.lower().replace(" ", "_"):
                if isinstance(value, Socket):
                    new_link(value.bsocket, input.bsocket)
                else:
                    input.default_value = value
                break
        else:
            try:
                setattr(self.bnode, key, value)
            except Exception as e:
                print(e, "Cannot set item of the Script node", f"{key = }", f"{value = }", sep='\n')

    def __getitem__(self, key: str | int):
        if type(key) == int:
            output = self.outputs[key]
            return output
        for output in self.outputs:
            if output.name == key:
                return output
        raise RuntimeError(f"Cannot find the ouput socket {key} of the script node")

    @property
    def fac(self):
        return self['Fac'].Float

    @property
    def height(self):
        return self['Height'].Float

    @property
    def color(self):
        return self['Color'].Color

    @property
    def vector(self):
        return self['Vector'].Vector


def new_node(bl_idname: str, properties: list[tuple] = None, inputs: list[tuple] = None):
    return Tree.tree.new_node(bl_idname, properties, inputs)


def new_link(bsocket_from: NodeSocket, bsocket_to: NodeSocket):
    return Tree.tree.new_link(bsocket_from, bsocket_to)


def update_modifier(default_value, input: NodeSocketInterface):
    if input.bl_socket_idname == "NodeSocketFloat":
        default_value = float(default_value)
    for obj in bpy.data.objects:
        for mod in obj.modifiers:
            if isinstance(mod, bpy.types.NodesModifier):
                if mod.node_group == Tree.tree.btree:
                    mod[input.identifier] = default_value


import inspect, functools, typing

Param = typing.ParamSpec("Param")
RT = typing.TypeVar('RT')


def convert_param_name(name: str):
    if len(name) == 1:
        return name
    elif len(name) == 2:
        if name[1].isdigit():
            return name
    return name.replace("_", " ").title()


def get_param_name(param: inspect.Parameter) -> str:
    if isinstance(param.default, tuple) and type(param.default[0]) == str:
        return param.default[0]
    return convert_param_name(param.name)


def dispath_tree(func: typing.Callable):
    if func.__name__ == "world":
        world_name = "World"
        world = bpy.data.worlds[world_name]
        world.use_nodes = True
        return world.node_tree
    func_name = func.__name__.replace("_", " ").title()
    func_doc = func.__doc__
    tree_name = func_name
    tree_type = "GeometryNodeTree"
    if func_doc is None:
        if bpy.data.node_groups.get(tree_name) is None:
            bpy.data.node_groups.new(tree_name, type=tree_type)
        return bpy.data.node_groups[tree_name]
    func_doc = func_doc.split('\n')[0].strip()
    if "@" not in func_doc:
        tree_name = func_doc
        if bpy.data.node_groups.get(tree_name) is None:
            bpy.data.node_groups.new(tree_name, type=tree_type)
        return bpy.data.node_groups[tree_name]
    if func_doc.lower().startswith("@material"):
        mat_name = func_name
        if ":" in func_doc:
            mat_name = func_doc.split(":")[-1].strip()
        if bpy.data.materials.get(mat_name) is None:
            bpy.data.materials.new(mat_name)
        mat = bpy.data.materials[mat_name]
        mat.use_nodes = True
        return mat.node_tree
    if func_doc.lower().startswith("@light"):
        light_name = func_name
        if ":" in func_doc:
            light_name = func_doc.split(":")[-1].strip()
        if bpy.data.lights.get(light_name) is None:
            bpy.data.lights.new(light_name)
        light = bpy.data.lights[light_name]
        light.use_nodes = True
        return light.node_tree
    if func_doc.lower().startswith("@world"):
        world_name = func_name
        if ":" in func_doc:
            world_name = func_doc.split(":")[-1].strip()
        if bpy.data.worlds.get(world_name) is None:
            bpy.data.worlds.new(world_name)
        world = bpy.data.worlds[world_name]
        world.use_nodes = True
        return world.node_tree
    if func_doc.lower().startswith("@scene") or func_doc.lower().startswith("@composit"):
        scene_name = func_name
        if ":" in func_doc:
            scene_name = func_doc.split(":")[-1].strip()
        if bpy.data.scenes.get(scene_name) is None:
            bpy.data.scenes.new(scene_name)
        scene = bpy.data.scenes[scene_name]
        scene.use_nodes = True
        return scene.node_tree
    if func_doc.lower().startswith("@shader"):
        tree_name = func_name
        if ":" in func_doc:
            tree_name = func_doc.split(":")[-1].strip()
        if bpy.data.node_groups.get(tree_name) is None:
            bpy.data.node_groups.new(tree_name, type="ShaderNodeTree")
        return bpy.data.node_groups[tree_name]
    raise RuntimeError("Cannot configure what tree the decorated function represents!")


def tree(func: typing.Callable[Param, RT]) -> typing.Callable[Param, RT]:
    """Decorate a function to make it represent a Node Tree.

    The function documentation(docstring) defines the type of the Node Tree.

    - Examples:

    ```
    @tree
    def node_group_name(): # A Geometry Node Group Tree with tree name `Node Group Name`
        ...
    @tree
    def foo(): # A Geometry Node Froup Tree with tree name `Node Group Name In Doc`
        '''Node Group Name In Doc'''
    @tree
    def node_group_name(): # A Shader Node Group Tree with tree name `Node Group Name`
        '''@Shader'''
    @tree
    def foo(): # A Shader Node Group Tree with tree name `Node Group Name In Doc`
        '''@Shader: Node Group Name In Doc'''
    @tree
    def mat_name(): # A material tree with material name `Mat Name`
        '''@Material'''
    @tree
    def foo(): # An material tree with material name `Mat Name In Doc`
        '''Material: Mat Name In Doc'''
    @tree
    def world_name(): # A world shader tree with world name `World Name`
        '''@World'''
    @tree
    def foo(): # An world shader tree with world name `World Name in Doc`
        '''@World: World Name in Doc'''
    @tree
    def light_name(): # A light shader tree with light name `Light Name`
        '''@Light'''
    @tree
    def foo(): # An light shader tree with light name `Light Name in Doc`
        '''@Light: Light Name in Doc'''
    @tree
    def scene_name(): # A scene compositor tree with scene name `Scene Name`
        '''@Scene'''
    @tree
    def foo(): # A scene compositor tree with light name `Scene Name in Doc`
        '''@Scene: Scene Name in Doc'''
    @tree
    def scene_name(): # A scene compositor tree with scene name `Scene Name`
        '''@Compositor'''
    @tree
    def foo(): # A scene compositor tree with light name `Scene Name in Doc`
        '''@Compositor: Scene Name in Doc'''
    ```
    """
    node_tree = dispath_tree(func)
    Tree(node_tree)
    sig = inspect.signature(func)
    args: list[Socket] = []
    from .datasocks import Vector, Color
    for param in sig.parameters.values():
        sig_param_default = param.default
        input_params = {"name": convert_param_name(param.name)}
        if isinstance(sig_param_default, tuple):
            if isinstance(sig_param_default[0], str):
                input_params['name'] = sig_param_default[0]
                sig_param_default = sig_param_default[1:]

            if issubclass(param.annotation, Vector) and len(sig_param_default) == 3 and all(isinstance(i, (int, float)) for i in param.default):
                input_params['default'] = sig_param_default
                sig_param_default = ()
            elif issubclass(param.annotation, Color) and len(sig_param_default) == 4 and all(isinstance(i, (int, float)) for i in param.default):
                input_params['default'] = sig_param_default
                sig_param_default = ()

            if sig_param_default:
                input_params['default'] = sig_param_default[0]
                sig_param_default = sig_param_default[1:]

            if sig_param_default:
                input_params['min'] = sig_param_default[0]
                sig_param_default = sig_param_default[1:]

            if sig_param_default:
                input_params['max'] = sig_param_default[0]

        elif not sig_param_default is inspect._empty:
            input_params['default'] = sig_param_default

        args.append(param.annotation.Input(**input_params))

    outputs = func(*args)

    if isinstance(outputs, tuple):
        output: Socket
        for output in outputs:
            output.func_ret_to_tree_output()
    elif isinstance(outputs, Socket):
        outputs.func_ret_to_tree_output()

    from .arrange import arrange
    arrange(Tree.tree.btree)

    @functools.wraps(func)
    def wrapped_function(*args, **kwargs) -> RT:
        kwargs = {get_param_name(sig.parameters.get(k)): v for k, v in kwargs.items()}
        for arg, param in zip(args, list(sig.parameters.values())[:len(args)]):
            kwargs[get_param_name(param)] = arg
        node = Tree.tree.new_group_node(node_tree)
        g = Group(node.bnode)(**kwargs)
        if isinstance(outputs, tuple):
            # return tuple(getattr(g[output.name], output.__class__.__name__) for output in outputs)
            return tuple(getattr(g.outputs[i], output.__class__.__name__) for i, output in enumerate(outputs))
        else:
            return getattr(g[outputs.name], outputs.__class__.__name__)

    return wrapped_function


def frame(label="Layout"):
    return Tree.tree.frame(label)


def reload():
    all_modules = sys.modules
    all_modules = dict(sorted(all_modules.items(), key=lambda x: x[0]))
    for k, v in all_modules.items():
        if k.startswith("pynodes"):
            del sys.modules[k]
