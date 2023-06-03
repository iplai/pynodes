import bpy, itertools, mathutils, json, re


attrs = 'bl_description bl_height_default bl_height_max bl_height_min bl_icon bl_idname bl_label bl_rna bl_static_type bl_width_default bl_width_max bl_width_min color dimensions draw_buttons draw_buttons_ext height hide input_template inputs internal_links is_registered_node_type label location mute name output_template outputs parent poll poll_instance rna_type select show_options show_preview show_texture socket_value_update type update use_clamp use_custom_color width width_hidden'
attrs = attrs.split()
btree = bpy.data.materials['Material'].node_tree
btree.nodes.clear()
data: list[dict] = json.load(open("pynodes_builder\\nodes_doc_url_shader.json"))
data_ouputs = {}
for node_data in data:
    bl_idname = node_data['bl_idname']
    bnode = btree.nodes.new(bl_idname)
    data_ouputs[bl_idname] = {}
    inputs = []
    outputs = []
    for input in bnode.inputs:
        identifier = input.identifier
        default_value = getattr(input, 'default_value', None)
        value_type = input.type
        if input.type == "VALUE":
            value_type = "FLOAT"
            if input.bl_idname == "NodeSocketFloatAngle":
                import math
                default_value = f"math.radians({round(math.degrees(default_value),1)})"
            else:
                default_value = round(default_value, 3)
                if default_value == round(default_value, 2):
                    default_value = round(default_value, 2)
                if default_value == round(default_value, 1):
                    default_value = round(default_value, 1)
        elif input.type in ("VECTOR", "RGBA"):
            default_value = tuple(default_value)
            tem = []
            for c in default_value:
                c = round(c, 3)
                if c == round(c, 2):
                    c = round(c, 2)
                if c == round(c, 1):
                    c = round(c, 1)
                tem.append(c)
            default_value = tuple(tem)
        elif input.type in ("STRING", "GEOMETRY", "BOOLEAN", "INT", "COLLECTION", "IMAGE", "OBJECT", "TEXTURE", "MATERIAL", "CUSTOM"):
            ...
        else:
            print(bl_idname + ",", identifier, default_value, default_value.__class__, input.type)
        inputs.append({
            "identifier": identifier,
            "default": str(default_value),
            "type": value_type,
            "bl_idname": input.bl_idname,
            "name": input.name,
            "bl_label": input.bl_label,
            "display_shape": input.display_shape,
        })

    for output in bnode.outputs:
        identifier = output.identifier
        default_value = getattr(output, 'default_value', None)
        value_type = output.type
        if output.type == "VALUE":
            value_type = "FLOAT"
            if output.bl_idname == "NodeSocketFloatAngle":
                import math
                default_value = f"math.radians({round(math.degrees(default_value),1)})"
            else:
                default_value = round(default_value, 3)
                if default_value == round(default_value, 2):
                    default_value = round(default_value, 2)
                if default_value == round(default_value, 1):
                    default_value = round(default_value, 1)
        elif output.type in ("VECTOR", "RGBA"):
            default_value = tuple(default_value)
            tem = []
            for c in default_value:
                c = round(c, 3)
                if c == round(c, 2):
                    c = round(c, 2)
                if c == round(c, 1):
                    c = round(c, 1)
                tem.append(c)
            default_value = tuple(tem)
        elif output.type in ("STRING", "GEOMETRY", "BOOLEAN", "INT", "COLLECTION", "IMAGE", "OBJECT", "TEXTURE", "MATERIAL", "CUSTOM"):
            ...
        else:
            print(bl_idname + ",", identifier, default_value, default_value.__class__, output.type)
        outputs.append({
            "identifier": identifier,
            "default": str(default_value),
            "type": value_type,
            "bl_idname": output.bl_idname,
            "name": output.name,
            "bl_label": output.bl_label,
            "display_shape": output.display_shape,
        })
    data_ouputs[bl_idname]['inputs'] = inputs
    data_ouputs[bl_idname]['outputs'] = outputs
json.dump(data_ouputs, open("pynodes_builder\\nodes_io_shader.json", "w"), indent=2)
