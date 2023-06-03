import bpy, json, re, mathutils, math

data: list[dict] = json.load(open("pynodes_builder\\nodes_doc_url_all.json"))
properties_data: dict[str, dict] = json.load(open("pynodes_builder\\nodes_property_all.json"))
ios_data: dict[str, dict] = json.load(open("pynodes_builder\\nodes_io_all.json"))

socket_types = ("Float", "Vector", "Boolean", "Integer", "Geometry", "Color", "String", "Collection", "Image", "Material", "Texture", "Object", "Shader")

file_text = "import math, typing\nfrom . import nodes\nfrom pynodes.core import new_node\n\n"

for node_data in data:
    bl_idname = node_data['bl_idname']
    func_name = bl_idname
    text = ""
    properties = properties_data[bl_idname]
    params_enum = []
    params = []
    for key, val in properties.items():
        if type(val) == str:
            params_enum.append((key, tuple(val.split(", "))))
        else:
            params.append((key, (val['default'], val['type'])))
    inputs = ios_data[bl_idname]['inputs']
    outputs = ios_data[bl_idname]['outputs']
    signature_items = []
    for param_enum in params_enum:
        signature_items.append(f"{param_enum[0]}={param_enum[1][0]!r}")
    for param in params:
        default_value = param[1][0]
        if default_value == "":
            default_value = "''"
        signature_items.append(f"{param[0]}={default_value}")
    for input in inputs:
        default_value = input['default']
        if input['bl_label'] in socket_types:
            if input['bl_label'] == "String":
                default_value = repr(default_value)
                print(bl_idname, default_value)
            if input['display_shape'] == "DIAMOND":
                default_value = None
                signature_items.append(f"{input['identifier'].lower().replace(' ', '_')}: \"{input['bl_label']}\"={default_value}")
            else:
                signature_items.append(f"{input['identifier'].lower().replace(' ', '_')}={default_value}")
        else:
            signature_items.append(f"{input['identifier'].lower().replace(' ', '_')}: {input['bl_label']}={input['default']}")
    node_param_items = []
    for param_enum in params_enum:
        node_param_items.append(f"{param_enum[0]}={param_enum[1][0]!r}")
    for param in params:
        default_value = param[1][0]
        if default_value == "":
            default_value = "''"
        node_param_items.append(f"{param[0]}={default_value}")
    for input in inputs:
        default_value = input['default']
        if input['bl_label'] == "String":
            default_value = repr(default_value)
        node_param_items.append(f"{input['identifier'].lower().replace(' ', '_')}={default_value}")

    params_all = []
    for i in params_enum:
        params_all.append((i[0], repr(i[1][0])))
    for i in params:
        params_all.append((i[0], i[1][0]))
    if not params_all:
        params_all_str = "\n    params_all = []"
    else:
        params_all_str = "\n    " + f"""params_all = [{', '.join(f"('{param[0]}', {param[0]}, {param[1]})" for param in params_all)}]"""
    inputs_all = []
    for input in inputs:
        name = input['identifier'].lower().replace(" ", "_")
        default_value = input['default']
        inputs_all.append((name, default_value if default_value != "" else "''"))
    if not inputs_all:
        inputs_all_str = "\n    inputs_all = []"
    else:
        inputs_all_str = "\n    " + f"""inputs_all = [{', '.join(f"({input[0]}, {input[1]})" for input in inputs_all)}]"""
    params_enum_docs = []
    if len(params_enum) > 0:
        params_enum_docs.append(f"\n    #### Properties:")
    for param_enum in params_enum:
        params_enum_docs.append(f"\n    - `{param_enum[0]}`: {', '.join(f'`{i}`' for i in param_enum[1])}")
    outputs_docs = []
    if len(outputs) > 0:
        outputs_docs.append(f"\n    #### Outputs:")
    for i, output in enumerate(outputs):
        default_value = output['default']
        if default_value == "":
            default_value = '""'
        outputs_docs.append(f"\n    - `#{i} {output['identifier'].lower().replace(' ', '_')}: {output['bl_label']} = {default_value}`")
    if len(outputs) == 1:
        ret = f"node.outputs[0].{outputs[0]['bl_label']}"
        if outputs[i]['bl_label'] == "Geometry" and outputs[0]['identifier'] in ["Mesh", "Curve", "Instances", "Points", "Volume"]:
            ret = f"node.outputs[0].{outputs[0]['identifier']}"
    else:
        ret_items = []
        for i in range(len(outputs)):
            if outputs[i]['bl_label'] == "Geometry" and outputs[i]['identifier'] in ["Mesh", "Curve", "Instances", "Points", "Volume"]:
                ret_items.append(f"node.outputs[{i}].{outputs[i]['identifier']}")
            else:
                ret_items.append(f"node.outputs[{i}].{outputs[i]['bl_label']}")
        # ret = ", ".join(f"node.outputs[{i}].{outputs[i][-1]}" for i in range(len(outputs)))
        ret = ", ".join(ret_items)
    if bl_idname in ["GeometryNodeViewer", "GeometryNodeGroup"]:
        ret = "node"
    selection = ""
    for item in signature_items:
        if "selection" in item:
            selection = "\n    # selection = selection if self._selection is None else self.selection"

    template = f'''
def {func_name}({", ".join(signature_items)}):
    """{node_data['documentation']}
    #### Path
    - {node_data['path']}{"".join(params_enum_docs) }{"".join(outputs_docs) }

    ![]({node_data['url2']})

    [[Manual]]({node_data['url1']}) [[API]](https://docs.blender.org/api/current/bpy.types.{bl_idname}.html)
    """{selection}
    node = new_node(*nodes.{bl_idname}({", ".join(item.split("=")[0] for item in node_param_items)}))
    return {ret}

'''
    if len(outputs) > 0 or bl_idname.startswith("ShaderNodeTex"):
        named_tuple_items = []
        for output in outputs:
            named_tuple_items.append(f"(\"{output['name'].lower().replace(' ', '_')}\", {output['bl_label']})")
        named_tuple_items = ', '.join(named_tuple_items)
        template = f'''
def {func_name}({", ".join(signature_items)}):
    """{node_data['documentation']}
    #### Path
    - {node_data['path']}{"".join(params_enum_docs) }{"".join(outputs_docs) }

    ![]({node_data['url2']})

    [[Manual]]({node_data['url1']}) [[API]](https://docs.blender.org/api/current/bpy.types.{bl_idname}.html)
    """{selection}
    node = new_node(*nodes.{bl_idname}({", ".join(item.split("=")[0] for item in node_param_items)}))
    ret = typing.NamedTuple("{bl_idname}", [{named_tuple_items}])
    return ret({ret})
    return {ret}

'''
    text += template
    file_text += text

with open("pynodes_builder/builders/functions_all.py", "w") as f:
    f.write(file_text)
    text = \
        '''
def GeometryNodeInputSceneTime():
    """The Scene Time node outputs the current time in the scene's animation in units of seconds or frames.
    #### Path
    - Input > Scene > Scene Time Node
    #### Outputs:
    - `#0 seconds: Float = 0.0`
    - `#1 frame: Float = 0.0`

    ![](https://docs.blender.org/manual/en/3.5/_images/node-types_GeometryNodeInputSceneTime.webp)

    [[Manual]](https://docs.blender.org/manual/en/3.5/modeling/geometry_nodes/input/scene/scene_time.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputSceneTime.html)
    """
    node = new_node(*nodes.GeometryNodeInputSceneTime())
    from pynodes.datasocks import Float
    ret = typing.NamedTuple("SceneTime", [("seconds", Float), ("frame", Float)])
    return ret(node.outputs[0].Float, node.outputs[1].Float)
    '''
    f.write(text)
