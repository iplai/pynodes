import bpy, json, mathutils

data: list[dict] = json.load(open("pynodes_builder\\nodes_doc_url_all.json"))
properties_data: dict[str, dict] = json.load(open("pynodes_builder\\nodes_property_all.json"))
ios_data: dict[str, dict] = json.load(open("pynodes_builder\\nodes_io_all.json"))

socket_types = ("Float", "Vector", "Boolean", "Integer", "Geometry", "Color", "String", "Collection", "Image", "Material", "Texture", "Object", "Shader")

file_text = "import math, bpy\n\n"

for node_data in data:
    bl_idname = node_data['bl_idname']
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
            if input['display_shape'] == "DIAMOND":
                default_value = None
            signature_items.append(f"{input['identifier'].lower().replace(' ', '_')}={default_value}")
        else:
            signature_items.append(f"{input['identifier'].lower().replace(' ', '_')}: {input['bl_label']}={input['default']}")
    params_all = []
    for i in params_enum:
        params_all.append((i[0], repr(i[1][0])))
    for i in params:
        param_default = i[1][0]
        if i[1][1] == "str":
            param_default = repr(param_default)
        params_all.append((i[0], param_default))
    if not params_all:
        params_all_str = "\n    params_all = []"
    else:
        params_all_str = "\n    " + f"""params_all = [{', '.join(f"('{param[0]}', {param[0]}, {param[1]})" for param in params_all)}]"""
    inputs_all = []
    for input in inputs:
        name = input['identifier'].lower().replace(" ", "_")
        default_value = input['default']
        if input['bl_label'] == "String":
            default_value = repr(default_value)
        if input['display_shape'] == "DIAMOND":
            default_value = None
        inputs_all.append((name, default_value if default_value != "" else "''"))
    if not inputs_all:
        inputs_all_str = "\n    inputs_all = []"
    else:
        inputs_all_str = "\n    " + f"""inputs_all = [{', '.join(f"({input[0]}, {input[1]})" for input in inputs_all)}]"""
    params_enum_docs = []
    for param_enum in params_enum:
        params_enum_docs.append(f"\n    - `{param_enum[0]}`: {', '.join(f'`{i}`' for i in param_enum[1])}")
    inputs_docs = []
    if len(inputs) > 0:
        inputs_docs.append(f"\n    #### Inputs:")
    for i, input in enumerate(inputs):
        default_value = input['default']
        if input['bl_label'] == "String":
            default_value = repr(default_value)
        inputs_docs.append(f"\n    - `#{i} {input['identifier'].lower().replace(' ', '_')}: {input['bl_label']} = {default_value}`")
    outputs_docs = []
    if len(outputs) > 0:
        outputs_docs.append(f"\n    #### Outputs:")
    for i, output in enumerate(outputs):
        default_value = output['default']
        if default_value == "":
            default_value = '""'
        outputs_docs.append(f"\n    - `#{i} {output['identifier'].lower().replace(' ', '_')}: {output['bl_label']} = {default_value}`")
    template = f'''
def {bl_idname}({", ".join(signature_items)}):
    """{"".join(params_enum_docs) }{"".join(inputs_docs)}{"".join(outputs_docs)}
    """{params_all_str}{inputs_all_str}
    return "{bl_idname}", params_all, inputs_all

'''
    text += template
    file_text += text

file_text += '''

def GeometryNodeInputSceneTime():
    """
    #### Outputs:
    - `#0 seconds: Float = 0.0`
    - `#1 frame: Float = 0.0`
    """
    params_all = []
    inputs_all = []
    return "GeometryNodeInputSceneTime", params_all, inputs_all

'''

file_text += '''


def ShaderNodeScript(mode="INTERNAL", script: bpy.types.Text = None):
    """
    - `mode`: `INTERNAL`, `EXTERNAL`
    """
    params_all = [("mode", mode, "INTERNAL"), ("script", script, None)]
    inputs_all = []
    return "ShaderNodeScript", params_all, inputs_all

'''
with open("nodes.py", "w") as f:
    f.write(file_text)
