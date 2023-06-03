# data_types = "FLOAT INT FLOAT_VECTOR FLOAT_COLOR BOOLEAN".split()
# domains = "POINT EDGE FACE CORNER CURVE INSTANCE".split()
# data_types_dict = {
#     "FLOAT": (0, "float", "Float", "value_float", "0.0"),
#     "INT": (1, "integer", "Integer", "value_int", "0"),
#     "FLOAT_VECTOR": (2, "vector", "Vector", "value_vector", "(0.0, 0.0, 0.0)"),
#     "FLOAT_COLOR": (3, "color", "Color", "value_color", "(0.0, 0.0, 0.0, 0.0)"),
#     "BOOLEAN": (4, "boolean", "Boolean", "value_bool", "False"),
# }
text = ""

# for data_type in data_types:
#     for domain in domains:
#         data = data_types_dict[data_type]
#         code = f"""
#     @staticmethod
#     def evaluate_{data[1]}_on_{domain.lower()}s({data[3]}={data[4]}):
#         \"\"\"The Evaluate on Domain allows evaluating a field for a different attribute domain than the domain from the field context. For example, the face index could be used instead of the face corner index, when setting the values of a UV Map
#         #### Path
#         - Utilities > Field > Evaluate on Domain Node
#         #### Outputs:
#         - `#{data[0]} {data[3]}: {data[2]} = {data[4]}`

#         ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeInterpolateDomain.png)

#         [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/field/evaluate_on_domain.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeFieldOnDomain.html)
#         \"\"\"
#         node = new_node(*nodes.GeometryNodeFieldOnDomain("{data_type}", "{domain}", {data[3]}={data[3]}))
#         return node.outputs[{data[0]}].{data[2]}

# """


# for data_type in data_types:
#     for domain in domains:
#         data = data_types_dict[data_type]
#         code = f"""
#     @staticmethod
#     def evaluate_{data[1]}_at_index_on_{domain.lower()}s(index=0, {data[3]}={data[4]}):
#         \"\"\"The Evaluate at Index node allows accessing data of other elements in the context geometry. It is similar to the Sample Index Node. The main difference is that this node does not require a geometry input, because the geometry from the field context is used.
#         #### Path
#         - Utilities > Field > Evaluate at Index Node
#         #### Outputs:
#         - `#{data[0]} {data[3]}: {data[2]} = {data[4]}`

#         ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeFieldAtIndex.webp)

#         [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/field/evaluate_at_index.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeFieldAtIndex.html)
#         \"\"\"
#         node = new_node(*nodes.GeometryNodeFieldAtIndex("{data_type}", "{domain}", index, {data[3]}={data[3]}))
#         return node.outputs[{data[0]}].{data[2]}

# """
#         text += code

# data_types = "FLOAT INT FLOAT_VECTOR".split()
# for data_type in data_types:
#     for domain in domains:
#         data = data_types_dict[data_type]
#         code = f"""
#     @staticmethod
#     def accumulate_{data[1]}_on_{domain.lower()}s({data[3]}={data[4]}, group_index=0):
#         \"\"\"The Accumulate Field node counts a running total of its input values, in the order defined by the geometry's indices. The node's essential operation is just addition, but instead of only outputting the final total, it outputs the current value at every element.
#         #### Path
#         - Utilities > Field > Accumulate Field Node
#         #### Outputs:
#         - `#{data[0]} leading_{data[1]}: {data[2]} = {data[4]}`
#         - `#{data[0]+3} trailing_{data[1]}: {data[2]} = {data[4]}`
#         - `#{data[0]+6} total_{data[1]}: {data[2]} = {data[4]}`

#         ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeAccumulateField.webp)

#         [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/field/accumulate_field.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeAccumulateField.html)
#         \"\"\"
#         node = new_node(*nodes.GeometryNodeAccumulateField("{data_type}", "{domain}", {data[3]}={data[3]}, group_index=group_index))
#         ret = typing.NamedTuple("GeometryNodeAccumulateField", [("leading", {data[2]}), ("trailing", {data[2]}), ("total", {data[2]})])
#         return ret(node.outputs[{data[0]}].{data[2]}, node.outputs[{data[0]+3}].{data[2]}, node.outputs[{data[0]+6}].{data[2]})


# """
#         text += code

# data_types = " FLOAT_VECTOR FLOAT FLOAT_COLOR BOOLEAN INT".split()
# domains = "POINT EDGE FACE CORNER CURVE INSTANCE".split()
# data_types_dict = {
#     "FLOAT_VECTOR": (0, "vector", "Vector", "value_vector", "(0.0, 0.0, 0.0)"),
#     "FLOAT": (1, "float", "Float", "value_float", "0.0"),
#     "FLOAT_COLOR": (2, "color", "Color", "value_color", "(0.0, 0.0, 0.0, 0.0)"),
#     "BOOLEAN": (3, "boolean", "Boolean", "value_bool", "False"),
#     "INT": (4, "integer", "Integer", "value_int", "0"),
# }
# for data_type in data_types:
#     for domain in domains:
#         data = data_types_dict[data_type]
#         code = f"""
#     def capture_{data[1]}_on_{domain.lower()}s(self, {data[3]}={data[4]}):
#         \"\"\"The Capture Attribute node stores the result of a field on a geometry, and outputs the data as a node socket so it can be used by other nodes.
#         - In-Place Operation
#         #### Path
#         - Attribute > Capture Attribute Node
#         #### Outputs:
#         - `#0 geometry: Geometry = None`
#         - `#{data[0]+1} attribute: {data[2]} = {data[4]}`

#         ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeCaptureAttribute.webp)

#         [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/capture_attribute.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeCaptureAttribute.html)
#         \"\"\"
#         node = new_node(*nodes.GeometryNodeCaptureAttribute("{data_type}", "{domain}", self, value_00{data[0]}={data[3]}))
#         self.bsocket = node.outputs[0].bsocket
#         return node.outputs[{data[0]+1}].{data[2]}


# """.replace("value_000", "value")
#         text += code

# modes = " FACES VERTICES EDGES".split()
# domains = "POINT EDGE FACE CORNER CURVE INSTANCE".split()
# data_types_dict = {
#     "FLOAT_VECTOR": (0, "vector", "Vector", "value_vector", "(0.0, 0.0, 0.0)"),
#     "FLOAT": (1, "float", "Float", "value_float", "0.0"),
#     "FLOAT_COLOR": (2, "color", "Color", "value_color", "(0.0, 0.0, 0.0, 0.0)"),
#     "BOOLEAN": (3, "boolean", "Boolean", "value_bool", "False"),
#     "INT": (4, "integer", "Integer", "value_int", "0"),
# }
# for mode in modes:
#     code = f"""
#     def extrude_{mode.lower()}(self, offset_scale=1.0, offset: "Vector" = None, individual=True, selection=True):
#         \"\"\"The Extrude Mesh Node generates new vertices, edges, or faces, on selected geometry and transforms them based on an offset.
#         #### Path
#         - Mesh > Operations > Extrude Mesh Node
#         #### Outputs:
#         - `#0 mesh: Geometry = None`
#         - `#1 top: Boolean = False`
#         - `#2 side: Boolean = False`

#         ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeExtrudeMesh.webp)

#         [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/operations/extrude_mesh.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeExtrudeMesh.html)
#         \"\"\"
#         selection = selection if self._selection is None else self.selection
#         node = new_node(*nodes.GeometryNodeExtrudeMesh("{mode}", self, selection, offset, offset_scale, individual))
#         ret = typing.NamedTuple("GeometryNodeExtrudeMesh", [("mesh", Mesh), ("top", Boolean), ("side", Boolean)])
#         return ret(node.outputs[0].Mesh, node.outputs[1].Boolean, node.outputs[2].Boolean)


# """
#     text += code

data_types = "FLOAT FLOAT_VECTOR".split()
domains = "POINT EDGE FACE CORNER CURVE INSTANCE".split()
data_types_dict = {
    "FLOAT": (0, "float", "Float", "value_float", "0.0"),
    "FLOAT_VECTOR": (1, "vector", "Vector", "value_vector", "(0.0, 0.0, 0.0)"),
}
for data_type in data_types:
    for domain in domains:
        data = data_types_dict[data_type]
        code = f"""
    def {data[1]}_statistic_on_{domain.lower()}s(self, attribute={data[4]}, selection=True):
        \"\"\"The Attribute Statistic node evaluates a field on a geometry and outputs a statistic about the entire data set.
        #### Path
        - Attribute > Attribute Statistic Node
        #### Outputs:
        - `#{data[0]*8+0} mean: {data[2]} = {data[4]}`
        - `#{data[0]*8+1} median: {data[2]} = {data[4]}`
        - `#{data[0]*8+2} sum: {data[2]} = {data[4]}`
        - `#{data[0]*8+3} min: {data[2]} = {data[4]}`
        - `#{data[0]*8+4} max: {data[2]} = {data[4]}`
        - `#{data[0]*8+5} range: {data[2]} = {data[4]}`
        - `#{data[0]*8+6} standard_deviation: {data[2]} = {data[4]}`
        - `#{data[0]*8+7} variance: {data[2]} = {data[4]}`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeAttributeStatistic.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/attribute_statistic.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeStatistic.html)
        \"\"\"
        selection = selection if self._selection is None else self.selection
        node = new_node(*nodes.GeometryNodeAttributeStatistic("{data_type}", "{domain}", self, selection, attribute))
        ret = typing.NamedTuple("AttributeStatistic", [("mean", {data[2]}), ("median", {data[2]}), ("sum", {data[2]}), ("min", {data[2]}), ("max", {data[2]}), ("range", {data[2]}), ("standard_deviation", {data[2]}), ("variance", {data[2]})])
        return ret(node.outputs[{data[0]*8+0}].{data[2]}, node.outputs[{data[0]*8+1}].{data[2]}, node.outputs[{data[0]*8+2}].{data[2]}, node.outputs[{data[0]*8+3}].{data[2]}, node.outputs[{data[0]*8+4}].{data[2]}, node.outputs[{data[0]*8+5}].{data[2]}, node.outputs[{data[0]*8+6}].{data[2]}, node.outputs[{data[0]*8+7}].{data[2]})



"""
        text += code

import bpy
bpy.context.window_manager.clipboard = text
