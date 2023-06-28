import bpy, enum, mathutils


class ObjType(enum.Enum):
    def __matmul__(self, name: str):
        return Key(self, name)


class O(ObjType):
    mesh = enum.auto()
    plane = "bpy.ops.mesh.primitive_plane_add()"
    cube = "bpy.ops.mesh.primitive_cube_add()"
    ico_sphere = "bpy.ops.mesh.primitive_ico_sphere_add()"
    monkey = "bpy.ops.mesh.primitive_monkey_add()"
    circle = enum.auto()
    cone = enum.auto()
    nurbs_path = enum.auto()
    bezier_curve = "bpy.ops.curve.primitive_bezier_curve_add()"
    empty_sphere = "bpy.ops.object.empty_add(type='SPHERE')"


class Mod(ObjType):
    geometry_nodes = "NODES"
    bevel = "BEVEL"
    subdivision = "SUBSURF"
    decimate = "DECIMATE"
    smooth = "SMOOTH"


class Mat(ObjType):
    slots = enum.auto()


class Key:
    def __init__(self, type: ObjType, name: str) -> None:
        self.type, self.name = type, name

    def __eq__(self, __o: object) -> bool:
        if not isinstance(__o, Key):
            return False
        return self.type == __o.type and self.name == __o.name

    def __hash__(self) -> int:
        return hash((self.type, self.name))


class Tree:
    def __init__(self, data: dict[ObjType | Key | bpy.types.Object, dict]) -> None:
        self.data = data
        self.objects: dict[Key | ObjType, bpy.types.Object] = {}

    def __getitem__(self, key):
        return self.objects[key]

    def load(self, clear_animation=True):
        for key, val in self.data.items():
            obj = None
            if isinstance(key, ObjType):
                obj_name = key.name.replace("_", " ").title()
                if bpy.data.objects.get(obj_name) is not None:
                    obj = bpy.data.objects[obj_name]
            elif isinstance(key, Key):
                obj_name = key.name
                if bpy.data.objects.get(obj_name) is not None:
                    obj = bpy.data.objects[obj_name]
            elif isinstance(key, bpy.types.Object):
                obj = key
                obj_name = obj.name
            if obj is None:
                try:
                    exec(key.value if isinstance(key, ObjType) else key.type.value, {"bpy": bpy})
                except AttributeError as e:
                    print("Error in Scene Tree load", key, val, e, sep="\n")
                    bpy.ops.mesh.primitive_cube_add()
                obj = bpy.context.active_object
                obj.select_set(False)
            if clear_animation:
                if obj.animation_data is not None:
                    obj.animation_data.action.fcurves.clear()
            self.objects[key] = obj

            if obj_name is not None:
                obj.name = obj_name

            for k, v in val.items():
                if isinstance(k, str):
                    if isinstance(v, list):
                        for frame, value in v:
                            obj.__setattr__(k, value)
                            obj.keyframe_insert(data_path=k, frame=frame)
                    else:
                        obj.__setattr__(k, v)
                    continue
                if isinstance(k, Mod):
                    self.parse_modifier(Key(k, k.name.title().replace("_", " ")), v, obj)
                    continue
                if k == Mat.slots:
                    self.parse_mat_slots(obj, v)
                    continue
                if isinstance(k, Key):
                    if isinstance(k.type, Mod):
                        self.parse_modifier(k, v, obj)

        return self

    def parse_modifier(self, k: Key, v: dict[str], obj: bpy.types.Object):
        mod_name = k.name
        mod_type = k.type.value
        if obj.modifiers.get(mod_name) is None:
            obj.modifiers.new(mod_name, mod_type)
        mod = obj.modifiers[mod_name]
        for mod_k, mod_v in v.items():
            if type(mod_v) == list:
                for frame, value in mod_v:
                    if k.type == Mod.geometry_nodes:
                        mod: bpy.types.NodesModifier
                        node_input = mod.node_group.inputs[mod_k]
                        if node_input.bl_label == "Float":
                            value = float(value)
                        elif node_input.bl_label == "Object":
                            if isinstance(value, str):
                                value = bpy.data.objects[value]
                        if isinstance(value, mathutils.Vector):
                            bpy.data.objects[obj.name].modifiers[mod_name][node_input.identifier][:] = value[:]
                        else:
                            mod[node_input.identifier] = value
                        path = f'modifiers["{mod_name}"]["{node_input.identifier}"]'
                    else:
                        mod[mod_k] = value
                        path = f'modifiers["{mod_name}"]["{mod_k}"]'
                    obj.keyframe_insert(data_path=path, frame=frame)
                    if k.type == Mod.geometry_nodes:
                        # node_input = mod.node_group.inputs[mod_k]
                        node_input.name = node_input.name
            else:
                value = mod_v
                if mod_k == "node_group":
                    tree_name = mod_v.replace("_", " ").title()
                    if bpy.data.node_groups.get(tree_name) is None:
                        bpy.data.node_groups.new(tree_name, "GeometryNodeTree")
                    node_group = bpy.data.node_groups[tree_name]
                    if mod.node_group != node_group:
                        mod.node_group = node_group
                elif k.type == Mod.geometry_nodes:
                    try:
                        node_input = mod.node_group.inputs[mod_k]
                    except KeyError:
                        node_input = mod.node_group.inputs[mod_k.title()]
                    if node_input.bl_label == "Float":
                        value = float(value)
                    elif isinstance(value, (ObjType, Key)):
                        value = self.objects[value]
                    elif node_input.bl_label == "Object" and type(value) == str:
                        value = bpy.data.objects[value]
                    elif node_input.bl_label == "Collection" and type(value) == str:
                        value = bpy.data.collections[value]
                    if isinstance(value, mathutils.Vector):
                        bpy.data.objects[obj.name].modifiers[mod_name][node_input.identifier][:] = value[:]
                    else:
                        mod[node_input.identifier] = value
                    node_input.name = node_input.name
                else:
                    mod.__setattr__(mod_k, value)

    def parse_mat_slots(self, obj: bpy.types.Object, material_names: list[str]):
        materials = [bpy.data.materials[name] for name in material_names]
        mesh: bpy.types.Mesh = obj.data
        for mat_new in materials:
            for mat_old in mesh.materials:
                if mat_new == mat_old:
                    break
            else:
                mesh.materials.append(mat_new)
