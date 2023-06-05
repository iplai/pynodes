import bpy, typing, math
from .core import Socket, new_node, new_link
from . import nodes


class Geometry(Socket):
    bl_idname = "NodeSocketGeometry"

    def __init__(self, bsocket: bpy.types.NodeSocket) -> None:
        super().__init__(bsocket)
        self._selection: Socket = None
        self._id = None
        self._index = None
        self._normal = None
        self._position = None
        self._radius = None

    def __getitem__(self, selection):
        socket = None
        if isinstance(selection, slice):
            start, stop = selection.start, selection.stop
            if start is None and stop is None:
                return self
            if stop is None:
                start = start if isinstance(start, Socket) else int(start)
                socket = self.index >= start
            elif selection.start is None:
                stop = stop if isinstance(stop, Socket) else int(stop)
                socket = self.index < stop
            else:
                from .datasocks import Compare
                socket = Compare("FLOAT", operation="EQUAL", a=self.index, b=(start + stop) / 2 - 0.1, epsilon=(stop - start) / 2)
        elif type(selection) == int:
            socket = self.index == selection
        elif isinstance(selection, Boolean):
            socket = selection
        elif type(selection) == tuple:
            conditions: list[Boolean] = []
            for sel in selection:
                if isinstance(sel, (int, Integer, Float)):
                    conditions.append(self.index == sel)
                elif isinstance(sel, Boolean):
                    conditions.append(sel)
            socket = conditions[0]
            for condition in conditions[1:]:
                socket = socket + condition
        if socket is None:
            return self
        if self._selection is not None:
            self._selection = socket * self._selection
        else:
            self._selection = socket
        return self

    @property
    def selection(self):
        socket = self._selection
        self._selection = None
        return socket

    def float_statistic_on_points(self, attribute=0.0, selection=True):
        """The Attribute Statistic node evaluates a field on a geometry and outputs a statistic about the entire data set.
        #### Path
        - Attribute > Attribute Statistic Node
        #### Outputs:
        - `#0 mean: Float = 0.0`
        - `#1 median: Float = 0.0`
        - `#2 sum: Float = 0.0`
        - `#3 min: Float = 0.0`
        - `#4 max: Float = 0.0`
        - `#5 range: Float = 0.0`
        - `#6 standard_deviation: Float = 0.0`
        - `#7 variance: Float = 0.0`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeAttributeStatistic.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/attribute_statistic.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeStatistic.html)
        """
        selection = selection if self._selection is None else self.selection
        node = new_node(*nodes.GeometryNodeAttributeStatistic("FLOAT", "POINT", self, selection, attribute))
        ret = typing.NamedTuple("AttributeStatistic", [("mean", Float), ("median", Float), ("sum", Float), ("min", Float), ("max", Float), ("range", Float), ("standard_deviation", Float), ("variance", Float)])
        return ret(node.outputs[0].Float, node.outputs[1].Float, node.outputs[2].Float, node.outputs[3].Float, node.outputs[4].Float, node.outputs[5].Float, node.outputs[6].Float, node.outputs[7].Float)

    def float_statistic_on_edges(self, attribute=0.0, selection=True):
        """The Attribute Statistic node evaluates a field on a geometry and outputs a statistic about the entire data set.
        #### Path
        - Attribute > Attribute Statistic Node
        #### Outputs:
        - `#0 mean: Float = 0.0`
        - `#1 median: Float = 0.0`
        - `#2 sum: Float = 0.0`
        - `#3 min: Float = 0.0`
        - `#4 max: Float = 0.0`
        - `#5 range: Float = 0.0`
        - `#6 standard_deviation: Float = 0.0`
        - `#7 variance: Float = 0.0`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeAttributeStatistic.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/attribute_statistic.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeStatistic.html)
        """
        selection = selection if self._selection is None else self.selection
        node = new_node(*nodes.GeometryNodeAttributeStatistic("FLOAT", "EDGE", self, selection, attribute))
        ret = typing.NamedTuple("AttributeStatistic", [("mean", Float), ("median", Float), ("sum", Float), ("min", Float), ("max", Float), ("range", Float), ("standard_deviation", Float), ("variance", Float)])
        return ret(node.outputs[0].Float, node.outputs[1].Float, node.outputs[2].Float, node.outputs[3].Float, node.outputs[4].Float, node.outputs[5].Float, node.outputs[6].Float, node.outputs[7].Float)

    def float_statistic_on_faces(self, attribute=0.0, selection=True):
        """The Attribute Statistic node evaluates a field on a geometry and outputs a statistic about the entire data set.
        #### Path
        - Attribute > Attribute Statistic Node
        #### Outputs:
        - `#0 mean: Float = 0.0`
        - `#1 median: Float = 0.0`
        - `#2 sum: Float = 0.0`
        - `#3 min: Float = 0.0`
        - `#4 max: Float = 0.0`
        - `#5 range: Float = 0.0`
        - `#6 standard_deviation: Float = 0.0`
        - `#7 variance: Float = 0.0`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeAttributeStatistic.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/attribute_statistic.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeStatistic.html)
        """
        selection = selection if self._selection is None else self.selection
        node = new_node(*nodes.GeometryNodeAttributeStatistic("FLOAT", "FACE", self, selection, attribute))
        ret = typing.NamedTuple("AttributeStatistic", [("mean", Float), ("median", Float), ("sum", Float), ("min", Float), ("max", Float), ("range", Float), ("standard_deviation", Float), ("variance", Float)])
        return ret(node.outputs[0].Float, node.outputs[1].Float, node.outputs[2].Float, node.outputs[3].Float, node.outputs[4].Float, node.outputs[5].Float, node.outputs[6].Float, node.outputs[7].Float)

    def float_statistic_on_corners(self, attribute=0.0, selection=True):
        """The Attribute Statistic node evaluates a field on a geometry and outputs a statistic about the entire data set.
        #### Path
        - Attribute > Attribute Statistic Node
        #### Outputs:
        - `#0 mean: Float = 0.0`
        - `#1 median: Float = 0.0`
        - `#2 sum: Float = 0.0`
        - `#3 min: Float = 0.0`
        - `#4 max: Float = 0.0`
        - `#5 range: Float = 0.0`
        - `#6 standard_deviation: Float = 0.0`
        - `#7 variance: Float = 0.0`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeAttributeStatistic.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/attribute_statistic.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeStatistic.html)
        """
        selection = selection if self._selection is None else self.selection
        node = new_node(*nodes.GeometryNodeAttributeStatistic("FLOAT", "CORNER", self, selection, attribute))
        ret = typing.NamedTuple("AttributeStatistic", [("mean", Float), ("median", Float), ("sum", Float), ("min", Float), ("max", Float), ("range", Float), ("standard_deviation", Float), ("variance", Float)])
        return ret(node.outputs[0].Float, node.outputs[1].Float, node.outputs[2].Float, node.outputs[3].Float, node.outputs[4].Float, node.outputs[5].Float, node.outputs[6].Float, node.outputs[7].Float)

    def float_statistic_on_curves(self, attribute=0.0, selection=True):
        """The Attribute Statistic node evaluates a field on a geometry and outputs a statistic about the entire data set.
        #### Path
        - Attribute > Attribute Statistic Node
        #### Outputs:
        - `#0 mean: Float = 0.0`
        - `#1 median: Float = 0.0`
        - `#2 sum: Float = 0.0`
        - `#3 min: Float = 0.0`
        - `#4 max: Float = 0.0`
        - `#5 range: Float = 0.0`
        - `#6 standard_deviation: Float = 0.0`
        - `#7 variance: Float = 0.0`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeAttributeStatistic.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/attribute_statistic.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeStatistic.html)
        """
        selection = selection if self._selection is None else self.selection
        node = new_node(*nodes.GeometryNodeAttributeStatistic("FLOAT", "CURVE", self, selection, attribute))
        ret = typing.NamedTuple("AttributeStatistic", [("mean", Float), ("median", Float), ("sum", Float), ("min", Float), ("max", Float), ("range", Float), ("standard_deviation", Float), ("variance", Float)])
        return ret(node.outputs[0].Float, node.outputs[1].Float, node.outputs[2].Float, node.outputs[3].Float, node.outputs[4].Float, node.outputs[5].Float, node.outputs[6].Float, node.outputs[7].Float)

    def float_statistic_on_instances(self, attribute=0.0, selection=True):
        """The Attribute Statistic node evaluates a field on a geometry and outputs a statistic about the entire data set.
        #### Path
        - Attribute > Attribute Statistic Node
        #### Outputs:
        - `#0 mean: Float = 0.0`
        - `#1 median: Float = 0.0`
        - `#2 sum: Float = 0.0`
        - `#3 min: Float = 0.0`
        - `#4 max: Float = 0.0`
        - `#5 range: Float = 0.0`
        - `#6 standard_deviation: Float = 0.0`
        - `#7 variance: Float = 0.0`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeAttributeStatistic.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/attribute_statistic.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeStatistic.html)
        """
        selection = selection if self._selection is None else self.selection
        node = new_node(*nodes.GeometryNodeAttributeStatistic("FLOAT", "INSTANCE", self, selection, attribute))
        ret = typing.NamedTuple("AttributeStatistic", [("mean", Float), ("median", Float), ("sum", Float), ("min", Float), ("max", Float), ("range", Float), ("standard_deviation", Float), ("variance", Float)])
        return ret(node.outputs[0].Float, node.outputs[1].Float, node.outputs[2].Float, node.outputs[3].Float, node.outputs[4].Float, node.outputs[5].Float, node.outputs[6].Float, node.outputs[7].Float)

    def vector_statistic_on_points(self, attribute=(0.0, 0.0, 0.0), selection=True):
        """The Attribute Statistic node evaluates a field on a geometry and outputs a statistic about the entire data set.
        #### Path
        - Attribute > Attribute Statistic Node
        #### Outputs:
        - `#8 mean: Vector = (0.0, 0.0, 0.0)`
        - `#9 median: Vector = (0.0, 0.0, 0.0)`
        - `#10 sum: Vector = (0.0, 0.0, 0.0)`
        - `#11 min: Vector = (0.0, 0.0, 0.0)`
        - `#12 max: Vector = (0.0, 0.0, 0.0)`
        - `#13 range: Vector = (0.0, 0.0, 0.0)`
        - `#14 standard_deviation: Vector = (0.0, 0.0, 0.0)`
        - `#15 variance: Vector = (0.0, 0.0, 0.0)`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeAttributeStatistic.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/attribute_statistic.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeStatistic.html)
        """
        selection = selection if self._selection is None else self.selection
        node = new_node(*nodes.GeometryNodeAttributeStatistic("FLOAT_VECTOR", "POINT", self, selection, attribute))
        ret = typing.NamedTuple("AttributeStatistic", [("mean", Vector), ("median", Vector), ("sum", Vector), ("min", Vector), ("max", Vector), ("range", Vector), ("standard_deviation", Vector), ("variance", Vector)])
        return ret(node.outputs[8].Vector, node.outputs[9].Vector, node.outputs[10].Vector, node.outputs[11].Vector, node.outputs[12].Vector, node.outputs[13].Vector, node.outputs[14].Vector, node.outputs[15].Vector)

    def vector_statistic_on_edges(self, attribute=(0.0, 0.0, 0.0), selection=True):
        """The Attribute Statistic node evaluates a field on a geometry and outputs a statistic about the entire data set.
        #### Path
        - Attribute > Attribute Statistic Node
        #### Outputs:
        - `#8 mean: Vector = (0.0, 0.0, 0.0)`
        - `#9 median: Vector = (0.0, 0.0, 0.0)`
        - `#10 sum: Vector = (0.0, 0.0, 0.0)`
        - `#11 min: Vector = (0.0, 0.0, 0.0)`
        - `#12 max: Vector = (0.0, 0.0, 0.0)`
        - `#13 range: Vector = (0.0, 0.0, 0.0)`
        - `#14 standard_deviation: Vector = (0.0, 0.0, 0.0)`
        - `#15 variance: Vector = (0.0, 0.0, 0.0)`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeAttributeStatistic.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/attribute_statistic.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeStatistic.html)
        """
        selection = selection if self._selection is None else self.selection
        node = new_node(*nodes.GeometryNodeAttributeStatistic("FLOAT_VECTOR", "EDGE", self, selection, attribute))
        ret = typing.NamedTuple("AttributeStatistic", [("mean", Vector), ("median", Vector), ("sum", Vector), ("min", Vector), ("max", Vector), ("range", Vector), ("standard_deviation", Vector), ("variance", Vector)])
        return ret(node.outputs[8].Vector, node.outputs[9].Vector, node.outputs[10].Vector, node.outputs[11].Vector, node.outputs[12].Vector, node.outputs[13].Vector, node.outputs[14].Vector, node.outputs[15].Vector)

    def vector_statistic_on_faces(self, attribute=(0.0, 0.0, 0.0), selection=True):
        """The Attribute Statistic node evaluates a field on a geometry and outputs a statistic about the entire data set.
        #### Path
        - Attribute > Attribute Statistic Node
        #### Outputs:
        - `#8 mean: Vector = (0.0, 0.0, 0.0)`
        - `#9 median: Vector = (0.0, 0.0, 0.0)`
        - `#10 sum: Vector = (0.0, 0.0, 0.0)`
        - `#11 min: Vector = (0.0, 0.0, 0.0)`
        - `#12 max: Vector = (0.0, 0.0, 0.0)`
        - `#13 range: Vector = (0.0, 0.0, 0.0)`
        - `#14 standard_deviation: Vector = (0.0, 0.0, 0.0)`
        - `#15 variance: Vector = (0.0, 0.0, 0.0)`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeAttributeStatistic.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/attribute_statistic.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeStatistic.html)
        """
        selection = selection if self._selection is None else self.selection
        node = new_node(*nodes.GeometryNodeAttributeStatistic("FLOAT_VECTOR", "FACE", self, selection, attribute))
        ret = typing.NamedTuple("AttributeStatistic", [("mean", Vector), ("median", Vector), ("sum", Vector), ("min", Vector), ("max", Vector), ("range", Vector), ("standard_deviation", Vector), ("variance", Vector)])
        return ret(node.outputs[8].Vector, node.outputs[9].Vector, node.outputs[10].Vector, node.outputs[11].Vector, node.outputs[12].Vector, node.outputs[13].Vector, node.outputs[14].Vector, node.outputs[15].Vector)

    def vector_statistic_on_corners(self, attribute=(0.0, 0.0, 0.0), selection=True):
        """The Attribute Statistic node evaluates a field on a geometry and outputs a statistic about the entire data set.
        #### Path
        - Attribute > Attribute Statistic Node
        #### Outputs:
        - `#8 mean: Vector = (0.0, 0.0, 0.0)`
        - `#9 median: Vector = (0.0, 0.0, 0.0)`
        - `#10 sum: Vector = (0.0, 0.0, 0.0)`
        - `#11 min: Vector = (0.0, 0.0, 0.0)`
        - `#12 max: Vector = (0.0, 0.0, 0.0)`
        - `#13 range: Vector = (0.0, 0.0, 0.0)`
        - `#14 standard_deviation: Vector = (0.0, 0.0, 0.0)`
        - `#15 variance: Vector = (0.0, 0.0, 0.0)`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeAttributeStatistic.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/attribute_statistic.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeStatistic.html)
        """
        selection = selection if self._selection is None else self.selection
        node = new_node(*nodes.GeometryNodeAttributeStatistic("FLOAT_VECTOR", "CORNER", self, selection, attribute))
        ret = typing.NamedTuple("AttributeStatistic", [("mean", Vector), ("median", Vector), ("sum", Vector), ("min", Vector), ("max", Vector), ("range", Vector), ("standard_deviation", Vector), ("variance", Vector)])
        return ret(node.outputs[8].Vector, node.outputs[9].Vector, node.outputs[10].Vector, node.outputs[11].Vector, node.outputs[12].Vector, node.outputs[13].Vector, node.outputs[14].Vector, node.outputs[15].Vector)

    def vector_statistic_on_curves(self, attribute=(0.0, 0.0, 0.0), selection=True):
        """The Attribute Statistic node evaluates a field on a geometry and outputs a statistic about the entire data set.
        #### Path
        - Attribute > Attribute Statistic Node
        #### Outputs:
        - `#8 mean: Vector = (0.0, 0.0, 0.0)`
        - `#9 median: Vector = (0.0, 0.0, 0.0)`
        - `#10 sum: Vector = (0.0, 0.0, 0.0)`
        - `#11 min: Vector = (0.0, 0.0, 0.0)`
        - `#12 max: Vector = (0.0, 0.0, 0.0)`
        - `#13 range: Vector = (0.0, 0.0, 0.0)`
        - `#14 standard_deviation: Vector = (0.0, 0.0, 0.0)`
        - `#15 variance: Vector = (0.0, 0.0, 0.0)`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeAttributeStatistic.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/attribute_statistic.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeStatistic.html)
        """
        selection = selection if self._selection is None else self.selection
        node = new_node(*nodes.GeometryNodeAttributeStatistic("FLOAT_VECTOR", "CURVE", self, selection, attribute))
        ret = typing.NamedTuple("AttributeStatistic", [("mean", Vector), ("median", Vector), ("sum", Vector), ("min", Vector), ("max", Vector), ("range", Vector), ("standard_deviation", Vector), ("variance", Vector)])
        return ret(node.outputs[8].Vector, node.outputs[9].Vector, node.outputs[10].Vector, node.outputs[11].Vector, node.outputs[12].Vector, node.outputs[13].Vector, node.outputs[14].Vector, node.outputs[15].Vector)

    def vector_statistic_on_instances(self, attribute=(0.0, 0.0, 0.0), selection=True):
        """The Attribute Statistic node evaluates a field on a geometry and outputs a statistic about the entire data set.
        #### Path
        - Attribute > Attribute Statistic Node
        #### Outputs:
        - `#8 mean: Vector = (0.0, 0.0, 0.0)`
        - `#9 median: Vector = (0.0, 0.0, 0.0)`
        - `#10 sum: Vector = (0.0, 0.0, 0.0)`
        - `#11 min: Vector = (0.0, 0.0, 0.0)`
        - `#12 max: Vector = (0.0, 0.0, 0.0)`
        - `#13 range: Vector = (0.0, 0.0, 0.0)`
        - `#14 standard_deviation: Vector = (0.0, 0.0, 0.0)`
        - `#15 variance: Vector = (0.0, 0.0, 0.0)`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeAttributeStatistic.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/attribute_statistic.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeStatistic.html)
        """
        selection = selection if self._selection is None else self.selection
        node = new_node(*nodes.GeometryNodeAttributeStatistic("FLOAT_VECTOR", "INSTANCE", self, selection, attribute))
        ret = typing.NamedTuple("AttributeStatistic", [("mean", Vector), ("median", Vector), ("sum", Vector), ("min", Vector), ("max", Vector), ("range", Vector), ("standard_deviation", Vector), ("variance", Vector)])
        return ret(node.outputs[8].Vector, node.outputs[9].Vector, node.outputs[10].Vector, node.outputs[11].Vector, node.outputs[12].Vector, node.outputs[13].Vector, node.outputs[14].Vector, node.outputs[15].Vector)

    def domain_size(self, component="MESH"):
        """The Domain Size outputs the size of an attribute domain on the selected geometry type, for example, the number of edges in a mesh, or the number of points in a point cloud.
        #### Path
        - Attribute > Domain Size Node
        #### Properties
        - `component`: `MESH`, `POINTCLOUD`, `CURVE`, `INSTANCES`
        #### Outputs:
        - `#0 point_count: Integer = 0`
        - `#1 edge_count: Integer = 0`
        - `#2 face_count: Integer = 0`
        - `#3 face_corner_count: Integer = 0`
        - `#4 spline_count: Integer = 0`
        - `#5 instance_count: Integer = 0`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeAttributeDomainSize.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/domain_size.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeDomainSize.html)
        """
        node = new_node(*nodes.GeometryNodeAttributeDomainSize(component, self))
        ret = typing.NamedTuple("GeometryNodeAttributeDomainSize", [("point_count", Integer), ("edge_count", Integer), ("face_count", Integer), ("face_corner_count", Integer), ("spline_count", Integer), ("instance_count", Integer)])
        return ret(node.outputs[0].Integer, node.outputs[1].Integer, node.outputs[2].Integer, node.outputs[3].Integer, node.outputs[4].Integer, node.outputs[5].Integer)

    @staticmethod
    def blur_float_attribute(value_float=0.0, iterations=1, weight=1.0):
        """The Blur Attribute node smooths attribute values between neighboring geometry elements.
        #### Path
        - Attribute > Blur Attribute Node
        #### Outputs:
        - `#0 value_float: Float = 0.0`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeBlurAttribute.jpg)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/blur_attribute.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeBlurAttribute.html)
        """
        node = new_node(*nodes.GeometryNodeBlurAttribute("Float", value_float=value_float, iterations=iterations, weight=weight))
        return node.outputs[0].Float

    @staticmethod
    def blur_integer_attribute(value_int=0, iterations=1, weight=1.0):
        """The Blur Attribute node smooths attribute values between neighboring geometry elements.
        #### Path
        - Attribute > Blur Attribute Node
        #### Outputs:
        - `#1 value_int: Integer = 0`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeBlurAttribute.jpg)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/blur_attribute.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeBlurAttribute.html)
        """
        node = new_node(*nodes.GeometryNodeBlurAttribute("INT", value_int=value_int, iterations=iterations, weight=weight))
        return node.outputs[1].Integer

    @staticmethod
    def blur_vector_attribute(value_vector=(0.0, 0.0, 0.0), iterations=1, weight=1.0):
        """The Blur Attribute node smooths attribute values between neighboring geometry elements.
        #### Path
        - Attribute > Blur Attribute Node
        #### Outputs:
        - `#2 value_vector: Vector = (0.0, 0.0, 0.0)`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeBlurAttribute.jpg)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/blur_attribute.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeBlurAttribute.html)
        """
        node = new_node(*nodes.GeometryNodeBlurAttribute("FLOAT_VECTOR", value_vector == value_vector, iterations=iterations, weight=weight))
        return node.outputs[2].Vector

    @staticmethod
    def blur_color_attribute(value_color=(0.0, 0.0, 0.0, 0.0), iterations=1, weight=1.0):
        """The Blur Attribute node smooths attribute values between neighboring geometry elements.
        #### Path
        - Attribute > Blur Attribute Node
        #### Outputs:
        - `#3 value_color: Color = (0.0, 0.0, 0.0, 0.0)`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeBlurAttribute.jpg)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/blur_attribute.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeBlurAttribute.html)
        """
        node = new_node(*nodes.GeometryNodeBlurAttribute("FLOAT_COLOR", value_color=value_color, iterations=iterations, weight=weight))
        return node.outputs[3].Color

    def switch(self, switch=False, true_geometry=None):
        """The Switch node outputs one of two inputs depending on a condition. Only the input that is passed through the node is computed.
        - In-Place Operation
        #### Path
        - Utilities > Switch Node
        #### Outputs:
        - `#6 output_006: Geometry = None`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeSwitch.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/switch.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeSwitch.html)
        """
        node = new_node(*nodes.GeometryNodeSwitch("GEOMETRY", switch_001=switch, false_006=self, true_006=true_geometry))
        self.bsocket = node.outputs[6].bsocket
        return self

    def capture_vector_on_points(self, value_vector=(0.0, 0.0, 0.0)):
        """The Capture Attribute node stores the result of a field on a geometry, and outputs the data as a node socket so it can be used by other nodes.
        - In-Place Operation
        #### Path
        - Attribute > Capture Attribute Node
        #### Outputs:
        - `#0 geometry: Geometry = None`
        - `#1 attribute: Vector = (0.0, 0.0, 0.0)`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeCaptureAttribute.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/capture_attribute.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeCaptureAttribute.html)
        """
        node = new_node(*nodes.GeometryNodeCaptureAttribute("FLOAT_VECTOR", "POINT", self, value=value_vector))
        self.bsocket = node.outputs[0].bsocket
        return node.outputs[1].Vector

    def capture_vector_on_edges(self, value_vector=(0.0, 0.0, 0.0)):
        """The Capture Attribute node stores the result of a field on a geometry, and outputs the data as a node socket so it can be used by other nodes.
        - In-Place Operation
        #### Path
        - Attribute > Capture Attribute Node
        #### Outputs:
        - `#0 geometry: Geometry = None`
        - `#1 attribute: Vector = (0.0, 0.0, 0.0)`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeCaptureAttribute.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/capture_attribute.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeCaptureAttribute.html)
        """
        node = new_node(*nodes.GeometryNodeCaptureAttribute("FLOAT_VECTOR", "EDGE", self, value=value_vector))
        self.bsocket = node.outputs[0].bsocket
        return node.outputs[1].Vector

    def capture_vector_on_faces(self, value_vector=(0.0, 0.0, 0.0)):
        """The Capture Attribute node stores the result of a field on a geometry, and outputs the data as a node socket so it can be used by other nodes.
        - In-Place Operation
        #### Path
        - Attribute > Capture Attribute Node
        #### Outputs:
        - `#0 geometry: Geometry = None`
        - `#1 attribute: Vector = (0.0, 0.0, 0.0)`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeCaptureAttribute.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/capture_attribute.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeCaptureAttribute.html)
        """
        node = new_node(*nodes.GeometryNodeCaptureAttribute("FLOAT_VECTOR", "FACE", self, value=value_vector))
        self.bsocket = node.outputs[0].bsocket
        return node.outputs[1].Vector

    def capture_vector_on_corners(self, value_vector=(0.0, 0.0, 0.0)):
        """The Capture Attribute node stores the result of a field on a geometry, and outputs the data as a node socket so it can be used by other nodes.
        - In-Place Operation
        #### Path
        - Attribute > Capture Attribute Node
        #### Outputs:
        - `#0 geometry: Geometry = None`
        - `#1 attribute: Vector = (0.0, 0.0, 0.0)`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeCaptureAttribute.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/capture_attribute.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeCaptureAttribute.html)
        """
        node = new_node(*nodes.GeometryNodeCaptureAttribute("FLOAT_VECTOR", "CORNER", self, value=value_vector))
        self.bsocket = node.outputs[0].bsocket
        return node.outputs[1].Vector

    def capture_vector_on_curves(self, value_vector=(0.0, 0.0, 0.0)):
        """The Capture Attribute node stores the result of a field on a geometry, and outputs the data as a node socket so it can be used by other nodes.
        - In-Place Operation
        #### Path
        - Attribute > Capture Attribute Node
        #### Outputs:
        - `#0 geometry: Geometry = None`
        - `#1 attribute: Vector = (0.0, 0.0, 0.0)`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeCaptureAttribute.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/capture_attribute.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeCaptureAttribute.html)
        """
        node = new_node(*nodes.GeometryNodeCaptureAttribute("FLOAT_VECTOR", "CURVE", self, value=value_vector))
        self.bsocket = node.outputs[0].bsocket
        return node.outputs[1].Vector

    def capture_vector_on_instances(self, value_vector=(0.0, 0.0, 0.0)):
        """The Capture Attribute node stores the result of a field on a geometry, and outputs the data as a node socket so it can be used by other nodes.
        - In-Place Operation
        #### Path
        - Attribute > Capture Attribute Node
        #### Outputs:
        - `#0 geometry: Geometry = None`
        - `#1 attribute: Vector = (0.0, 0.0, 0.0)`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeCaptureAttribute.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/capture_attribute.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeCaptureAttribute.html)
        """
        node = new_node(*nodes.GeometryNodeCaptureAttribute("FLOAT_VECTOR", "INSTANCE", self, value=value_vector))
        self.bsocket = node.outputs[0].bsocket
        return node.outputs[1].Vector

    def capture_float_on_points(self, value_float=0.0):
        """The Capture Attribute node stores the result of a field on a geometry, and outputs the data as a node socket so it can be used by other nodes.
        - In-Place Operation
        #### Path
        - Attribute > Capture Attribute Node
        #### Outputs:
        - `#0 geometry: Geometry = None`
        - `#2 attribute: Float = 0.0`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeCaptureAttribute.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/capture_attribute.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeCaptureAttribute.html)
        """
        node = new_node(*nodes.GeometryNodeCaptureAttribute("FLOAT", "POINT", self, value_001=value_float))
        self.bsocket = node.outputs[0].bsocket
        return node.outputs[2].Float

    def capture_float_on_edges(self, value_float=0.0):
        """The Capture Attribute node stores the result of a field on a geometry, and outputs the data as a node socket so it can be used by other nodes.
        - In-Place Operation
        #### Path
        - Attribute > Capture Attribute Node
        #### Outputs:
        - `#0 geometry: Geometry = None`
        - `#2 attribute: Float = 0.0`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeCaptureAttribute.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/capture_attribute.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeCaptureAttribute.html)
        """
        node = new_node(*nodes.GeometryNodeCaptureAttribute("FLOAT", "EDGE", self, value_001=value_float))
        self.bsocket = node.outputs[0].bsocket
        return node.outputs[2].Float

    def capture_float_on_faces(self, value_float=0.0):
        """The Capture Attribute node stores the result of a field on a geometry, and outputs the data as a node socket so it can be used by other nodes.
        - In-Place Operation
        #### Path
        - Attribute > Capture Attribute Node
        #### Outputs:
        - `#0 geometry: Geometry = None`
        - `#2 attribute: Float = 0.0`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeCaptureAttribute.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/capture_attribute.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeCaptureAttribute.html)
        """
        node = new_node(*nodes.GeometryNodeCaptureAttribute("FLOAT", "FACE", self, value_001=value_float))
        self.bsocket = node.outputs[0].bsocket
        return node.outputs[2].Float

    def capture_float_on_corners(self, value_float=0.0):
        """The Capture Attribute node stores the result of a field on a geometry, and outputs the data as a node socket so it can be used by other nodes.
        - In-Place Operation
        #### Path
        - Attribute > Capture Attribute Node
        #### Outputs:
        - `#0 geometry: Geometry = None`
        - `#2 attribute: Float = 0.0`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeCaptureAttribute.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/capture_attribute.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeCaptureAttribute.html)
        """
        node = new_node(*nodes.GeometryNodeCaptureAttribute("FLOAT", "CORNER", self, value_001=value_float))
        self.bsocket = node.outputs[0].bsocket
        return node.outputs[2].Float

    def capture_float_on_curves(self, value_float=0.0):
        """The Capture Attribute node stores the result of a field on a geometry, and outputs the data as a node socket so it can be used by other nodes.
        - In-Place Operation
        #### Path
        - Attribute > Capture Attribute Node
        #### Outputs:
        - `#0 geometry: Geometry = None`
        - `#2 attribute: Float = 0.0`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeCaptureAttribute.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/capture_attribute.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeCaptureAttribute.html)
        """
        node = new_node(*nodes.GeometryNodeCaptureAttribute("FLOAT", "CURVE", self, value_001=value_float))
        self.bsocket = node.outputs[0].bsocket
        return node.outputs[2].Float

    def capture_float_on_instances(self, value_float=0.0):
        """The Capture Attribute node stores the result of a field on a geometry, and outputs the data as a node socket so it can be used by other nodes.
        - In-Place Operation
        #### Path
        - Attribute > Capture Attribute Node
        #### Outputs:
        - `#0 geometry: Geometry = None`
        - `#2 attribute: Float = 0.0`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeCaptureAttribute.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/capture_attribute.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeCaptureAttribute.html)
        """
        node = new_node(*nodes.GeometryNodeCaptureAttribute("FLOAT", "INSTANCE", self, value_001=value_float))
        self.bsocket = node.outputs[0].bsocket
        return node.outputs[2].Float

    def capture_color_on_points(self, value_color=(0.0, 0.0, 0.0, 0.0)):
        """The Capture Attribute node stores the result of a field on a geometry, and outputs the data as a node socket so it can be used by other nodes.
        - In-Place Operation
        #### Path
        - Attribute > Capture Attribute Node
        #### Outputs:
        - `#0 geometry: Geometry = None`
        - `#3 attribute: Color = (0.0, 0.0, 0.0, 0.0)`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeCaptureAttribute.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/capture_attribute.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeCaptureAttribute.html)
        """
        node = new_node(*nodes.GeometryNodeCaptureAttribute("FLOAT_COLOR", "POINT", self, value_002=value_color))
        self.bsocket = node.outputs[0].bsocket
        return node.outputs[3].Color

    def capture_color_on_edges(self, value_color=(0.0, 0.0, 0.0, 0.0)):
        """The Capture Attribute node stores the result of a field on a geometry, and outputs the data as a node socket so it can be used by other nodes.
        - In-Place Operation
        #### Path
        - Attribute > Capture Attribute Node
        #### Outputs:
        - `#0 geometry: Geometry = None`
        - `#3 attribute: Color = (0.0, 0.0, 0.0, 0.0)`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeCaptureAttribute.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/capture_attribute.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeCaptureAttribute.html)
        """
        node = new_node(*nodes.GeometryNodeCaptureAttribute("FLOAT_COLOR", "EDGE", self, value_002=value_color))
        self.bsocket = node.outputs[0].bsocket
        return node.outputs[3].Color

    def capture_color_on_faces(self, value_color=(0.0, 0.0, 0.0, 0.0)):
        """The Capture Attribute node stores the result of a field on a geometry, and outputs the data as a node socket so it can be used by other nodes.
        - In-Place Operation
        #### Path
        - Attribute > Capture Attribute Node
        #### Outputs:
        - `#0 geometry: Geometry = None`
        - `#3 attribute: Color = (0.0, 0.0, 0.0, 0.0)`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeCaptureAttribute.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/capture_attribute.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeCaptureAttribute.html)
        """
        node = new_node(*nodes.GeometryNodeCaptureAttribute("FLOAT_COLOR", "FACE", self, value_002=value_color))
        self.bsocket = node.outputs[0].bsocket
        return node.outputs[3].Color

    def capture_color_on_corners(self, value_color=(0.0, 0.0, 0.0, 0.0)):
        """The Capture Attribute node stores the result of a field on a geometry, and outputs the data as a node socket so it can be used by other nodes.
        - In-Place Operation
        #### Path
        - Attribute > Capture Attribute Node
        #### Outputs:
        - `#0 geometry: Geometry = None`
        - `#3 attribute: Color = (0.0, 0.0, 0.0, 0.0)`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeCaptureAttribute.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/capture_attribute.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeCaptureAttribute.html)
        """
        node = new_node(*nodes.GeometryNodeCaptureAttribute("FLOAT_COLOR", "CORNER", self, value_002=value_color))
        self.bsocket = node.outputs[0].bsocket
        return node.outputs[3].Color

    def capture_color_on_curves(self, value_color=(0.0, 0.0, 0.0, 0.0)):
        """The Capture Attribute node stores the result of a field on a geometry, and outputs the data as a node socket so it can be used by other nodes.
        - In-Place Operation
        #### Path
        - Attribute > Capture Attribute Node
        #### Outputs:
        - `#0 geometry: Geometry = None`
        - `#3 attribute: Color = (0.0, 0.0, 0.0, 0.0)`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeCaptureAttribute.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/capture_attribute.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeCaptureAttribute.html)
        """
        node = new_node(*nodes.GeometryNodeCaptureAttribute("FLOAT_COLOR", "CURVE", self, value_002=value_color))
        self.bsocket = node.outputs[0].bsocket
        return node.outputs[3].Color

    def capture_color_on_instances(self, value_color=(0.0, 0.0, 0.0, 0.0)):
        """The Capture Attribute node stores the result of a field on a geometry, and outputs the data as a node socket so it can be used by other nodes.
        - In-Place Operation
        #### Path
        - Attribute > Capture Attribute Node
        #### Outputs:
        - `#0 geometry: Geometry = None`
        - `#3 attribute: Color = (0.0, 0.0, 0.0, 0.0)`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeCaptureAttribute.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/capture_attribute.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeCaptureAttribute.html)
        """
        node = new_node(*nodes.GeometryNodeCaptureAttribute("FLOAT_COLOR", "INSTANCE", self, value_002=value_color))
        self.bsocket = node.outputs[0].bsocket
        return node.outputs[3].Color

    def capture_boolean_on_points(self, value_bool=False):
        """The Capture Attribute node stores the result of a field on a geometry, and outputs the data as a node socket so it can be used by other nodes.
        - In-Place Operation
        #### Path
        - Attribute > Capture Attribute Node
        #### Outputs:
        - `#0 geometry: Geometry = None`
        - `#4 attribute: Boolean = False`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeCaptureAttribute.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/capture_attribute.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeCaptureAttribute.html)
        """
        node = new_node(*nodes.GeometryNodeCaptureAttribute("BOOLEAN", "POINT", self, value_003=value_bool))
        self.bsocket = node.outputs[0].bsocket
        return node.outputs[4].Boolean

    def capture_boolean_on_edges(self, value_bool=False):
        """The Capture Attribute node stores the result of a field on a geometry, and outputs the data as a node socket so it can be used by other nodes.
        - In-Place Operation
        #### Path
        - Attribute > Capture Attribute Node
        #### Outputs:
        - `#0 geometry: Geometry = None`
        - `#4 attribute: Boolean = False`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeCaptureAttribute.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/capture_attribute.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeCaptureAttribute.html)
        """
        node = new_node(*nodes.GeometryNodeCaptureAttribute("BOOLEAN", "EDGE", self, value_003=value_bool))
        self.bsocket = node.outputs[0].bsocket
        return node.outputs[4].Boolean

    def capture_boolean_on_faces(self, value_bool=False):
        """The Capture Attribute node stores the result of a field on a geometry, and outputs the data as a node socket so it can be used by other nodes.
        - In-Place Operation
        #### Path
        - Attribute > Capture Attribute Node
        #### Outputs:
        - `#0 geometry: Geometry = None`
        - `#4 attribute: Boolean = False`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeCaptureAttribute.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/capture_attribute.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeCaptureAttribute.html)
        """
        node = new_node(*nodes.GeometryNodeCaptureAttribute("BOOLEAN", "FACE", self, value_003=value_bool))
        self.bsocket = node.outputs[0].bsocket
        return node.outputs[4].Boolean

    def capture_boolean_on_corners(self, value_bool=False):
        """The Capture Attribute node stores the result of a field on a geometry, and outputs the data as a node socket so it can be used by other nodes.
        - In-Place Operation
        #### Path
        - Attribute > Capture Attribute Node
        #### Outputs:
        - `#0 geometry: Geometry = None`
        - `#4 attribute: Boolean = False`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeCaptureAttribute.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/capture_attribute.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeCaptureAttribute.html)
        """
        node = new_node(*nodes.GeometryNodeCaptureAttribute("BOOLEAN", "CORNER", self, value_003=value_bool))
        self.bsocket = node.outputs[0].bsocket
        return node.outputs[4].Boolean

    def capture_boolean_on_curves(self, value_bool=False):
        """The Capture Attribute node stores the result of a field on a geometry, and outputs the data as a node socket so it can be used by other nodes.
        - In-Place Operation
        #### Path
        - Attribute > Capture Attribute Node
        #### Outputs:
        - `#0 geometry: Geometry = None`
        - `#4 attribute: Boolean = False`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeCaptureAttribute.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/capture_attribute.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeCaptureAttribute.html)
        """
        node = new_node(*nodes.GeometryNodeCaptureAttribute("BOOLEAN", "CURVE", self, value_003=value_bool))
        self.bsocket = node.outputs[0].bsocket
        return node.outputs[4].Boolean

    def capture_boolean_on_instances(self, value_bool=False):
        """The Capture Attribute node stores the result of a field on a geometry, and outputs the data as a node socket so it can be used by other nodes.
        - In-Place Operation
        #### Path
        - Attribute > Capture Attribute Node
        #### Outputs:
        - `#0 geometry: Geometry = None`
        - `#4 attribute: Boolean = False`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeCaptureAttribute.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/capture_attribute.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeCaptureAttribute.html)
        """
        node = new_node(*nodes.GeometryNodeCaptureAttribute("BOOLEAN", "INSTANCE", self, value_003=value_bool))
        self.bsocket = node.outputs[0].bsocket
        return node.outputs[4].Boolean

    def capture_integer_on_points(self, value_int=0):
        """The Capture Attribute node stores the result of a field on a geometry, and outputs the data as a node socket so it can be used by other nodes.
        - In-Place Operation
        #### Path
        - Attribute > Capture Attribute Node
        #### Outputs:
        - `#0 geometry: Geometry = None`
        - `#5 attribute: Integer = 0`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeCaptureAttribute.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/capture_attribute.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeCaptureAttribute.html)
        """
        node = new_node(*nodes.GeometryNodeCaptureAttribute("INT", "POINT", self, value_004=value_int))
        self.bsocket = node.outputs[0].bsocket
        return node.outputs[5].Integer

    def capture_integer_on_edges(self, value_int=0):
        """The Capture Attribute node stores the result of a field on a geometry, and outputs the data as a node socket so it can be used by other nodes.
        - In-Place Operation
        #### Path
        - Attribute > Capture Attribute Node
        #### Outputs:
        - `#0 geometry: Geometry = None`
        - `#5 attribute: Integer = 0`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeCaptureAttribute.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/capture_attribute.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeCaptureAttribute.html)
        """
        node = new_node(*nodes.GeometryNodeCaptureAttribute("INT", "EDGE", self, value_004=value_int))
        self.bsocket = node.outputs[0].bsocket
        return node.outputs[5].Integer

    def capture_integer_on_faces(self, value_int=0):
        """The Capture Attribute node stores the result of a field on a geometry, and outputs the data as a node socket so it can be used by other nodes.
        - In-Place Operation
        #### Path
        - Attribute > Capture Attribute Node
        #### Outputs:
        - `#0 geometry: Geometry = None`
        - `#5 attribute: Integer = 0`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeCaptureAttribute.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/capture_attribute.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeCaptureAttribute.html)
        """
        node = new_node(*nodes.GeometryNodeCaptureAttribute("INT", "FACE", self, value_004=value_int))
        self.bsocket = node.outputs[0].bsocket
        return node.outputs[5].Integer

    def capture_integer_on_corners(self, value_int=0):
        """The Capture Attribute node stores the result of a field on a geometry, and outputs the data as a node socket so it can be used by other nodes.
        - In-Place Operation
        #### Path
        - Attribute > Capture Attribute Node
        #### Outputs:
        - `#0 geometry: Geometry = None`
        - `#5 attribute: Integer = 0`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeCaptureAttribute.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/capture_attribute.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeCaptureAttribute.html)
        """
        node = new_node(*nodes.GeometryNodeCaptureAttribute("INT", "CORNER", self, value_004=value_int))
        self.bsocket = node.outputs[0].bsocket
        return node.outputs[5].Integer

    def capture_integer_on_curves(self, value_int=0):
        """The Capture Attribute node stores the result of a field on a geometry, and outputs the data as a node socket so it can be used by other nodes.
        - In-Place Operation
        #### Path
        - Attribute > Capture Attribute Node
        #### Outputs:
        - `#0 geometry: Geometry = None`
        - `#5 attribute: Integer = 0`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeCaptureAttribute.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/capture_attribute.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeCaptureAttribute.html)
        """
        node = new_node(*nodes.GeometryNodeCaptureAttribute("INT", "CURVE", self, value_004=value_int))
        self.bsocket = node.outputs[0].bsocket
        return node.outputs[5].Integer

    def capture_integer_on_instances(self, value_int=0):
        """The Capture Attribute node stores the result of a field on a geometry, and outputs the data as a node socket so it can be used by other nodes.
        - In-Place Operation
        #### Path
        - Attribute > Capture Attribute Node
        #### Outputs:
        - `#0 geometry: Geometry = None`
        - `#5 attribute: Integer = 0`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeCaptureAttribute.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/capture_attribute.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeCaptureAttribute.html)
        """
        node = new_node(*nodes.GeometryNodeCaptureAttribute("INT", "INSTANCE", self, value_004=value_int))
        self.bsocket = node.outputs[0].bsocket
        return node.outputs[5].Integer

    def remove_attribute(self, name=''):
        """The Remove Named Attribute node deletes an attribute with a certain name from its geometry input. Any attribute that exists on geometry data will be automatically propagated when the geometry storing it is changed, which can be an expensive operation, so using this node can be a simple way to optimize the performance of a geometry node tree or even to lower the memory usage of the entire scene.
        - In-Place Operation
        #### Path
        - Attribute > Remove Named Attribute Node
        #### Outputs:
        - `#0 geometry: Geometry = None`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeRemoveNamedAttribute.png)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/remove_named_attribute.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeRemoveAttribute.html)
        """
        node = new_node(*nodes.GeometryNodeRemoveAttribute(self, name))
        self.bsocket = node.outputs[0].bsocket
        return self

    def _store_named_attribute(self, data_type='FLOAT', domain='POINT', selection=True, name='', value_vector=(0.0, 0.0, 0.0), value_float=0.0, value_color=(0.0, 0.0, 0.0, 0.0), value_bool=False, value_int=0):
        selection = selection if self._selection is None else self.selection
        node = new_node(*nodes.GeometryNodeStoreNamedAttribute(data_type, domain, self, selection, name, value_vector, value_float, value_color, value_bool, value_int))
        self.bsocket = node.outputs[0].bsocket
        return self

    def store_named_attribute(self, name: str, value, domain="POINT", selection=True):
        """The Store Named Attribute node stores the result of a field on a geometry as an attribute with the specified name. If the attribute already exists, the data type and domain will be updated to the values chosen in the node. However, keep in mind that the domain and data type of Built-In Attributes cannot be changed.
        - In-Place Operation
        #### Path
        - Attribute > Store Named Attribute Node
        #### Properties
        - `data_type`: `FLOAT`, `INT`, `FLOAT_VECTOR`, `FLOAT_COLOR`, `BYTE_COLOR`, `BOOLEAN`, `FLOAT2`
        - `domain`: `POINT`, `EDGE`, `FACE`, `CORNER`, `CURVE`, `INSTANCE`
        #### Outputs:
        - `#0 geometry: Geometry = None`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeStoreNamedAttribute.png)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/store_named_attribute.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeStoreNamedAttribute.html)
        """
        selection = selection if self._selection is None else self.selection
        if isinstance(value, (int, Integer)):
            data_type = "INT"
            value_name = "value_int"
        elif isinstance(value, (float, Float)):
            data_type = "FLOAT"
            value_name = "value_float"
        elif isinstance(value, Vector) or (hasattr(value, "__len__") and len(value) == 3):
            data_type = "FLOAT_VECTOR"
            value_name = "value_vector"
        elif isinstance(value, Color) or (hasattr(value, "__len__") and len(value) == 4):
            data_type = "FLOAT_COLOR"
            value_name = "value_color"
        elif isinstance(value, (bool, Boolean)):
            data_type = "BOOLEAN"
            value_name = "value_bool"
        return self._store_named_attribute(data_type, domain, selection, name, **{value_name: value})

    @property
    def ID(self):
        """The ID node gives an integer value indicating the stable random identifier of each element on the point domain, which is stored in the id attribute.
        #### Path
        - Geometry > Read > ID Node
        #### Outputs:
        - `#0 id: Integer = 0`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeInputID.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/read/id.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputID.html)
        """
        if self._id is None:
            node = new_node(*nodes.GeometryNodeInputID())
            self._id = node.outputs[0].Integer
        return self._id

    @property
    def index(self):
        """The Index node gives an integer value indicating the position of each element in the list, starting at zero. This depends on the internal order of the data in the geometry, which is not necessarily visible in the 3D Viewport. However, the index value is visible in the left-most column in the Spreadsheet Editor.
        #### Path
        - Geometry > Read > Index Node
        #### Outputs:
        - `#0 index: Integer = 0`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeInputIndex.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/read/input_index.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputIndex.html)
        """
        if self._index is None:
            node = new_node(*nodes.GeometryNodeInputIndex())
            self._index = node.outputs[0].Integer
        return self._index

    @staticmethod
    def named_attribute_vector(name=''):
        """The Named Attribute node outputs the data of an attribute based on the context of where it is connected (the Field Context).
        #### Path
        - Geometry > Read > Named Attribute Node
        #### Outputs:
        - `#0 attribute_vector: Vector = (0.0, 0.0, 0.0)`
        - `#5 exists: Boolean = False`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeNamedAttribute.png)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/read/named_attribute.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNamedAttribute.html)
        """
        node = new_node(*nodes.GeometryNodeInputNamedAttribute("FLOAT_VECTOR", name))
        ret = typing.NamedTuple("NamedAttribute", [("attribute", Vector), ("exists", Boolean)])
        return ret(node.outputs[0].Vector, node.outputs[5].Boolean)

    @staticmethod
    def named_attribute_float(name=''):
        """The Named Attribute node outputs the data of an attribute based on the context of where it is connected (the Field Context).
        #### Path
        - Geometry > Read > Named Attribute Node
        #### Outputs:
        - `#1 attribute_float: Float = 0.0`
        - `#5 exists: Boolean = False`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeNamedAttribute.png)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/read/named_attribute.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNamedAttribute.html)
        """
        node = new_node(*nodes.GeometryNodeInputNamedAttribute("FLOAT", name))
        ret = typing.NamedTuple("NamedAttribute", [("attribute", Float), ("exists", Boolean)])
        return ret(node.outputs[1].Float, node.outputs[5].Boolean)

    @staticmethod
    def named_attribute_color(name=''):
        """The Named Attribute node outputs the data of an attribute based on the context of where it is connected (the Field Context).
        #### Path
        - Geometry > Read > Named Attribute Node
        #### Outputs:
        - `#2 attribute_color: Color = (0.0, 0.0, 0.0, 0.0)`
        - `#5 exists: Boolean = False`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeNamedAttribute.png)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/read/named_attribute.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNamedAttribute.html)
        """
        node = new_node(*nodes.GeometryNodeInputNamedAttribute("FLOAT_COLOR", name))
        ret = typing.NamedTuple("NamedAttribute", [("attribute", Color), ("exists", Boolean)])
        return ret(node.outputs[2].Color, node.outputs[5].Boolean)

    @staticmethod
    def named_attribute_boolean(name=''):
        """The Named Attribute node outputs the data of an attribute based on the context of where it is connected (the Field Context).
        #### Path
        - Geometry > Read > Named Attribute Node
        #### Outputs:
        - `#3 attribute_bool: Boolean = False`
        - `#5 exists: Boolean = False`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeNamedAttribute.png)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/read/named_attribute.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNamedAttribute.html)
        """
        node = new_node(*nodes.GeometryNodeInputNamedAttribute("BOOLEAN", name))
        ret = typing.NamedTuple("NamedAttribute", [("attribute", Boolean), ("exists", Boolean)])
        return ret(node.outputs[3].Boolean, node.outputs[5].Boolean)

    @staticmethod
    def named_attribute_integer(name=''):
        """The Named Attribute node outputs the data of an attribute based on the context of where it is connected (the Field Context).
        #### Path
        - Geometry > Read > Named Attribute Node
        #### Outputs:
        - `#4 attribute_int: Integer = 0`
        - `#5 exists: Boolean = False`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeNamedAttribute.png)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/read/named_attribute.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNamedAttribute.html)
        """
        node = new_node(*nodes.GeometryNodeInputNamedAttribute("INT", name))
        ret = typing.NamedTuple("NamedAttribute", [("attribute", Integer), ("exists", Boolean)])
        return ret(node.outputs[4].Integer, node.outputs[5].Boolean)

    @property
    def normal(self):
        """The Normal node returns a vector for each evaluated point indicating the normal direction. The output can depend on the attribute domain used in the node evaluating the field, but the output is always a normalized unit vector.
        #### Path
        - Geometry > Read > Normal Node
        #### Outputs:
        - `#0 normal: Vector = (0.0, 0.0, 0.0)`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeInputNormal.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/read/normal.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNormal.html)
        """
        if self._normal is None:
            node = new_node(*nodes.GeometryNodeInputNormal())
            self._normal = node.outputs[0].Vector
        return self._normal

    @property
    def position(self):
        """The Position node outputs a vector of each point of the geometry the node is connected to.
        #### Path
        - Geometry > Read > Position Node
        #### Outputs:
        - `#0 position: Vector = (0.0, 0.0, 0.0)`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeInputPosition.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/read/position.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputPosition.html)
        """
        if self._position is None:
            node = new_node(*nodes.GeometryNodeInputPosition())
            self._position = node.outputs[0].Vector
        return self._position

    @property
    def radius(self):
        """The Radius node outputs the radius value at each point on the evaluated geometry. For curves, this value is used for things like determining the size of the mesh created in the Curve to Mesh node. For point clouds, the value is used for the display size of the point in the viewport.
        #### Path
        - Geometry > Read > Radius Node
        #### Outputs:
        - `#0 radius: Float = 1.0`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeInputRadius.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/read/radius.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputRadius.html)
        """
        if self._radius is None:
            node = new_node(*nodes.GeometryNodeInputRadius())
            self._radius = node.outputs[0].Float
        return self._radius

    def set_id(self, id: "Integer" = None, selection=True):
        """The Set ID node fills the id attribute on the input geometry. If the attribute does not exist yet, it will be created with a default value of zero. The ID is also created by the Distribute Points on Faces, and it is used in the Random Value Node and other nodes if it exists.
        - In-Place Operation
        #### Path
        - Geometry > Write > Set ID Node
        #### Outputs:
        - `#0 geometry: Geometry = None`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeSetID.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/write/set_id.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetID.html)
        """
        selection = selection if self._selection is None else self.selection
        node = new_node(*nodes.GeometryNodeSetID(self, selection, id))
        self.bsocket = node.outputs[0].bsocket
        return self

    def set_position(self, position: "Vector" = None, offset=(0.0, 0.0, 0.0), selection=True):
        """The Set Position node controls the location of each point, the same way as controlling the position attribute. If the input geometry contains instances, this node will affect the location of the origin of each instance.
        - In-Place Operation
        #### Path
        - Geometry > Write > Set Position Node
        #### Outputs:
        - `#0 geometry: Geometry = None`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeSetPosition.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/write/set_position.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetPosition.html)
        """
        selection = selection if self._selection is None else self.selection
        node = new_node(*nodes.GeometryNodeSetPosition(self, selection, position, offset))
        self.bsocket = node.outputs[0].bsocket
        return self

    def proximity(self, target_element='FACES', source_position: "Vector" = None):
        """The Geometry Proximity node computes the closest location on the target geometry.
        #### Path
        - Geometry > Sample > Geometry Proximity Node
        #### Properties
        - `target_element`: `FACES`, `POINTS`, `EDGES`
        #### Outputs:
        - `#0 position: Vector = (0.0, 0.0, 0.0)`
        - `#1 distance: Float = 0.0`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeProximity.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/sample/geometry_proximity.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeProximity.html)
        """
        node = new_node(*nodes.GeometryNodeProximity(target_element, self, source_position))
        ret = typing.NamedTuple("GeometryNodeProximity", [("position", Vector), ("distance", Float)])
        return ret(node.outputs[0].Vector, node.outputs[1].Float)

    def raycast_vector(self, mapping='INTERPOLATED', attribute=(0.0, 0.0, 0.0), source_position: "Vector" = None, ray_direction=(0.0, 0.0, -1.0), ray_length=100.0):
        """The Raycast node intersects rays from one geometry onto another. The source geometry is defined by the context of the node that the Raycast node is connected to. Each ray computes hit points on the target mesh and outputs normals, distances and any surface attribute specified.
        #### Path
        - Geometry > Sample > Raycast Node
        #### Properties
        - `mapping`: `INTERPOLATED`, `NEAREST`
        #### Outputs:
        - `#0 is_hit: Boolean = False`
        - `#1 hit_position: Vector = (0.0, 0.0, 0.0)`
        - `#2 hit_normal: Vector = (0.0, 0.0, 0.0)`
        - `#3 hit_distance: Float = 0.0`
        - `#4 attribute: Vector = (0.0, 0.0, 0.0)`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeRaycast.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/sample/raycast.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeRaycast.html)
        """
        node = new_node(*nodes.GeometryNodeRaycast("FLOAT_VECTOR", mapping, self, attribute=attribute, source_position=source_position, ray_direction=ray_direction, ray_length=ray_length))
        ret = typing.NamedTuple("GeometryNodeRaycast", [("is_hit", Boolean), ("hit_position", Vector), ("hit_normal", Vector), ("hit_distance", Float), ("attribute", Vector)])
        return ret(node.outputs[0].Boolean, node.outputs[1].Vector, node.outputs[2].Vector, node.outputs[3].Float, node.outputs[4].Vector)

    def raycast_float(self, mapping='INTERPOLATED', attribute=0.0, source_position: "Vector" = None, ray_direction=(0.0, 0.0, -1.0), ray_length=100.0):
        """The Raycast node intersects rays from one geometry onto another. The source geometry is defined by the context of the node that the Raycast node is connected to. Each ray computes hit points on the target mesh and outputs normals, distances and any surface attribute specified.
        #### Path
        - Geometry > Sample > Raycast Node
        #### Properties
        - `mapping`: `INTERPOLATED`, `NEAREST`
        #### Outputs:
        - `#0 is_hit: Boolean = False`
        - `#1 hit_position: Vector = (0.0, 0.0, 0.0)`
        - `#2 hit_normal: Vector = (0.0, 0.0, 0.0)`
        - `#3 hit_distance: Float = 0.0`
        - `#5 attribute_001: Float = 0.0`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeRaycast.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/sample/raycast.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeRaycast.html)
        """
        node = new_node(*nodes.GeometryNodeRaycast("FLOAT", mapping, self, attribute_001=attribute, source_position=source_position, ray_direction=ray_direction, ray_length=ray_length))
        ret = typing.NamedTuple("GeometryNodeRaycast", [("is_hit", Boolean), ("hit_position", Vector), ("hit_normal", Vector), ("hit_distance", Float), ("attribute", Float)])
        return ret(node.outputs[0].Boolean, node.outputs[1].Vector, node.outputs[2].Vector, node.outputs[3].Float, node.outputs[5].Float)

    def raycast_color(self, mapping='INTERPOLATED', attribute=(0.0, 0.0, 0.0, 0.0), source_position: "Vector" = None, ray_direction=(0.0, 0.0, -1.0), ray_length=100.0):
        """The Raycast node intersects rays from one geometry onto another. The source geometry is defined by the context of the node that the Raycast node is connected to. Each ray computes hit points on the target mesh and outputs normals, distances and any surface attribute specified.
        #### Path
        - Geometry > Sample > Raycast Node
        #### Properties
        - `mapping`: `INTERPOLATED`, `NEAREST`
        #### Outputs:
        - `#0 is_hit: Boolean = False`
        - `#1 hit_position: Vector = (0.0, 0.0, 0.0)`
        - `#2 hit_normal: Vector = (0.0, 0.0, 0.0)`
        - `#3 hit_distance: Float = 0.0`
        - `#6 attribute_002: Color = (0.0, 0.0, 0.0, 0.0)`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeRaycast.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/sample/raycast.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeRaycast.html)
        """
        node = new_node(*nodes.GeometryNodeRaycast("FLOAT_VECTOR", mapping, self, attribute_002=attribute, source_position=source_position, ray_direction=ray_direction, ray_length=ray_length))
        ret = typing.NamedTuple("GeometryNodeRaycast", [("is_hit", Boolean), ("hit_position", Vector), ("hit_normal", Vector), ("hit_distance", Float), ("attribute", Color)])
        return ret(node.outputs[0].Boolean, node.outputs[1].Vector, node.outputs[2].Vector, node.outputs[3].Float, node.outputs[6].Color)

    def raycast_boolean(self, mapping='INTERPOLATED', attribute=False, source_position: "Vector" = None, ray_direction=(0.0, 0.0, -1.0), ray_length=100.0):
        """The Raycast node intersects rays from one geometry onto another. The source geometry is defined by the context of the node that the Raycast node is connected to. Each ray computes hit points on the target mesh and outputs normals, distances and any surface attribute specified.
        #### Path
        - Geometry > Sample > Raycast Node
        #### Properties
        - `mapping`: `INTERPOLATED`, `NEAREST`
        #### Outputs:
        - `#0 is_hit: Boolean = False`
        - `#1 hit_position: Vector = (0.0, 0.0, 0.0)`
        - `#2 hit_normal: Vector = (0.0, 0.0, 0.0)`
        - `#3 hit_distance: Float = 0.0`
        - `#7 attribute_003: Boolean = False`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeRaycast.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/sample/raycast.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeRaycast.html)
        """
        node = new_node(*nodes.GeometryNodeRaycast("FLOAT_VECTOR", mapping, self, attribute_003=attribute, source_position=source_position, ray_direction=ray_direction, ray_length=ray_length))
        ret = typing.NamedTuple("GeometryNodeRaycast", [("is_hit", Boolean), ("hit_position", Vector), ("hit_normal", Vector), ("hit_distance", Float), ("attribute", Boolean)])
        return ret(node.outputs[0].Boolean, node.outputs[1].Vector, node.outputs[2].Vector, node.outputs[3].Float, node.outputs[7].Color)

    def raycast_integer(self, mapping='INTERPOLATED', attribute=0, source_position: "Vector" = None, ray_direction=(0.0, 0.0, -1.0), ray_length=100.0):
        """The Raycast node intersects rays from one geometry onto another. The source geometry is defined by the context of the node that the Raycast node is connected to. Each ray computes hit points on the target mesh and outputs normals, distances and any surface attribute specified.
        #### Path
        - Geometry > Sample > Raycast Node
        #### Properties
        - `mapping`: `INTERPOLATED`, `NEAREST`
        #### Outputs:
        - `#0 is_hit: Boolean = False`
        - `#1 hit_position: Vector = (0.0, 0.0, 0.0)`
        - `#2 hit_normal: Vector = (0.0, 0.0, 0.0)`
        - `#3 hit_distance: Float = 0.0`
        - `#8 attribute_004: Integer = 0`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeRaycast.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/sample/raycast.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeRaycast.html)
        """
        node = new_node(*nodes.GeometryNodeRaycast("INT", mapping, self, attribute_004=attribute, source_position=source_position, ray_direction=ray_direction, ray_length=ray_length))
        ret = typing.NamedTuple("GeometryNodeRaycast", [("is_hit", Boolean), ("hit_position", Vector), ("hit_normal", Vector), ("hit_distance", Float), ("attribute", Integer)])
        return ret(node.outputs[0].Boolean, node.outputs[1].Vector, node.outputs[2].Vector, node.outputs[3].Float, node.outputs[8].Integer)

    def sample_index(self, data_type="FLOAT", domain="POINT", clamp=False, value_float=0.0, value_int=0, value_vector=(0.0, 0.0, 0.0), value_color=(0.0, 0.0, 0.0, 0.0), value_bool=False, index=0):
        """The Sample Index node retrieves values from a source geometry at a specific index.
        #### Path
        - Geometry > Sample > Sample Index Node
        #### Properties
        - `data_type`: `FLOAT`, `INT`, `FLOAT_VECTOR`, `FLOAT_COLOR`, `BOOLEAN`
        - `domain`: `POINT`, `EDGE`, `FACE`, `CORNER`, `CURVE`, `INSTANCE`
        #### Outputs:
        - `#0 value_float: Float = 0.0`
        - `#1 value_int: Integer = 0`
        - `#2 value_vector: Vector = (0.0, 0.0, 0.0)`
        - `#3 value_color: Color = (0.0, 0.0, 0.0, 0.0)`
        - `#4 value_bool: Boolean = False`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeSampleIndex.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/sample/sample_index.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeSampleIndex.html)
        """
        node = new_node(*nodes.GeometryNodeSampleIndex(data_type, domain, clamp, self, value_float, value_int, value_vector, value_color, value_bool, index))
        return node.outputs[0].Float, node.outputs[1].Integer, node.outputs[2].Vector, node.outputs[3].Color, node.outputs[4].Boolean

    def sample_float_index(self, value_float=0.0, index=0, domain="POINT", clamp=False):
        """The Sample Index node retrieves values from a source geometry at a specific index.
        #### Path
        - Geometry > Sample > Sample Index Node
        #### Properties
        - `domain`: `POINT`, `EDGE`, `FACE`, `CORNER`, `CURVE`, `INSTANCE`
        #### Outputs:
        - `#0 value_float: Float = 0.0`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeSampleIndex.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/sample/sample_index.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeSampleIndex.html)
        """
        node = new_node(*nodes.GeometryNodeSampleIndex("FLOAT", domain, clamp, self, value_float=value_float, index=index))
        return node.outputs[0].Float

    def sample_integer_index(self, value_int=0, index=0, domain="POINT", clamp=False):
        """The Sample Index node retrieves values from a source geometry at a specific index.
        #### Path
        - Geometry > Sample > Sample Index Node
        #### Properties
        - `domain`: `POINT`, `EDGE`, `FACE`, `CORNER`, `CURVE`, `INSTANCE`
        #### Outputs:
        - `#1 value_int: Integer = 0`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeSampleIndex.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/sample/sample_index.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeSampleIndex.html)
        """
        node = new_node(*nodes.GeometryNodeSampleIndex("INT", domain, clamp, self, value_int == value_int, index=index))
        return node.outputs[1].Integer

    def sample_vector_index(self, value_vector=(0.0, 0.0, 0.0), index=0, domain="POINT", clamp=False):
        """The Sample Index node retrieves values from a source geometry at a specific index.
        #### Path
        - Geometry > Sample > Sample Index Node
        #### Properties
        - `domain`: `POINT`, `EDGE`, `FACE`, `CORNER`, `CURVE`, `INSTANCE`
        #### Outputs:
        - `#2 value_vector: Vector = (0.0, 0.0, 0.0)`
        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeSampleIndex.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/sample/sample_index.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeSampleIndex.html)
        """
        node = new_node(*nodes.GeometryNodeSampleIndex("FLOAT_VECTOR", domain, clamp, self, value_vector=value_vector, index=index))
        return node.outputs[2].Vector

    def sample_color_index(self, value_color=(0.0, 0.0, 0.0, 0.0), index=0, domain="POINT", clamp=False):
        """The Sample Index node retrieves values from a source geometry at a specific index.
        #### Path
        - Geometry > Sample > Sample Index Node
        #### Properties
        - `domain`: `POINT`, `EDGE`, `FACE`, `CORNER`, `CURVE`, `INSTANCE`
        #### Outputs:
        - `#3 value_color: Color = (0.0, 0.0, 0.0, 0.0)`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeSampleIndex.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/sample/sample_index.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeSampleIndex.html)
        """
        node = new_node(*nodes.GeometryNodeSampleIndex("FLOAT_COLOR", domain, clamp, self, value_color=value_color, index=index))
        return node.outputs[3].color

    def sample_boolean_index(self, value_bool=False, index=0, domain="POINT", clamp=False):
        """The Sample Index node retrieves values from a source geometry at a specific index.
        #### Path
        - Geometry > Sample > Sample Index Node
        #### Properties
        - `domain`: `POINT`, `EDGE`, `FACE`, `CORNER`, `CURVE`, `INSTANCE`
        #### Outputs:
        - `#4 value_bool: Boolean = False`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeSampleIndex.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/sample/sample_index.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeSampleIndex.html)
        """
        node = new_node(*nodes.GeometryNodeSampleIndex("BOOLEAN", domain, clamp, self, value_bool=value_bool, index=index))
        return node.outputs[4].Boolean

    def sample_nearest(self, sample_position: "Vector" = None, domain="POINT"):
        """The Sample Nearest node retrieves the index of the geometry element in its input geometry that is closest to the input position. This node is similar to the Geometry Proximity Node, but it outputs the index of the closest element instead of its distance from the current location.
        #### Path
        - Geometry > Sample > Sample Nearest Node
        #### Properties
        - `domain`: `POINT`, `EDGE`, `FACE`, `CORNER`
        #### Outputs:
        - `#0 index: Integer = 0`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeSampleNearest.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/sample/sample_nearest.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeSampleNearest.html)
        """
        node = new_node(*nodes.GeometryNodeSampleNearest(domain, self, sample_position))
        return node.outputs[0].Integer

    def bound_box(self):
        """The Bounding Box node creates a box mesh with the minimum volume that encapsulates the geometry of the input. The node also can output the vector positions of the bounding dimensions.
        #### Path
        - Geometry > Operations > Bounding Box Node
        #### Outputs:
        - `#0 bounding_box: Geometry = None`
        - `#1 min: Vector = (0.0, 0.0, 0.0)`
        - `#2 max: Vector = (0.0, 0.0, 0.0)`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeBoundBox.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/operations/bounding_box.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeBoundBox.html)
        """
        node = new_node(*nodes.GeometryNodeBoundBox(self))
        ret = typing.NamedTuple("GeometryNodeBoundBox", [("bounding_box", Geometry), ("min", Vector), ("max", Vector)])
        return ret(node.outputs[0].Geometry, node.outputs[1].Vector, node.outputs[2].Vector)

    def convex_hull(self):
        """The Convex Hull node outputs a convex mesh that is enclosing all points in the input geometry.
        #### Path
        - Geometry > Operations > Convex Hull Node
        #### Outputs:
        - `#0 convex_hull: Geometry = None`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeConvexHull.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/operations/convex_hull.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeConvexHull.html)
        """
        node = new_node(*nodes.GeometryNodeConvexHull(self))
        return node.outputs[0].Geometry

    def delete(self, domain="POINT", mode="ALL", selection=True):
        """The Delete Geometry node removes the selected part of a geometry. It behaves similarly to the Delete tool in Edit Mode. The type of elements to be deleted can be specified with the domain and mode properties.
        - In-Place Operation
        #### Path
        - Geometry > Operations > Delete Geometry Node
        #### Properties
        - `domain`: `POINT`, `EDGE`, `FACE`, `CURVE`, `INSTANCE`
        - `mode`: `ALL`, `EDGE_FACE`, `ONLY_FACE`
        #### Outputs:
        - `#0 geometry: Geometry = None`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeDeleteGeometry.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/operations/delete_geometry.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeDeleteGeometry.html)
        """
        selection = selection if self._selection is None else self.selection
        node = new_node(*nodes.GeometryNodeDeleteGeometry(domain, mode, self, selection))
        self.bsocket = node.outputs[0].bsocket
        return self

    def duplicate_elements(self, amount=1, domain="POINT", selection=True):
        """The Duplicate Elements node creates a new geometry with the specified elements from the input duplicated an arbitrary number of times. The positions of elements are not changed, so all of the duplicates will be at the exact same location.
        #### Path
        - Geometry > Operations > Duplicate Elements Node
        #### Properties
        - `domain`: `POINT`, `EDGE`, `FACE`, `SPLINE`, `INSTANCE`
        #### Outputs:
        - `#0 geometry: Geometry = None`
        - `#1 duplicate_index: Integer = 0`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeDuplicateElements.png)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/operations/duplicate_elements.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeDuplicateElements.html)
        """
        selection = selection if self._selection is None else self.selection
        node = new_node(*nodes.GeometryNodeDuplicateElements(domain, self, selection, amount))
        ret = typing.NamedTuple("GeometryNodeDuplicateElements", [("geometry", Geometry), ("duplicate_index", Integer)])
        return ret(node.outputs[0].Geometry, node.outputs[1].Integer)

    def merge_by_distance(self, distance=0.001, mode="ALL", selection=True):
        """The Merge by Distance node merges selected mesh vertices or point cloud points within a given distance, merging surrounding geometry where necessary. This operation is similar to the Merge by Distance operator or the Weld Modifier.
        #### Path
        - Geometry > Operations > Merge by Distance Node
        #### Properties
        - `mode`: `ALL`, `CONNECTED`
        #### Outputs:
        - `#0 geometry: Geometry = None`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeMergeByDistance.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/operations/merge_by_distance.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeMergeByDistance.html)
        """
        selection = selection if self._selection is None else self.selection
        node = new_node(*nodes.GeometryNodeMergeByDistance(mode, self, selection, distance))
        return node.outputs[0].Geometry

    def transform(self, translation=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(1.0, 1.0, 1.0)):
        """The Transform Geometry Node allows you to move, rotate or scale the geometry. The transformation is applied to the entire geometry, and not per element. The Set Position Node is used for moving individual points of a geometry. For transforming instances individually, the instance translate, rotate, or scale nodes can be used.
        - In-Place Operation
        #### Path
        - Geometry > Operations > Transform Geometry Node
        #### Outputs:
        - `#0 geometry: Geometry = None`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeTransformGeometry.jpg)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/operations/transform_geometry.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeTransform.html)
        """
        node = new_node(*nodes.GeometryNodeTransform(self, translation, rotation, scale))
        self.bsocket = node.outputs[0].bsocket
        return self

    def separate_components(self):
        """The Separate Components node splits a geometry into a separate output for each type of data in the geometry.
        #### Path
        - Geometry > Operations > Separate Components Node
        #### Outputs:
        - `#0 mesh: Geometry = None`
        - `#1 point_cloud: Geometry = None`
        - `#2 curve: Geometry = None`
        - `#3 volume: Geometry = None`
        - `#4 instances: Geometry = None`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeSeparateComponents.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/operations/separate_components.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeSeparateComponents.html)
        """
        node = new_node(*nodes.GeometryNodeSeparateComponents(self))
        ret = typing.NamedTuple("GeometryNodeSeparateComponents", [("mesh", Mesh), ("point_cloud", Points), ("curve", Curve), ("volume", Volume), ("instances", Instances)])
        return ret(node.outputs[0].Mesh, node.outputs[1].Points, node.outputs[2].Curve, node.outputs[3].Volume, node.outputs[4].Instances)

    def separate(self, selection=True, domain="POINT"):
        """The Separate Geometry node produces two geometry outputs. Based on the Selection input, the input geometry is split between the two outputs.
        #### Path
        - Geometry > Operations > Separate Geometry Node
        #### Properties
        - `domain`: `POINT`, `EDGE`, `FACE`, `CURVE`, `INSTANCE`
        #### Outputs:
        - `#0 selection: Geometry = None`
        - `#1 inverted: Geometry = None`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeSeparateGeometry.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/operations/separate_geometry.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeSeparateGeometry.html)
        """
        selection = selection if self._selection is None else self.selection
        node = new_node(*nodes.GeometryNodeSeparateGeometry(domain, self, selection))
        ret = typing.NamedTuple("GeometryNodeSeparateGeometry", [("selected", Geometry), ("inverted", Geometry)])
        return ret(node.outputs[0].Geometry, node.outputs[1].Geometry)

    def separate_edges(self, selection=True):
        """The Separate Geometry node produces two geometry outputs. Based on the Selection input, the input geometry is split between the two outputs.
        #### Path
        - Geometry > Operations > Separate Geometry Node
        #### Outputs:
        - `#0 selection: Geometry = None`
        - `#1 inverted: Geometry = None`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeSeparateGeometry.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/operations/separate_geometry.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeSeparateGeometry.html)
        """
        selection = selection if self._selection is None else self.selection
        node = new_node(*nodes.GeometryNodeSeparateGeometry("EDGE", self, selection))
        ret = typing.NamedTuple("GeometryNodeSeparateGeometry", [("selected", Mesh), ("inverted", Mesh)])
        return ret(node.outputs[0].Mesh, node.outputs[1].Mesh)

    def separate_faces(self, selection=True):
        """The Separate Geometry node produces two geometry outputs. Based on the Selection input, the input geometry is split between the two outputs.
        #### Path
        - Geometry > Operations > Separate Geometry Node
        #### Outputs:
        - `#0 selection: Geometry = None`
        - `#1 inverted: Geometry = None`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeSeparateGeometry.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/operations/separate_geometry.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeSeparateGeometry.html)
        """
        selection = selection if self._selection is None else self.selection
        node = new_node(*nodes.GeometryNodeSeparateGeometry("FACE", self, selection))
        ret = typing.NamedTuple("GeometryNodeSeparateGeometry", [("selected", Mesh), ("inverted", Mesh)])
        return ret(node.outputs[0].Mesh, node.outputs[1].Mesh)

    def separate_curves(self, selection=True):
        """The Separate Geometry node produces two geometry outputs. Based on the Selection input, the input geometry is split between the two outputs.
        #### Path
        - Geometry > Operations > Separate Geometry Node
        #### Outputs:
        - `#0 selection: Geometry = None`
        - `#1 inverted: Geometry = None`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeSeparateGeometry.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/operations/separate_geometry.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeSeparateGeometry.html)
        """
        selection = selection if self._selection is None else self.selection
        node = new_node(*nodes.GeometryNodeSeparateGeometry("CURVE", self, selection))
        ret = typing.NamedTuple("GeometryNodeSeparateGeometry", [("selected", Curve), ("inverted", Curve)])
        return ret(node.outputs[0].Curve, node.outputs[1].Curve)

    def separate_instances(self, selection=True):
        """The Separate Geometry node produces two geometry outputs. Based on the Selection input, the input geometry is split between the two outputs.
        #### Path
        - Geometry > Operations > Separate Geometry Node
        #### Outputs:
        - `#0 selection: Geometry = None`
        - `#1 inverted: Geometry = None`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeSeparateGeometry.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/operations/separate_geometry.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeSeparateGeometry.html)
        """
        selection = selection if self._selection is None else self.selection
        node = new_node(*nodes.GeometryNodeSeparateGeometry("INSTANCE", self, selection))
        ret = typing.NamedTuple("GeometryNodeSeparateGeometry", [("selected", Instances), ("inverted", Instances)])
        return ret(node.outputs[0].Instances, node.outputs[1].Instances)

    def select(self, selection=True, domain="POINT"):
        """The Separate Geometry node produces two geometry outputs. Based on the Selection input, the input geometry is split between the two outputs.
        - In-Place Operation
        #### Path
        - Geometry > Operations > Separate Geometry Node
        #### Properties
        - `domain`: `POINT`, `EDGE`, `FACE`, `CURVE`, `INSTANCE`
        #### Outputs:
        - `#0 selection: Geometry = None`
        - `#1 inverted: Geometry = None`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeSeparateGeometry.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/operations/separate_geometry.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeSeparateGeometry.html)
        """
        selection = selection if self._selection is None else self.selection
        node = new_node(*nodes.GeometryNodeSeparateGeometry(domain, self, selection))
        self.bsocket = node.outputs[0].bsocket
        return self

    def select_points(self, selection=True):
        """The Separate Geometry node produces two geometry outputs. Based on the Selection input, the input geometry is split between the two outputs.
        - In-Place Operation
        #### Path
        - Geometry > Operations > Separate Geometry Node
        #### Outputs:
        - `#0 selection: Geometry = None`
        - `#1 inverted: Geometry = None`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeSeparateGeometry.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/operations/separate_geometry.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeSeparateGeometry.html)
        """
        selection = selection if self._selection is None else self.selection
        node = new_node(*nodes.GeometryNodeSeparateGeometry("POINT", self, selection))
        self.bsocket = node.outputs[0].bsocket
        return self

    def select_edges(self, selection=True):
        """The Separate Geometry node produces two geometry outputs. Based on the Selection input, the input geometry is split between the two outputs.
        - In-Place Operation
        #### Path
        - Geometry > Operations > Separate Geometry Node
        #### Outputs:
        - `#0 selection: Geometry = None`
        - `#1 inverted: Geometry = None`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeSeparateGeometry.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/operations/separate_geometry.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeSeparateGeometry.html)
        """
        selection = selection if self._selection is None else self.selection
        node = new_node(*nodes.GeometryNodeSeparateGeometry("EDGE", self, selection))
        self.bsocket = node.outputs[0].bsocket
        return self

    def select_faces(self, selection=True):
        """The Separate Geometry node produces two geometry outputs. Based on the Selection input, the input geometry is split between the two outputs.
        - In-Place Operation
        #### Path
        - Geometry > Operations > Separate Geometry Node
        #### Outputs:
        - `#0 selection: Geometry = None`
        - `#1 inverted: Geometry = None`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeSeparateGeometry.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/operations/separate_geometry.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeSeparateGeometry.html)
        """
        selection = selection if self._selection is None else self.selection
        node = new_node(*nodes.GeometryNodeSeparateGeometry("FACE", self, selection))
        self.bsocket = node.outputs[0].bsocket
        return self

    def select_curves(self, selection=True):
        """The Separate Geometry node produces two geometry outputs. Based on the Selection input, the input geometry is split between the two outputs.
        - In-Place Operation
        #### Path
        - Geometry > Operations > Separate Geometry Node
        #### Outputs:
        - `#0 selection: Geometry = None`
        - `#1 inverted: Geometry = None`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeSeparateGeometry.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/operations/separate_geometry.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeSeparateGeometry.html)
        """
        selection = selection if self._selection is None else self.selection
        node = new_node(*nodes.GeometryNodeSeparateGeometry("CURVE", self, selection))
        self.bsocket = node.outputs[0].bsocket
        return self

    def select_instances(self, selection=True):
        """The Separate Geometry node produces two geometry outputs. Based on the Selection input, the input geometry is split between the two outputs.
        - In-Place Operation
        #### Path
        - Geometry > Operations > Separate Geometry Node
        #### Outputs:
        - `#0 selection: Geometry = None`
        - `#1 inverted: Geometry = None`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeSeparateGeometry.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/operations/separate_geometry.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeSeparateGeometry.html)
        """
        selection = selection if self._selection is None else self.selection
        node = new_node(*nodes.GeometryNodeSeparateGeometry("INSTANCE", self, selection))
        self.bsocket = node.outputs[0].bsocket
        return self

    def join(self, *others: "Geometry"):
        """The Join Geometry node merges separately generated geometries into a single one. If the geometry inputs contain different types of data, the output will also contain different data types.
        - In-Place Operation
        #### Path
        - Geometry > Join Geometry Node
        #### Outputs:
        - `#0 geometry: Geometry = None`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeJoinGeometry.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/join_geometry.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeJoinGeometry.html)
        """
        items = list(reversed(others)) + [self]
        node = new_node(*nodes.GeometryNodeJoinGeometry())
        for item in items:
            new_link(item.bsocket, node.bnode.inputs[0])
        self.bsocket = node.outputs[0].bsocket
        return self

    def __add__(self, *others: "Geometry"):
        items = list(reversed(others)) + [self]
        node = new_node(*nodes.GeometryNodeJoinGeometry())
        for item in items:
            new_link(item.bsocket, node.bnode.inputs[0])
        return node.outputs[0].Geometry

    def join_to_instances(self, *others: "Geometry"):
        """The Geometry to Instance node turns every connected input geometry into an instance. Visually, the node has a similar result as the Join Geometry Node, but it outputs the result as separate instances instead. The geometry data itself isn’t actually joined.
        #### Path
        - Geometry > Geometry to Instance Node
        #### Outputs:
        - `#0 instances: Geometry = None`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeGeometryToInstance.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/geometry_to_instance.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeGeometryToInstance.html)
        """
        items = list(reversed(others)) + [self]
        node = new_node(*nodes.GeometryNodeGeometryToInstance())
        for item in items:
            self.tree.new_link(item.bsocket, node.bnode.inputs[0])
        return node.outputs[0].Instances

    def on_points(self, points: "Points" = None, pick_instance=False, instance_index: "Integer" = None, rotation=(0.0, 0.0, 0.0), scale=(1.0, 1.0, 1.0), selection=True):
        """The Instance on Points node adds a reference to a geometry to each of the points present in the input geometry. Instances are a fast way to add the same geometry to a scene many times without duplicating the underlying data. The node works on any geometry type with a Point domain, including meshes, point clouds, and curve control points.
        - In-Place Operation
        #### Path
        - Instances > Instance on Points Node
        #### Outputs:
        - `#0 instances: Geometry = None`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeInstanceOnPoints.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/instance_on_points.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeInstanceOnPoints.html)
        """
        selection = selection if points._selection is None else points.selection
        node = new_node(*nodes.GeometryNodeInstanceOnPoints(points, selection, self, pick_instance, instance_index, rotation, scale))
        self.bsocket = node.outputs[0].bsocket
        return self

    def replace_material(self, old=None, new=None):
        """The Replace Material node swaps one material with another. Replacing a material with this node is more efficient than creating a selection of all faces with the old material with the Material Selection Node and then using the Set Material Node.
        #### Path
        - Material > Replace Material Node
        #### Outputs:
        - `#0 geometry: Geometry = None`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeReplaceMaterial.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/replace_material.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeReplaceMaterial.html)
        """
        node = new_node(*nodes.GeometryNodeReplaceMaterial(self, old, new))
        return node.outputs[0].Geometry

    def set_material(self, material=None, selection=True):
        """The Set Material changes the material assignment in the specified selection, by adjusting the material_index attribute. If the material is already used on the geometry, the existing material index will be reused.
        - In-Place Operation
        #### Path
        - Material > Set Material Node
        #### Outputs:
        - `#0 geometry: Geometry = None`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeSetMaterial.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/set_material.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetMaterial.html)
        """
        selection = selection if self._selection is None else self.selection
        node = new_node(*nodes.GeometryNodeSetMaterial(self, selection, material))
        self.bsocket = node.outputs[0].bsocket
        return self

    def set_material_index(self, material_index=0, selection=True):
        """The Set Material Index node sets the material index for a geometry.
        - In-Place Operation
        #### Path
        - Material > Set Material Index Node
        #### Outputs:
        - `#0 geometry: Geometry = None`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeSetMaterialIndex.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/set_material_index.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetMaterialIndex.html)
        """
        selection = selection if self._selection is None else self.selection
        node = new_node(*nodes.GeometryNodeSetMaterialIndex(self, selection, material_index))
        self.bsocket = node.outputs[0].bsocket
        return self

    @staticmethod
    def accumulate_float_on_points(value_float=0.0, group_index=0):
        """The Accumulate Field node counts a running total of its input values, in the order defined by the geometry's indices. The node's essential operation is just addition, but instead of only outputting the final total, it outputs the current value at every element.
        #### Path
        - Utilities > Field > Accumulate Field Node
        #### Outputs:
        - `#0 leading_float: Float = 0.0`
        - `#3 trailing_float: Float = 0.0`
        - `#6 total_float: Float = 0.0`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeAccumulateField.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/field/accumulate_field.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeAccumulateField.html)
        """
        node = new_node(*nodes.GeometryNodeAccumulateField("FLOAT", "POINT", value_float=value_float, group_index=group_index))
        ret = typing.NamedTuple("GeometryNodeAccumulateField", [("leading", Float), ("trailing", Float), ("total", Float)])
        return ret(node.outputs[0].Float, node.outputs[3].Float, node.outputs[6].Float)

    @staticmethod
    def accumulate_float_on_edges(value_float=0.0, group_index=0):
        """The Accumulate Field node counts a running total of its input values, in the order defined by the geometry's indices. The node's essential operation is just addition, but instead of only outputting the final total, it outputs the current value at every element.
        #### Path
        - Utilities > Field > Accumulate Field Node
        #### Outputs:
        - `#0 leading_float: Float = 0.0`
        - `#3 trailing_float: Float = 0.0`
        - `#6 total_float: Float = 0.0`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeAccumulateField.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/field/accumulate_field.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeAccumulateField.html)
        """
        node = new_node(*nodes.GeometryNodeAccumulateField("FLOAT", "EDGE", value_float=value_float, group_index=group_index))
        ret = typing.NamedTuple("GeometryNodeAccumulateField", [("leading", Float), ("trailing", Float), ("total", Float)])
        return ret(node.outputs[0].Float, node.outputs[3].Float, node.outputs[6].Float)

    @staticmethod
    def accumulate_float_on_faces(value_float=0.0, group_index=0):
        """The Accumulate Field node counts a running total of its input values, in the order defined by the geometry's indices. The node's essential operation is just addition, but instead of only outputting the final total, it outputs the current value at every element.
        #### Path
        - Utilities > Field > Accumulate Field Node
        #### Outputs:
        - `#0 leading_float: Float = 0.0`
        - `#3 trailing_float: Float = 0.0`
        - `#6 total_float: Float = 0.0`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeAccumulateField.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/field/accumulate_field.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeAccumulateField.html)
        """
        node = new_node(*nodes.GeometryNodeAccumulateField("FLOAT", "FACE", value_float=value_float, group_index=group_index))
        ret = typing.NamedTuple("GeometryNodeAccumulateField", [("leading", Float), ("trailing", Float), ("total", Float)])
        return ret(node.outputs[0].Float, node.outputs[3].Float, node.outputs[6].Float)

    @staticmethod
    def accumulate_float_on_corners(value_float=0.0, group_index=0):
        """The Accumulate Field node counts a running total of its input values, in the order defined by the geometry's indices. The node's essential operation is just addition, but instead of only outputting the final total, it outputs the current value at every element.
        #### Path
        - Utilities > Field > Accumulate Field Node
        #### Outputs:
        - `#0 leading_float: Float = 0.0`
        - `#3 trailing_float: Float = 0.0`
        - `#6 total_float: Float = 0.0`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeAccumulateField.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/field/accumulate_field.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeAccumulateField.html)
        """
        node = new_node(*nodes.GeometryNodeAccumulateField("FLOAT", "CORNER", value_float=value_float, group_index=group_index))
        ret = typing.NamedTuple("GeometryNodeAccumulateField", [("leading", Float), ("trailing", Float), ("total", Float)])
        return ret(node.outputs[0].Float, node.outputs[3].Float, node.outputs[6].Float)

    @staticmethod
    def accumulate_float_on_curves(value_float=0.0, group_index=0):
        """The Accumulate Field node counts a running total of its input values, in the order defined by the geometry's indices. The node's essential operation is just addition, but instead of only outputting the final total, it outputs the current value at every element.
        #### Path
        - Utilities > Field > Accumulate Field Node
        #### Outputs:
        - `#0 leading_float: Float = 0.0`
        - `#3 trailing_float: Float = 0.0`
        - `#6 total_float: Float = 0.0`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeAccumulateField.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/field/accumulate_field.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeAccumulateField.html)
        """
        node = new_node(*nodes.GeometryNodeAccumulateField("FLOAT", "CURVE", value_float=value_float, group_index=group_index))
        ret = typing.NamedTuple("GeometryNodeAccumulateField", [("leading", Float), ("trailing", Float), ("total", Float)])
        return ret(node.outputs[0].Float, node.outputs[3].Float, node.outputs[6].Float)

    @staticmethod
    def accumulate_float_on_instances(value_float=0.0, group_index=0):
        """The Accumulate Field node counts a running total of its input values, in the order defined by the geometry's indices. The node's essential operation is just addition, but instead of only outputting the final total, it outputs the current value at every element.
        #### Path
        - Utilities > Field > Accumulate Field Node
        #### Outputs:
        - `#0 leading_float: Float = 0.0`
        - `#3 trailing_float: Float = 0.0`
        - `#6 total_float: Float = 0.0`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeAccumulateField.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/field/accumulate_field.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeAccumulateField.html)
        """
        node = new_node(*nodes.GeometryNodeAccumulateField("FLOAT", "INSTANCE", value_float=value_float, group_index=group_index))
        ret = typing.NamedTuple("GeometryNodeAccumulateField", [("leading", Float), ("trailing", Float), ("total", Float)])
        return ret(node.outputs[0].Float, node.outputs[3].Float, node.outputs[6].Float)

    @staticmethod
    def accumulate_integer_on_points(value_int=0, group_index=0):
        """The Accumulate Field node counts a running total of its input values, in the order defined by the geometry's indices. The node's essential operation is just addition, but instead of only outputting the final total, it outputs the current value at every element.
        #### Path
        - Utilities > Field > Accumulate Field Node
        #### Outputs:
        - `#1 leading_integer: Integer = 0`
        - `#4 trailing_integer: Integer = 0`
        - `#7 total_integer: Integer = 0`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeAccumulateField.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/field/accumulate_field.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeAccumulateField.html)
        """
        node = new_node(*nodes.GeometryNodeAccumulateField("INT", "POINT", value_int=value_int, group_index=group_index))
        ret = typing.NamedTuple("GeometryNodeAccumulateField", [("leading", Integer), ("trailing", Integer), ("total", Integer)])
        return ret(node.outputs[1].Integer, node.outputs[4].Integer, node.outputs[7].Integer)

    @staticmethod
    def accumulate_integer_on_edges(value_int=0, group_index=0):
        """The Accumulate Field node counts a running total of its input values, in the order defined by the geometry's indices. The node's essential operation is just addition, but instead of only outputting the final total, it outputs the current value at every element.
        #### Path
        - Utilities > Field > Accumulate Field Node
        #### Outputs:
        - `#1 leading_integer: Integer = 0`
        - `#4 trailing_integer: Integer = 0`
        - `#7 total_integer: Integer = 0`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeAccumulateField.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/field/accumulate_field.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeAccumulateField.html)
        """
        node = new_node(*nodes.GeometryNodeAccumulateField("INT", "EDGE", value_int=value_int, group_index=group_index))
        ret = typing.NamedTuple("GeometryNodeAccumulateField", [("leading", Integer), ("trailing", Integer), ("total", Integer)])
        return ret(node.outputs[1].Integer, node.outputs[4].Integer, node.outputs[7].Integer)

    @staticmethod
    def accumulate_integer_on_faces(value_int=0, group_index=0):
        """The Accumulate Field node counts a running total of its input values, in the order defined by the geometry's indices. The node's essential operation is just addition, but instead of only outputting the final total, it outputs the current value at every element.
        #### Path
        - Utilities > Field > Accumulate Field Node
        #### Outputs:
        - `#1 leading_integer: Integer = 0`
        - `#4 trailing_integer: Integer = 0`
        - `#7 total_integer: Integer = 0`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeAccumulateField.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/field/accumulate_field.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeAccumulateField.html)
        """
        node = new_node(*nodes.GeometryNodeAccumulateField("INT", "FACE", value_int=value_int, group_index=group_index))
        ret = typing.NamedTuple("GeometryNodeAccumulateField", [("leading", Integer), ("trailing", Integer), ("total", Integer)])
        return ret(node.outputs[1].Integer, node.outputs[4].Integer, node.outputs[7].Integer)

    @staticmethod
    def accumulate_integer_on_corners(value_int=0, group_index=0):
        """The Accumulate Field node counts a running total of its input values, in the order defined by the geometry's indices. The node's essential operation is just addition, but instead of only outputting the final total, it outputs the current value at every element.
        #### Path
        - Utilities > Field > Accumulate Field Node
        #### Outputs:
        - `#1 leading_integer: Integer = 0`
        - `#4 trailing_integer: Integer = 0`
        - `#7 total_integer: Integer = 0`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeAccumulateField.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/field/accumulate_field.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeAccumulateField.html)
        """
        node = new_node(*nodes.GeometryNodeAccumulateField("INT", "CORNER", value_int=value_int, group_index=group_index))
        ret = typing.NamedTuple("GeometryNodeAccumulateField", [("leading", Integer), ("trailing", Integer), ("total", Integer)])
        return ret(node.outputs[1].Integer, node.outputs[4].Integer, node.outputs[7].Integer)

    @staticmethod
    def accumulate_integer_on_curves(value_int=0, group_index=0):
        """The Accumulate Field node counts a running total of its input values, in the order defined by the geometry's indices. The node's essential operation is just addition, but instead of only outputting the final total, it outputs the current value at every element.
        #### Path
        - Utilities > Field > Accumulate Field Node
        #### Outputs:
        - `#1 leading_integer: Integer = 0`
        - `#4 trailing_integer: Integer = 0`
        - `#7 total_integer: Integer = 0`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeAccumulateField.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/field/accumulate_field.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeAccumulateField.html)
        """
        node = new_node(*nodes.GeometryNodeAccumulateField("INT", "CURVE", value_int=value_int, group_index=group_index))
        ret = typing.NamedTuple("GeometryNodeAccumulateField", [("leading", Integer), ("trailing", Integer), ("total", Integer)])
        return ret(node.outputs[1].Integer, node.outputs[4].Integer, node.outputs[7].Integer)

    @staticmethod
    def accumulate_integer_on_instances(value_int=0, group_index=0):
        """The Accumulate Field node counts a running total of its input values, in the order defined by the geometry's indices. The node's essential operation is just addition, but instead of only outputting the final total, it outputs the current value at every element.
        #### Path
        - Utilities > Field > Accumulate Field Node
        #### Outputs:
        - `#1 leading_integer: Integer = 0`
        - `#4 trailing_integer: Integer = 0`
        - `#7 total_integer: Integer = 0`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeAccumulateField.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/field/accumulate_field.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeAccumulateField.html)
        """
        node = new_node(*nodes.GeometryNodeAccumulateField("INT", "INSTANCE", value_int=value_int, group_index=group_index))
        ret = typing.NamedTuple("GeometryNodeAccumulateField", [("leading", Integer), ("trailing", Integer), ("total", Integer)])
        return ret(node.outputs[1].Integer, node.outputs[4].Integer, node.outputs[7].Integer)

    @staticmethod
    def accumulate_vector_on_points(value_vector=(0.0, 0.0, 0.0), group_index=0):
        """The Accumulate Field node counts a running total of its input values, in the order defined by the geometry's indices. The node's essential operation is just addition, but instead of only outputting the final total, it outputs the current value at every element.
        #### Path
        - Utilities > Field > Accumulate Field Node
        #### Outputs:
        - `#2 leading_vector: Vector = (0.0, 0.0, 0.0)`
        - `#5 trailing_vector: Vector = (0.0, 0.0, 0.0)`
        - `#8 total_vector: Vector = (0.0, 0.0, 0.0)`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeAccumulateField.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/field/accumulate_field.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeAccumulateField.html)
        """
        node = new_node(*nodes.GeometryNodeAccumulateField("FLOAT_VECTOR", "POINT", value_vector=value_vector, group_index=group_index))
        ret = typing.NamedTuple("GeometryNodeAccumulateField", [("leading", Vector), ("trailing", Vector), ("total", Vector)])
        return ret(node.outputs[2].Vector, node.outputs[5].Vector, node.outputs[8].Vector)

    @staticmethod
    def accumulate_vector_on_edges(value_vector=(0.0, 0.0, 0.0), group_index=0):
        """The Accumulate Field node counts a running total of its input values, in the order defined by the geometry's indices. The node's essential operation is just addition, but instead of only outputting the final total, it outputs the current value at every element.
        #### Path
        - Utilities > Field > Accumulate Field Node
        #### Outputs:
        - `#2 leading_vector: Vector = (0.0, 0.0, 0.0)`
        - `#5 trailing_vector: Vector = (0.0, 0.0, 0.0)`
        - `#8 total_vector: Vector = (0.0, 0.0, 0.0)`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeAccumulateField.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/field/accumulate_field.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeAccumulateField.html)
        """
        node = new_node(*nodes.GeometryNodeAccumulateField("FLOAT_VECTOR", "EDGE", value_vector=value_vector, group_index=group_index))
        ret = typing.NamedTuple("GeometryNodeAccumulateField", [("leading", Vector), ("trailing", Vector), ("total", Vector)])
        return ret(node.outputs[2].Vector, node.outputs[5].Vector, node.outputs[8].Vector)

    @staticmethod
    def accumulate_vector_on_faces(value_vector=(0.0, 0.0, 0.0), group_index=0):
        """The Accumulate Field node counts a running total of its input values, in the order defined by the geometry's indices. The node's essential operation is just addition, but instead of only outputting the final total, it outputs the current value at every element.
        #### Path
        - Utilities > Field > Accumulate Field Node
        #### Outputs:
        - `#2 leading_vector: Vector = (0.0, 0.0, 0.0)`
        - `#5 trailing_vector: Vector = (0.0, 0.0, 0.0)`
        - `#8 total_vector: Vector = (0.0, 0.0, 0.0)`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeAccumulateField.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/field/accumulate_field.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeAccumulateField.html)
        """
        node = new_node(*nodes.GeometryNodeAccumulateField("FLOAT_VECTOR", "FACE", value_vector=value_vector, group_index=group_index))
        ret = typing.NamedTuple("GeometryNodeAccumulateField", [("leading", Vector), ("trailing", Vector), ("total", Vector)])
        return ret(node.outputs[2].Vector, node.outputs[5].Vector, node.outputs[8].Vector)

    @staticmethod
    def accumulate_vector_on_corners(value_vector=(0.0, 0.0, 0.0), group_index=0):
        """The Accumulate Field node counts a running total of its input values, in the order defined by the geometry's indices. The node's essential operation is just addition, but instead of only outputting the final total, it outputs the current value at every element.
        #### Path
        - Utilities > Field > Accumulate Field Node
        #### Outputs:
        - `#2 leading_vector: Vector = (0.0, 0.0, 0.0)`
        - `#5 trailing_vector: Vector = (0.0, 0.0, 0.0)`
        - `#8 total_vector: Vector = (0.0, 0.0, 0.0)`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeAccumulateField.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/field/accumulate_field.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeAccumulateField.html)
        """
        node = new_node(*nodes.GeometryNodeAccumulateField("FLOAT_VECTOR", "CORNER", value_vector=value_vector, group_index=group_index))
        ret = typing.NamedTuple("GeometryNodeAccumulateField", [("leading", Vector), ("trailing", Vector), ("total", Vector)])
        return ret(node.outputs[2].Vector, node.outputs[5].Vector, node.outputs[8].Vector)

    @staticmethod
    def accumulate_vector_on_curves(value_vector=(0.0, 0.0, 0.0), group_index=0):
        """The Accumulate Field node counts a running total of its input values, in the order defined by the geometry's indices. The node's essential operation is just addition, but instead of only outputting the final total, it outputs the current value at every element.
        #### Path
        - Utilities > Field > Accumulate Field Node
        #### Outputs:
        - `#2 leading_vector: Vector = (0.0, 0.0, 0.0)`
        - `#5 trailing_vector: Vector = (0.0, 0.0, 0.0)`
        - `#8 total_vector: Vector = (0.0, 0.0, 0.0)`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeAccumulateField.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/field/accumulate_field.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeAccumulateField.html)
        """
        node = new_node(*nodes.GeometryNodeAccumulateField("FLOAT_VECTOR", "CURVE", value_vector=value_vector, group_index=group_index))
        ret = typing.NamedTuple("GeometryNodeAccumulateField", [("leading", Vector), ("trailing", Vector), ("total", Vector)])
        return ret(node.outputs[2].Vector, node.outputs[5].Vector, node.outputs[8].Vector)

    @staticmethod
    def accumulate_vector_on_instances(value_vector=(0.0, 0.0, 0.0), group_index=0):
        """The Accumulate Field node counts a running total of its input values, in the order defined by the geometry's indices. The node's essential operation is just addition, but instead of only outputting the final total, it outputs the current value at every element.
        #### Path
        - Utilities > Field > Accumulate Field Node
        #### Outputs:
        - `#2 leading_vector: Vector = (0.0, 0.0, 0.0)`
        - `#5 trailing_vector: Vector = (0.0, 0.0, 0.0)`
        - `#8 total_vector: Vector = (0.0, 0.0, 0.0)`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeAccumulateField.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/field/accumulate_field.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeAccumulateField.html)
        """
        node = new_node(*nodes.GeometryNodeAccumulateField("FLOAT_VECTOR", "INSTANCE", value_vector=value_vector, group_index=group_index))
        ret = typing.NamedTuple("GeometryNodeAccumulateField", [("leading", Vector), ("trailing", Vector), ("total", Vector)])
        return ret(node.outputs[2].Vector, node.outputs[5].Vector, node.outputs[8].Vector)

    @staticmethod
    def evaluate_float_at_index_on_points(index=0, value_float=0.0):
        """The Evaluate at Index node allows accessing data of other elements in the context geometry. It is similar to the Sample Index Node. The main difference is that this node does not require a geometry input, because the geometry from the field context is used.
        #### Path
        - Utilities > Field > Evaluate at Index Node
        #### Outputs:
        - `#0 value_float: Float = 0.0`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeFieldAtIndex.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/field/evaluate_at_index.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeFieldAtIndex.html)
        """
        node = new_node(*nodes.GeometryNodeFieldAtIndex("FLOAT", "POINT", index, value_float=value_float))
        return node.outputs[0].Float

    @staticmethod
    def evaluate_float_at_index_on_edges(index=0, value_float=0.0):
        """The Evaluate at Index node allows accessing data of other elements in the context geometry. It is similar to the Sample Index Node. The main difference is that this node does not require a geometry input, because the geometry from the field context is used.
        #### Path
        - Utilities > Field > Evaluate at Index Node
        #### Outputs:
        - `#0 value_float: Float = 0.0`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeFieldAtIndex.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/field/evaluate_at_index.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeFieldAtIndex.html)
        """
        node = new_node(*nodes.GeometryNodeFieldAtIndex("FLOAT", "EDGE", index, value_float=value_float))
        return node.outputs[0].Float

    @staticmethod
    def evaluate_float_at_index_on_faces(index=0, value_float=0.0):
        """The Evaluate at Index node allows accessing data of other elements in the context geometry. It is similar to the Sample Index Node. The main difference is that this node does not require a geometry input, because the geometry from the field context is used.
        #### Path
        - Utilities > Field > Evaluate at Index Node
        #### Outputs:
        - `#0 value_float: Float = 0.0`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeFieldAtIndex.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/field/evaluate_at_index.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeFieldAtIndex.html)
        """
        node = new_node(*nodes.GeometryNodeFieldAtIndex("FLOAT", "FACE", index, value_float=value_float))
        return node.outputs[0].Float

    @staticmethod
    def evaluate_float_at_index_on_corners(index=0, value_float=0.0):
        """The Evaluate at Index node allows accessing data of other elements in the context geometry. It is similar to the Sample Index Node. The main difference is that this node does not require a geometry input, because the geometry from the field context is used.
        #### Path
        - Utilities > Field > Evaluate at Index Node
        #### Outputs:
        - `#0 value_float: Float = 0.0`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeFieldAtIndex.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/field/evaluate_at_index.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeFieldAtIndex.html)
        """
        node = new_node(*nodes.GeometryNodeFieldAtIndex("FLOAT", "CORNER", index, value_float=value_float))
        return node.outputs[0].Float

    @staticmethod
    def evaluate_float_at_index_on_curves(index=0, value_float=0.0):
        """The Evaluate at Index node allows accessing data of other elements in the context geometry. It is similar to the Sample Index Node. The main difference is that this node does not require a geometry input, because the geometry from the field context is used.
        #### Path
        - Utilities > Field > Evaluate at Index Node
        #### Outputs:
        - `#0 value_float: Float = 0.0`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeFieldAtIndex.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/field/evaluate_at_index.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeFieldAtIndex.html)
        """
        node = new_node(*nodes.GeometryNodeFieldAtIndex("FLOAT", "CURVE", index, value_float=value_float))
        return node.outputs[0].Float

    @staticmethod
    def evaluate_float_at_index_on_instances(index=0, value_float=0.0):
        """The Evaluate at Index node allows accessing data of other elements in the context geometry. It is similar to the Sample Index Node. The main difference is that this node does not require a geometry input, because the geometry from the field context is used.
        #### Path
        - Utilities > Field > Evaluate at Index Node
        #### Outputs:
        - `#0 value_float: Float = 0.0`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeFieldAtIndex.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/field/evaluate_at_index.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeFieldAtIndex.html)
        """
        node = new_node(*nodes.GeometryNodeFieldAtIndex("FLOAT", "INSTANCE", index, value_float=value_float))
        return node.outputs[0].Float

    @staticmethod
    def evaluate_integer_at_index_on_points(index=0, value_int=0):
        """The Evaluate at Index node allows accessing data of other elements in the context geometry. It is similar to the Sample Index Node. The main difference is that this node does not require a geometry input, because the geometry from the field context is used.
        #### Path
        - Utilities > Field > Evaluate at Index Node
        #### Outputs:
        - `#1 value_int: Integer = 0`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeFieldAtIndex.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/field/evaluate_at_index.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeFieldAtIndex.html)
        """
        node = new_node(*nodes.GeometryNodeFieldAtIndex("INT", "POINT", index, value_int=value_int))
        return node.outputs[1].Integer

    @staticmethod
    def evaluate_integer_at_index_on_edges(index=0, value_int=0):
        """The Evaluate at Index node allows accessing data of other elements in the context geometry. It is similar to the Sample Index Node. The main difference is that this node does not require a geometry input, because the geometry from the field context is used.
        #### Path
        - Utilities > Field > Evaluate at Index Node
        #### Outputs:
        - `#1 value_int: Integer = 0`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeFieldAtIndex.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/field/evaluate_at_index.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeFieldAtIndex.html)
        """
        node = new_node(*nodes.GeometryNodeFieldAtIndex("INT", "EDGE", index, value_int=value_int))
        return node.outputs[1].Integer

    @staticmethod
    def evaluate_integer_at_index_on_faces(index=0, value_int=0):
        """The Evaluate at Index node allows accessing data of other elements in the context geometry. It is similar to the Sample Index Node. The main difference is that this node does not require a geometry input, because the geometry from the field context is used.
        #### Path
        - Utilities > Field > Evaluate at Index Node
        #### Outputs:
        - `#1 value_int: Integer = 0`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeFieldAtIndex.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/field/evaluate_at_index.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeFieldAtIndex.html)
        """
        node = new_node(*nodes.GeometryNodeFieldAtIndex("INT", "FACE", index, value_int=value_int))
        return node.outputs[1].Integer

    @staticmethod
    def evaluate_integer_at_index_on_corners(index=0, value_int=0):
        """The Evaluate at Index node allows accessing data of other elements in the context geometry. It is similar to the Sample Index Node. The main difference is that this node does not require a geometry input, because the geometry from the field context is used.
        #### Path
        - Utilities > Field > Evaluate at Index Node
        #### Outputs:
        - `#1 value_int: Integer = 0`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeFieldAtIndex.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/field/evaluate_at_index.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeFieldAtIndex.html)
        """
        node = new_node(*nodes.GeometryNodeFieldAtIndex("INT", "CORNER", index, value_int=value_int))
        return node.outputs[1].Integer

    @staticmethod
    def evaluate_integer_at_index_on_curves(index=0, value_int=0):
        """The Evaluate at Index node allows accessing data of other elements in the context geometry. It is similar to the Sample Index Node. The main difference is that this node does not require a geometry input, because the geometry from the field context is used.
        #### Path
        - Utilities > Field > Evaluate at Index Node
        #### Outputs:
        - `#1 value_int: Integer = 0`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeFieldAtIndex.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/field/evaluate_at_index.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeFieldAtIndex.html)
        """
        node = new_node(*nodes.GeometryNodeFieldAtIndex("INT", "CURVE", index, value_int=value_int))
        return node.outputs[1].Integer

    @staticmethod
    def evaluate_integer_at_index_on_instances(index=0, value_int=0):
        """The Evaluate at Index node allows accessing data of other elements in the context geometry. It is similar to the Sample Index Node. The main difference is that this node does not require a geometry input, because the geometry from the field context is used.
        #### Path
        - Utilities > Field > Evaluate at Index Node
        #### Outputs:
        - `#1 value_int: Integer = 0`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeFieldAtIndex.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/field/evaluate_at_index.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeFieldAtIndex.html)
        """
        node = new_node(*nodes.GeometryNodeFieldAtIndex("INT", "INSTANCE", index, value_int=value_int))
        return node.outputs[1].Integer

    @staticmethod
    def evaluate_vector_at_index_on_points(index=0, value_vector=(0.0, 0.0, 0.0)):
        """The Evaluate at Index node allows accessing data of other elements in the context geometry. It is similar to the Sample Index Node. The main difference is that this node does not require a geometry input, because the geometry from the field context is used.
        #### Path
        - Utilities > Field > Evaluate at Index Node
        #### Outputs:
        - `#2 value_vector: Vector = (0.0, 0.0, 0.0)`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeFieldAtIndex.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/field/evaluate_at_index.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeFieldAtIndex.html)
        """
        node = new_node(*nodes.GeometryNodeFieldAtIndex("FLOAT_VECTOR", "POINT", index, value_vector=value_vector))
        return node.outputs[2].Vector

    @staticmethod
    def evaluate_vector_at_index_on_edges(index=0, value_vector=(0.0, 0.0, 0.0)):
        """The Evaluate at Index node allows accessing data of other elements in the context geometry. It is similar to the Sample Index Node. The main difference is that this node does not require a geometry input, because the geometry from the field context is used.
        #### Path
        - Utilities > Field > Evaluate at Index Node
        #### Outputs:
        - `#2 value_vector: Vector = (0.0, 0.0, 0.0)`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeFieldAtIndex.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/field/evaluate_at_index.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeFieldAtIndex.html)
        """
        node = new_node(*nodes.GeometryNodeFieldAtIndex("FLOAT_VECTOR", "EDGE", index, value_vector=value_vector))
        return node.outputs[2].Vector

    @staticmethod
    def evaluate_vector_at_index_on_faces(index=0, value_vector=(0.0, 0.0, 0.0)):
        """The Evaluate at Index node allows accessing data of other elements in the context geometry. It is similar to the Sample Index Node. The main difference is that this node does not require a geometry input, because the geometry from the field context is used.
        #### Path
        - Utilities > Field > Evaluate at Index Node
        #### Outputs:
        - `#2 value_vector: Vector = (0.0, 0.0, 0.0)`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeFieldAtIndex.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/field/evaluate_at_index.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeFieldAtIndex.html)
        """
        node = new_node(*nodes.GeometryNodeFieldAtIndex("FLOAT_VECTOR", "FACE", index, value_vector=value_vector))
        return node.outputs[2].Vector

    @staticmethod
    def evaluate_vector_at_index_on_corners(index=0, value_vector=(0.0, 0.0, 0.0)):
        """The Evaluate at Index node allows accessing data of other elements in the context geometry. It is similar to the Sample Index Node. The main difference is that this node does not require a geometry input, because the geometry from the field context is used.
        #### Path
        - Utilities > Field > Evaluate at Index Node
        #### Outputs:
        - `#2 value_vector: Vector = (0.0, 0.0, 0.0)`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeFieldAtIndex.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/field/evaluate_at_index.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeFieldAtIndex.html)
        """
        node = new_node(*nodes.GeometryNodeFieldAtIndex("FLOAT_VECTOR", "CORNER", index, value_vector=value_vector))
        return node.outputs[2].Vector

    @staticmethod
    def evaluate_vector_at_index_on_curves(index=0, value_vector=(0.0, 0.0, 0.0)):
        """The Evaluate at Index node allows accessing data of other elements in the context geometry. It is similar to the Sample Index Node. The main difference is that this node does not require a geometry input, because the geometry from the field context is used.
        #### Path
        - Utilities > Field > Evaluate at Index Node
        #### Outputs:
        - `#2 value_vector: Vector = (0.0, 0.0, 0.0)`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeFieldAtIndex.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/field/evaluate_at_index.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeFieldAtIndex.html)
        """
        node = new_node(*nodes.GeometryNodeFieldAtIndex("FLOAT_VECTOR", "CURVE", index, value_vector=value_vector))
        return node.outputs[2].Vector

    @staticmethod
    def evaluate_vector_at_index_on_instances(index=0, value_vector=(0.0, 0.0, 0.0)):
        """The Evaluate at Index node allows accessing data of other elements in the context geometry. It is similar to the Sample Index Node. The main difference is that this node does not require a geometry input, because the geometry from the field context is used.
        #### Path
        - Utilities > Field > Evaluate at Index Node
        #### Outputs:
        - `#2 value_vector: Vector = (0.0, 0.0, 0.0)`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeFieldAtIndex.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/field/evaluate_at_index.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeFieldAtIndex.html)
        """
        node = new_node(*nodes.GeometryNodeFieldAtIndex("FLOAT_VECTOR", "INSTANCE", index, value_vector=value_vector))
        return node.outputs[2].Vector

    @staticmethod
    def evaluate_color_at_index_on_points(index=0, value_color=(0.0, 0.0, 0.0, 0.0)):
        """The Evaluate at Index node allows accessing data of other elements in the context geometry. It is similar to the Sample Index Node. The main difference is that this node does not require a geometry input, because the geometry from the field context is used.
        #### Path
        - Utilities > Field > Evaluate at Index Node
        #### Outputs:
        - `#3 value_color: Color = (0.0, 0.0, 0.0, 0.0)`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeFieldAtIndex.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/field/evaluate_at_index.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeFieldAtIndex.html)
        """
        node = new_node(*nodes.GeometryNodeFieldAtIndex("FLOAT_COLOR", "POINT", index, value_color=value_color))
        return node.outputs[3].Color

    @staticmethod
    def evaluate_color_at_index_on_edges(index=0, value_color=(0.0, 0.0, 0.0, 0.0)):
        """The Evaluate at Index node allows accessing data of other elements in the context geometry. It is similar to the Sample Index Node. The main difference is that this node does not require a geometry input, because the geometry from the field context is used.
        #### Path
        - Utilities > Field > Evaluate at Index Node
        #### Outputs:
        - `#3 value_color: Color = (0.0, 0.0, 0.0, 0.0)`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeFieldAtIndex.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/field/evaluate_at_index.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeFieldAtIndex.html)
        """
        node = new_node(*nodes.GeometryNodeFieldAtIndex("FLOAT_COLOR", "EDGE", index, value_color=value_color))
        return node.outputs[3].Color

    @staticmethod
    def evaluate_color_at_index_on_faces(index=0, value_color=(0.0, 0.0, 0.0, 0.0)):
        """The Evaluate at Index node allows accessing data of other elements in the context geometry. It is similar to the Sample Index Node. The main difference is that this node does not require a geometry input, because the geometry from the field context is used.
        #### Path
        - Utilities > Field > Evaluate at Index Node
        #### Outputs:
        - `#3 value_color: Color = (0.0, 0.0, 0.0, 0.0)`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeFieldAtIndex.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/field/evaluate_at_index.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeFieldAtIndex.html)
        """
        node = new_node(*nodes.GeometryNodeFieldAtIndex("FLOAT_COLOR", "FACE", index, value_color=value_color))
        return node.outputs[3].Color

    @staticmethod
    def evaluate_color_at_index_on_corners(index=0, value_color=(0.0, 0.0, 0.0, 0.0)):
        """The Evaluate at Index node allows accessing data of other elements in the context geometry. It is similar to the Sample Index Node. The main difference is that this node does not require a geometry input, because the geometry from the field context is used.
        #### Path
        - Utilities > Field > Evaluate at Index Node
        #### Outputs:
        - `#3 value_color: Color = (0.0, 0.0, 0.0, 0.0)`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeFieldAtIndex.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/field/evaluate_at_index.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeFieldAtIndex.html)
        """
        node = new_node(*nodes.GeometryNodeFieldAtIndex("FLOAT_COLOR", "CORNER", index, value_color=value_color))
        return node.outputs[3].Color

    @staticmethod
    def evaluate_color_at_index_on_curves(index=0, value_color=(0.0, 0.0, 0.0, 0.0)):
        """The Evaluate at Index node allows accessing data of other elements in the context geometry. It is similar to the Sample Index Node. The main difference is that this node does not require a geometry input, because the geometry from the field context is used.
        #### Path
        - Utilities > Field > Evaluate at Index Node
        #### Outputs:
        - `#3 value_color: Color = (0.0, 0.0, 0.0, 0.0)`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeFieldAtIndex.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/field/evaluate_at_index.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeFieldAtIndex.html)
        """
        node = new_node(*nodes.GeometryNodeFieldAtIndex("FLOAT_COLOR", "CURVE", index, value_color=value_color))
        return node.outputs[3].Color

    @staticmethod
    def evaluate_color_at_index_on_instances(index=0, value_color=(0.0, 0.0, 0.0, 0.0)):
        """The Evaluate at Index node allows accessing data of other elements in the context geometry. It is similar to the Sample Index Node. The main difference is that this node does not require a geometry input, because the geometry from the field context is used.
        #### Path
        - Utilities > Field > Evaluate at Index Node
        #### Outputs:
        - `#3 value_color: Color = (0.0, 0.0, 0.0, 0.0)`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeFieldAtIndex.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/field/evaluate_at_index.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeFieldAtIndex.html)
        """
        node = new_node(*nodes.GeometryNodeFieldAtIndex("FLOAT_COLOR", "INSTANCE", index, value_color=value_color))
        return node.outputs[3].Color

    @staticmethod
    def evaluate_boolean_at_index_on_points(index=0, value_bool=False):
        """The Evaluate at Index node allows accessing data of other elements in the context geometry. It is similar to the Sample Index Node. The main difference is that this node does not require a geometry input, because the geometry from the field context is used.
        #### Path
        - Utilities > Field > Evaluate at Index Node
        #### Outputs:
        - `#4 value_bool: Boolean = False`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeFieldAtIndex.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/field/evaluate_at_index.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeFieldAtIndex.html)
        """
        node = new_node(*nodes.GeometryNodeFieldAtIndex("BOOLEAN", "POINT", index, value_bool=value_bool))
        return node.outputs[4].Boolean

    @staticmethod
    def evaluate_boolean_at_index_on_edges(index=0, value_bool=False):
        """The Evaluate at Index node allows accessing data of other elements in the context geometry. It is similar to the Sample Index Node. The main difference is that this node does not require a geometry input, because the geometry from the field context is used.
        #### Path
        - Utilities > Field > Evaluate at Index Node
        #### Outputs:
        - `#4 value_bool: Boolean = False`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeFieldAtIndex.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/field/evaluate_at_index.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeFieldAtIndex.html)
        """
        node = new_node(*nodes.GeometryNodeFieldAtIndex("BOOLEAN", "EDGE", index, value_bool=value_bool))
        return node.outputs[4].Boolean

    @staticmethod
    def evaluate_boolean_at_index_on_faces(index=0, value_bool=False):
        """The Evaluate at Index node allows accessing data of other elements in the context geometry. It is similar to the Sample Index Node. The main difference is that this node does not require a geometry input, because the geometry from the field context is used.
        #### Path
        - Utilities > Field > Evaluate at Index Node
        #### Outputs:
        - `#4 value_bool: Boolean = False`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeFieldAtIndex.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/field/evaluate_at_index.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeFieldAtIndex.html)
        """
        node = new_node(*nodes.GeometryNodeFieldAtIndex("BOOLEAN", "FACE", index, value_bool=value_bool))
        return node.outputs[4].Boolean

    @staticmethod
    def evaluate_boolean_at_index_on_corners(index=0, value_bool=False):
        """The Evaluate at Index node allows accessing data of other elements in the context geometry. It is similar to the Sample Index Node. The main difference is that this node does not require a geometry input, because the geometry from the field context is used.
        #### Path
        - Utilities > Field > Evaluate at Index Node
        #### Outputs:
        - `#4 value_bool: Boolean = False`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeFieldAtIndex.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/field/evaluate_at_index.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeFieldAtIndex.html)
        """
        node = new_node(*nodes.GeometryNodeFieldAtIndex("BOOLEAN", "CORNER", index, value_bool=value_bool))
        return node.outputs[4].Boolean

    @staticmethod
    def evaluate_boolean_at_index_on_curves(index=0, value_bool=False):
        """The Evaluate at Index node allows accessing data of other elements in the context geometry. It is similar to the Sample Index Node. The main difference is that this node does not require a geometry input, because the geometry from the field context is used.
        #### Path
        - Utilities > Field > Evaluate at Index Node
        #### Outputs:
        - `#4 value_bool: Boolean = False`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeFieldAtIndex.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/field/evaluate_at_index.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeFieldAtIndex.html)
        """
        node = new_node(*nodes.GeometryNodeFieldAtIndex("BOOLEAN", "CURVE", index, value_bool=value_bool))
        return node.outputs[4].Boolean

    @staticmethod
    def evaluate_boolean_at_index_on_instances(index=0, value_bool=False):
        """The Evaluate at Index node allows accessing data of other elements in the context geometry. It is similar to the Sample Index Node. The main difference is that this node does not require a geometry input, because the geometry from the field context is used.
        #### Path
        - Utilities > Field > Evaluate at Index Node
        #### Outputs:
        - `#4 value_bool: Boolean = False`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeFieldAtIndex.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/field/evaluate_at_index.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeFieldAtIndex.html)
        """
        node = new_node(*nodes.GeometryNodeFieldAtIndex("BOOLEAN", "INSTANCE", index, value_bool=value_bool))
        return node.outputs[4].Boolean

    @staticmethod
    def evaluate_float_on_points(value_float=0.0):
        """The Evaluate on Domain allows evaluating a field for a different attribute domain than the domain from the field context. For example, the face index could be used instead of the face corner index, when setting the values of a UV Map
        #### Path
        - Utilities > Field > Evaluate on Domain Node
        #### Outputs:
        - `#0 value_float: Float = 0.0`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeInterpolateDomain.png)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/field/evaluate_on_domain.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeFieldOnDomain.html)
        """
        node = new_node(*nodes.GeometryNodeFieldOnDomain("FLOAT", "POINT", value_float=value_float))
        return node.outputs[0].Float

    @staticmethod
    def evaluate_float_on_edges(value_float=0.0):
        """The Evaluate on Domain allows evaluating a field for a different attribute domain than the domain from the field context. For example, the face index could be used instead of the face corner index, when setting the values of a UV Map
        #### Path
        - Utilities > Field > Evaluate on Domain Node
        #### Outputs:
        - `#0 value_float: Float = 0.0`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeInterpolateDomain.png)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/field/evaluate_on_domain.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeFieldOnDomain.html)
        """
        node = new_node(*nodes.GeometryNodeFieldOnDomain("FLOAT", "EDGE", value_float=value_float))
        return node.outputs[0].Float

    @staticmethod
    def evaluate_float_on_faces(value_float=0.0):
        """The Evaluate on Domain allows evaluating a field for a different attribute domain than the domain from the field context. For example, the face index could be used instead of the face corner index, when setting the values of a UV Map
        #### Path
        - Utilities > Field > Evaluate on Domain Node
        #### Outputs:
        - `#0 value_float: Float = 0.0`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeInterpolateDomain.png)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/field/evaluate_on_domain.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeFieldOnDomain.html)
        """
        node = new_node(*nodes.GeometryNodeFieldOnDomain("FLOAT", "FACE", value_float=value_float))
        return node.outputs[0].Float

    @staticmethod
    def evaluate_float_on_corners(value_float=0.0):
        """The Evaluate on Domain allows evaluating a field for a different attribute domain than the domain from the field context. For example, the face index could be used instead of the face corner index, when setting the values of a UV Map
        #### Path
        - Utilities > Field > Evaluate on Domain Node
        #### Outputs:
        - `#0 value_float: Float = 0.0`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeInterpolateDomain.png)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/field/evaluate_on_domain.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeFieldOnDomain.html)
        """
        node = new_node(*nodes.GeometryNodeFieldOnDomain("FLOAT", "CORNER", value_float=value_float))
        return node.outputs[0].Float

    @staticmethod
    def evaluate_float_on_curves(value_float=0.0):
        """The Evaluate on Domain allows evaluating a field for a different attribute domain than the domain from the field context. For example, the face index could be used instead of the face corner index, when setting the values of a UV Map
        #### Path
        - Utilities > Field > Evaluate on Domain Node
        #### Outputs:
        - `#0 value_float: Float = 0.0`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeInterpolateDomain.png)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/field/evaluate_on_domain.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeFieldOnDomain.html)
        """
        node = new_node(*nodes.GeometryNodeFieldOnDomain("FLOAT", "CURVE", value_float=value_float))
        return node.outputs[0].Float

    @staticmethod
    def evaluate_float_on_instances(value_float=0.0):
        """The Evaluate on Domain allows evaluating a field for a different attribute domain than the domain from the field context. For example, the face index could be used instead of the face corner index, when setting the values of a UV Map
        #### Path
        - Utilities > Field > Evaluate on Domain Node
        #### Outputs:
        - `#0 value_float: Float = 0.0`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeInterpolateDomain.png)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/field/evaluate_on_domain.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeFieldOnDomain.html)
        """
        node = new_node(*nodes.GeometryNodeFieldOnDomain("FLOAT", "INSTANCE", value_float=value_float))
        return node.outputs[0].Float

    @staticmethod
    def evaluate_integer_on_points(value_int=0):
        """The Evaluate on Domain allows evaluating a field for a different attribute domain than the domain from the field context. For example, the face index could be used instead of the face corner index, when setting the values of a UV Map
        #### Path
        - Utilities > Field > Evaluate on Domain Node
        #### Outputs:
        - `#1 value_int: Integer = 0`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeInterpolateDomain.png)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/field/evaluate_on_domain.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeFieldOnDomain.html)
        """
        node = new_node(*nodes.GeometryNodeFieldOnDomain("INT", "POINT", value_int=value_int))
        return node.outputs[1].Integer

    @staticmethod
    def evaluate_integer_on_edges(value_int=0):
        """The Evaluate on Domain allows evaluating a field for a different attribute domain than the domain from the field context. For example, the face index could be used instead of the face corner index, when setting the values of a UV Map
        #### Path
        - Utilities > Field > Evaluate on Domain Node
        #### Outputs:
        - `#1 value_int: Integer = 0`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeInterpolateDomain.png)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/field/evaluate_on_domain.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeFieldOnDomain.html)
        """
        node = new_node(*nodes.GeometryNodeFieldOnDomain("INT", "EDGE", value_int=value_int))
        return node.outputs[1].Integer

    @staticmethod
    def evaluate_integer_on_faces(value_int=0):
        """The Evaluate on Domain allows evaluating a field for a different attribute domain than the domain from the field context. For example, the face index could be used instead of the face corner index, when setting the values of a UV Map
        #### Path
        - Utilities > Field > Evaluate on Domain Node
        #### Outputs:
        - `#1 value_int: Integer = 0`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeInterpolateDomain.png)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/field/evaluate_on_domain.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeFieldOnDomain.html)
        """
        node = new_node(*nodes.GeometryNodeFieldOnDomain("INT", "FACE", value_int=value_int))
        return node.outputs[1].Integer

    @staticmethod
    def evaluate_integer_on_corners(value_int=0):
        """The Evaluate on Domain allows evaluating a field for a different attribute domain than the domain from the field context. For example, the face index could be used instead of the face corner index, when setting the values of a UV Map
        #### Path
        - Utilities > Field > Evaluate on Domain Node
        #### Outputs:
        - `#1 value_int: Integer = 0`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeInterpolateDomain.png)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/field/evaluate_on_domain.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeFieldOnDomain.html)
        """
        node = new_node(*nodes.GeometryNodeFieldOnDomain("INT", "CORNER", value_int=value_int))
        return node.outputs[1].Integer

    @staticmethod
    def evaluate_integer_on_curves(value_int=0):
        """The Evaluate on Domain allows evaluating a field for a different attribute domain than the domain from the field context. For example, the face index could be used instead of the face corner index, when setting the values of a UV Map
        #### Path
        - Utilities > Field > Evaluate on Domain Node
        #### Outputs:
        - `#1 value_int: Integer = 0`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeInterpolateDomain.png)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/field/evaluate_on_domain.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeFieldOnDomain.html)
        """
        node = new_node(*nodes.GeometryNodeFieldOnDomain("INT", "CURVE", value_int=value_int))
        return node.outputs[1].Integer

    @staticmethod
    def evaluate_integer_on_instances(value_int=0):
        """The Evaluate on Domain allows evaluating a field for a different attribute domain than the domain from the field context. For example, the face index could be used instead of the face corner index, when setting the values of a UV Map
        #### Path
        - Utilities > Field > Evaluate on Domain Node
        #### Outputs:
        - `#1 value_int: Integer = 0`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeInterpolateDomain.png)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/field/evaluate_on_domain.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeFieldOnDomain.html)
        """
        node = new_node(*nodes.GeometryNodeFieldOnDomain("INT", "INSTANCE", value_int=value_int))
        return node.outputs[1].Integer

    @staticmethod
    def evaluate_vector_on_points(value_vector=(0.0, 0.0, 0.0)):
        """The Evaluate on Domain allows evaluating a field for a different attribute domain than the domain from the field context. For example, the face index could be used instead of the face corner index, when setting the values of a UV Map
        #### Path
        - Utilities > Field > Evaluate on Domain Node
        #### Outputs:
        - `#2 value_vector: Vector = (0.0, 0.0, 0.0)`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeInterpolateDomain.png)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/field/evaluate_on_domain.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeFieldOnDomain.html)
        """
        node = new_node(*nodes.GeometryNodeFieldOnDomain("FLOAT_VECTOR", "POINT", value_vector=value_vector))
        return node.outputs[2].Vector

    @staticmethod
    def evaluate_vector_on_edges(value_vector=(0.0, 0.0, 0.0)):
        """The Evaluate on Domain allows evaluating a field for a different attribute domain than the domain from the field context. For example, the face index could be used instead of the face corner index, when setting the values of a UV Map
        #### Path
        - Utilities > Field > Evaluate on Domain Node
        #### Outputs:
        - `#2 value_vector: Vector = (0.0, 0.0, 0.0)`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeInterpolateDomain.png)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/field/evaluate_on_domain.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeFieldOnDomain.html)
        """
        node = new_node(*nodes.GeometryNodeFieldOnDomain("FLOAT_VECTOR", "EDGE", value_vector=value_vector))
        return node.outputs[2].Vector

    @staticmethod
    def evaluate_vector_on_faces(value_vector=(0.0, 0.0, 0.0)):
        """The Evaluate on Domain allows evaluating a field for a different attribute domain than the domain from the field context. For example, the face index could be used instead of the face corner index, when setting the values of a UV Map
        #### Path
        - Utilities > Field > Evaluate on Domain Node
        #### Outputs:
        - `#2 value_vector: Vector = (0.0, 0.0, 0.0)`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeInterpolateDomain.png)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/field/evaluate_on_domain.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeFieldOnDomain.html)
        """
        node = new_node(*nodes.GeometryNodeFieldOnDomain("FLOAT_VECTOR", "FACE", value_vector=value_vector))
        return node.outputs[2].Vector

    @staticmethod
    def evaluate_vector_on_corners(value_vector=(0.0, 0.0, 0.0)):
        """The Evaluate on Domain allows evaluating a field for a different attribute domain than the domain from the field context. For example, the face index could be used instead of the face corner index, when setting the values of a UV Map
        #### Path
        - Utilities > Field > Evaluate on Domain Node
        #### Outputs:
        - `#2 value_vector: Vector = (0.0, 0.0, 0.0)`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeInterpolateDomain.png)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/field/evaluate_on_domain.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeFieldOnDomain.html)
        """
        node = new_node(*nodes.GeometryNodeFieldOnDomain("FLOAT_VECTOR", "CORNER", value_vector=value_vector))
        return node.outputs[2].Vector

    @staticmethod
    def evaluate_vector_on_curves(value_vector=(0.0, 0.0, 0.0)):
        """The Evaluate on Domain allows evaluating a field for a different attribute domain than the domain from the field context. For example, the face index could be used instead of the face corner index, when setting the values of a UV Map
        #### Path
        - Utilities > Field > Evaluate on Domain Node
        #### Outputs:
        - `#2 value_vector: Vector = (0.0, 0.0, 0.0)`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeInterpolateDomain.png)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/field/evaluate_on_domain.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeFieldOnDomain.html)
        """
        node = new_node(*nodes.GeometryNodeFieldOnDomain("FLOAT_VECTOR", "CURVE", value_vector=value_vector))
        return node.outputs[2].Vector

    @staticmethod
    def evaluate_vector_on_instances(value_vector=(0.0, 0.0, 0.0)):
        """The Evaluate on Domain allows evaluating a field for a different attribute domain than the domain from the field context. For example, the face index could be used instead of the face corner index, when setting the values of a UV Map
        #### Path
        - Utilities > Field > Evaluate on Domain Node
        #### Outputs:
        - `#2 value_vector: Vector = (0.0, 0.0, 0.0)`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeInterpolateDomain.png)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/field/evaluate_on_domain.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeFieldOnDomain.html)
        """
        node = new_node(*nodes.GeometryNodeFieldOnDomain("FLOAT_VECTOR", "INSTANCE", value_vector=value_vector))
        return node.outputs[2].Vector

    @staticmethod
    def evaluate_color_on_points(value_color=(0.0, 0.0, 0.0, 0.0)):
        """The Evaluate on Domain allows evaluating a field for a different attribute domain than the domain from the field context. For example, the face index could be used instead of the face corner index, when setting the values of a UV Map
        #### Path
        - Utilities > Field > Evaluate on Domain Node
        #### Outputs:
        - `#3 value_color: Color = (0.0, 0.0, 0.0, 0.0)`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeInterpolateDomain.png)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/field/evaluate_on_domain.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeFieldOnDomain.html)
        """
        node = new_node(*nodes.GeometryNodeFieldOnDomain("FLOAT_COLOR", "POINT", value_color=value_color))
        return node.outputs[3].Color

    @staticmethod
    def evaluate_color_on_edges(value_color=(0.0, 0.0, 0.0, 0.0)):
        """The Evaluate on Domain allows evaluating a field for a different attribute domain than the domain from the field context. For example, the face index could be used instead of the face corner index, when setting the values of a UV Map
        #### Path
        - Utilities > Field > Evaluate on Domain Node
        #### Outputs:
        - `#3 value_color: Color = (0.0, 0.0, 0.0, 0.0)`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeInterpolateDomain.png)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/field/evaluate_on_domain.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeFieldOnDomain.html)
        """
        node = new_node(*nodes.GeometryNodeFieldOnDomain("FLOAT_COLOR", "EDGE", value_color=value_color))
        return node.outputs[3].Color

    @staticmethod
    def evaluate_color_on_faces(value_color=(0.0, 0.0, 0.0, 0.0)):
        """The Evaluate on Domain allows evaluating a field for a different attribute domain than the domain from the field context. For example, the face index could be used instead of the face corner index, when setting the values of a UV Map
        #### Path
        - Utilities > Field > Evaluate on Domain Node
        #### Outputs:
        - `#3 value_color: Color = (0.0, 0.0, 0.0, 0.0)`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeInterpolateDomain.png)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/field/evaluate_on_domain.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeFieldOnDomain.html)
        """
        node = new_node(*nodes.GeometryNodeFieldOnDomain("FLOAT_COLOR", "FACE", value_color=value_color))
        return node.outputs[3].Color

    @staticmethod
    def evaluate_color_on_corners(value_color=(0.0, 0.0, 0.0, 0.0)):
        """The Evaluate on Domain allows evaluating a field for a different attribute domain than the domain from the field context. For example, the face index could be used instead of the face corner index, when setting the values of a UV Map
        #### Path
        - Utilities > Field > Evaluate on Domain Node
        #### Outputs:
        - `#3 value_color: Color = (0.0, 0.0, 0.0, 0.0)`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeInterpolateDomain.png)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/field/evaluate_on_domain.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeFieldOnDomain.html)
        """
        node = new_node(*nodes.GeometryNodeFieldOnDomain("FLOAT_COLOR", "CORNER", value_color=value_color))
        return node.outputs[3].Color

    @staticmethod
    def evaluate_color_on_curves(value_color=(0.0, 0.0, 0.0, 0.0)):
        """The Evaluate on Domain allows evaluating a field for a different attribute domain than the domain from the field context. For example, the face index could be used instead of the face corner index, when setting the values of a UV Map
        #### Path
        - Utilities > Field > Evaluate on Domain Node
        #### Outputs:
        - `#3 value_color: Color = (0.0, 0.0, 0.0, 0.0)`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeInterpolateDomain.png)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/field/evaluate_on_domain.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeFieldOnDomain.html)
        """
        node = new_node(*nodes.GeometryNodeFieldOnDomain("FLOAT_COLOR", "CURVE", value_color=value_color))
        return node.outputs[3].Color

    @staticmethod
    def evaluate_color_on_instances(value_color=(0.0, 0.0, 0.0, 0.0)):
        """The Evaluate on Domain allows evaluating a field for a different attribute domain than the domain from the field context. For example, the face index could be used instead of the face corner index, when setting the values of a UV Map
        #### Path
        - Utilities > Field > Evaluate on Domain Node
        #### Outputs:
        - `#3 value_color: Color = (0.0, 0.0, 0.0, 0.0)`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeInterpolateDomain.png)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/field/evaluate_on_domain.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeFieldOnDomain.html)
        """
        node = new_node(*nodes.GeometryNodeFieldOnDomain("FLOAT_COLOR", "INSTANCE", value_color=value_color))
        return node.outputs[3].Color

    @staticmethod
    def evaluate_boolean_on_points(value_bool=False):
        """The Evaluate on Domain allows evaluating a field for a different attribute domain than the domain from the field context. For example, the face index could be used instead of the face corner index, when setting the values of a UV Map
        #### Path
        - Utilities > Field > Evaluate on Domain Node
        #### Outputs:
        - `#4 value_bool: Boolean = False`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeInterpolateDomain.png)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/field/evaluate_on_domain.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeFieldOnDomain.html)
        """
        node = new_node(*nodes.GeometryNodeFieldOnDomain("BOOLEAN", "POINT", value_bool=value_bool))
        return node.outputs[4].Boolean

    @staticmethod
    def evaluate_boolean_on_edges(value_bool=False):
        """The Evaluate on Domain allows evaluating a field for a different attribute domain than the domain from the field context. For example, the face index could be used instead of the face corner index, when setting the values of a UV Map
        #### Path
        - Utilities > Field > Evaluate on Domain Node
        #### Outputs:
        - `#4 value_bool: Boolean = False`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeInterpolateDomain.png)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/field/evaluate_on_domain.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeFieldOnDomain.html)
        """
        node = new_node(*nodes.GeometryNodeFieldOnDomain("BOOLEAN", "EDGE", value_bool=value_bool))
        return node.outputs[4].Boolean

    @staticmethod
    def evaluate_boolean_on_faces(value_bool=False):
        """The Evaluate on Domain allows evaluating a field for a different attribute domain than the domain from the field context. For example, the face index could be used instead of the face corner index, when setting the values of a UV Map
        #### Path
        - Utilities > Field > Evaluate on Domain Node
        #### Outputs:
        - `#4 value_bool: Boolean = False`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeInterpolateDomain.png)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/field/evaluate_on_domain.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeFieldOnDomain.html)
        """
        node = new_node(*nodes.GeometryNodeFieldOnDomain("BOOLEAN", "FACE", value_bool=value_bool))
        return node.outputs[4].Boolean

    @staticmethod
    def evaluate_boolean_on_corners(value_bool=False):
        """The Evaluate on Domain allows evaluating a field for a different attribute domain than the domain from the field context. For example, the face index could be used instead of the face corner index, when setting the values of a UV Map
        #### Path
        - Utilities > Field > Evaluate on Domain Node
        #### Outputs:
        - `#4 value_bool: Boolean = False`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeInterpolateDomain.png)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/field/evaluate_on_domain.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeFieldOnDomain.html)
        """
        node = new_node(*nodes.GeometryNodeFieldOnDomain("BOOLEAN", "CORNER", value_bool=value_bool))
        return node.outputs[4].Boolean

    @staticmethod
    def evaluate_boolean_on_curves(value_bool=False):
        """The Evaluate on Domain allows evaluating a field for a different attribute domain than the domain from the field context. For example, the face index could be used instead of the face corner index, when setting the values of a UV Map
        #### Path
        - Utilities > Field > Evaluate on Domain Node
        #### Outputs:
        - `#4 value_bool: Boolean = False`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeInterpolateDomain.png)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/field/evaluate_on_domain.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeFieldOnDomain.html)
        """
        node = new_node(*nodes.GeometryNodeFieldOnDomain("BOOLEAN", "CURVE", value_bool=value_bool))
        return node.outputs[4].Boolean

    @staticmethod
    def evaluate_boolean_on_instances(value_bool=False):
        """The Evaluate on Domain allows evaluating a field for a different attribute domain than the domain from the field context. For example, the face index could be used instead of the face corner index, when setting the values of a UV Map
        #### Path
        - Utilities > Field > Evaluate on Domain Node
        #### Outputs:
        - `#4 value_bool: Boolean = False`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeInterpolateDomain.png)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/field/evaluate_on_domain.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeFieldOnDomain.html)
        """
        node = new_node(*nodes.GeometryNodeFieldOnDomain("BOOLEAN", "INSTANCE", value_bool=value_bool))
        return node.outputs[4].Boolean

    def realize_instances(self, legacy_behavior=False):
        """The Realize Instances node makes any instances (efficient duplicates of the same geometry) into real geometry data. This makes it possible to affect each instance individually, whereas without this node, the exact same changes are applied to every instance of the same geometry. However, performance can become much worse when the input contains many instances of complex geometry, which is a fundamental limitation when procedurally processing geometry.
        - In-Place Operation
        #### Path
        - Instances > Realize Instances Node
        #### Outputs:
        - `#0 geometry: Geometry = None`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeRealizeInstances.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/realize_instances.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeRealizeInstances.html)
        """
        node = new_node(*nodes.GeometryNodeRealizeInstances(legacy_behavior, self))
        self.bsocket = node.outputs[0].bsocket
        return self


class Curve(Geometry):
    def __init__(self, bsocket: bpy.types.NodeSocket) -> None:
        super().__init__(bsocket)
        self._parameter = None
        self._tangent = None
        self._tilt = None

    @property
    def domain_size(self):
        """The Domain Size outputs the size of an attribute domain on the selected geometry type, for example, the number of edges in a mesh, or the number of points in a point cloud.
        #### Path
        - Attribute > Domain Size Node
        #### Outputs:
        - `#0 point_count: Integer = 0`
        - `#4 spline_count: Integer = 0`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeAttributeDomainSize.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/domain_size.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeDomainSize.html)
        """
        node = new_node(*nodes.GeometryNodeAttributeDomainSize("CURVE", self))
        ret = typing.NamedTuple("GeometryNodeAttributeDomainSize", [("point_count", Integer), ("spline_count", Integer)])
        return ret(node.outputs[0].Integer, node.outputs[4].Integer)

    @staticmethod
    def handle_positions(relative=False):
        """The Curve Handle Position node outputs the position of each of a Bézier spline's handles. If the curve does not contain Bézier splines, the node will output zero.
        #### Path
        - Curve > Read > Curve Handle Position Node
        #### Outputs:
        - `#0 left: Vector = (0.0, 0.0, 0.0)`
        - `#1 right: Vector = (0.0, 0.0, 0.0)`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeInputCurveHandlePositions.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/read/curve_handle_position.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputCurveHandlePositions.html)
        """
        node = new_node(*nodes.GeometryNodeInputCurveHandlePositions(relative))
        ret = typing.NamedTuple("HandlePositions", [("left", Vector), ("right", Vector)])
        return ret(node.outputs[0].Vector, node.outputs[1].Vector)

    @property
    def curve_length(self):
        """The Curve Length node outputs the length of all splines added together.
        #### Path
        - Curve > Read > Curve Length Node
        #### Outputs:
        - `#0 length: Float = 0.0`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeCurveLength.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/read/curve_length.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveLength.html)
        """
        node = new_node(*nodes.GeometryNodeCurveLength(self))
        return node.outputs[0].Float

    @property
    def spline_length(self):
        """The Spline Length node outputs the total length of each spline, as a distance, or a number of points. This is different than the Curve Length node, which adds up the total length for all of the curve’s splines.
        #### Path
        - Curve > Read > Spline Length Node
        #### Outputs:
        - `#0 length: Float = 0.0`
        - `#1 point_count: Integer = 0`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeSplineLength.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/read/spline_length.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeSplineLength.html)
        """
        node = new_node(*nodes.GeometryNodeSplineLength())
        ret = typing.NamedTuple("GeometryNodeSplineLength", [("length", Float), ("point_count", Integer)])
        return ret(node.outputs[0].Float, node.outputs[1].Integer)

    @property
    def tangent(self):
        """The Curve Tangent node outputs the direction that a curve points in at each control point, depending on the direction of the curve (which can be controlled with the Reverse Curve Node). The output values are normalized vectors.
        #### Path
        - Curve > Read > Curve Tangent Node
        #### Outputs:
        - `#0 tangent: Vector = (0.0, 0.0, 0.0)`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeInputTangent.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/read/curve_tangent.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputTangent.html)
        """
        if self._tangent is None:
            node = new_node(*nodes.GeometryNodeInputTangent())
            self._tangent = node.outputs[0].Vector
        return self._tangent

    @property
    def tilt(self):
        """The Curve Tilt node outputs the angle used to turn the curve normal around the direction of the curve tangent in its evaluated points. Keep in mind that the output is per control point, just like the values that can be controlled in curve Edit Mode. For NURBS and Bézier splines, the values will be interpolated to the final evaluated points.
        #### Path
        - Curve > Read > Curve Tilt Node
        #### Outputs:
        - `#0 tilt: Float = 0.0`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeInputCurveTilt.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/read/curve_tilt.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputCurveTilt.html)
        """
        if self._tilt is None:
            node = new_node(*nodes.GeometryNodeInputCurveTilt())
            self._tilt = node.outputs[0].Float
        return self._tilt

    @staticmethod
    def endpoint_selection(start_size=1, end_size=1):
        """The Endpoint Selection node provides a selection for an arbitrary number of endpoints in each spline in a curve.
        #### Path
        - Curve > Read > Endpoint Selection Node
        #### Outputs:
        - `#0 selection: Boolean = False`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeCurveEndpointSelection.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/read/endpoint_selection.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveEndpointSelection.html)
        """
        node = new_node(*nodes.GeometryNodeCurveEndpointSelection(start_size, end_size))
        return node.outputs[0].Boolean

    @staticmethod
    def handle_type_selection(handle_type='AUTO', mode: set = {'LEFT', 'RIGHT'}):
        """Creates a selection based on the handle types of the control points.
        #### Path
        - Curve > Read > Handle Type Selection Node
        #### Properties
        - `handle_type`: `AUTO`, `FREE`, `VECTOR`, `ALIGN`
        #### Outputs:
        - `#0 selection: Boolean = False`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeCurveHandleTypeSelection.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/read/handle_type_selection.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveHandleTypeSelection.html)
        """
        node = new_node(*nodes.GeometryNodeCurveHandleTypeSelection(handle_type, mode))
        return node.outputs[0].Boolean

    @property
    def is_cyclic(self):
        """The Is Spline Cyclic controls whether each of the curve splines start and endpoints form a connection. Its output corresponds to the built-in cyclic attribute on the curve spline domain.
        #### Path
        - Curve > Read > Is Spline Cyclic Node
        #### Outputs:
        - `#0 cyclic: Boolean = False`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeInputSplineCyclic.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/read/is_spline_cyclic.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputSplineCyclic.html)
        """
        node = new_node(*nodes.GeometryNodeInputSplineCyclic())
        return node.outputs[0].Boolean

    @property
    def parameter(self):
        """The Spline Parameter node outputs how far along each spline a control point is. The Factor output is different from dividing the index by the total number of control points, because the control points might not be equally spaced along the curve.
        #### Path
        - Curve > Read > Spline Parameter Node
        #### Outputs:
        - `#0 factor: Float = 0.0`
        - `#1 length: Float = 0.0`
        - `#2 index: Integer = 0`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeSplineParameter.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/read/spline_parameter.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeSplineParameter.html)
        """
        if self._parameter is None:
            node = new_node(*nodes.GeometryNodeSplineParameter())
            ret = typing.NamedTuple("GeometryNodeSplineParameter", [("factor", Float), ("length", Float), ("index", Integer)])
            self._parameter = ret(node.outputs[0].Float, node.outputs[1].Float, node.outputs[2].Integer)
        return self._parameter

    @property
    def resolution(self):
        """The Spline Resolution outputs the number of evaluated curve points that will be generated for every control point on the spline. This node works for NURBS and Bézier splines, for poly splines, there is a one-to-one correspondence between original points and evaluated points, so the resolution value will be 1.
        #### Path
        - Curve > Read > Spline Resolution Node
        #### Outputs:
        - `#0 resolution: Integer = 0`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeInputSplineResolution.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/read/spline_resolution.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputSplineResolution.html)
        """
        node = new_node(*nodes.GeometryNodeInputSplineResolution())
        return node.outputs[0].Integer

    def sample_curve(self, data_type='FLOAT', mode='FACTOR', use_all_curves=False, value_float=0.0, value_int=0, value_vector=(0.0, 0.0, 0.0), value_color=(0.0, 0.0, 0.0, 0.0), value_bool=False, factor=0.0, length=0.0, curve_index=0):
        """The Sample Curve calculates a point on a curve at a certain distance from the start of the curve, specified by the length or factor inputs. It also outputs data retrieved from that position on the curve. The sampled values are linearly interpolated from the values at the evaluated curve points at each side of the sampled point.
        #### Path
        - Curve > Sample > Sample Curve Node
        #### Properties
        - `data_type`: `FLOAT`, `INT`, `FLOAT_VECTOR`, `FLOAT_COLOR`, `BOOLEAN`
        - `mode`: `FACTOR`, `LENGTH`
        #### Outputs:
        - `#0 value_float: Float = 0.0`
        - `#1 value_int: Integer = 0`
        - `#2 value_vector: Vector = (0.0, 0.0, 0.0)`
        - `#3 value_color: Color = (0.0, 0.0, 0.0, 0.0)`
        - `#4 value_bool: Boolean = False`
        - `#5 position: Vector = (0.0, 0.0, 0.0)`
        - `#6 tangent: Vector = (0.0, 0.0, 0.0)`
        - `#7 normal: Vector = (0.0, 0.0, 0.0)`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeSampleCurve.png)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/sample/sample_curve.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeSampleCurve.html)
        """
        node = new_node(*nodes.GeometryNodeSampleCurve(data_type, mode, use_all_curves, self, value_float, value_int, value_vector, value_color, value_bool, factor, length, curve_index))
        return node.outputs[0].Float, node.outputs[1].Integer, node.outputs[2].Vector, node.outputs[3].Color, node.outputs[4].Boolean, node.outputs[5].Vector, node.outputs[6].Vector, node.outputs[7].Vector

    def sample_float(self, mode='FACTOR', use_all_curves=False, value_float=0.0, factor=0.0, length=0.0, curve_index=0):
        """The Sample Curve calculates a point on a curve at a certain distance from the start of the curve, specified by the length or factor inputs. It also outputs data retrieved from that position on the curve. The sampled values are linearly interpolated from the values at the evaluated curve points at each side of the sampled point.
        #### Path
        - Curve > Sample > Sample Curve Node
        #### Properties
        - `mode`: `FACTOR`, `LENGTH`
        #### Outputs:
        - `#0 value_float: Float = 0.0`
        - `#5 position: Vector = (0.0, 0.0, 0.0)`
        - `#6 tangent: Vector = (0.0, 0.0, 0.0)`
        - `#7 normal: Vector = (0.0, 0.0, 0.0)`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeSampleCurve.png)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/sample/sample_curve.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeSampleCurve.html)
        """
        node = new_node(*nodes.GeometryNodeSampleCurve("FLOAT", mode, use_all_curves, self, value_float, 0, (0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), False, factor, length, curve_index))
        ret = typing.NamedTuple("GeometryNodeSampleCurve", [("value", Float), ("position", Vector), ("tangent", Vector), ("normal", Vector)])
        return ret(node.outputs[0].Float, node.outputs[5].Vector, node.outputs[6].Vector, node.outputs[7].Vector)

    def sample_integer(self, mode='FACTOR', use_all_curves=False, value_int=0, factor=0.0, length=0.0, curve_index=0):
        """The Sample Curve calculates a point on a curve at a certain distance from the start of the curve, specified by the length or factor inputs. It also outputs data retrieved from that position on the curve. The sampled values are linearly interpolated from the values at the evaluated curve points at each side of the sampled point.
        #### Path
        - Curve > Sample > Sample Curve Node
        #### Properties
        - `mode`: `FACTOR`, `LENGTH`
        #### Outputs:
        - `#1 value_int: Integer = 0`
        - `#5 position: Vector = (0.0, 0.0, 0.0)`
        - `#6 tangent: Vector = (0.0, 0.0, 0.0)`
        - `#7 normal: Vector = (0.0, 0.0, 0.0)`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeSampleCurve.png)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/sample/sample_curve.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeSampleCurve.html)
        """
        node = new_node(*nodes.GeometryNodeSampleCurve("INT", mode, use_all_curves, self, 0.0, value_int, (0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), False, factor, length, curve_index))
        ret = typing.NamedTuple("GeometryNodeSampleCurve", [("value", Integer), ("position", Vector), ("tangent", Vector), ("normal", Vector)])
        return ret(node.outputs[1].Integer, node.outputs[5].Vector, node.outputs[6].Vector, node.outputs[7].Vector)

    def sample_vector(self, mode='FACTOR', use_all_curves=False, value_vector=(0.0, 0.0, 0.0), factor=0.0, length=0.0, curve_index=0):
        """The Sample Curve calculates a point on a curve at a certain distance from the start of the curve, specified by the length or factor inputs. It also outputs data retrieved from that position on the curve. The sampled values are linearly interpolated from the values at the evaluated curve points at each side of the sampled point.
        #### Path
        - Curve > Sample > Sample Curve Node
        #### Properties
        - `mode`: `FACTOR`, `LENGTH`
        #### Outputs:
        - `#2 value_vector: Vector = (0.0, 0.0, 0.0)`
        - `#5 position: Vector = (0.0, 0.0, 0.0)`
        - `#6 tangent: Vector = (0.0, 0.0, 0.0)`
        - `#7 normal: Vector = (0.0, 0.0, 0.0)`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeSampleCurve.png)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/sample/sample_curve.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeSampleCurve.html)
        """
        node = new_node(*nodes.GeometryNodeSampleCurve("FLOAT_VECTOR", mode, use_all_curves, self, 0.0, 0, value_vector, (0.0, 0.0, 0.0, 0.0), False, factor, length, curve_index))
        ret = typing.NamedTuple("GeometryNodeSampleCurve", [("value", Vector), ("position", Vector), ("tangent", Vector), ("normal", Vector)])
        return ret(node.outputs[2].Vector, node.outputs[5].Vector, node.outputs[6].Vector, node.outputs[7].Vector)

    def sample_color(self, mode='FACTOR', use_all_curves=False, value_color=(0.0, 0.0, 0.0, 0.0), factor=0.0, length=0.0, curve_index=0):
        """The Sample Curve calculates a point on a curve at a certain distance from the start of the curve, specified by the length or factor inputs. It also outputs data retrieved from that position on the curve. The sampled values are linearly interpolated from the values at the evaluated curve points at each side of the sampled point.
        #### Path
        - Curve > Sample > Sample Curve Node
        #### Properties
        - `mode`: `FACTOR`, `LENGTH`
        #### Outputs:
        - `#3 value_color: Color = (0.0, 0.0, 0.0, 0.0)`
        - `#5 position: Vector = (0.0, 0.0, 0.0)`
        - `#6 tangent: Vector = (0.0, 0.0, 0.0)`
        - `#7 normal: Vector = (0.0, 0.0, 0.0)`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeSampleCurve.png)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/sample/sample_curve.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeSampleCurve.html)
        """
        node = new_node(*nodes.GeometryNodeSampleCurve("FLOAT_COLOR", mode, use_all_curves, self, 0.0, 0, (0.0, 0.0, 0.0), value_color, False, factor, length, curve_index))
        ret = typing.NamedTuple("GeometryNodeSampleCurve", [("value", Color), ("position", Vector), ("tangent", Vector), ("normal", Vector)])
        return ret(node.outputs[3].Color, node.outputs[5].Vector, node.outputs[6].Vector, node.outputs[7].Vector)

    def sample_boolean(self, mode='FACTOR', use_all_curves=False, value_bool=False, factor=0.0, length=0.0, curve_index=0):
        """The Sample Curve calculates a point on a curve at a certain distance from the start of the curve, specified by the length or factor inputs. It also outputs data retrieved from that position on the curve. The sampled values are linearly interpolated from the values at the evaluated curve points at each side of the sampled point.
        #### Path
        - Curve > Sample > Sample Curve Node
        #### Properties
        - `mode`: `FACTOR`, `LENGTH`
        #### Outputs:
        - `#4 value_bool: Boolean = False`
        - `#5 position: Vector = (0.0, 0.0, 0.0)`
        - `#6 tangent: Vector = (0.0, 0.0, 0.0)`
        - `#7 normal: Vector = (0.0, 0.0, 0.0)`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeSampleCurve.png)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/sample/sample_curve.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeSampleCurve.html)
        """
        node = new_node(*nodes.GeometryNodeSampleCurve("BOOLEAN", mode, use_all_curves, self, 0.0, 0, (0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), value_bool, factor, length, curve_index))
        ret = typing.NamedTuple("GeometryNodeSampleCurve", [("value", Boolean), ("position", Vector), ("tangent", Vector), ("normal", Vector)])
        return ret(node.outputs[4].Boolean, node.outputs[5].Vector, node.outputs[6].Vector, node.outputs[7].Vector)

    def set_normal(self, mode='MINIMUM_TWIST', selection=True):
        """The Set Curve Normal controls the method used to calculate curve normals for every curve.
        - In-Place Operation
        #### Path
        - Curve > Write > Set Curve Normal Node
        #### Properties
        - `mode`: `MINIMUM_TWIST`, `Z_UP`
        #### Outputs:
        - `#0 curve: Geometry = None`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeSetCurveNormal.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/write/set_curve_normal.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetCurveNormal.html)
        """
        selection = selection if self._selection is None else self.selection
        node = new_node(*nodes.GeometryNodeSetCurveNormal(mode, self, selection))
        self.bsocket = node.outputs[0].bsocket
        return self

    def set_radius(self, radius=0.005, selection=True):
        """The Set Curve Radius controls the radius of the curve, used for operations like the size of the profile in the Curve to Mesh node. The value is set for every control point, and is then interpolated to each evaluated point in between the control points.
        - In-Place Operation
        #### Path
        - Curve > Write > Set Curve Radius Node
        #### Outputs:
        - `#0 curve: Geometry = None`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeSetCurveRadius.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/write/set_curve_radius.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetCurveRadius.html)
        """
        selection = selection if self._selection is None else self.selection
        node = new_node(*nodes.GeometryNodeSetCurveRadius(self, selection, radius))
        self.bsocket = node.outputs[0].bsocket
        return self

    def set_tilt(self, tilt=math.radians(0.0), selection=True):
        """The Set Curve Tilt controls the tilt angle at each curve control point. That angle rotates normal vector which is generated at each point when evaluating the curve. The normal then can be retrieved with the Normal Node.
        - In-Place Operation
        #### Path
        - Curve > Write > Set Curve Tilt Node
        #### Outputs:
        - `#0 curve: Geometry = None`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeSetCurveTilt.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/write/set_curve_tilt.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetCurveTilt.html)
        """
        selection = selection if self._selection is None else self.selection
        node = new_node(*nodes.GeometryNodeSetCurveTilt(self, selection, tilt))
        self.bsocket = node.outputs[0].bsocket
        return self

    def set_handle_positions(self, mode='LEFT', position: "Vector" = None, offset=(0.0, 0.0, 0.0), selection=True):
        """The Set Handle Positions node sets the positions for the handles of Bézier curves. They can be used to alter the generated shape of the curve. The input node for this data is the Curve Handle Position Node. See the Bézier curves page for more details.
        - In-Place Operation
        #### Path
        - Curve > Write > Set Handle Positions Node
        #### Properties
        - `mode`: `LEFT`, `RIGHT`
        #### Outputs:
        - `#0 curve: Geometry = None`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeSetCurveHandlePositions.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/write/set_handle_positions.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetCurveHandlePositions.html)
        """
        selection = selection if self._selection is None else self.selection
        node = new_node(*nodes.GeometryNodeSetCurveHandlePositions(mode, self, selection, position, offset))
        self.bsocket = node.outputs[0].bsocket
        return self

    def set_handle_type(self, handle_type='AUTO', mode: set = {'LEFT', 'RIGHT'}, selection=True):
        """Sets the handle type for the points on the Bézier curve that are in the selection.
        - In-Place Operation
        #### Path
        - Curve > Write > Set Handle Type Node
        #### Properties
        - `handle_type`: `AUTO`, `FREE`, `VECTOR`, `ALIGN`
        #### Outputs:
        - `#0 curve: Geometry = None`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeCurveSetHandles.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/write/set_handle_type.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveSetHandles.html)
        """
        selection = selection if self._selection is None else self.selection
        node = new_node(*nodes.GeometryNodeCurveSetHandles(handle_type, mode, self, selection))
        self.bsocket = node.outputs[0].bsocket
        return self

    def set_cyclic(self, cyclic=False, selection=True):
        """The Set Spline Cyclic controls whether each spline will loop back on itself. Each spline has the same number of control points whether or not it is set as cyclic. But when displaying in the viewport or for operations with other nodes, a connection will be made between the first and last control points.
        - In-Place Operation
        #### Path
        - Curve > Write > Set Spline Cyclic Node
        #### Outputs:
        - `#0 geometry: Geometry = None`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeSetSplineCyclic.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/write/set_spline_cyclic.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetSplineCyclic.html)
        """
        selection = selection if self._selection is None else self.selection
        node = new_node(*nodes.GeometryNodeSetSplineCyclic(self, selection, cyclic))
        self.bsocket = node.outputs[0].bsocket
        return self

    def set_resolution(self, resolution=12, selection=True):
        """The Set Spline Resolution node sets the value for how many evaluated points should be generated on the curve for every control point. It only has an effect on NURBS and Bézier splines. The evaluated points are displayed in the viewport, used in the Curve to Mesh Node node, and optionally used in the Resample Curve Node.
        - In-Place Operation
        #### Path
        - Curve > Write > Set Spline Resolution Node
        #### Outputs:
        - `#0 geometry: Geometry = None`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeSetSplineResolution.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/write/set_spline_resolution.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetSplineResolution.html)
        """
        selection = selection if self._selection is None else self.selection
        node = new_node(*nodes.GeometryNodeSetSplineResolution(self, selection, resolution))
        self.bsocket = node.outputs[0].bsocket
        return self

    def set_spline_type(self, spline_type='POLY', selection=True):
        """Sets the spline type for the splines in the curve component that are in the selection.
        - In-Place Operation
        #### Path
        - Curve > Write > Set Spline Type Node
        #### Properties
        - `spline_type`: `POLY`, `CATMULL_ROM`, `BEZIER`, `NURBS`
        #### Outputs:
        - `#0 curve: Geometry = None`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeCurveSplineType.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/write/set_spline_type.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveSplineType.html)
        """
        selection = selection if self._selection is None else self.selection
        node = new_node(*nodes.GeometryNodeCurveSplineType(spline_type, self, selection))
        self.bsocket = node.outputs[0].bsocket
        return self

    def to_mesh(self, profile_curve=None, fill_caps=False):
        """The Curve to Mesh node converts all splines of a curve to a mesh. Optionally, a profile curve can be provided to give the curve a custom shape.
        #### Path
        - Curve > Operations > Curve to Mesh Node
        #### Outputs:
        - `#0 mesh: Geometry = None`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeCurveToMesh.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/operations/curve_to_mesh.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveToMesh.html)
        """
        node = new_node(*nodes.GeometryNodeCurveToMesh(self, profile_curve, fill_caps))
        return node.outputs[0].Mesh

    def to_points(self, mode="COUNT", count=10, length=0.1):
        """The Curve to Points node generates a point cloud from a curve.
        #### Path
        - Curve > Operations > Curve to Points Node
        #### Properties
        - `mode`: `COUNT`, `EVALUATED`, `LENGTH`
        #### Outputs:
        - `#0 points: Geometry = None`
        - `#1 tangent: Vector = (0.0, 0.0, 0.0)`
        - `#2 normal: Vector = (0.0, 0.0, 0.0)`
        - `#3 rotation: Vector = (0.0, 0.0, 0.0)`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeCurveToPoints.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/operations/curve_to_points.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveToPoints.html)
        """
        node = new_node(*nodes.GeometryNodeCurveToPoints(mode, self, count, length))
        ret = typing.NamedTuple("GeometryNodeCurveToPoints", [("points", Points), ("tangent", Vector), ("normal", Vector), ("rotation", Vector)])
        return ret(node.outputs[0].Points, node.outputs[1].Vector, node.outputs[2].Vector, node.outputs[3].Vector)

    def deform_on_surface(self):
        """The Deform Curves on Surface node translates and rotates each curve based on the difference in its root position. The root position is defined by UV coordinates stored on each curve and the UV Map selected for the purpose in the Curves surface settings.
        #### Path
        - Curve > Operations > Deform Curves on Surface Node
        #### Outputs:
        - `#0 curves: Geometry = None`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryDeformCurvesOnSurface.png)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/operations/deform_curves_on_surface.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeDeformCurvesOnSurface.html)
        """
        node = new_node(*nodes.GeometryNodeDeformCurvesOnSurface(self))
        return node.outputs[0].Curve

    def fill_curve(self, mode='TRIANGLES'):
        """The Fill Curve node generates a mesh using the constrained Delaunay triangulation algorithm with the curves as boundaries. The mesh is only generated flat with a local Z of 0.
        #### Path
        - Curve > Operations > Fill Curve Node
        #### Properties
        - `mode`: `TRIANGLES`, `NGONS`
        #### Outputs:
        - `#0 mesh: Geometry = None`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeFillCurve.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/operations/fill_curve.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeFillCurve.html)
        """
        node = new_node(*nodes.GeometryNodeFillCurve(mode, self))
        return node.outputs[0].Mesh

    @property
    def filled_mesh(self):
        """The Fill Curve node generates a mesh using the constrained Delaunay triangulation algorithm with the curves as boundaries. The mesh is only generated flat with a local Z of 0.
        #### Path
        - Curve > Operations > Fill Curve Node
        #### Outputs:
        - `#0 mesh: Geometry = None`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeFillCurve.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/operations/fill_curve.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeFillCurve.html)
        """
        node = new_node(*nodes.GeometryNodeFillCurve("TRIANGLES", self))
        return node.outputs[0].Mesh

    @property
    def filled_ngons(self):
        """The Fill Curve node generates a mesh using the constrained Delaunay triangulation algorithm with the curves as boundaries. The mesh is only generated flat with a local Z of 0.
        #### Path
        - Curve > Operations > Fill Curve Node
        #### Outputs:
        - `#0 mesh: Geometry = None`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeFillCurve.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/operations/fill_curve.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeFillCurve.html)
        """
        node = new_node(*nodes.GeometryNodeFillCurve("NGONS", self))
        return node.outputs[0].Mesh

    def fillet_curve(self, mode='BEZIER', count=1, radius=0.25, limit_radius=False):
        """The Fillet Curve rounds corners on curve control points, similar to the effect of the Bevel Modifier on a 2D mesh. However, a key difference is that the rounded portions created by the Fillet Curve node are always portions of a circle.
        #### Path
        - Curve > Operations > Fillet Curve Node
        #### Properties
        - `mode`: `BEZIER`, `POLY`
        #### Outputs:
        - `#0 curve: Geometry = None`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeFilletCurve.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/operations/fillet_curve.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeFilletCurve.html)
        """
        node = new_node(*nodes.GeometryNodeFilletCurve(mode, self, count, radius, limit_radius))
        return node.outputs[0].Curve

    def fillet_bezier(self, radius=0.25, count=1, limit_radius=False):
        """The Fillet Curve rounds corners on curve control points, similar to the effect of the Bevel Modifier on a 2D mesh. However, a key difference is that the rounded portions created by the Fillet Curve node are always portions of a circle.
        #### Path
        - Curve > Operations > Fillet Curve Node
        #### Outputs:
        - `#0 curve: Geometry = None`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeFilletCurve.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/operations/fillet_curve.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeFilletCurve.html)
        """
        node = new_node(*nodes.GeometryNodeFilletCurve("BEZIER", self, count, radius, limit_radius))
        return node.outputs[0].Curve

    def fillet_poly(self, radius=0.25, count=1, limit_radius=False):
        """The Fillet Curve rounds corners on curve control points, similar to the effect of the Bevel Modifier on a 2D mesh. However, a key difference is that the rounded portions created by the Fillet Curve node are always portions of a circle.
        #### Path
        - Curve > Operations > Fillet Curve Node
        #### Outputs:
        - `#0 curve: Geometry = None`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeFilletCurve.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/operations/fillet_curve.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeFilletCurve.html)
        """
        node = new_node(*nodes.GeometryNodeFilletCurve("POLY", self, count, radius, limit_radius))
        return node.outputs[0].Curve

    def interpolate_curves(self, guide_up=(0.0, 0.0, 0.0), guide_group_id=0, points=None, point_up=(0.0, 0.0, 0.0), point_group_id=0, max_neighbors=4):
        """Generate new curves on points by interpolating between existing curves. This is useful to have a smaller set of original curves to make editing easier and faster while still generating high-density curves for the viewport or a final render.
        #### Path
        - Curve > Operations > Interpolate Curves Node
        #### Outputs:
        - `#0 curves: Geometry = None`
        - `#1 closest_index: Integer = 0`
        - `#2 closest_weight: Float = 0.0`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeInterpolateCurves.png)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/operations/interpolate_curves.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeInterpolateCurves.html)
        """
        node = new_node(*nodes.GeometryNodeInterpolateCurves(self, guide_up, guide_group_id, points, point_up, point_group_id, max_neighbors))
        ret = typing.NamedTuple("GeometryNodeInterpolateCurves", [("curves", Curve), ("closest_index", Integer), ("closest_weight", Float)])
        return ret(node.outputs[0].Curve, node.outputs[1].Integer, node.outputs[2].Float)

    def resample(self, count=10, length=0.1, mode='COUNT', selection=True):
        """The Resample Curve node creates a poly spline for each input spline. In the Count and Length modes, the control points of the new poly splines will have uniform spacing.
        #### Path
        - Curve > Operations > Resample Curve Node
        #### Properties
        - `mode`: `COUNT`, `EVALUATED`, `LENGTH`
        #### Outputs:
        - `#0 curve: Geometry = None`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeResampleCurve.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/operations/resample_curve.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeResampleCurve.html)
        """
        selection = selection if self._selection is None else self.selection
        node = new_node(*nodes.GeometryNodeResampleCurve(mode, self, selection, count, length))
        return node.outputs[0].Curve

    def resample_length(self, length=0.1, selection=True):
        """The Resample Curve node creates a poly spline for each input spline. In the Count and Length modes, the control points of the new poly splines will have uniform spacing.
        #### Path
        - Curve > Operations > Resample Curve Node
        #### Outputs:
        - `#0 curve: Geometry = None`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeResampleCurve.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/operations/resample_curve.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeResampleCurve.html)
        """
        selection = selection if self._selection is None else self.selection
        node = new_node(*nodes.GeometryNodeResampleCurve("LENGTH", self, selection, length=length))
        return node.outputs[0].Curve

    def resample_evaluated(self, selection=True):
        """The Resample Curve node creates a poly spline for each input spline. In the Count and Length modes, the control points of the new poly splines will have uniform spacing.
        #### Path
        - Curve > Operations > Resample Curve Node
        #### Outputs:
        - `#0 curve: Geometry = None`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeResampleCurve.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/operations/resample_curve.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeResampleCurve.html)
        """
        selection = selection if self._selection is None else self.selection
        node = new_node(*nodes.GeometryNodeResampleCurve("EVALUATED", self, selection))
        return node.outputs[0].Curve

    def reverse(self, selection=True):
        """The Reverse Curve node swaps the start and end of splines. The shape of the splines is not changed.
        #### Path
        - Curve > Operations > Reverse Curve Node
        #### Outputs:
        - `#0 curve: Geometry = None`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeReverseCurve.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/operations/reverse_curve.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeReverseCurve.html)
        """
        selection = selection if self._selection is None else self.selection
        node = new_node(*nodes.GeometryNodeReverseCurve(self, selection))
        return node.outputs[0].Curve

    def subdivide(self, cuts=1):
        """The Subdivide Curve node adds more control points in between existing control points on the curve input. For Bézier and poly splines, the shape of the spline will not be changed at all.
        #### Path
        - Curve > Operations > Subdivide Curve Node
        #### Outputs:
        - `#0 curve: Geometry = None`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeSubdivideCurve.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/operations/subdivide_curve.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeSubdivideCurve.html)
        """
        node = new_node(*nodes.GeometryNodeSubdivideCurve(self, cuts))
        return node.outputs[0].Curve

    def trim_factor(self, start=0.0, end=1.0, selection=True):
        """The Trim Curve node shortens each spline in the curve by removing sections at the start and end of each spline.
        #### Path
        - Curve > Operations > Trim Curve Node
        #### Outputs:
        - `#0 curve: Geometry = None`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeTrimCurve.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/operations/trim_curve.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeTrimCurve.html)
        """
        selection = selection if self._selection is None else self.selection
        node = new_node(*nodes.GeometryNodeTrimCurve("FACTOR", self, selection, start, end))
        return node.outputs[0].Curve

    def trim_length(self, start=0.0, end=1.0, selection=True):
        """The Trim Curve node shortens each spline in the curve by removing sections at the start and end of each spline.
        #### Path
        - Curve > Operations > Trim Curve Node
        #### Outputs:
        - `#0 curve: Geometry = None`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeTrimCurve.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/operations/trim_curve.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeTrimCurve.html)
        """
        selection = selection if self._selection is None else self.selection
        node = new_node(*nodes.GeometryNodeTrimCurve("LENGTH", self, selection, 0.0, 1.0, start, end))
        return node.outputs[0].Curve

    @staticmethod
    def curve_of_point(point_index: "Integer" = None):
        """The Curve of Point node retrieves the index of the curve a control point is part of. This node is conceptually similar to the Face of Corner Node.
        #### Path
        - Curve > Topology > Curve of Point Node
        #### Outputs:
        - `#0 curve_index: Integer = 0`
        - `#1 index_in_curve: Integer = 0`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeCurveOfPoint.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/topology/curve_of_point.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveOfPoint.html)
        """
        node = new_node(*nodes.GeometryNodeCurveOfPoint(point_index))
        ret = typing.NamedTuple("GeometryNodeCurveOfPoint", [("curve_index", Integer), ("index_in_curve", Integer)])
        return ret(node.outputs[0].Integer, node.outputs[1].Integer)

    @staticmethod
    def offset_point_in_curve(point_index: "Integer" = None, offset=0):
        """The Offset Point in Curve node retrieves other points in the same curve as the input control point. This is like starting at a specific control point and walking along neighboring points toward the start or end of the curve.
        #### Path
        - Curve > Topology > Offset Point in Curve Node
        #### Outputs:
        - `#0 is_valid_offset: Boolean = False`
        - `#1 point_index: Integer = 0`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeOffsetPointInCurve.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/topology/offset_point_in_curve.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeOffsetPointInCurve.html)
        """
        node = new_node(*nodes.GeometryNodeOffsetPointInCurve(point_index, offset))
        ret = typing.NamedTuple("GeometryNodeOffsetPointInCurve", [("is_valid_offset", Boolean), ("point_index", Integer)])
        return ret(node.outputs[0].Boolean, node.outputs[1].Integer)

    @staticmethod
    def points_of_curve(curve_index: "Integer" = None, weights=0.0, sort_index=0):
        """The Points of Curve node retrieves indices of specific control points in a curve.
        #### Path
        - Curve > Topology > Points of Curve Node
        #### Outputs:
        - `#0 point_index: Integer = 0`
        - `#1 total: Integer = 0`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodePointsOfCurve.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/topology/points_of_curve.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodePointsOfCurve.html)
        """
        node = new_node(*nodes.GeometryNodePointsOfCurve(curve_index, weights, sort_index))
        ret = typing.NamedTuple("GeometryNodePointsOfCurve", [("point_index", Integer), ("total", Integer)])
        return ret(node.outputs[0].Integer, node.outputs[1].Integer)


class Mesh(Geometry):

    @property
    def domain_size(self):
        """The Domain Size outputs the size of an attribute domain on the selected geometry type, for example, the number of edges in a mesh, or the number of points in a point cloud.
        #### Path
        - Attribute > Domain Size Node
        #### Outputs:
        - `#0 point_count: Integer = 0`
        - `#1 edge_count: Integer = 0`
        - `#2 face_count: Integer = 0`
        - `#3 face_corner_count: Integer = 0`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeAttributeDomainSize.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/domain_size.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeDomainSize.html)
        """
        node = new_node(*nodes.GeometryNodeAttributeDomainSize("MESH", self))
        ret = typing.NamedTuple("GeometryNodeAttributeDomainSize", [("point_count", Integer), ("edge_count", Integer), ("face_count", Integer), ("face_corner_count", Integer)])
        return ret(node.outputs[0].Integer, node.outputs[1].Integer, node.outputs[2].Integer, node.outputs[3].Integer)

    def merge_by_distance(self, distance=0.001, mode="ALL", selection=True):
        """The Merge by Distance node merges selected mesh vertices or point cloud points within a given distance, merging surrounding geometry where necessary. This operation is similar to the Merge by Distance operator or the Weld Modifier.
        #### Path
        - Geometry > Operations > Merge by Distance Node
        #### Properties
        - `mode`: `ALL`, `CONNECTED`
        #### Outputs:
        - `#0 geometry: Geometry = None`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeMergeByDistance.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/operations/merge_by_distance.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeMergeByDistance.html)
        """
        selection = selection if self._selection is None else self.selection
        node = new_node(*nodes.GeometryNodeMergeByDistance(mode, self, selection, distance))
        return node.outputs[0].Mesh

    @property
    def edge_angle(self):
        """The Edge Angle node calculates the angle in radians between two faces that meet at an edge. For the Face, Face Corner, and Point domains, the node uses simple domain interpolation to move values from the mesh’s edges.
        #### Path
        - Mesh > Read > Edge Angle Node
        #### Outputs:
        - `#0 unsigned_angle: Float = 0.0`
        - `#1 signed_angle: Float = 0.0`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeInputMeshEdgeAngle.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/read/edge_angle.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshEdgeAngle.html)
        """
        node = new_node(*nodes.GeometryNodeInputMeshEdgeAngle())
        ret = typing.NamedTuple("GeometryNodeInputMeshEdgeAngle", [("unsigned_angle", Float), ("signed_angle", Float)])
        return ret(node.outputs[0].Float, node.outputs[1].Float)

    @property
    def edge_neighbors(self):
        """The Edge Neighbors node outputs topology information relating to each edge of a mesh.
        #### Path
        - Mesh > Read > Edge Neighbors Node
        #### Outputs:
        - `#0 face_count: Integer = 0`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeInputMeshEdgeNeighbors.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/read/edge_neighbors.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshEdgeNeighbors.html)
        """
        node = new_node(*nodes.GeometryNodeInputMeshEdgeNeighbors())
        return node.outputs[0].Integer

    @property
    def edge_vertices(self):
        """The Edge Vertices node outputs the position and index of the two vertices of each of a mesh’s edges.
        #### Path
        - Mesh > Read > Edge Vertices Node
        #### Outputs:
        - `#0 vertex_index_1: Integer = 0`
        - `#1 vertex_index_2: Integer = 0`
        - `#2 position_1: Vector = (0.0, 0.0, 0.0)`
        - `#3 position_2: Vector = (0.0, 0.0, 0.0)`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeInputMeshEdgeVertices.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/read/edge_vertices.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshEdgeVertices.html)
        """
        node = new_node(*nodes.GeometryNodeInputMeshEdgeVertices())
        ret = typing.NamedTuple("MeshEdgeVertices", [("vertex_index_1", Integer), ("vertex_index_2", Integer), ("position_1", Vector), ("position_2", Vector)])
        return ret(node.outputs[0].Integer, node.outputs[1].Integer, node.outputs[2].Vector, node.outputs[3].Vector)

    @staticmethod
    def edges_to_face_groups(boundary_edges=True):
        """The Edges to Face Groups node group faces into regions surrounded by the selected boundary edges.
        #### Path
        - Mesh > Read > Edges to Face Groups Node
        #### Outputs:
        - `#0 face_group_id: Integer = 0`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeEdgesToFaceGroups.png)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/read/edges_to_face_groups.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeEdgesToFaceGroups.html)
        """
        node = new_node(*nodes.GeometryNodeEdgesToFaceGroups(boundary_edges))
        return node.outputs[0].Integer

    @property
    def face_area(self):
        """The Face Area node outputs the surface area of a mesh’s faces. The units are in Blender units no matter the unit system, equivalent to meters-squared at the default unit scale.
        #### Path
        - Mesh > Read > Face Area Node
        #### Outputs:
        - `#0 area: Float = 0.0`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeInputMeshFaceArea.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/read/face_area.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshFaceArea.html)
        """
        node = new_node(*nodes.GeometryNodeInputMeshFaceArea())
        return node.outputs[0].Float

    @property
    def face_neighbors(self):
        """The Face Neighbors node outputs topology information relating to each face of a mesh.
        #### Path
        - Mesh > Read > Face Neighbors Node
        #### Outputs:
        - `#0 vertex_count: Integer = 0`
        - `#1 face_count: Integer = 0`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeInputMeshFaceNeighbors.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/read/face_neighbors.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshFaceNeighbors.html)
        """
        node = new_node(*nodes.GeometryNodeInputMeshFaceNeighbors())
        ret = typing.NamedTuple("GeometryNodeInputMeshFaceNeighbors", [("vertex_count", Integer), ("face_count", Integer)])
        return ret(node.outputs[0].Integer, node.outputs[1].Integer)

    @staticmethod
    def faceset_boundaries(face_set=0):
        """The Face Group Boundaries Node finds the edges which lie on the boundaries of specified regions. These edges could be used to mark seams for UV unwrapping, for example.
        #### Path
        - Mesh > Read > Face Group Boundaries Node
        #### Outputs:
        - `#0 boundary_edges: Boolean = False`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeMeshFaceSetBoundaries.png)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/read/face_group_boundaries.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshFaceSetBoundaries.html)
        """
        node = new_node(*nodes.GeometryNodeMeshFaceSetBoundaries(face_set))
        return node.outputs[0].Boolean

    @staticmethod
    def face_is_planar(threshold=0.01):
        """The Is Face Planar node outputs whether every triangle of a quads or N-gons is on the same plane as all of the others, in other words, if they have the same normal.
        #### Path
        - Mesh > Read > Is Face Planar Node
        #### Outputs:
        - `#0 planar: Boolean = False`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeInputMeshFaceIsPlanar.png)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/read/face_is_planar.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshFaceIsPlanar.html)
        """
        node = new_node(*nodes.GeometryNodeInputMeshFaceIsPlanar(threshold))
        return node.outputs[0].Boolean

    @property
    def is_shade_smooth(self):
        """The Is Shade Smooth node outputs true for each face of the mesh if that face is marked to render smooth shaded. Otherwise, if the face is marked to render as flat shaded, so the node outputs false.
        #### Path
        - Mesh > Read > Is Shade Smooth Node
        #### Outputs:
        - `#0 smooth: Boolean = False`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeInputShadeSmooth.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/read/is_shade_smooth.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputShadeSmooth.html)
        """
        node = new_node(*nodes.GeometryNodeInputShadeSmooth())
        return node.outputs[0].Boolean

    @property
    def mesh_island(self):
        """The Mesh Island node outputs information about separate connected regions, or “islands” of a mesh. Whenever two vertices are connected together by an edge, they are considered as part of the same island, and will have the same Island Index output.
        #### Path
        - Mesh > Read > Mesh Island Node
        #### Outputs:
        - `#0 island_index: Integer = 0`
        - `#1 island_count: Integer = 0`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeInputMeshIsland.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/read/mesh_island.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshIsland.html)
        """
        node = new_node(*nodes.GeometryNodeInputMeshIsland())
        ret = typing.NamedTuple("GeometryNodeInputMeshIsland", [("island_index", Integer), ("island_count", Integer)])
        return ret(node.outputs[0].Integer, node.outputs[1].Integer)

    @staticmethod
    def shortest_edge_paths(end_vertex=False, edge_cost=1.0):
        """The Shortest Edge Paths node finds paths along mesh edges to a selection of end vertices. The cost used to define “shortest” can be set to anything. By default there is a constant cost for every edge, but a typical input would be the length of each edge.
        #### Path
        - Mesh > Read > Shortest Edge Paths Node
        #### Outputs:
        - `#0 next_vertex_index: Integer = 0`
        - `#1 total_cost: Float = 0.0`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeInputShortestEdgePaths.png)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/read/shortest_edge_paths.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputShortestEdgePaths.html)
        """
        node = new_node(*nodes.GeometryNodeInputShortestEdgePaths(end_vertex, edge_cost))
        ret = typing.NamedTuple("GeometryNodeInputShortestEdgePaths", [("next_vertex_index", Integer), ("total_cost", Float)])
        return ret(node.outputs[0].Integer, node.outputs[1].Float)

    @property
    def vertex_neighbors(self):
        """The Vertex Neighbors node outputs topology information relating to each vertex of a mesh.
        #### Path
        - Mesh > Read > Vertex Neighbors Node
        #### Outputs:
        - `#0 vertex_count: Integer = 0`
        - `#1 face_count: Integer = 0`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeInputMeshVertexNeighbors.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/read/vertex_neighbors.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMeshVertexNeighbors.html)
        """
        node = new_node(*nodes.GeometryNodeInputMeshVertexNeighbors())
        ret = typing.NamedTuple("GeometryNodeInputMeshVertexNeighbors", [("vertex_count", Integer), ("face_count", Integer)])
        return ret(node.outputs[0].Integer, node.outputs[1].Integer)

    def nearest_surface(self, data_type='FLOAT', value_float=0.0, value_int=0, value_vector=(0.0, 0.0, 0.0), value_color=(0.0, 0.0, 0.0, 0.0), value_bool=False, sample_position: "Vector" = None):
        """The Sample Nearest Surface node finds values at the closest points on the surface of a source mesh geometry. Non-face attributes are interpolated across the surface.
        #### Path
        - Mesh > Sample > Sample Nearest Surface Node
        #### Properties
        - `data_type`: `FLOAT`, `INT`, `FLOAT_VECTOR`, `FLOAT_COLOR`, `BOOLEAN`
        #### Outputs:
        - `#0 value_float: Float = 0.0`
        - `#1 value_int: Integer = 0`
        - `#2 value_vector: Vector = (0.0, 0.0, 0.0)`
        - `#3 value_color: Color = (0.0, 0.0, 0.0, 0.0)`
        - `#4 value_bool: Boolean = False`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeSampleNearestSurface.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/sample/sample_nearest_surface.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeSampleNearestSurface.html)
        """
        node = new_node(*nodes.GeometryNodeSampleNearestSurface(data_type, self, value_float, value_int, value_vector, value_color, value_bool, sample_position))
        return node.outputs[0].Float, node.outputs[1].Integer, node.outputs[2].Vector, node.outputs[3].Color, node.outputs[4].Boolean

    def nearest_surface_float(self, value_float=0.0, sample_position: "Vector" = None):
        """The Sample Nearest Surface node finds values at the closest points on the surface of a source mesh geometry. Non-face attributes are interpolated across the surface.
        #### Path
        - Mesh > Sample > Sample Nearest Surface Node
        #### Outputs:
        - `#0 value_float: Float = 0.0`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeSampleNearestSurface.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/sample/sample_nearest_surface.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeSampleNearestSurface.html)
        """
        node = new_node(*nodes.GeometryNodeSampleNearestSurface("FLOAT", self, value_float, 0, (0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), False, sample_position))
        return node.outputs[0].Float

    def nearest_surface_integer(self, value_int=0, sample_position: "Vector" = None):
        """The Sample Nearest Surface node finds values at the closest points on the surface of a source mesh geometry. Non-face attributes are interpolated across the surface.
        #### Path
        - Mesh > Sample > Sample Nearest Surface Node
        #### Outputs:
        - `#1 value_int: Integer = 0`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeSampleNearestSurface.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/sample/sample_nearest_surface.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeSampleNearestSurface.html)
        """
        node = new_node(*nodes.GeometryNodeSampleNearestSurface("INT", self, 0.0, value_int, (0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), False, sample_position))
        return node.outputs[1].Integer

    def nearest_surface_vector(self, value_vector=(0.0, 0.0, 0.0), sample_position: "Vector" = None):
        """The Sample Nearest Surface node finds values at the closest points on the surface of a source mesh geometry. Non-face attributes are interpolated across the surface.
        #### Path
        - Mesh > Sample > Sample Nearest Surface Node
        #### Outputs:
        - `#2 value_vector: Vector = (0.0, 0.0, 0.0)`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeSampleNearestSurface.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/sample/sample_nearest_surface.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeSampleNearestSurface.html)
        """
        node = new_node(*nodes.GeometryNodeSampleNearestSurface("FLOAT_VECTOR", self, 0.0, 0, value_vector, (0.0, 0.0, 0.0, 0.0), False, sample_position))
        return node.outputs[2].Vector

    def nearest_surface_color(self, value_color=(0.0, 0.0, 0.0, 0.0), sample_position: "Vector" = None):
        """The Sample Nearest Surface node finds values at the closest points on the surface of a source mesh geometry. Non-face attributes are interpolated across the surface.
        #### Path
        - Mesh > Sample > Sample Nearest Surface Node
        #### Outputs:
        - `#3 value_color: Color = (0.0, 0.0, 0.0, 0.0)`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeSampleNearestSurface.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/sample/sample_nearest_surface.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeSampleNearestSurface.html)
        """
        node = new_node(*nodes.GeometryNodeSampleNearestSurface("FLOAT_COLOR", self, 0.0, 0, (0.0, 0.0, 0.0), value_color, False, sample_position))
        return node.outputs[3].Color

    def nearest_surface_boolean(self, value_bool=False, sample_position: "Vector" = None):
        """The Sample Nearest Surface node finds values at the closest points on the surface of a source mesh geometry. Non-face attributes are interpolated across the surface.
        #### Path
        - Mesh > Sample > Sample Nearest Surface Node
        #### Outputs:
        - `#4 value_bool: Boolean = False`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeSampleNearestSurface.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/sample/sample_nearest_surface.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeSampleNearestSurface.html)
        """
        node = new_node(*nodes.GeometryNodeSampleNearestSurface("BOOLEAN", self, 0.0, 0, (0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), value_bool, sample_position))
        return node.outputs[4].Boolean

    def sample_uv_surface_float(self, value_float=0.0, source_uv_map=(0.0, 0.0, 0.0), sample_uv=(0.0, 0.0, 0.0)):
        """The Sample UV Surface node finds values on a mesh's surface at specific UV locations. Internally the process is a “reverse UV lookup” from a location in 2D space. The node then finds the face that corresponds to each UV coordinate, and the location within that face.
        #### Path
        - Mesh > Sample > Sample UV Surface Node
        #### Outputs:
        - `#0 value_float: Float = 0.0`
        - `#5 is_valid: Boolean = False`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeSampleUVSurface.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/sample/sample_uv_surface.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeSampleUVSurface.html)
        """
        node = new_node(*nodes.GeometryNodeSampleUVSurface("FLOAT", self, value_float, 0, (0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), False, source_uv_map, sample_uv))
        ret = typing.NamedTuple("GeometryNodeSampleUVSurface", [("value", Float), ("is_valid", Boolean)])
        return ret(node.outputs[0].Float, node.outputs[5].Boolean)

    def sample_uv_surface_integer(self, value_int=0.0, source_uv_map=(0.0, 0.0, 0.0), sample_uv=(0.0, 0.0, 0.0)):
        """The Sample UV Surface node finds values on a mesh's surface at specific UV locations. Internally the process is a “reverse UV lookup” from a location in 2D space. The node then finds the face that corresponds to each UV coordinate, and the location within that face.
        #### Path
        - Mesh > Sample > Sample UV Surface Node
        #### Outputs:
        - `#1 value_int: Integer = 0`
        - `#5 is_valid: Boolean = False`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeSampleUVSurface.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/sample/sample_uv_surface.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeSampleUVSurface.html)
        """
        node = new_node(*nodes.GeometryNodeSampleUVSurface("INT", self, 0.0, value_int, (0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), False, source_uv_map, sample_uv))
        ret = typing.NamedTuple("GeometryNodeSampleUVSurface", [("value", Integer), ("is_valid", Boolean)])
        return ret(node.outputs[1].Integer, node.outputs[5].Boolean)

    def sample_uv_surface_vector(self, value_vector=(0.0, 0.0, 0.0), source_uv_map=(0.0, 0.0, 0.0), sample_uv=(0.0, 0.0, 0.0)):
        """The Sample UV Surface node finds values on a mesh's surface at specific UV locations. Internally the process is a “reverse UV lookup” from a location in 2D space. The node then finds the face that corresponds to each UV coordinate, and the location within that face.
        #### Path
        - Mesh > Sample > Sample UV Surface Node
        #### Outputs:
        - `#2 value_vector: Vector = (0.0, 0.0, 0.0)`
        - `#5 is_valid: Boolean = False`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeSampleUVSurface.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/sample/sample_uv_surface.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeSampleUVSurface.html)
        """
        node = new_node(*nodes.GeometryNodeSampleUVSurface("FLOAT_VECTOR", self, 0.0, 0, value_vector, (0.0, 0.0, 0.0, 0.0), False, source_uv_map, sample_uv))
        ret = typing.NamedTuple("GeometryNodeSampleUVSurface", [("value", Vector), ("is_valid", Boolean)])
        return ret(node.outputs[2].Vector, node.outputs[5].Boolean)

    def sample_uv_surface_color(self, value_color=(0.0, 0.0, 0.0, 0.0), source_uv_map=(0.0, 0.0, 0.0), sample_uv=(0.0, 0.0, 0.0)):
        """The Sample UV Surface node finds values on a mesh's surface at specific UV locations. Internally the process is a “reverse UV lookup” from a location in 2D space. The node then finds the face that corresponds to each UV coordinate, and the location within that face.
        #### Path
        - Mesh > Sample > Sample UV Surface Node
        #### Outputs:
        - `#3 value_color: Color = (0.0, 0.0, 0.0, 0.0)`
        - `#5 is_valid: Boolean = False`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeSampleUVSurface.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/sample/sample_uv_surface.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeSampleUVSurface.html)
        """
        node = new_node(*nodes.GeometryNodeSampleUVSurface("FLOAT_COLOR", self, 0.0, 0, (0.0, 0.0, 0.0), value_color, False, source_uv_map, sample_uv))
        ret = typing.NamedTuple("GeometryNodeSampleUVSurface", [("value", Color), ("is_valid", Boolean)])
        return ret(node.outputs[3].Color, node.outputs[5].Boolean)

    def sample_uv_surface_boolean(self, value_bool=False, source_uv_map=(0.0, 0.0, 0.0), sample_uv=(0.0, 0.0, 0.0)):
        """The Sample UV Surface node finds values on a mesh's surface at specific UV locations. Internally the process is a “reverse UV lookup” from a location in 2D space. The node then finds the face that corresponds to each UV coordinate, and the location within that face.
        #### Path
        - Mesh > Sample > Sample UV Surface Node
        #### Outputs:
        - `#4 value_bool: Boolean = False`
        - `#5 is_valid: Boolean = False`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeSampleUVSurface.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/sample/sample_uv_surface.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeSampleUVSurface.html)
        """
        node = new_node(*nodes.GeometryNodeSampleUVSurface("BOOLEAN", self, 0.0, 0, (0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), value_bool, source_uv_map, sample_uv))
        ret = typing.NamedTuple("GeometryNodeSampleUVSurface", [("value", Boolean), ("is_valid", Boolean)])
        return ret(node.outputs[4].Boolean, node.outputs[5].Boolean)

    def set_shade_smooth(self, shade_smooth=True, selection=True):
        """The Set Shade Smooth node controls whether the mesh's faces look smooth in the viewport and renders. The input node for this data is the Is Shade Smooth node.
        - In-Place Operation
        #### Path
        - Mesh > Write > Set Shade Smooth Node
        #### Outputs:
        - `#0 geometry: Geometry = None`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeSetShadeSmooth.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/write/set_shade_smooth.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetShadeSmooth.html)
        """
        selection = selection if self._selection is None else self.selection
        node = new_node(*nodes.GeometryNodeSetShadeSmooth(self, selection, shade_smooth))
        self.bsocket = node.outputs[0].bsocket
        return self

    def dual_mesh(self, keep_boundaries=False):
        """The Dual Mesh Node converts a mesh into it's dual, i.e. faces are turned into vertices and vertices are turned into faces. This also means that attributes which were on the face domain are transferred to the point domain in the dual mesh.
        #### Path
        - Mesh > Operations > Dual Mesh Node
        #### Outputs:
        - `#0 dual_mesh: Geometry = None`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeDualMesh.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/operations/dual_mesh.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeDualMesh.html)
        """
        node = new_node(*nodes.GeometryNodeDualMesh(self, keep_boundaries))
        return node.outputs[0].Mesh

    def edge_paths_to_curves(self, start_vertices=True, next_vertex_index=-1):
        """The Edge Paths to Curves node output curves that follow paths across mesh edges.
        #### Path
        - Mesh > Operations > Edge Paths to Curves Node
        #### Outputs:
        - `#0 curves: Geometry = None`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeEdgePathsToCurves.png)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/operations/edge_paths_to_curves.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeEdgePathsToCurves.html)
        """
        node = new_node(*nodes.GeometryNodeEdgePathsToCurves(self, start_vertices, next_vertex_index))
        return node.outputs[0].Curve

    @staticmethod
    def edge_paths_to_selection(start_vertices=True, next_vertex_index=-1):
        """The Edge Paths to Selection node follows paths across mesh edges and outputs a selection of every visited edge.
        #### Path
        - Mesh > Operations > Edge Paths to Selection Node
        #### Outputs:
        - `#0 selection: Boolean = False`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeEdgePathsToSelection.png)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/operations/edge_paths_to_selection.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeEdgePathsToSelection.html)
        """
        node = new_node(*nodes.GeometryNodeEdgePathsToSelection(start_vertices, next_vertex_index))
        return node.outputs[0].Boolean

    def extrude(self, offset_scale=1.0, offset: "Vector" = None, individual=True, mode='FACES', selection=True):
        """The Extrude Mesh Node generates new vertices, edges, or faces, on selected geometry and transforms them based on an offset.
        #### Path
        - Mesh > Operations > Extrude Mesh Node
        #### Properties
        - `mode`: `FACES`, `VERTICES`, `EDGES`
        #### Outputs:
        - `#0 mesh: Geometry = None`
        - `#1 top: Boolean = False`
        - `#2 side: Boolean = False`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeExtrudeMesh.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/operations/extrude_mesh.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeExtrudeMesh.html)
        """
        selection = selection if self._selection is None else self.selection
        node = new_node(*nodes.GeometryNodeExtrudeMesh(mode, self, selection, offset, offset_scale, individual))
        ret = typing.NamedTuple("GeometryNodeExtrudeMesh", [("mesh", Mesh), ("top", Boolean), ("side", Boolean)])
        return ret(node.outputs[0].Mesh, node.outputs[1].Boolean, node.outputs[2].Boolean)

    def extrude_faces(self, offset_scale=1.0, offset: "Vector" = None, individual=True, selection=True):
        """The Extrude Mesh Node generates new vertices, edges, or faces, on selected geometry and transforms them based on an offset.
        #### Path
        - Mesh > Operations > Extrude Mesh Node
        #### Outputs:
        - `#0 mesh: Geometry = None`
        - `#1 top: Boolean = False`
        - `#2 side: Boolean = False`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeExtrudeMesh.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/operations/extrude_mesh.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeExtrudeMesh.html)
        """
        selection = selection if self._selection is None else self.selection
        node = new_node(*nodes.GeometryNodeExtrudeMesh("FACES", self, selection, offset, offset_scale, individual))
        ret = typing.NamedTuple("GeometryNodeExtrudeMesh", [("mesh", Mesh), ("top", Boolean), ("side", Boolean)])
        return ret(node.outputs[0].Mesh, node.outputs[1].Boolean, node.outputs[2].Boolean)

    def extrude_vertices(self, offset_scale=1.0, offset: "Vector" = None, individual=True, selection=True):
        """The Extrude Mesh Node generates new vertices, edges, or faces, on selected geometry and transforms them based on an offset.
        #### Path
        - Mesh > Operations > Extrude Mesh Node
        #### Outputs:
        - `#0 mesh: Geometry = None`
        - `#1 top: Boolean = False`
        - `#2 side: Boolean = False`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeExtrudeMesh.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/operations/extrude_mesh.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeExtrudeMesh.html)
        """
        selection = selection if self._selection is None else self.selection
        node = new_node(*nodes.GeometryNodeExtrudeMesh("VERTICES", self, selection, offset, offset_scale, individual))
        ret = typing.NamedTuple("GeometryNodeExtrudeMesh", [("mesh", Mesh), ("top", Boolean), ("side", Boolean)])
        return ret(node.outputs[0].Mesh, node.outputs[1].Boolean, node.outputs[2].Boolean)

    def extrude_edges(self, offset_scale=1.0, offset: "Vector" = None, individual=True, selection=True):
        """The Extrude Mesh Node generates new vertices, edges, or faces, on selected geometry and transforms them based on an offset.
        #### Path
        - Mesh > Operations > Extrude Mesh Node
        #### Outputs:
        - `#0 mesh: Geometry = None`
        - `#1 top: Boolean = False`
        - `#2 side: Boolean = False`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeExtrudeMesh.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/operations/extrude_mesh.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeExtrudeMesh.html)
        """
        selection = selection if self._selection is None else self.selection
        node = new_node(*nodes.GeometryNodeExtrudeMesh("EDGES", self, selection, offset, offset_scale, individual))
        ret = typing.NamedTuple("GeometryNodeExtrudeMesh", [("mesh", Mesh), ("top", Boolean), ("side", Boolean)])
        return ret(node.outputs[0].Mesh, node.outputs[1].Boolean, node.outputs[2].Boolean)

    def flip_faces(self, selection=True):
        """The Flip Faces Node reverses the order of the vertices and edges of each selected face. The most common use of this node is to flip the normals of a face. Any face corner domain attributes of selected faces are also reversed.
        #### Path
        - Mesh > Operations > Flip Faces Node
        #### Outputs:
        - `#0 mesh: Geometry = None`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeFlipFaces.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/operations/flip_faces.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeFlipFaces.html)
        """
        selection = selection if self._selection is None else self.selection
        node = new_node(*nodes.GeometryNodeFlipFaces(self, selection))
        return node.outputs[0].Mesh

    def mesh_union(self, *others: "Mesh", self_intersection=False, hole_tolerant=False):
        """The Mesh Boolean Node allows you to cut, subtract, and join the geometry of two inputs. This node offers the same operations as the Boolean modifier.
        #### Path
        - Mesh > Operations > Mesh Boolean Node
        #### Outputs:
        - `#0 mesh: Geometry = None`
        - `#1 intersecting_edges: Boolean = False`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeMeshBoolean.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/operations/mesh_boolean.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshBoolean.html)
        """
        node = new_node(*nodes.GeometryNodeMeshBoolean("UNION", None, None, self_intersection, hole_tolerant))
        items = list(reversed(others)) + [self]
        for item in items:
            new_link(item.bsocket, node.bnode.inputs[1])
        ret = typing.NamedTuple("GeometryNodeMeshBoolean", [("mesh", Mesh), ("intersecting_edges", Boolean)])
        return ret(node.outputs[0].Mesh, node.outputs[1].Boolean)

    def mesh_intersect(self, *others: "Mesh", self_intersection=False, hole_tolerant=False):
        """The Mesh Boolean Node allows you to cut, subtract, and join the geometry of two inputs. This node offers the same operations as the Boolean modifier.
        #### Path
        - Mesh > Operations > Mesh Boolean Node
        #### Outputs:
        - `#0 mesh: Geometry = None`
        - `#1 intersecting_edges: Boolean = False`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeMeshBoolean.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/operations/mesh_boolean.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshBoolean.html)
        """
        node = new_node(*nodes.GeometryNodeMeshBoolean("INTERSECT", None, None, self_intersection, hole_tolerant))
        items = list(reversed(others)) + [self]
        for item in items:
            new_link(item.bsocket, node.bnode.inputs[1])
        ret = typing.NamedTuple("GeometryNodeMeshBoolean", [("mesh", Mesh), ("intersecting_edges", Boolean)])
        return ret(node.outputs[0].Mesh, node.outputs[1].Boolean)

    def mesh_difference(self, *others: "Mesh", self_intersection=False, hole_tolerant=False):
        """The Mesh Boolean Node allows you to cut, subtract, and join the geometry of two inputs. This node offers the same operations as the Boolean modifier.
        #### Path
        - Mesh > Operations > Mesh Boolean Node
        #### Outputs:
        - `#0 mesh: Geometry = None`
        - `#1 intersecting_edges: Boolean = False`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeMeshBoolean.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/operations/mesh_boolean.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshBoolean.html)
        """
        node = new_node(*nodes.GeometryNodeMeshBoolean("DIFFERENCE", self, None, self_intersection, hole_tolerant))
        items = list(reversed(others))
        for item in items:
            new_link(item.bsocket, node.bnode.inputs[1])
        ret = typing.NamedTuple("GeometryNodeMeshBoolean", [("mesh", Mesh), ("intersecting_edges", Boolean)])
        return ret(node.outputs[0].Mesh, node.outputs[1].Boolean)

    def to_curve(self, selection=True):
        """The Mesh to Curve node generates a curve from a mesh. The result is a poly spline, with a point for every selected vertex on the mesh. Any intersection of more than two selected edges will cause a break in the spline. Meaning that if a the mesh has grid-like topology and a continuous spline is desired, the Selection input is very important.
        #### Path
        - Mesh > Operations > Mesh to Curve Node
        #### Outputs:
        - `#0 curve: Geometry = None`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeMeshToCurve.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/operations/mesh_to_curve.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshToCurve.html)
        """
        selection = selection if self._selection is None else self.selection
        node = new_node(*nodes.GeometryNodeMeshToCurve(self, selection))
        return node.outputs[0].Curve

    def to_points(self, mode='VERTICES', position: "Vector" = None, radius=0.05, selection=True):
        """The Mesh to Points node generates a point cloud from a mesh.
        #### Path
        - Mesh > Operations > Mesh to Points Node
        #### Properties
        - `mode`: `VERTICES`, `EDGES`, `FACES`, `CORNERS`
        #### Outputs:
        - `#0 points: Geometry = None`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeMeshToPoints.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/operations/mesh_to_points.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshToPoints.html)
        """
        selection = selection if self._selection is None else self.selection
        node = new_node(*nodes.GeometryNodeMeshToPoints(mode, self, selection, position, radius))
        return node.outputs[0].Points

    def to_volume(self, resolution_mode='VOXEL_AMOUNT', density=1.0, voxel_size=0.3, voxel_amount=64.0, exterior_band_width=0.1, interior_band_width=0.0, fill_volume=True):
        """The Mesh to Volume node creates a fog volumes based on the shape of a mesh. The volume is created with a grid of the name “density”.
        #### Path
        - Mesh > Operations > Mesh to Volume Node
        #### Properties
        - `resolution_mode`: `VOXEL_AMOUNT`, `VOXEL_SIZE`
        #### Outputs:
        - `#0 volume: Geometry = None`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeMeshToVolume.png)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/operations/mesh_to_volume.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshToVolume.html)
        """
        node = new_node(*nodes.GeometryNodeMeshToVolume(resolution_mode, self, density, voxel_size, voxel_amount, exterior_band_width, interior_band_width, fill_volume))
        return node.outputs[0].Volume

    def scale_elements(self, scale=1.0, center: "Vector" = None, axis=(1.0, 0.0, 0.0), domain='FACE', scale_mode='UNIFORM', selection=True):
        """The Scale Elements Node scales groups of connected edges and faces. When multiple selected faces/edges share the same vertices, they are scaled together. The center and scaling factor is averaged in this case.
        #### Path
        - Mesh > Operations > Scale Elements Node
        #### Properties
        - `domain`: `FACE`, `EDGE`
        - `scale_mode`: `UNIFORM`, `SINGLE_AXIS`
        #### Outputs:
        - `#0 geometry: Geometry = None`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeScaleElements.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/operations/scale_elements.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeScaleElements.html)
        """
        selection = selection if self._selection is None else self.selection
        node = new_node(*nodes.GeometryNodeScaleElements(domain, scale_mode, self, selection, scale, center, axis))
        return node.outputs[0].Mesh

    def split_edges(self, selection=True):
        """Like the Edge Split Modifier, the Split Edges node splits and duplicates edges within a mesh, breaking ‘links’ between faces around those split edges.
        #### Path
        - Mesh > Operations > Split Edges Node
        #### Outputs:
        - `#0 mesh: Geometry = None`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeSplitEdges.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/operations/split_edges.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeSplitEdges.html)
        """
        selection = selection if self._selection is None else self.selection
        node = new_node(*nodes.GeometryNodeSplitEdges(self, selection))
        return node.outputs[0].Mesh

    def subdivide_mesh(self, level=1):
        """The Subdivide Mesh node adds new faces to mesh geometry using a simple interpolation for deformation.
        #### Path
        - Mesh > Operations > Subdivide Mesh Node
        #### Outputs:
        - `#0 mesh: Geometry = None`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeSubdivideMesh.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/operations/subdivide_mesh.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeSubdivideMesh.html)
        """
        node = new_node(*nodes.GeometryNodeSubdivideMesh(self, level))
        return node.outputs[0].Mesh

    def subdivision_surface(self, uv_smooth='PRESERVE_BOUNDARIES', boundary_smooth='ALL', level=1, edge_crease=0.0, vertex_crease=0.0):
        """The Subdivision Surface node adds new faces to mesh geometry using a Catmull-Clark subdivision method.
        #### Path
        - Mesh > Operations > Subdivision Surface Node
        #### Properties
        - `boundary_smooth`: `ALL`, `PRESERVE_CORNERS`
        - `uv_smooth`: `PRESERVE_BOUNDARIES`, `NONE`, `PRESERVE_CORNERS`, `PRESERVE_CORNERS_AND_JUNCTIONS`, `PRESERVE_CORNERS_JUNCTIONS_AND_CONCAVE`, `SMOOTH_ALL`
        #### Outputs:
        - `#0 mesh: Geometry = None`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeSubdivisionSurface.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/operations/subdivision_surface.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeSubdivisionSurface.html)
        """
        node = new_node(*nodes.GeometryNodeSubdivisionSurface(boundary_smooth, uv_smooth, self, level, edge_crease, vertex_crease))
        return node.outputs[0].Mesh

    def triangulate(self, ngon_method='BEAUTY', quad_method='SHORTEST_DIAGONAL', minimum_vertices=4, selection=True):
        """The Triangulate node converts all faces in a mesh (quads and n-gons) to triangular faces. It functions the same as the Triangulate tool in Edit Mode.
        #### Path
        - Mesh > Operations > Triangulate Node
        #### Properties
        - `ngon_method`: `BEAUTY`, `CLIP`
        - `quad_method`: `SHORTEST_DIAGONAL`, `BEAUTY`, `FIXED`, `FIXED_ALTERNATE`, `LONGEST_DIAGONAL`
        #### Outputs:
        - `#0 mesh: Geometry = None`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeTriangulate.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/operations/triangulate.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeTriangulate.html)
        """
        selection = selection if self._selection is None else self.selection
        node = new_node(*nodes.GeometryNodeTriangulate(ngon_method, quad_method, self, selection, minimum_vertices))
        return node.outputs[0].Mesh

    @staticmethod
    def corners_of_face(face_index: "Integer" = None, weights=0.0, sort_index=0):
        """The Corners of Face node gives access to specific corners of input faces.
        #### Path
        - Mesh > Topology > Corners of Face Node
        #### Outputs:
        - `#0 corner_index: Integer = 0`
        - `#1 total: Integer = 0`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryCornersOfFace.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/topology/corners_of_face.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeCornersOfFace.html)
        """
        node = new_node(*nodes.GeometryNodeCornersOfFace(face_index, weights, sort_index))
        ret = typing.NamedTuple("GeometryNodeCornersOfFace", [("corner_index", Integer), ("total", Integer)])
        return ret(node.outputs[0].Integer, node.outputs[1].Integer)

    @staticmethod
    def corners_of_vertex(vertex_index: "Integer" = None, weights=0.0, sort_index=0):
        """The Corners of Vertex node retrieves face corners attached to each vertex. The node first gathers a list of the corners of all faces connected to the vertex. That list is then sorted based on the values of the Sort Weight input. The Total output is the number of connected faces/corners, and the Corner Index output is one of those corners, chosen with the Sort Index input.
        #### Path
        - Mesh > Topology > Corners of Vertex Node
        #### Outputs:
        - `#0 corner_index: Integer = 0`
        - `#1 total: Integer = 0`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeCornersOfVertex.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/topology/corners_of_vertex.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeCornersOfVertex.html)
        """
        node = new_node(*nodes.GeometryNodeCornersOfVertex(vertex_index, weights, sort_index))
        ret = typing.NamedTuple("GeometryNodeCornersOfVertex", [("corner_index", Integer), ("total", Integer)])
        return ret(node.outputs[0].Integer, node.outputs[1].Integer)

    @staticmethod
    def edges_of_corner(corner_index: "Integer" = None):
        """The Edges of Corner node retrieves the edges on both sides of a face corner.
        #### Path
        - Mesh > Topology > Edges of Corner Node
        #### Outputs:
        - `#0 next_edge_index: Integer = 0`
        - `#1 previous_edge_index: Integer = 0`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeEdgesOfCorner.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/topology/edges_of_corner.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeEdgesOfCorner.html)
        """
        node = new_node(*nodes.GeometryNodeEdgesOfCorner(corner_index))
        ret = typing.NamedTuple("GeometryNodeEdgesOfCorner", [("next_edge_index", Integer), ("previous_edge_index", Integer)])
        return ret(node.outputs[0].Integer, node.outputs[1].Integer)

    @staticmethod
    def edges_of_vertex(vertex_index: "Integer" = None, weights=0.0, sort_index=0):
        """The Edges of Vertex node retrieves the edges connected to each vertex. Each vertex is connected to several edges. The node first collects a list of those edges, then sorts them based on the Sort Weight input. The Total output is the number of edges in that list, and the Edge Index output is one of those edges chosen with the Sort Index input.
        #### Path
        - Mesh > Topology > Edges of Vertex Node
        #### Outputs:
        - `#0 edge_index: Integer = 0`
        - `#1 total: Integer = 0`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeEdgesOfVertex.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/topology/edges_of_vertex.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeEdgesOfVertex.html)
        """
        node = new_node(*nodes.GeometryNodeEdgesOfVertex(vertex_index, weights, sort_index))
        ret = typing.NamedTuple("GeometryNodeEdgesOfVertex", [("edge_index", Integer), ("total", Integer)])
        return ret(node.outputs[0].Integer, node.outputs[1].Integer)

    @staticmethod
    def face_of_corner(corner_index: "Integer" = None):
        """The Face of Corner node retrieves the face a face corner is part of.
        #### Path
        - Mesh > Topology > Face of Corner Node
        #### Outputs:
        - `#0 face_index: Integer = 0`
        - `#1 index_in_face: Integer = 0`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeFaceOfCorner.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/topology/face_of_corner.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeFaceOfCorner.html)
        """
        node = new_node(*nodes.GeometryNodeFaceOfCorner(corner_index))
        ret = typing.NamedTuple("GeometryNodeFaceOfCorner", [("face_index", Integer), ("index_in_face", Integer)])
        return ret(node.outputs[0].Integer, node.outputs[1].Integer)

    @staticmethod
    def offset_corner_in_face(corner_index: "Integer" = None, offset=0):
        """The Offset Corner in Face node retrieves other corners in the same face as the input face corner. This is like “rotating” the input corner around in its face.
        #### Path
        - Mesh > Topology > Offset Corner in Face Node
        #### Outputs:
        - `#0 corner_index: Integer = 0`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeOffsetCornerInFace.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/topology/offset_corner_in_face.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeOffsetCornerInFace.html)
        """
        node = new_node(*nodes.GeometryNodeOffsetCornerInFace(corner_index, offset))
        return node.outputs[0].Integer

    @staticmethod
    def vertex_of_corner(corner_index: "Integer" = None):
        """The Vertex of Corner node outputs the index of the vertex that a face corner is attached to.
        #### Path
        - Mesh > Topology > Vertex of Corner Node
        #### Outputs:
        - `#0 vertex_index: Integer = 0`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeVertexOfCorner.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/topology/vertex_of_corner.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeVertexOfCorner.html)
        """
        node = new_node(*nodes.GeometryNodeVertexOfCorner(corner_index))
        return node.outputs[0].Integer

    def pack_uv_islands(self, uv=(0.0, 0.0, 0.0), margin=0.001, rotate=True, selection=True):
        """The Pack UV Islands Node scales islands of a UV map and moves them so they fill the UV space as much as possible.
        #### Path
        - Mesh > UV > Pack UV Islands Node
        #### Outputs:
        - `#0 uv: Vector = (0.0, 0.0, 0.0)`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryUVPackIslands.png)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/uv/pack_uv_islands.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeUVPackIslands.html)
        """
        selection = selection if self._selection is None else self.selection
        node = new_node(*nodes.GeometryNodeUVPackIslands(uv, selection, margin, rotate))
        return node.outputs[0].Vector

    def uv_unwrap(self, method='ANGLE_BASED', seam=False, margin=0.001, fill_holes=True, selection=True):
        """The UV Unwrap Node generates a UV map islands based on a selection of seam edges. The node implicitly performs a Pack Islands operation upon completion, because the results may not be generally useful otherwise.
        #### Path
        - Mesh > UV > UV Unwrap Node
        #### Properties
        - `method`: `ANGLE_BASED`, `CONFORMAL`
        #### Outputs:
        - `#0 uv: Vector = (0.0, 0.0, 0.0)`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryUVUnrwap.png)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/uv/uv_unwrap.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeUVUnwrap.html)
        """
        selection = selection if self._selection is None else self.selection
        node = new_node(*nodes.GeometryNodeUVUnwrap(method, selection, seam, margin, fill_holes))
        return node.outputs[0].Vector

    def distribute_points_on_faces(self, distribute_method='RANDOM', use_legacy_normal=False, distance_min=0.0, density_max=10.0, density=10.0, density_factor=1.0, seed=0, selection=True):
        """The Distribute Points on Faces node places points on the surface of the input geometry object. Point, corner, and polygon attributes of the input geometry are transferred to the generated points. That includes vertex weights and UV maps. Additionally, the node has Normal and Rotation outputs.
        #### Path
        - Point > Distribute Points on Faces
        #### Properties
        - `distribute_method`: `RANDOM`, `POISSON`
        #### Outputs:
        - `#0 points: Geometry = None`
        - `#1 normal: Vector = (0.0, 0.0, 0.0)`
        - `#2 rotation: Vector = (0.0, 0.0, 0.0)`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeDistributePointsOnFaces.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/distribute_points_on_faces.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeDistributePointsOnFaces.html)
        """
        selection = selection if self._selection is None else self.selection
        node = new_node(*nodes.GeometryNodeDistributePointsOnFaces(distribute_method, use_legacy_normal, self, selection, distance_min, density_max, density, density_factor, seed))
        ret = typing.NamedTuple("GeometryNodeDistributePointsOnFaces", [("points", Points), ("normal", Vector), ("rotation", Vector)])
        return ret(node.outputs[0].Points, node.outputs[1].Vector, node.outputs[2].Vector)


class Points(Geometry):

    @property
    def domain_size(self):
        """The Domain Size outputs the size of an attribute domain on the selected geometry type, for example, the number of edges in a mesh, or the number of points in a point cloud.
        #### Path
        - Attribute > Domain Size Node
        #### Outputs:
        - `#0 point_count: Integer = 0`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeAttributeDomainSize.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/domain_size.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeDomainSize.html)
        """
        node = new_node(*nodes.GeometryNodeAttributeDomainSize("POINTCLOUD", self))
        ret = typing.NamedTuple("GeometryNodeAttributeDomainSize", [("point_count", Integer)])
        return ret(node.outputs[0].Integer)

    def merge_by_distance(self, distance=0.001, mode="ALL", selection=True):
        """The Merge by Distance node merges selected mesh vertices or point cloud points within a given distance, merging surrounding geometry where necessary. This operation is similar to the Merge by Distance operator or the Weld Modifier.
        #### Path
        - Geometry > Operations > Merge by Distance Node
        #### Properties
        - `mode`: `ALL`, `CONNECTED`
        #### Outputs:
        - `#0 geometry: Geometry = None`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeMergeByDistance.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/operations/merge_by_distance.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeMergeByDistance.html)
        """
        selection = selection if self._selection is None else self.selection
        node = new_node(*nodes.GeometryNodeMergeByDistance(mode, self, selection, distance))
        return node.outputs[0].Points

    def to_vertices(self, selection=True):
        """The Points to Vertices node generate a mesh vertex in the output geometry for each point cloud point in the input geometry.
        #### Path
        - Point > Points to Vertices Node
        #### Outputs:
        - `#0 mesh: Geometry = None`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodePointsToVertices.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/points_to_vertices.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodePointsToVertices.html)
        """
        selection = selection if self._selection is None else self.selection
        node = new_node(*nodes.GeometryNodePointsToVertices(self, selection))
        return node.outputs[0].Mesh

    def to_volume(self, resolution_mode='VOXEL_AMOUNT', density=1.0, voxel_size=0.3, voxel_amount=64.0, radius=0.5):
        """The Points to Volume node generates a fog volume sphere around every point in the input geometry. The new volume grid is named “density”.
        #### Path
        - Point > Points to Volume Node
        #### Properties:
        - `resolution_mode`: `VOXEL_AMOUNT`, `VOXEL_SIZE`
        #### Outputs:
        - `#0 volume: Geometry = None`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodePointsToVolume.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/points_to_volume.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodePointsToVolume.html)
        """
        node = new_node(*nodes.GeometryNodePointsToVolume(resolution_mode, self, density, voxel_size, voxel_amount, radius))
        return node.outputs[0].Volume

    def set_radius(self, radius=0.05, selection=True):
        """The Set Point Radius node controls the size each selected point cloud point should display with in the viewport.
        #### Path
        - Point > Set Point Radius Node
        #### Outputs:
        - `#0 points: Geometry = None`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeSetPointRadius.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/set_point_radius.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetPointRadius.html)
        """
        selection = selection if self._selection is None else self.selection
        node = new_node(*nodes.GeometryNodeSetPointRadius(self, selection, radius))
        return node.outputs[0].Points


class Instances(Geometry):

    @property
    def domain_size(self):
        """The Domain Size outputs the size of an attribute domain on the selected geometry type, for example, the number of edges in a mesh, or the number of points in a point cloud.
        #### Path
        - Attribute > Domain Size Node
        #### Outputs:
        - `#5 instance_count: Integer = 0`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeAttributeDomainSize.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/domain_size.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeDomainSize.html)
        """
        node = new_node(*nodes.GeometryNodeAttributeDomainSize("INSTANCES", self))
        ret = typing.NamedTuple("GeometryNodeAttributeDomainSize", [("instance_count", Integer)])
        return ret(node.outputs[5].Integer)

    def separate(self, selection=True):
        """The Separate Geometry node produces two geometry outputs. Based on the Selection input, the input geometry is split between the two outputs.
        #### Path
        - Geometry > Operations > Separate Geometry Node
        #### Outputs:
        - `#0 selection: Geometry = None`
        - `#1 inverted: Geometry = None`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeSeparateGeometry.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/operations/separate_geometry.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeSeparateGeometry.html)
        """
        selection = selection if self._selection is None else self.selection
        node = new_node(*nodes.GeometryNodeSeparateGeometry("INSTANCE", self, selection))
        ret = typing.NamedTuple("GeometryNodeSeparateGeometry", [("selected", Instances), ("inverted", Instances)])
        return ret(node.outputs[0].Instances, node.outputs[1].Instances)

    def scale_elements(self, domain='FACE', scale_mode='UNIFORM', scale=1.0, center: "Vector" = None, axis=(1.0, 0.0, 0.0), selection=True):
        """The Scale Elements Node scales groups of connected edges and faces. When multiple selected faces/edges share the same vertices, they are scaled together. The center and scaling factor is averaged in this case.
        #### Path
        - Mesh > Operations > Scale Elements Node
        #### Properties
        - `domain`: `FACE`, `EDGE`
        - `scale_mode`: `UNIFORM`, `SINGLE_AXIS`
        #### Outputs:
        - `#0 geometry: Geometry = None`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeScaleElements.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/operations/scale_elements.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeScaleElements.html)
        """
        selection = selection if self._selection is None else self.selection
        node = new_node(*nodes.GeometryNodeScaleElements(domain, scale_mode, self, selection, scale, center, axis))
        return node.outputs[0].Instances

    def to_points(self, position: "Vector" = None, radius=0.05, selection=True):
        """The Instances to Points node generates points at the origins of top-level instances. Attributes on the instance domain are moved to the point cloud points.
        #### Path
        - Instances > Instances to Points Node
        #### Outputs:
        - `#0 points: Geometry = None`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeInstancesToPoints.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/instances_to_points.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeInstancesToPoints.html)
        """
        selection = selection if self._selection is None else self.selection
        node = new_node(*nodes.GeometryNodeInstancesToPoints(self, selection, position, radius))
        return node.outputs[0].Points

    def rotate_instances(self, rotation=(0.0, 0.0, 0.0), pivot_point=(0.0, 0.0, 0.0), local_space=True, selection=True):
        """The Rotate Instances node rotates geometry instances in local or global space.
        #### Path
        - Instances > Rotate Instances Node
        #### Outputs:
        - `#0 instances: Geometry = None`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeRotateInstances.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/rotate_instances.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeRotateInstances.html)
        """
        selection = selection if self._selection is None else self.selection
        node = new_node(*nodes.GeometryNodeRotateInstances(self, selection, rotation, pivot_point, local_space))
        return node.outputs[0].Instances

    def scale_instances(self, scale=(1.0, 1.0, 1.0), center=(0.0, 0.0, 0.0), local_space=True, selection=True):
        """The Scale Instances node scales geometry instances in local or global space.
        #### Path
        - Instances > Scale Instances Node
        #### Outputs:
        - `#0 instances: Geometry = None`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeScaleInstances.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/scale_instances.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeScaleInstances.html)
        """
        selection = selection if self._selection is None else self.selection
        node = new_node(*nodes.GeometryNodeScaleInstances(self, selection, scale, center, local_space))
        return node.outputs[0].Instances

    def translate_instances(self, translation=(0.0, 0.0, 0.0), local_space=True, selection=True):
        """The Translate Instances node moves top-level geometry instances in local or global space.
        #### Path
        - Instances > Translate Instances Node
        #### Outputs:
        - `#0 instances: Geometry = None`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeTranslateInstances.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/translate_instances.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeTranslateInstances.html)
        """
        selection = selection if self._selection is None else self.selection
        node = new_node(*nodes.GeometryNodeTranslateInstances(self, selection, translation, local_space))
        return node.outputs[0].Instances

    def realize_instances(self, legacy_behavior=False):
        """The Realize Instances node makes any instances (efficient duplicates of the same geometry) into real geometry data. This makes it possible to affect each instance individually, whereas without this node, the exact same changes are applied to every instance of the same geometry. However, performance can become much worse when the input contains many instances of complex geometry, which is a fundamental limitation when procedurally processing geometry.
        #### Path
        - Instances > Realize Instances Node
        #### Outputs:
        - `#0 geometry: Geometry = None`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeRealizeInstances.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/realize_instances.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeRealizeInstances.html)
        """
        node = new_node(*nodes.GeometryNodeRealizeInstances(legacy_behavior, self))
        return node.outputs[0].Geometry

    @ property
    def rotation(self):
        """The Instance Rotation outputs the XYZ Euler rotation of each top-level instance in the local space of the modifier object.
        #### Path
        - Instances > Instance Rotation Node
        #### Outputs:
        - `#0 rotation: Vector = (0.0, 0.0, 0.0)`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeInputInstanceRotation.png)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/instance_rotation.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputInstanceRotation.html)
        """
        node = new_node(*nodes.GeometryNodeInputInstanceRotation())
        return node.outputs[0].Vector

    @ property
    def scale(self):
        """The Instance Scale outputs the size of top-level instances on each axis in the local space of the modifier object.
        #### Path
        - Instances > Instance Scale Node
        #### Outputs:
        - `#0 scale: Vector = (0.0, 0.0, 0.0)`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeInputInstanceScale.png)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/instance_scale.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputInstanceScale.html)
        """
        node = new_node(*nodes.GeometryNodeInputInstanceScale())
        return node.outputs[0].Vector


class Volume(Geometry):

    def distribute_points_random(self, density=1.0, seed=0):
        """The Distribute Points in Volume node creates points inside of volume grids. The node has two basic modes of operation: distributing points randomly, or in a regular grid. Both methods operate on all of the float grids in the volume.
        #### Path
        - Point > Distribute Points in Volume
        #### Outputs:
        - `#0 points: Geometry = None`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeDistributePointsInVolume.png)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/distribute_points_in_volume.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeDistributePointsInVolume.html)
        """
        node = new_node(*nodes.GeometryNodeDistributePointsInVolume("DENSITY_RANDOM", self, density, seed))
        return node.outputs[0].Points

    def distribute_points_grid(self, spacing=(0.3, 0.3, 0.3), threshold=0.1):
        """The Distribute Points in Volume node creates points inside of volume grids. The node has two basic modes of operation: distributing points randomly, or in a regular grid. Both methods operate on all of the float grids in the volume.
        #### Path
        - Point > Distribute Points in Volume
        #### Outputs:
        - `#0 points: Geometry = None`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeDistributePointsInVolume.png)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/distribute_points_in_volume.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeDistributePointsInVolume.html)
        """
        node = new_node(*nodes.GeometryNodeDistributePointsInVolume("DENSITY_GRID", self, 1.0, 0, spacing, threshold))
        return node.outputs[0].Points

    def to_mesh(self, resolution_mode='GRID', voxel_size=0.3, voxel_amount=64.0, threshold=0.1, adaptivity=0.0):
        """The Volume to Mesh node generates a mesh on the “surface” of a volume. The surface is defined by a threshold value. All voxels with a larger value than the threshold are considered to be inside.
        #### Path
        - Volume > Volume to Mesh Node
        #### Properties:
        - `resolution_mode`: `GRID`, `VOXEL_AMOUNT`, `VOXEL_SIZE`
        #### Outputs:
        - `#0 mesh: Geometry = None`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeVolumeToMesh.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/volume/volume_to_mesh.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeVolumeToMesh.html)
        """
        node = new_node(*nodes.GeometryNodeVolumeToMesh(resolution_mode, self, voxel_size, voxel_amount, threshold, adaptivity))
        return node.outputs[0].Mesh


def CurveArc(resolution=16, radius=1.0, start_angle=math.radians(0.0), sweep_angle=math.radians(315.0), connect_center=False, invert_arc=False):
    """The Arc node generates a poly spline arc. The node has two modes, Radius and Points.
    #### Path
    - Curve > Primitives > Arc Node
    #### Outputs:
    - `#0 curve: Geometry = None`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeCurveArc.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/primitives/arc.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveArc.html)
    """
    node = new_node(*nodes.GeometryNodeCurveArc("RADIUS", resolution, radius=radius, start_angle=start_angle, sweep_angle=sweep_angle, connect_center=connect_center, invert_arc=invert_arc))
    return node.outputs[0].Curve


def CurveArcPoints(resolution=16, start=(-1.0, 0.0, 0.0), middle=(0.0, 2.0, 0.0), end=(1.0, 0.0, 0.0), offset_angle=math.radians(0.0), connect_center=False, invert_arc=False):
    """The Arc node generates a poly spline arc. The node has two modes, Radius and Points.
    #### Path
    - Curve > Primitives > Arc Node
    #### Outputs:
    - `#0 curve: Geometry = None`
    - `#1 center: Vector = (0.0, 0.0, 0.0)`
    - `#2 normal: Vector = (0.0, 0.0, 0.0)`
    - `#3 radius: Float = 0.0`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeCurveArc.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/primitives/arc.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveArc.html)
    """
    node = new_node(*nodes.GeometryNodeCurveArc("RADIUS", resolution, start, middle, end, offset_angle=offset_angle, connect_center=connect_center, invert_arc=invert_arc))
    ret = typing.NamedTuple("CurveArc", [("curve", Curve), ("center", Vector), ("normal", Vector), ("radius", Float)])
    return ret(node.outputs[0].Curve, node.outputs[1].Vector, node.outputs[2].Vector, node.outputs[3].Float)


def BezierSegment(mode='POSITION', resolution=16, start=(-1.0, 0.0, 0.0), start_handle=(-0.5, 0.5, 0.0), end_handle=(0.0, 0.0, 0.0), end=(1.0, 0.0, 0.0)):
    """The Bézier Segment node generates a 2D Bézier spline from the given control points and handles.
    #### Path
    - Curve > Primitives > Bézier Segment Node
    #### Properties
    - `mode`: `POSITION`, `OFFSET`
    #### Outputs:
    - `#0 curve: Geometry = None`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeCurvePrimitiveBezierSegment.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/primitives/bezier_segment.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurvePrimitiveBezierSegment.html)
    """
    node = new_node(*nodes.GeometryNodeCurvePrimitiveBezierSegment(mode, resolution, start, start_handle, end_handle, end))
    return node.outputs[0].Curve


def CurveCircle(radius=1.0, resolution=32):
    """The Curve Circle node generates a poly spline circle.
    #### Path
    - Curve > Primitives > Curve Circle Node
    #### Outputs:
    - `#0 curve: Geometry = None`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeCurvePrimitiveCircle.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/primitives/curve_circle.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurvePrimitiveCircle.html)
    """
    node = new_node(*nodes.GeometryNodeCurvePrimitiveCircle("RADIUS", resolution=resolution, radius=radius))
    return node.outputs[0].Curve


def CurveCirclePoints(resolution=32, point_1=(-1.0, 0.0, 0.0), point_2=(0.0, 1.0, 0.0), point_3=(1.0, 0.0, 0.0)):
    """The Curve Circle node generates a poly spline circle.
    #### Path
    - Curve > Primitives > Curve Circle Node
    #### Outputs:
    - `#0 curve: Geometry = None`
    - `#1 center: Vector = (0.0, 0.0, 0.0)`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeCurvePrimitiveCircle.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/primitives/curve_circle.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurvePrimitiveCircle.html)
    """
    node = new_node(*nodes.GeometryNodeCurvePrimitiveCircle("POINTS", resolution=resolution, point_1=point_1, point_2=point_2, point_3=point_3))
    ret = typing.NamedTuple("GeometryNodeCurvePrimitiveCircle", [("curve", Curve), ("center", Vector)])
    return ret(node.outputs[0].Curve, node.outputs[1].Vector)


def CurveLine(start=(0.0, 0.0, 0.0), end=(0.0, 0.0, 1.0), direction=(0.0, 0.0, 1.0), length=1.0, mode='POINTS'):
    """The Curve Line node generates poly spline line.
    #### Path
    - Curve > Primitives > Curve Line Node
    #### Properties
    - `mode`: `POINTS`, `DIRECTION`
    #### Outputs:
    - `#0 curve: Geometry = None`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeCurvePrimitiveLine.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/primitives/curve_line.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurvePrimitiveLine.html)
    """
    node = new_node(*nodes.GeometryNodeCurvePrimitiveLine(mode, start, end, direction, length))
    return node.outputs[0].Curve


def CurveSpiral(resolution=32, rotations=2.0, start_radius=1.0, end_radius=2.0, height=2.0, reverse=False):
    """The Curve Spiral node generates a poly spline in a spiral shape. It can be used to create springs or other similar objects. By default the spiral twists in a clockwise fashion.
    #### Path
    - Curve > Primitives > Curve Spiral Node

    #### Outputs:
    - `#0 curve: Geometry = None`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeCurveSpiral.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/primitives/curve_spiral.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveSpiral.html)
    """
    node = new_node(*nodes.GeometryNodeCurveSpiral(resolution, rotations, start_radius, end_radius, height, reverse))
    return node.outputs[0].Curve


def CurveQuadraticBezier(resolution=16, start=(-1.0, 0.0, 0.0), middle=(0.0, 2.0, 0.0), end=(1.0, 0.0, 0.0)):
    """The Quadratic Bézier node generates a poly spline curve from the given control points. The generated shape is a parabola.
    #### Path
    - Curve > Primitives > Quadratic Bézier Node

    #### Outputs:
    - `#0 curve: Geometry = None`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeCurveQuadraticBezier.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/primitives/quadratic_bezier.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveQuadraticBezier.html)
    """
    node = new_node(*nodes.GeometryNodeCurveQuadraticBezier(resolution, start, middle, end))
    return node.outputs[0].Curve


def Rectangle(width=2.0, height=2.0):
    """The Quadrilateral node generates a polygon with four points, with different modes.
    #### Path
    - Curve > Primitives > Quadrilateral Node
    #### Outputs:
    - `#0 curve: Geometry = None`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeCurvePrimitiveQuadrilateral.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/primitives/quadrilateral.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurvePrimitiveQuadrilateral.html)
    """
    node = new_node(*nodes.GeometryNodeCurvePrimitiveQuadrilateral("RECTANGLE", width, height))
    return node.outputs[0].Curve


def Parallelogram(width=2.0, height=2.0, offset=1.0):
    """The Quadrilateral node generates a polygon with four points, with different modes.
    #### Path
    - Curve > Primitives > Quadrilateral Node
    #### Outputs:
    - `#0 curve: Geometry = None`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeCurvePrimitiveQuadrilateral.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/primitives/quadrilateral.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurvePrimitiveQuadrilateral.html)
    """
    node = new_node(*nodes.GeometryNodeCurvePrimitiveQuadrilateral("PARALLELOGRAM", width, height, offset=offset))
    return node.outputs[0].Curve


def Trapezoid(height=2.0, bottom_width=4.0, top_width=2.0, offset=1.0):
    """The Quadrilateral node generates a polygon with four points, with different modes.
    #### Path
    - Curve > Primitives > Quadrilateral Node
    #### Outputs:
    - `#0 curve: Geometry = None`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeCurvePrimitiveQuadrilateral.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/primitives/quadrilateral.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurvePrimitiveQuadrilateral.html)
    """
    node = new_node(*nodes.GeometryNodeCurvePrimitiveQuadrilateral("TRAPEZOID", height=height, bottom_width=bottom_width, top_width=top_width, offset=offset))
    return node.outputs[0].Curve


def Kite(width=2.0, bottom_height=3.0, top_height=1.0):
    """The Quadrilateral node generates a polygon with four points, with different modes.
    #### Path
    - Curve > Primitives > Quadrilateral Node
    #### Outputs:
    - `#0 curve: Geometry = None`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeCurvePrimitiveQuadrilateral.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/primitives/quadrilateral.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurvePrimitiveQuadrilateral.html)
    """
    node = new_node(*nodes.GeometryNodeCurvePrimitiveQuadrilateral("KITE", width=width, bottom_height=bottom_height, top_height=top_height))
    return node.outputs[0].Curve


def Quadrangle(point_1=(-1.0, -1.0, 0.0), point_2=(1.0, -1.0, 0.0), point_3=(1.0, 1.0, 0.0), point_4=(-1.0, 1.0, 0.0)):
    """The Quadrilateral node generates a polygon with four points, with different modes.
    #### Path
    - Curve > Primitives > Quadrilateral Node
    #### Outputs:
    - `#0 curve: Geometry = None`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeCurvePrimitiveQuadrilateral.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/primitives/quadrilateral.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurvePrimitiveQuadrilateral.html)
    """
    node = new_node(*nodes.GeometryNodeCurvePrimitiveQuadrilateral("POINTS", point_1=point_1, point_2=point_2, point_3=point_3, point_4=point_4))
    return node.outputs[0].Curve


def CurveStar(points=8, inner_radius=1.0, outer_radius=2.0, twist=math.radians(0.0)):
    """The Star node generates a poly spline in a star pattern by connecting alternating points of two circles. The points on the inner circle are offset by a rotation so that they lie in between the points on the outer circle. This offset can be changed with the twist input.
    #### Path
    - Curve > Primitives > Star Node

    #### Outputs:
    - `#0 curve: Geometry = None`
    - `#1 outer_points: Boolean = False`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeCurveStar.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/primitives/star.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveStar.html)
    """
    node = new_node(*nodes.GeometryNodeCurveStar(points, inner_radius, outer_radius, twist))
    return node.outputs[0].Curve, node.outputs[1].Boolean


def MeshCone(fill_type='NGON', vertices=32, side_segments=1, fill_segments=1, radius_top=0.0, radius_bottom=1.0, depth=2.0):
    """The Cone node generates a cone mesh that is optionally truncated.
    #### Path
    - Mesh > Primitives > Cone Node
    #### Properties
    - `fill_type`: `NGON`, `NONE`, `TRIANGLE_FAN`
    #### Outputs:
    - `#0 mesh: Geometry = None`
    - `#1 top: Boolean = False`
    - `#2 bottom: Boolean = False`
    - `#3 side: Boolean = False`
    - `#4 uv_map: Vector = (0.0, 0.0, 0.0)`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeMeshCone.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/primitives/cone.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshCone.html)
    """
    node = new_node(*nodes.GeometryNodeMeshCone(fill_type, vertices, side_segments, fill_segments, radius_top, radius_bottom, depth))
    ret = typing.NamedTuple("GeometryNodeMeshCone", [("mesh", Mesh), ("top", Boolean), ("bottom", Boolean), ("side", Boolean), ("uv_map", Vector)])
    return ret(node.outputs[0].Mesh, node.outputs[1].Boolean, node.outputs[2].Boolean, node.outputs[3].Boolean, node.outputs[4].Vector)


def MeshCube(size=(1.0, 1.0, 1.0), vertices_x=2, vertices_y=2, vertices_z=2):
    """The Cube node generates a cuboid mesh with variable side lengths and subdivisions. The inside of the mesh is still hollow like a normal cube.
    #### Path
    - Mesh > Primitives > Cube Node
    #### Outputs:
    - `#0 mesh: Geometry = None`
    - `#1 uv_map: Vector = (0.0, 0.0, 0.0)`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeMeshCube.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/primitives/cube.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshCube.html)
    """
    node = new_node(*nodes.GeometryNodeMeshCube(size, vertices_x, vertices_y, vertices_z))
    ret = typing.NamedTuple("GeometryNodeMeshCube", [("mesh", Mesh), ("uv_map", Vector)])
    return ret(node.outputs[0].Mesh, node.outputs[1].Vector)


def MeshCylinder(fill_type='NGON', vertices=32, side_segments=1, fill_segments=1, radius=1.0, depth=2.0):
    """The Cylinder node generates a cylinder mesh. It is similar to the Cone node but always uses the same radius for the circles at the top and bottom.
    #### Path
    - Mesh > Primitives > Cylinder Node
    #### Properties
    - `fill_type`: `NGON`, `NONE`, `TRIANGLE_FAN`
    #### Outputs:
    - `#0 mesh: Geometry = None`
    - `#1 top: Boolean = False`
    - `#2 side: Boolean = False`
    - `#3 bottom: Boolean = False`
    - `#4 uv_map: Vector = (0.0, 0.0, 0.0)`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeMeshCylinder.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/primitives/cylinder.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshCylinder.html)
    """
    node = new_node(*nodes.GeometryNodeMeshCylinder(fill_type, vertices, side_segments, fill_segments, radius, depth))
    ret = typing.NamedTuple("GeometryNodeMeshCylinder", [("mesh", Mesh), ("top", Boolean), ("side", Boolean), ("bottom", Boolean), ("uv_map", Vector)])
    return ret(node.outputs[0].Mesh, node.outputs[1].Boolean, node.outputs[2].Boolean, node.outputs[3].Boolean, node.outputs[4].Vector)


def MeshGrid(size_x=1.0, size_y=1.0, vertices_x=3, vertices_y=3):
    """The Grid node generates a planar mesh on the XY plane.
    #### Path
    - Mesh > Primitives > Grid Node
    #### Outputs:
    - `#0 mesh: Geometry = None`
    - `#1 uv_map: Vector = (0.0, 0.0, 0.0)`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeMeshGrid.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/primitives/grid.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshGrid.html)
    """
    node = new_node(*nodes.GeometryNodeMeshGrid(size_x, size_y, vertices_x, vertices_y))
    ret = typing.NamedTuple("GeometryNodeMeshGrid", [("mesh", Mesh), ("uv_map", Vector)])
    return ret(node.outputs[0].Mesh, node.outputs[1].Vector)


def MeshIcoSphere(radius=1.0, subdivisions=1):
    """The Icosphere node generates a spherical mesh that consists of equally sized triangles.
    #### Path
    - Mesh > Primitives > Icosphere Node
    #### Outputs:
    - `#0 mesh: Geometry = None`
    - `#1 uv_map: Vector = (0.0, 0.0, 0.0)`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeMeshIcoSphere.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/primitives/icosphere.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshIcoSphere.html)
    """
    node = new_node(*nodes.GeometryNodeMeshIcoSphere(radius, subdivisions))
    ret = typing.NamedTuple("GeometryNodeMeshIcoSphere", [("mesh", Mesh), ("uv_map", Vector)])
    return ret(node.outputs[0].Mesh, node.outputs[1].Vector)


def MeshCircle(vertices=32, radius=1.0, fill_type='NONE'):
    """The Mesh Circle node generates a circular ring of edges that is optionally filled with faces.
    #### Path
    - Mesh > Primitives > Mesh Circle Node
    #### Properties
    - `fill_type`: `NONE`, `NGON`, `TRIANGLE_FAN`
    #### Outputs:
    - `#0 mesh: Geometry = None`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeMeshCircle.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/primitives/mesh_circle.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshCircle.html)
    """
    node = new_node(*nodes.GeometryNodeMeshCircle(fill_type, vertices, radius))
    return node.outputs[0].Mesh


def MeshLine(count_mode='TOTAL', mode='OFFSET', count=10, resolution=1.0, start_location=(0.0, 0.0, 0.0), offset=(0.0, 0.0, 1.0)):
    """The Mesh Line node generates vertices in a line and connects them with edges.
    #### Path
    - Mesh > Primitives > Mesh Line Node
    #### Properties
    - `count_mode`: `TOTAL`, `RESOLUTION`
    - `mode`: `OFFSET`, `END_POINTS`
    #### Outputs:
    - `#0 mesh: Geometry = None`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeMeshLine.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/primitives/mesh_line.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshLine.html)
    """
    node = new_node(*nodes.GeometryNodeMeshLine(count_mode, mode, count, resolution, start_location, offset))
    return node.outputs[0].Mesh


def MeshUVSphere(segments=32, rings=16, radius=1.0):
    """The UV Sphere node generates a spherical mesh mostly out of quads except for triangles at the top and bottom.
    #### Path
    - Mesh > Primitives > UV Sphere Node
    #### Outputs:
    - `#0 mesh: Geometry = None`
    - `#1 uv_map: Vector = (0.0, 0.0, 0.0)`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeMeshUVSphere.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/primitives/uv_sphere.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshUVSphere.html)
    """
    node = new_node(*nodes.GeometryNodeMeshUVSphere(segments, rings, radius))
    ret = typing.NamedTuple("GeometryNodeMeshUVSphere", [("mesh", Mesh), ("uv_map", Vector)])
    return ret(node.outputs[0].Mesh, node.outputs[1].Vector)


def InputPoints(count=1, position=(0.0, 0.0, 0.0), radius=0.1):
    """The Points node generate a point cloud with positions and radii defined by fields.
    #### Path
    - Point > Points Node
    #### Outputs:
    - `#0 geometry: Geometry = None`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodePoints.png)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/points.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodePoints.html)
    """
    node = new_node(*nodes.GeometryNodePoints(count, position, radius))
    return node.outputs[0].Points


def VolumeCube(density=1.0, background=0.0, min=(-1.0, -1.0, -1.0), max=(1.0, 1.0, 1.0), resolution_x=32, resolution_y=32, resolution_z=32):
    """The Volume Cube generates a volume from scratch by evaluating an input field on every single voxel in a rectangular prism. The Density field defines the output volume grid’s value at every voxel. The field can only depend on the Position Node.
    #### Path
    - Volume > Volume Cube Node
    #### Outputs:
    - `#0 volume: Geometry = None`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeVolumeCube.png)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/volume/volume_cube.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeVolumeCube.html)
    """
    node = new_node(*nodes.GeometryNodeVolumeCube(density, background, min, max, resolution_x, resolution_y, resolution_z))
    return node.outputs[0].Volume


def join(*items: "Geometry"):
    """The Join Geometry node merges separately generated geometries into a single one. If the geometry inputs contain different types of data, the output will also contain different data types.
    - In-Place Operation
    #### Path
    - Geometry > Join Geometry Node
    #### Outputs:
    - `#0 geometry: Geometry = None`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeJoinGeometry.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/join_geometry.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeJoinGeometry.html)
    """
    if len(items) == 1 and isinstance(items[0], (tuple, list)):
        return join(*items[0])
    items = list(reversed(items))
    node = new_node(*nodes.GeometryNodeJoinGeometry())
    for item in items:
        new_link(item.bsocket, node.bnode.inputs[0])
    return node.outputs[0].Geometry


from .datasocks import Float, Vector, Integer, Color, Boolean
