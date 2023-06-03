import json

# data1 = json.load(open("pynodes_builder/nodes_dimension_geo.json"))
# data2 = json.load(open("pynodes_builder/nodes_dimension_shader.json"))

# for key, val in data2.items():
#     if key in data1:
#         continue
#     data1[key] = val

# for key, val in data1.items():
#     if "params" in val:
#         del val['params']

# json.dump(data1, open("pynodes_builder/nodes_dimension_all.json", 'w', encoding='utf-8'), indent=2)

data1 = json.load(open("pynodes_builder/nodes_property_geo.json"))
data2 = json.load(open("pynodes_builder/nodes_property_shader.json"))

for key, val in data2.items():
    if key in data1:
        continue
    data1[key] = val

json.dump(data1, open("pynodes_builder/nodes_property_all.json", 'w', encoding='utf-8'), indent=2)


# data1 = json.load(open("pynodes_builder/nodes_io_geo.json"))
# data2 = json.load(open("pynodes_builder/nodes_io_shader.json"))

# for key, val in data2.items():
#     if key in data1:
#         continue
#     data1[key] = val

# json.dump(data1, open("pynodes_builder/nodes_io_all.json", 'w', encoding='utf-8'), indent=2)

# data1 = json.load(open("pynodes_builder/nodes_doc_url_geo.json"))
# data2 = json.load(open("pynodes_builder/nodes_doc_url_shader.json"))

# names = [a['bl_idname'] for a in data1]

# for item in data2:
#     if item['bl_idname'] not in names:
#         data1.append(item)


# json.dump(data1, open("pynodes_builder/nodes_doc_url_all.json", 'w', encoding='utf-8'), indent=2)
