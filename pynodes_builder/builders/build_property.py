import bpy, itertools, mathutils, json, re


attrs = 'bl_description bl_height_default bl_height_max bl_height_min bl_icon bl_idname bl_label bl_rna bl_static_type bl_width_default bl_width_max bl_width_min color dimensions draw_buttons draw_buttons_ext height hide input_template inputs internal_links is_registered_node_type label location mute name output_template outputs parent poll poll_instance rna_type select show_options show_preview show_texture socket_value_update type update use_custom_color width width_hidden'.split()
attrs_without_type = 'bl_description bl_height_default bl_height_max bl_height_min bl_icon bl_idname bl_label bl_rna bl_static_type bl_width_default bl_width_max bl_width_min color dimensions draw_buttons draw_buttons_ext height hide input_template inputs internal_links is_registered_node_type label location mute name output_template outputs parent poll poll_instance rna_type select show_options show_preview show_texture socket_value_update update use_custom_color width width_hidden'.split()

btree = bpy.data.node_groups["Geometry Nodes"]
btree.nodes.clear()
data: list[dict] = json.load(open("pynodes_builder\\nodes_doc_url.json"))
data_ouputs = {}
for node_data in data:
    bl_idname = node_data['bl_idname']
    if bl_idname in ['FunctionNodeRotateEuler']:
        attrs_filter = attrs_without_type
    else:
        attrs_filter = attrs
    bnode = btree.nodes.new(bl_idname)
    data_ouputs[bl_idname] = {}
    properties_enum = {}
    properties = {}
    for attr in dir(bnode):
        if attr.startswith("__") or attr in attrs_filter:
            continue
        value = getattr(bnode, attr)
        if value.__class__.__module__ == 'builtins':
            attr_type = value.__class__.__name__
        else:
            attr_type = f"{value.__class__.__module__}.{value.__class__.__name__}"

        enum_values = None
        if attr_type == "str":
            try:
                setattr(bnode, attr, "TOTO")
            except TypeError as e:
                enum_values = str(e)[54:]
        if enum_values is not None:
            enum_values = eval(enum_values)
            tem = [value]
            for i in enum_values:
                if i != value:
                    tem.append(i)
            properties_enum[attr] = ', '.join(tem)
        else:
            if isinstance(value, mathutils.Vector):
                value = tuple(value)
            if attr == "material":
                attr_type = "bpy.types.Material"
            if attr_type.startswith("bpy.types"):
                value = None
            properties[attr] = {
                "default": str(value),
                "type": attr_type,
            }
    for k, v in properties_enum.items():
        data_ouputs[bl_idname][k] = v
    for k, v in properties.items():
        data_ouputs[bl_idname][k] = v
json.dump(data_ouputs, open("pynodes_builder\\nodes_property.json", "w"), indent=2)
