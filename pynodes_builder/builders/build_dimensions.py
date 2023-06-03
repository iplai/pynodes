import bpy, itertools, json

attrs = 'bl_description bl_height_default bl_height_max bl_height_min bl_icon bl_idname bl_label bl_rna bl_static_type bl_width_default bl_width_max bl_width_min color dimensions draw_buttons draw_buttons_ext height hide input_template inputs internal_links is_registered_node_type label location mute name output_template outputs parent poll poll_instance rna_type select show_options show_preview show_texture socket_value_update type update use_custom_color width width_hidden'.split()


def gen_dimensions(btree: bpy.types.NodeTree):
    btree.nodes.clear()
    nodes: dict[str, dict] = {}
    for tp in dir(bpy.types):
        try:
            bnode = btree.nodes.new(type=tp)
        except:
            continue

        bpy.ops.wm.redraw_timer(type="DRAW_WIN_SWAP", iterations=1)
        info = {}
        nodes[bnode.bl_idname] = info
        info["params"] = {}
        info['params_enum'] = {}
        default_dim = str((int(bnode.dimensions.x), int(bnode.dimensions.y)))
        for attr in dir(bnode):
            if attr.startswith("__") or attr in attrs:
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
                info['params_enum'][attr] = enum_values
            else:
                info['params'][attr] = attr_type
        info["dimensions"] = default_dim
        if info["params_enum"]:
            param_names = list(info["params_enum"])
            param_values_list = [eval(info["params_enum"][name]) for name in param_names]
            combines = list(itertools.product(*[list(range(len(values))) for values in param_values_list]))
            for combine in combines:
                valid = True
                for i in range(len(param_names)):
                    param_name = param_names[i]
                    param_value = param_values_list[i][combine[i]]
                    try:
                        setattr(bnode, param_name, param_value)
                    except TypeError:
                        valid = False
                if valid:
                    bpy.ops.wm.redraw_timer(type="DRAW_WIN_SWAP", iterations=1)
                    dim = str((int(bnode.dimensions.x), int(bnode.dimensions.y)))
                    if dim != default_dim:
                        info[f"dimensions_{'_'.join(str(n) for n in combine)}"] = dim

        for cate in ['params', 'params_enum']:
            if not info[cate]:
                del info[cate]

    return nodes


btree = bpy.data.node_groups['Geometry Nodes']
nodes = gen_dimensions(btree)
json.dump(nodes, open("pynodes_builder/nodes_dimension.json", "w", encoding="utf-8"), indent=2)
