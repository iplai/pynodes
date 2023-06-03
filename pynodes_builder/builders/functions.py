import math, typing
from . import nodes
from pynodes.core import new_node


def GeometryNodeAttributeStatistic(data_type='FLOAT', domain='POINT', geometry=None, selection=True, attribute=0.0, attribute_001=(0.0, 0.0, 0.0)):
    """The Attribute Statistic node evaluates a field on a geometry and outputs a statistic about the entire data set.
    #### Path
    - Attribute > Attribute Statistic Node
    #### Properties:
    - `data_type`: `FLOAT`, `FLOAT_VECTOR`
    - `domain`: `POINT`, `EDGE`, `FACE`, `CORNER`, `CURVE`, `INSTANCE`
    #### Outputs:
    - `#0 mean: Float = 0.0`
    - `#1 median: Float = 0.0`
    - `#2 sum: Float = 0.0`
    - `#3 min: Float = 0.0`
    - `#4 max: Float = 0.0`
    - `#5 range: Float = 0.0`
    - `#6 standard_deviation: Float = 0.0`
    - `#7 variance: Float = 0.0`
    - `#8 mean_001: Vector = (0.0, 0.0, 0.0)`
    - `#9 median_001: Vector = (0.0, 0.0, 0.0)`
    - `#10 sum_001: Vector = (0.0, 0.0, 0.0)`
    - `#11 min_001: Vector = (0.0, 0.0, 0.0)`
    - `#12 max_001: Vector = (0.0, 0.0, 0.0)`
    - `#13 range_001: Vector = (0.0, 0.0, 0.0)`
    - `#14 standard_deviation_001: Vector = (0.0, 0.0, 0.0)`
    - `#15 variance_001: Vector = (0.0, 0.0, 0.0)`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeAttributeStatistic.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/attribute_statistic.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeAttributeStatistic.html)
    """
    # selection = selection if self._selection is None else self.selection
    node = new_node(*nodes.GeometryNodeAttributeStatistic(data_type, domain, geometry, selection, attribute, attribute_001))
    ret = typing.NamedTuple("GeometryNodeAttributeStatistic", [("mean", Float), ("median", Float), ("sum", Float), ("min", Float), ("max", Float), ("range", Float), ("standard_deviation", Float), ("variance", Float), ("mean", Vector), ("median", Vector), ("sum", Vector), ("min", Vector), ("max", Vector), ("range", Vector), ("standard_deviation", Vector), ("variance", Vector)])
    return ret(node.outputs[0].Float, node.outputs[1].Float, node.outputs[2].Float, node.outputs[3].Float, node.outputs[4].Float, node.outputs[5].Float, node.outputs[6].Float, node.outputs[7].Float, node.outputs[8].Vector, node.outputs[9].Vector, node.outputs[10].Vector, node.outputs[11].Vector, node.outputs[12].Vector, node.outputs[13].Vector, node.outputs[14].Vector, node.outputs[15].Vector)
    return node.outputs[0].Float, node.outputs[1].Float, node.outputs[2].Float, node.outputs[3].Float, node.outputs[4].Float, node.outputs[5].Float, node.outputs[6].Float, node.outputs[7].Float, node.outputs[8].Vector, node.outputs[9].Vector, node.outputs[10].Vector, node.outputs[11].Vector, node.outputs[12].Vector, node.outputs[13].Vector, node.outputs[14].Vector, node.outputs[15].Vector


def GeometryNodeAttributeDomainSize(component='MESH', geometry=None):
    """The Domain Size outputs the size of an attribute domain on the selected geometry type, for example, the number of edges in a mesh, or the number of points in a point cloud.
    #### Path
    - Attribute > Domain Size Node
    #### Properties:
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
    node = new_node(*nodes.GeometryNodeAttributeDomainSize(component, geometry))
    ret = typing.NamedTuple("GeometryNodeAttributeDomainSize", [("point_count", Integer), ("edge_count", Integer), ("face_count", Integer), ("face_corner_count", Integer), ("spline_count", Integer), ("instance_count", Integer)])
    return ret(node.outputs[0].Integer, node.outputs[1].Integer, node.outputs[2].Integer, node.outputs[3].Integer, node.outputs[4].Integer, node.outputs[5].Integer)
    return node.outputs[0].Integer, node.outputs[1].Integer, node.outputs[2].Integer, node.outputs[3].Integer, node.outputs[4].Integer, node.outputs[5].Integer


def GeometryNodeBlurAttribute(data_type='FLOAT', value_float=0.0, value_int=0, value_vector=(0.0, 0.0, 0.0), value_color=(0.0, 0.0, 0.0, 0.0), iterations=1, weight=1.0):
    """The Blur Attribute node smooths attribute values between neighboring geometry elements.
    #### Path
    - Attribute > Blur Attribute Node
    #### Properties:
    - `data_type`: `FLOAT`, `INT`, `FLOAT_VECTOR`, `FLOAT_COLOR`
    #### Outputs:
    - `#0 value_float: Float = 0.0`
    - `#1 value_int: Integer = 0`
    - `#2 value_vector: Vector = (0.0, 0.0, 0.0)`
    - `#3 value_color: Color = (0.0, 0.0, 0.0, 0.0)`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeBlurAttribute.jpg)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/blur_attribute.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeBlurAttribute.html)
    """
    node = new_node(*nodes.GeometryNodeBlurAttribute(data_type, value_float, value_int, value_vector, value_color, iterations, weight))
    ret = typing.NamedTuple("GeometryNodeBlurAttribute", [("value", Float), ("value", Integer), ("value", Vector), ("value", Color)])
    return ret(node.outputs[0].Float, node.outputs[1].Integer, node.outputs[2].Vector, node.outputs[3].Color)
    return node.outputs[0].Float, node.outputs[1].Integer, node.outputs[2].Vector, node.outputs[3].Color


def GeometryNodeCaptureAttribute(data_type='FLOAT', domain='POINT', geometry=None, value=(0.0, 0.0, 0.0), value_001=0.0, value_002=(0.0, 0.0, 0.0, 0.0), value_003=False, value_004=0):
    """The Capture Attribute node stores the result of a field on a geometry, and outputs the data as a node socket so it can be used by other nodes.
    #### Path
    - Attribute > Capture Attribute Node
    #### Properties:
    - `data_type`: `FLOAT`, `INT`, `FLOAT_VECTOR`, `FLOAT_COLOR`, `BOOLEAN`
    - `domain`: `POINT`, `EDGE`, `FACE`, `CORNER`, `CURVE`, `INSTANCE`
    #### Outputs:
    - `#0 geometry: Geometry = None`
    - `#1 attribute: Vector = (0.0, 0.0, 0.0)`
    - `#2 attribute_001: Float = 0.0`
    - `#3 attribute_002: Color = (0.0, 0.0, 0.0, 0.0)`
    - `#4 attribute_003: Boolean = False`
    - `#5 attribute_004: Integer = 0`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeCaptureAttribute.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/capture_attribute.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeCaptureAttribute.html)
    """
    node = new_node(*nodes.GeometryNodeCaptureAttribute(data_type, domain, geometry, value, value_001, value_002, value_003, value_004))
    ret = typing.NamedTuple("GeometryNodeCaptureAttribute", [("geometry", Geometry), ("attribute", Vector), ("attribute", Float), ("attribute", Color), ("attribute", Boolean), ("attribute", Integer)])
    return ret(node.outputs[0].Geometry, node.outputs[1].Vector, node.outputs[2].Float, node.outputs[3].Color, node.outputs[4].Boolean, node.outputs[5].Integer)
    return node.outputs[0].Geometry, node.outputs[1].Vector, node.outputs[2].Float, node.outputs[3].Color, node.outputs[4].Boolean, node.outputs[5].Integer


def GeometryNodeRemoveAttribute(geometry=None, name=''):
    """The Remove Named Attribute node deletes an attribute with a certain name from its geometry input. Any attribute that exists on geometry data will be automatically propagated when the geometry storing it is changed, which can be an expensive operation, so using this node can be a simple way to optimize the performance of a geometry node tree or even to lower the memory usage of the entire scene.
    #### Path
    - Attribute > Remove Named Attribute Node
    #### Outputs:
    - `#0 geometry: Geometry = None`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeRemoveNamedAttribute.png)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/remove_named_attribute.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeRemoveAttribute.html)
    """
    node = new_node(*nodes.GeometryNodeRemoveAttribute(geometry, name))
    return node.outputs[0].Geometry


def GeometryNodeStoreNamedAttribute(data_type='FLOAT', domain='POINT', geometry=None, selection=True, name='', value_vector=(0.0, 0.0, 0.0), value_float=0.0, value_color=(0.0, 0.0, 0.0, 0.0), value_bool=False, value_int=0):
    """The Store Named Attribute node stores the result of a field on a geometry as an attribute with the specified name. If the attribute already exists, the data type and domain will be updated to the values chosen in the node. However, keep in mind that the domain and data type of Built-In Attributes cannot be changed.
    #### Path
    - Attribute > Store Named Attribute Node
    #### Properties:
    - `data_type`: `FLOAT`, `INT`, `FLOAT_VECTOR`, `FLOAT_COLOR`, `BYTE_COLOR`, `BOOLEAN`, `FLOAT2`
    - `domain`: `POINT`, `EDGE`, `FACE`, `CORNER`, `CURVE`, `INSTANCE`
    #### Outputs:
    - `#0 geometry: Geometry = None`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeStoreNamedAttribute.png)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/attribute/store_named_attribute.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeStoreNamedAttribute.html)
    """
    # selection = selection if self._selection is None else self.selection
    node = new_node(*nodes.GeometryNodeStoreNamedAttribute(data_type, domain, geometry, selection, name, value_vector, value_float, value_color, value_bool, value_int))
    return node.outputs[0].Geometry


def FunctionNodeInputBool(boolean=False):
    """The Boolean node provides a Boolean value.
    #### Path
    - Input > Constant > Boolean Node
    #### Outputs:
    - `#0 boolean: Boolean = False`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_FunctionNodeInputBool.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/constant/boolean.html) [[API]](https://docs.blender.org/api/current/bpy.types.FunctionNodeInputBool.html)
    """
    node = new_node(*nodes.FunctionNodeInputBool(boolean))
    return node.outputs[0].Boolean


def FunctionNodeInputColor():
    """The Color node outputs the color value chosen with the color picker widget.
    #### Path
    - Input > Constant > Color Node
    #### Outputs:
    - `#0 color: Color = (0.0, 0.0, 0.0, 0.0)`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_FunctionNodeInputColor.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/constant/color.html) [[API]](https://docs.blender.org/api/current/bpy.types.FunctionNodeInputColor.html)
    """
    node = new_node(*nodes.FunctionNodeInputColor())
    return node.outputs[0].Color


def GeometryNodeInputImage(image=None):
    """The Image node provides access to a image file which allows you to conveniently enter and switch images for multiple nodes in the tree.
    #### Path
    - Input > Constant > Image Node
    #### Outputs:
    - `#0 image: Image = None`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeImage.jpg)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/constant/image.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputImage.html)
    """
    node = new_node(*nodes.GeometryNodeInputImage(image))
    return node.outputs[0].Image


def FunctionNodeInputInt(integer=0):
    """The Integer node provides an integer value.
    #### Path
    - Input > Constant > Integer Node
    #### Outputs:
    - `#0 integer: Integer = 0`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_FunctionNodeInputInt.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/constant/integer.html) [[API]](https://docs.blender.org/api/current/bpy.types.FunctionNodeInputInt.html)
    """
    node = new_node(*nodes.FunctionNodeInputInt(integer))
    return node.outputs[0].Integer


def GeometryNodeInputMaterial(material=None):
    """The Material input node outputs a single material. It can be connected to other material sockets to make using the same material name in multiple places more convenient.
    #### Path
    - Input > Constant > Material Node
    #### Outputs:
    - `#0 material: Material = None`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeInputMaterial.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/constant/material.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMaterial.html)
    """
    node = new_node(*nodes.GeometryNodeInputMaterial(material))
    return node.outputs[0].Material


def FunctionNodeInputString(string=''):
    """The String input node creates a single string. It can be connected to attribute name sockets to make using the same attribute name in multiple places more convenient.
    #### Path
    - Input > Constant > String Node
    #### Outputs:
    - `#0 string: String = ""`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_FunctionNodeInputString.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/constant/string.html) [[API]](https://docs.blender.org/api/current/bpy.types.FunctionNodeInputString.html)
    """
    node = new_node(*nodes.FunctionNodeInputString(string))
    return node.outputs[0].String


def ShaderNodeValue():
    """The Value Node is a simple node to input numerical values to other nodes in the tree.
    #### Path
    - Input > Constant > Value Node
    #### Outputs:
    - `#0 value: Float = 0.0`

    ![](https://docs.blender.org/manual/en/latest/_images/compositing_node-types_CompositorNodeValue.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/constant/value.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeValue.html)
    """
    node = new_node(*nodes.ShaderNodeValue())
    return node.outputs[0].Float


def FunctionNodeInputVector(vector=(0.0, 0.0, 0.0)):
    """The Vector input node creates a single vector.
    #### Path
    - Input > Constant > Vector Node
    #### Outputs:
    - `#0 vector: Vector = (0.0, 0.0, 0.0)`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_FunctionNodeInputVector.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/constant/vector.html) [[API]](https://docs.blender.org/api/current/bpy.types.FunctionNodeInputVector.html)
    """
    node = new_node(*nodes.FunctionNodeInputVector(vector))
    return node.outputs[0].Vector


def GeometryNodeCollectionInfo(transform_space='ORIGINAL', collection=None, separate_children=False, reset_children=False):
    """The Collection Info node gets information from collections. This can be useful to control parameters in the geometry node tree with an external collection.
    #### Path
    - Input > Scene > Collection Info Node
    #### Properties:
    - `transform_space`: `ORIGINAL`, `RELATIVE`
    #### Outputs:
    - `#0 instances: Geometry = None`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeCollectionInfo.jpeg)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/scene/collection_info.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeCollectionInfo.html)
    """
    node = new_node(*nodes.GeometryNodeCollectionInfo(transform_space, collection, separate_children, reset_children))
    return node.outputs[0].Instances


def GeometryNodeImageInfo(image=None, frame=0):
    """The Image Info node gets information from image and animation. This can be useful to generate parameters in the geometry node for arbitrary images. Image information can be either general or frame-specific.
    #### Path
    - Input > Scene > Image Info Node
    #### Outputs:
    - `#0 width: Integer = 0`
    - `#1 height: Integer = 0`
    - `#2 has_alpha: Boolean = False`
    - `#3 frame_count: Integer = 0`
    - `#4 fps: Float = 0.0`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeImageInfo.jpg)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/scene/image_info.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeImageInfo.html)
    """
    node = new_node(*nodes.GeometryNodeImageInfo(image, frame))
    ret = typing.NamedTuple("GeometryNodeImageInfo", [("width", Integer), ("height", Integer), ("has_alpha", Boolean), ("frame_count", Integer), ("fps", Float)])
    return ret(node.outputs[0].Integer, node.outputs[1].Integer, node.outputs[2].Boolean, node.outputs[3].Integer, node.outputs[4].Float)
    return node.outputs[0].Integer, node.outputs[1].Integer, node.outputs[2].Boolean, node.outputs[3].Integer, node.outputs[4].Float


def GeometryNodeIsViewport():
    """The Is Viewport node outputs true when geometry nodes are evaluated for the viewport. For the final render the node outputs false.
    #### Path
    - Input > Scene > Is Viewport Node
    #### Outputs:
    - `#0 is_viewport: Boolean = False`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeIsViewport.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/scene/is_viewport.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeIsViewport.html)
    """
    node = new_node(*nodes.GeometryNodeIsViewport())
    return node.outputs[0].Boolean


def GeometryNodeObjectInfo(transform_space='ORIGINAL', object=None, as_instance=False):
    """The Object Info node gets information from objects. This can be useful to control parameters in the geometry node tree with an external object, either directly by using its geometry, or via its transformation properties.
    #### Path
    - Input > Scene > Object Info Node
    #### Properties:
    - `transform_space`: `ORIGINAL`, `RELATIVE`
    #### Outputs:
    - `#0 location: Vector = (0.0, 0.0, 0.0)`
    - `#1 rotation: Vector = (0.0, 0.0, 0.0)`
    - `#2 scale: Vector = (0.0, 0.0, 0.0)`
    - `#3 geometry: Geometry = None`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeObjectInfo.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/scene/object_info.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeObjectInfo.html)
    """
    node = new_node(*nodes.GeometryNodeObjectInfo(transform_space, object, as_instance))
    ret = typing.NamedTuple("GeometryNodeObjectInfo", [("location", Vector), ("rotation", Vector), ("scale", Vector), ("geometry", Geometry)])
    return ret(node.outputs[0].Vector, node.outputs[1].Vector, node.outputs[2].Vector, node.outputs[3].Geometry)
    return node.outputs[0].Vector, node.outputs[1].Vector, node.outputs[2].Vector, node.outputs[3].Geometry


def GeometryNodeSelfObject():
    """The Self Object node outputs the object that contains the geometry nodes modifier currently being executed. This can be used to retrieve the original transforms.
    #### Path
    - Input > Scene > Self Object Node
    #### Outputs:
    - `#0 self_object: Object = None`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeSelfObject.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/scene/self_object.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeSelfObject.html)
    """
    node = new_node(*nodes.GeometryNodeSelfObject())
    return node.outputs[0].Object


def GeometryNodeViewer(data_type='FLOAT', domain='AUTO', geometry=None, value=0.0, value_001=(0.0, 0.0, 0.0), value_002=(0.0, 0.0, 0.0, 0.0), value_003=0, value_004=False):
    """The Viewer node allows viewing data from inside a geometry node group in the Spreadsheet Editor and the 3D Viewport.
    #### Path
    - Output > Viewer Node
    #### Properties:
    - `data_type`: `FLOAT`, `INT`, `FLOAT_VECTOR`, `FLOAT_COLOR`, `BOOLEAN`
    - `domain`: `AUTO`, `POINT`, `EDGE`, `FACE`, `CORNER`, `CURVE`, `INSTANCE`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeViewer.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/output/viewer.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeViewer.html)
    """
    node = new_node(*nodes.GeometryNodeViewer(data_type, domain, geometry, value, value_001, value_002, value_003, value_004))
    return node


def GeometryNodeInputID():
    """The ID node gives an integer value indicating the stable random identifier of each element on the point domain, which is stored in the id attribute.
    #### Path
    - Geometry > Read > ID Node
    #### Outputs:
    - `#0 id: Integer = 0`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeInputID.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/read/id.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputID.html)
    """
    node = new_node(*nodes.GeometryNodeInputID())
    return node.outputs[0].Integer


def GeometryNodeInputIndex():
    """The Index node gives an integer value indicating the position of each element in the list, starting at zero. This depends on the internal order of the data in the geometry, which is not necessarily visible in the 3D Viewport. However, the index value is visible in the left-most column in the Spreadsheet Editor.
    #### Path
    - Geometry > Read > Index Node
    #### Outputs:
    - `#0 index: Integer = 0`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeInputIndex.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/read/input_index.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputIndex.html)
    """
    node = new_node(*nodes.GeometryNodeInputIndex())
    return node.outputs[0].Integer


def GeometryNodeInputNamedAttribute(data_type='FLOAT', name=''):
    """The Named Attribute node outputs the data of an attribute based on the context of where it is connected (the Field Context).
    #### Path
    - Geometry > Read > Named Attribute Node
    #### Properties:
    - `data_type`: `FLOAT`, `INT`, `FLOAT_VECTOR`, `FLOAT_COLOR`, `BOOLEAN`
    #### Outputs:
    - `#0 attribute_vector: Vector = (0.0, 0.0, 0.0)`
    - `#1 attribute_float: Float = 0.0`
    - `#2 attribute_color: Color = (0.0, 0.0, 0.0, 0.0)`
    - `#3 attribute_bool: Boolean = False`
    - `#4 attribute_int: Integer = 0`
    - `#5 exists: Boolean = False`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeNamedAttribute.png)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/read/named_attribute.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNamedAttribute.html)
    """
    node = new_node(*nodes.GeometryNodeInputNamedAttribute(data_type, name))
    ret = typing.NamedTuple("GeometryNodeInputNamedAttribute", [("attribute", Vector), ("attribute", Float), ("attribute", Color), ("attribute", Boolean), ("attribute", Integer), ("exists", Boolean)])
    return ret(node.outputs[0].Vector, node.outputs[1].Float, node.outputs[2].Color, node.outputs[3].Boolean, node.outputs[4].Integer, node.outputs[5].Boolean)
    return node.outputs[0].Vector, node.outputs[1].Float, node.outputs[2].Color, node.outputs[3].Boolean, node.outputs[4].Integer, node.outputs[5].Boolean


def GeometryNodeInputNormal():
    """The Normal node returns a vector for each evaluated point indicating the normal direction. The output can depend on the attribute domain used in the node evaluating the field, but the output is always a normalized unit vector.
    #### Path
    - Geometry > Read > Normal Node
    #### Outputs:
    - `#0 normal: Vector = (0.0, 0.0, 0.0)`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeInputNormal.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/read/normal.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputNormal.html)
    """
    node = new_node(*nodes.GeometryNodeInputNormal())
    return node.outputs[0].Vector


def GeometryNodeInputPosition():
    """The Position node outputs a vector of each point of the geometry the node is connected to.
    #### Path
    - Geometry > Read > Position Node
    #### Outputs:
    - `#0 position: Vector = (0.0, 0.0, 0.0)`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeInputPosition.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/read/position.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputPosition.html)
    """
    node = new_node(*nodes.GeometryNodeInputPosition())
    return node.outputs[0].Vector


def GeometryNodeInputRadius():
    """The Radius node outputs the radius value at each point on the evaluated geometry. For curves, this value is used for things like determining the size of the mesh created in the Curve to Mesh node. For point clouds, the value is used for the display size of the point in the viewport.
    #### Path
    - Geometry > Read > Radius Node
    #### Outputs:
    - `#0 radius: Float = 1.0`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeInputRadius.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/read/radius.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputRadius.html)
    """
    node = new_node(*nodes.GeometryNodeInputRadius())
    return node.outputs[0].Float


def GeometryNodeSetID(geometry=None, selection=True, id: "Integer"=None):
    """The Set ID node fills the id attribute on the input geometry. If the attribute does not exist yet, it will be created with a default value of zero. The ID is also created by the Distribute Points on Faces, and it is used in the Random Value Node and other nodes if it exists.
    #### Path
    - Geometry > Write > Set ID Node
    #### Outputs:
    - `#0 geometry: Geometry = None`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeSetID.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/write/set_id.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetID.html)
    """
    # selection = selection if self._selection is None else self.selection
    node = new_node(*nodes.GeometryNodeSetID(geometry, selection, id))
    return node.outputs[0].Geometry


def GeometryNodeSetPosition(geometry=None, selection=True, position: "Vector"=None, offset=(0.0, 0.0, 0.0)):
    """The Set Position node controls the location of each point, the same way as controlling the position attribute. If the input geometry contains instances, this node will affect the location of the origin of each instance.
    #### Path
    - Geometry > Write > Set Position Node
    #### Outputs:
    - `#0 geometry: Geometry = None`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeSetPosition.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/write/set_position.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetPosition.html)
    """
    # selection = selection if self._selection is None else self.selection
    node = new_node(*nodes.GeometryNodeSetPosition(geometry, selection, position, offset))
    return node.outputs[0].Geometry


def GeometryNodeProximity(target_element='FACES', target=None, source_position: "Vector"=None):
    """The Geometry Proximity node computes the closest location on the target geometry.
    #### Path
    - Geometry > Sample > Geometry Proximity Node
    #### Properties:
    - `target_element`: `FACES`, `POINTS`, `EDGES`
    #### Outputs:
    - `#0 position: Vector = (0.0, 0.0, 0.0)`
    - `#1 distance: Float = 0.0`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeProximity.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/sample/geometry_proximity.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeProximity.html)
    """
    node = new_node(*nodes.GeometryNodeProximity(target_element, target, source_position))
    ret = typing.NamedTuple("GeometryNodeProximity", [("position", Vector), ("distance", Float)])
    return ret(node.outputs[0].Vector, node.outputs[1].Float)
    return node.outputs[0].Vector, node.outputs[1].Float


def GeometryNodeRaycast(data_type='FLOAT', mapping='INTERPOLATED', target_geometry=None, attribute=(0.0, 0.0, 0.0), attribute_001=0.0, attribute_002=(0.0, 0.0, 0.0, 0.0), attribute_003=False, attribute_004=0, source_position: "Vector"=None, ray_direction=(0.0, 0.0, -1.0), ray_length=100.0):
    """The Raycast node intersects rays from one geometry onto another. The source geometry is defined by the context of the node that the Raycast node is connected to. Each ray computes hit points on the target mesh and outputs normals, distances and any surface attribute specified.
    #### Path
    - Geometry > Sample > Raycast Node
    #### Properties:
    - `data_type`: `FLOAT`, `INT`, `FLOAT_VECTOR`, `FLOAT_COLOR`, `BOOLEAN`
    - `mapping`: `INTERPOLATED`, `NEAREST`
    #### Outputs:
    - `#0 is_hit: Boolean = False`
    - `#1 hit_position: Vector = (0.0, 0.0, 0.0)`
    - `#2 hit_normal: Vector = (0.0, 0.0, 0.0)`
    - `#3 hit_distance: Float = 0.0`
    - `#4 attribute: Vector = (0.0, 0.0, 0.0)`
    - `#5 attribute_001: Float = 0.0`
    - `#6 attribute_002: Color = (0.0, 0.0, 0.0, 0.0)`
    - `#7 attribute_003: Boolean = False`
    - `#8 attribute_004: Integer = 0`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeRaycast.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/sample/raycast.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeRaycast.html)
    """
    node = new_node(*nodes.GeometryNodeRaycast(data_type, mapping, target_geometry, attribute, attribute_001, attribute_002, attribute_003, attribute_004, source_position, ray_direction, ray_length))
    ret = typing.NamedTuple("GeometryNodeRaycast", [("is_hit", Boolean), ("hit_position", Vector), ("hit_normal", Vector), ("hit_distance", Float), ("attribute", Vector), ("attribute", Float), ("attribute", Color), ("attribute", Boolean), ("attribute", Integer)])
    return ret(node.outputs[0].Boolean, node.outputs[1].Vector, node.outputs[2].Vector, node.outputs[3].Float, node.outputs[4].Vector, node.outputs[5].Float, node.outputs[6].Color, node.outputs[7].Boolean, node.outputs[8].Integer)
    return node.outputs[0].Boolean, node.outputs[1].Vector, node.outputs[2].Vector, node.outputs[3].Float, node.outputs[4].Vector, node.outputs[5].Float, node.outputs[6].Color, node.outputs[7].Boolean, node.outputs[8].Integer


def GeometryNodeSampleIndex(data_type='FLOAT', domain='POINT', clamp=False, geometry=None, value_float=0.0, value_int=0, value_vector=(0.0, 0.0, 0.0), value_color=(0.0, 0.0, 0.0, 0.0), value_bool=False, index=0):
    """The Sample Index node retrieves values from a source geometry at a specific index.
    #### Path
    - Geometry > Sample > Sample Index Node
    #### Properties:
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
    node = new_node(*nodes.GeometryNodeSampleIndex(data_type, domain, clamp, geometry, value_float, value_int, value_vector, value_color, value_bool, index))
    ret = typing.NamedTuple("GeometryNodeSampleIndex", [("value", Float), ("value", Integer), ("value", Vector), ("value", Color), ("value", Boolean)])
    return ret(node.outputs[0].Float, node.outputs[1].Integer, node.outputs[2].Vector, node.outputs[3].Color, node.outputs[4].Boolean)
    return node.outputs[0].Float, node.outputs[1].Integer, node.outputs[2].Vector, node.outputs[3].Color, node.outputs[4].Boolean


def GeometryNodeSampleNearest(domain='POINT', geometry=None, sample_position: "Vector"=None):
    """The Sample Nearest node retrieves the index of the geometry element in its input geometry that is closest to the input position. This node is similar to the Geometry Proximity Node, but it outputs the index of the closest element instead of its distance from the current location.
    #### Path
    - Geometry > Sample > Sample Nearest Node
    #### Properties:
    - `domain`: `POINT`, `EDGE`, `FACE`, `CORNER`
    #### Outputs:
    - `#0 index: Integer = 0`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeSampleNearest.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/sample/sample_nearest.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeSampleNearest.html)
    """
    node = new_node(*nodes.GeometryNodeSampleNearest(domain, geometry, sample_position))
    return node.outputs[0].Integer


def GeometryNodeBoundBox(geometry=None):
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
    node = new_node(*nodes.GeometryNodeBoundBox(geometry))
    ret = typing.NamedTuple("GeometryNodeBoundBox", [("bounding_box", Geometry), ("min", Vector), ("max", Vector)])
    return ret(node.outputs[0].Geometry, node.outputs[1].Vector, node.outputs[2].Vector)
    return node.outputs[0].Geometry, node.outputs[1].Vector, node.outputs[2].Vector


def GeometryNodeConvexHull(geometry=None):
    """The Convex Hull node outputs a convex mesh that is enclosing all points in the input geometry.
    #### Path
    - Geometry > Operations > Convex Hull Node
    #### Outputs:
    - `#0 convex_hull: Geometry = None`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeConvexHull.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/operations/convex_hull.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeConvexHull.html)
    """
    node = new_node(*nodes.GeometryNodeConvexHull(geometry))
    return node.outputs[0].Geometry


def GeometryNodeDeleteGeometry(domain='POINT', mode='ALL', geometry=None, selection=True):
    """The Delete Geometry node removes the selected part of a geometry. It behaves similarly to the Delete tool in Edit Mode. The type of elements to be deleted can be specified with the domain and mode properties.
    #### Path
    - Geometry > Operations > Delete Geometry Node
    #### Properties:
    - `domain`: `POINT`, `EDGE`, `FACE`, `CURVE`, `INSTANCE`
    - `mode`: `ALL`, `EDGE_FACE`, `ONLY_FACE`
    #### Outputs:
    - `#0 geometry: Geometry = None`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeDeleteGeometry.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/operations/delete_geometry.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeDeleteGeometry.html)
    """
    # selection = selection if self._selection is None else self.selection
    node = new_node(*nodes.GeometryNodeDeleteGeometry(domain, mode, geometry, selection))
    return node.outputs[0].Geometry


def GeometryNodeDuplicateElements(domain='POINT', geometry=None, selection=True, amount=1):
    """The Duplicate Elements node creates a new geometry with the specified elements from the input duplicated an arbitrary number of times. The positions of elements are not changed, so all of the duplicates will be at the exact same location.
    #### Path
    - Geometry > Operations > Duplicate Elements Node
    #### Properties:
    - `domain`: `POINT`, `EDGE`, `FACE`, `SPLINE`, `INSTANCE`
    #### Outputs:
    - `#0 geometry: Geometry = None`
    - `#1 duplicate_index: Integer = 0`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeDuplicateElements.png)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/operations/duplicate_elements.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeDuplicateElements.html)
    """
    # selection = selection if self._selection is None else self.selection
    node = new_node(*nodes.GeometryNodeDuplicateElements(domain, geometry, selection, amount))
    ret = typing.NamedTuple("GeometryNodeDuplicateElements", [("geometry", Geometry), ("duplicate_index", Integer)])
    return ret(node.outputs[0].Geometry, node.outputs[1].Integer)
    return node.outputs[0].Geometry, node.outputs[1].Integer


def GeometryNodeMergeByDistance(mode='ALL', geometry=None, selection=True, distance=0.001):
    """The Merge by Distance node merges selected mesh vertices or point cloud points within a given distance, merging surrounding geometry where necessary. This operation is similar to the Merge by Distance operator or the Weld Modifier.
    #### Path
    - Geometry > Operations > Merge by Distance Node
    #### Properties:
    - `mode`: `ALL`, `CONNECTED`
    #### Outputs:
    - `#0 geometry: Geometry = None`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeMergeByDistance.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/operations/merge_by_distance.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeMergeByDistance.html)
    """
    # selection = selection if self._selection is None else self.selection
    node = new_node(*nodes.GeometryNodeMergeByDistance(mode, geometry, selection, distance))
    return node.outputs[0].Geometry


def GeometryNodeTransform(geometry=None, translation=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(1.0, 1.0, 1.0)):
    """The Transform Geometry Node allows you to move, rotate or scale the geometry. The transformation is applied to the entire geometry, and not per element. The Set Position Node is used for moving individual points of a geometry. For transforming instances individually, the instance translate, rotate, or scale nodes can be used.
    #### Path
    - Geometry > Operations > Transform Geometry Node
    #### Outputs:
    - `#0 geometry: Geometry = None`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeTransformGeometry.jpg)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/operations/transform_geometry.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeTransform.html)
    """
    node = new_node(*nodes.GeometryNodeTransform(geometry, translation, rotation, scale))
    return node.outputs[0].Geometry


def GeometryNodeSeparateComponents(geometry=None):
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
    node = new_node(*nodes.GeometryNodeSeparateComponents(geometry))
    ret = typing.NamedTuple("GeometryNodeSeparateComponents", [("mesh", Geometry), ("point_cloud", Geometry), ("curve", Geometry), ("volume", Geometry), ("instances", Geometry)])
    return ret(node.outputs[0].Mesh, node.outputs[1].Geometry, node.outputs[2].Curve, node.outputs[3].Volume, node.outputs[4].Instances)
    return node.outputs[0].Mesh, node.outputs[1].Geometry, node.outputs[2].Curve, node.outputs[3].Volume, node.outputs[4].Instances


def GeometryNodeSeparateGeometry(domain='POINT', geometry=None, selection=True):
    """The Separate Geometry node produces two geometry outputs. Based on the Selection input, the input geometry is split between the two outputs.
    #### Path
    - Geometry > Operations > Separate Geometry Node
    #### Properties:
    - `domain`: `POINT`, `EDGE`, `FACE`, `CURVE`, `INSTANCE`
    #### Outputs:
    - `#0 selection: Geometry = None`
    - `#1 inverted: Geometry = None`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeSeparateGeometry.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/operations/separate_geometry.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeSeparateGeometry.html)
    """
    # selection = selection if self._selection is None else self.selection
    node = new_node(*nodes.GeometryNodeSeparateGeometry(domain, geometry, selection))
    ret = typing.NamedTuple("GeometryNodeSeparateGeometry", [("selection", Geometry), ("inverted", Geometry)])
    return ret(node.outputs[0].Geometry, node.outputs[1].Geometry)
    return node.outputs[0].Geometry, node.outputs[1].Geometry


def GeometryNodeJoinGeometry(geometry=None):
    """The Join Geometry node merges separately generated geometries into a single one. If the geometry inputs contain different types of data, the output will also contain different data types.
    #### Path
    - Geometry > Join Geometry Node
    #### Outputs:
    - `#0 geometry: Geometry = None`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeJoinGeometry.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/join_geometry.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeJoinGeometry.html)
    """
    node = new_node(*nodes.GeometryNodeJoinGeometry(geometry))
    return node.outputs[0].Geometry


def GeometryNodeGeometryToInstance(geometry=None):
    """The Geometry to Instance node turns every connected input geometry into an instance. Visually, the node has a similar result as the Join Geometry Node, but it outputs the result as separate instances instead. The geometry data itself isn’t actually joined.
    #### Path
    - Geometry > Geometry to Instance Node
    #### Outputs:
    - `#0 instances: Geometry = None`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeGeometryToInstance.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/geometry_to_instance.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeGeometryToInstance.html)
    """
    node = new_node(*nodes.GeometryNodeGeometryToInstance(geometry))
    return node.outputs[0].Instances


def GeometryNodeInputCurveHandlePositions(relative=False):
    """The Curve Handle Position node outputs the position of each of a Bézier spline’s handles. If the curve does not contain Bézier splines, the node will output zero.
    #### Path
    - Curve > Read > Curve Handle Position Node
    #### Outputs:
    - `#0 left: Vector = (0.0, 0.0, 0.0)`
    - `#1 right: Vector = (0.0, 0.0, 0.0)`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeInputCurveHandlePositions.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/read/curve_handle_position.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputCurveHandlePositions.html)
    """
    node = new_node(*nodes.GeometryNodeInputCurveHandlePositions(relative))
    ret = typing.NamedTuple("GeometryNodeInputCurveHandlePositions", [("left", Vector), ("right", Vector)])
    return ret(node.outputs[0].Vector, node.outputs[1].Vector)
    return node.outputs[0].Vector, node.outputs[1].Vector


def GeometryNodeCurveLength(curve=None):
    """The Curve Length node outputs the length of all splines added together.
    #### Path
    - Curve > Read > Curve Length Node
    #### Outputs:
    - `#0 length: Float = 0.0`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeCurveLength.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/read/curve_length.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveLength.html)
    """
    node = new_node(*nodes.GeometryNodeCurveLength(curve))
    return node.outputs[0].Float


def GeometryNodeInputTangent():
    """The Curve Tangent node outputs the direction that a curve points in at each control point, depending on the direction of the curve (which can be controlled with the Reverse Curve Node). The output values are normalized vectors.
    #### Path
    - Curve > Read > Curve Tangent Node
    #### Outputs:
    - `#0 tangent: Vector = (0.0, 0.0, 0.0)`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeInputTangent.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/read/curve_tangent.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputTangent.html)
    """
    node = new_node(*nodes.GeometryNodeInputTangent())
    return node.outputs[0].Vector


def GeometryNodeInputCurveTilt():
    """The Curve Tilt node outputs the angle used to turn the curve normal around the direction of the curve tangent in its evaluated points. Keep in mind that the output is per control point, just like the values that can be controlled in curve Edit Mode. For NURBS and Bézier splines, the values will be interpolated to the final evaluated points.
    #### Path
    - Curve > Read > Curve Tilt Node
    #### Outputs:
    - `#0 tilt: Float = 0.0`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeInputCurveTilt.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/read/curve_tilt.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputCurveTilt.html)
    """
    node = new_node(*nodes.GeometryNodeInputCurveTilt())
    return node.outputs[0].Float


def GeometryNodeCurveEndpointSelection(start_size=1, end_size=1):
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


def GeometryNodeCurveHandleTypeSelection(handle_type='AUTO', mode={'RIGHT', 'LEFT'}):
    """Creates a selection based on the handle types of the control points.
    #### Path
    - Curve > Read > Handle Type Selection Node
    #### Properties:
    - `handle_type`: `AUTO`, `FREE`, `VECTOR`, `ALIGN`
    #### Outputs:
    - `#0 selection: Boolean = False`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeCurveHandleTypeSelection.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/read/handle_type_selection.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveHandleTypeSelection.html)
    """
    node = new_node(*nodes.GeometryNodeCurveHandleTypeSelection(handle_type, mode))
    return node.outputs[0].Boolean


def GeometryNodeInputSplineCyclic():
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


def GeometryNodeSplineLength():
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
    return node.outputs[0].Float, node.outputs[1].Integer


def GeometryNodeSplineParameter():
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
    node = new_node(*nodes.GeometryNodeSplineParameter())
    ret = typing.NamedTuple("GeometryNodeSplineParameter", [("factor", Float), ("length", Float), ("index", Integer)])
    return ret(node.outputs[0].Float, node.outputs[1].Float, node.outputs[2].Integer)
    return node.outputs[0].Float, node.outputs[1].Float, node.outputs[2].Integer


def GeometryNodeInputSplineResolution():
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


def GeometryNodeSampleCurve(data_type='FLOAT', mode='FACTOR', use_all_curves=False, curves=None, value_float=0.0, value_int=0, value_vector=(0.0, 0.0, 0.0), value_color=(0.0, 0.0, 0.0, 0.0), value_bool=False, factor=0.0, length=0.0, curve_index=0):
    """The Sample Curve calculates a point on a curve at a certain distance from the start of the curve, specified by the length or factor inputs. It also outputs data retrieved from that position on the curve. The sampled values are linearly interpolated from the values at the evaluated curve points at each side of the sampled point.
    #### Path
    - Curve > Sample > Sample Curve Node
    #### Properties:
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
    node = new_node(*nodes.GeometryNodeSampleCurve(data_type, mode, use_all_curves, curves, value_float, value_int, value_vector, value_color, value_bool, factor, length, curve_index))
    ret = typing.NamedTuple("GeometryNodeSampleCurve", [("value", Float), ("value", Integer), ("value", Vector), ("value", Color), ("value", Boolean), ("position", Vector), ("tangent", Vector), ("normal", Vector)])
    return ret(node.outputs[0].Float, node.outputs[1].Integer, node.outputs[2].Vector, node.outputs[3].Color, node.outputs[4].Boolean, node.outputs[5].Vector, node.outputs[6].Vector, node.outputs[7].Vector)
    return node.outputs[0].Float, node.outputs[1].Integer, node.outputs[2].Vector, node.outputs[3].Color, node.outputs[4].Boolean, node.outputs[5].Vector, node.outputs[6].Vector, node.outputs[7].Vector


def GeometryNodeSetCurveNormal(mode='MINIMUM_TWIST', curve=None, selection=True):
    """The Set Curve Normal controls the method used to calculate curve normals for every curve.
    #### Path
    - Curve > Write > Set Curve Normal Node
    #### Properties:
    - `mode`: `MINIMUM_TWIST`, `Z_UP`
    #### Outputs:
    - `#0 curve: Geometry = None`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeSetCurveNormal.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/write/set_curve_normal.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetCurveNormal.html)
    """
    # selection = selection if self._selection is None else self.selection
    node = new_node(*nodes.GeometryNodeSetCurveNormal(mode, curve, selection))
    return node.outputs[0].Curve


def GeometryNodeSetCurveRadius(curve=None, selection=True, radius=0.005):
    """The Set Curve Radius controls the radius of the curve, used for operations like the size of the profile in the Curve to Mesh node. The value is set for every control point, and is then interpolated to each evaluated point in between the control points.
    #### Path
    - Curve > Write > Set Curve Radius Node
    #### Outputs:
    - `#0 curve: Geometry = None`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeSetCurveRadius.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/write/set_curve_radius.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetCurveRadius.html)
    """
    # selection = selection if self._selection is None else self.selection
    node = new_node(*nodes.GeometryNodeSetCurveRadius(curve, selection, radius))
    return node.outputs[0].Curve


def GeometryNodeSetCurveTilt(curve=None, selection=True, tilt=math.radians(0.0)):
    """The Set Curve Tilt controls the tilt angle at each curve control point. That angle rotates normal vector which is generated at each point when evaluating the curve. The normal then can be retrieved with the Normal Node.
    #### Path
    - Curve > Write > Set Curve Tilt Node
    #### Outputs:
    - `#0 curve: Geometry = None`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeSetCurveTilt.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/write/set_curve_tilt.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetCurveTilt.html)
    """
    # selection = selection if self._selection is None else self.selection
    node = new_node(*nodes.GeometryNodeSetCurveTilt(curve, selection, tilt))
    return node.outputs[0].Curve


def GeometryNodeSetCurveHandlePositions(mode='LEFT', curve=None, selection=True, position: "Vector"=None, offset=(0.0, 0.0, 0.0)):
    """The Set Handle Positions node sets the positions for the handles of Bézier curves. They can be used to alter the generated shape of the curve. The input node for this data is the Curve Handle Position Node. See the Bézier curves page for more details.
    #### Path
    - Curve > Write > Set Handle Positions Node
    #### Properties:
    - `mode`: `LEFT`, `RIGHT`
    #### Outputs:
    - `#0 curve: Geometry = None`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeSetCurveHandlePositions.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/write/set_handle_positions.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetCurveHandlePositions.html)
    """
    # selection = selection if self._selection is None else self.selection
    node = new_node(*nodes.GeometryNodeSetCurveHandlePositions(mode, curve, selection, position, offset))
    return node.outputs[0].Curve


def GeometryNodeCurveSetHandles(handle_type='AUTO', mode={'RIGHT', 'LEFT'}, curve=None, selection=True):
    """Sets the handle type for the points on the Bézier curve that are in the selection.
    #### Path
    - Curve > Write > Set Handle Type Node
    #### Properties:
    - `handle_type`: `AUTO`, `FREE`, `VECTOR`, `ALIGN`
    #### Outputs:
    - `#0 curve: Geometry = None`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeCurveSetHandles.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/write/set_handle_type.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveSetHandles.html)
    """
    # selection = selection if self._selection is None else self.selection
    node = new_node(*nodes.GeometryNodeCurveSetHandles(handle_type, mode, curve, selection))
    return node.outputs[0].Curve


def GeometryNodeSetSplineCyclic(geometry=None, selection=True, cyclic=False):
    """The Set Spline Cyclic controls whether each spline will loop back on itself. Each spline has the same number of control points whether or not it is set as cyclic. But when displaying in the viewport or for operations with other nodes, a connection will be made between the first and last control points.
    #### Path
    - Curve > Write > Set Spline Cyclic Node
    #### Outputs:
    - `#0 geometry: Geometry = None`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeSetSplineCyclic.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/write/set_spline_cyclic.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetSplineCyclic.html)
    """
    # selection = selection if self._selection is None else self.selection
    node = new_node(*nodes.GeometryNodeSetSplineCyclic(geometry, selection, cyclic))
    return node.outputs[0].Geometry


def GeometryNodeSetSplineResolution(geometry=None, selection=True, resolution=12):
    """The Set Spline Resolution node sets the value for how many evaluated points should be generated on the curve for every control point. It only has an effect on NURBS and Bézier splines. The evaluated points are displayed in the viewport, used in the Curve to Mesh Node node, and optionally used in the Resample Curve Node.
    #### Path
    - Curve > Write > Set Spline Resolution Node
    #### Outputs:
    - `#0 geometry: Geometry = None`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeSetSplineResolution.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/write/set_spline_resolution.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetSplineResolution.html)
    """
    # selection = selection if self._selection is None else self.selection
    node = new_node(*nodes.GeometryNodeSetSplineResolution(geometry, selection, resolution))
    return node.outputs[0].Geometry


def GeometryNodeCurveSplineType(spline_type='POLY', curve=None, selection=True):
    """Sets the spline type for the splines in the curve component that are in the selection.
    #### Path
    - Curve > Write > Set Spline Type Node
    #### Properties:
    - `spline_type`: `POLY`, `CATMULL_ROM`, `BEZIER`, `NURBS`
    #### Outputs:
    - `#0 curve: Geometry = None`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeCurveSplineType.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/write/set_spline_type.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveSplineType.html)
    """
    # selection = selection if self._selection is None else self.selection
    node = new_node(*nodes.GeometryNodeCurveSplineType(spline_type, curve, selection))
    return node.outputs[0].Curve


def GeometryNodeCurveToMesh(curve=None, profile_curve=None, fill_caps=False):
    """The Curve to Mesh node converts all splines of a curve to a mesh. Optionally, a profile curve can be provided to give the curve a custom shape.
    #### Path
    - Curve > Operations > Curve to Mesh Node
    #### Outputs:
    - `#0 mesh: Geometry = None`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeCurveToMesh.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/operations/curve_to_mesh.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveToMesh.html)
    """
    node = new_node(*nodes.GeometryNodeCurveToMesh(curve, profile_curve, fill_caps))
    return node.outputs[0].Mesh


def GeometryNodeCurveToPoints(mode='COUNT', curve=None, count=10, length=0.1):
    """The Curve to Points node generates a point cloud from a curve.
    #### Path
    - Curve > Operations > Curve to Points Node
    #### Properties:
    - `mode`: `COUNT`, `EVALUATED`, `LENGTH`
    #### Outputs:
    - `#0 points: Geometry = None`
    - `#1 tangent: Vector = (0.0, 0.0, 0.0)`
    - `#2 normal: Vector = (0.0, 0.0, 0.0)`
    - `#3 rotation: Vector = (0.0, 0.0, 0.0)`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeCurveToPoints.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/operations/curve_to_points.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveToPoints.html)
    """
    node = new_node(*nodes.GeometryNodeCurveToPoints(mode, curve, count, length))
    ret = typing.NamedTuple("GeometryNodeCurveToPoints", [("points", Geometry), ("tangent", Vector), ("normal", Vector), ("rotation", Vector)])
    return ret(node.outputs[0].Points, node.outputs[1].Vector, node.outputs[2].Vector, node.outputs[3].Vector)
    return node.outputs[0].Points, node.outputs[1].Vector, node.outputs[2].Vector, node.outputs[3].Vector


def GeometryNodeDeformCurvesOnSurface(curves=None):
    """The Deform Curves on Surface node translates and rotates each curve based on the difference in its root position. The root position is defined by UV coordinates stored on each curve and the UV Map selected for the purpose in the Curves surface settings.
    #### Path
    - Curve > Operations > Deform Curves on Surface Node
    #### Outputs:
    - `#0 curves: Geometry = None`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryDeformCurvesOnSurface.png)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/operations/deform_curves_on_surface.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeDeformCurvesOnSurface.html)
    """
    node = new_node(*nodes.GeometryNodeDeformCurvesOnSurface(curves))
    return node.outputs[0].Geometry


def GeometryNodeFillCurve(mode='TRIANGLES', curve=None):
    """The Fill Curve node generates a mesh using the constrained Delaunay triangulation algorithm with the curves as boundaries. The mesh is only generated flat with a local Z of 0.
    #### Path
    - Curve > Operations > Fill Curve Node
    #### Properties:
    - `mode`: `TRIANGLES`, `NGONS`
    #### Outputs:
    - `#0 mesh: Geometry = None`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeFillCurve.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/operations/fill_curve.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeFillCurve.html)
    """
    node = new_node(*nodes.GeometryNodeFillCurve(mode, curve))
    return node.outputs[0].Mesh


def GeometryNodeFilletCurve(mode='BEZIER', curve=None, count=1, radius=0.25, limit_radius=False):
    """The Fillet Curve rounds corners on curve control points, similar to the effect of the Bevel Modifier on a 2D mesh. However, a key difference is that the rounded portions created by the Fillet Curve node are always portions of a circle.
    #### Path
    - Curve > Operations > Fillet Curve Node
    #### Properties:
    - `mode`: `BEZIER`, `POLY`
    #### Outputs:
    - `#0 curve: Geometry = None`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeFilletCurve.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/operations/fillet_curve.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeFilletCurve.html)
    """
    node = new_node(*nodes.GeometryNodeFilletCurve(mode, curve, count, radius, limit_radius))
    return node.outputs[0].Curve


def GeometryNodeInterpolateCurves(guide_curves=None, guide_up=(0.0, 0.0, 0.0), guide_group_id=0, points=None, point_up=(0.0, 0.0, 0.0), point_group_id=0, max_neighbors=4):
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
    node = new_node(*nodes.GeometryNodeInterpolateCurves(guide_curves, guide_up, guide_group_id, points, point_up, point_group_id, max_neighbors))
    ret = typing.NamedTuple("GeometryNodeInterpolateCurves", [("curves", Geometry), ("closest_index", Integer), ("closest_weight", Float)])
    return ret(node.outputs[0].Geometry, node.outputs[1].Integer, node.outputs[2].Float)
    return node.outputs[0].Geometry, node.outputs[1].Integer, node.outputs[2].Float


def GeometryNodeResampleCurve(mode='COUNT', curve=None, selection=True, count=10, length=0.1):
    """The Resample Curve node creates a poly spline for each input spline. In the Count and Length modes, the control points of the new poly splines will have uniform spacing.
    #### Path
    - Curve > Operations > Resample Curve Node
    #### Properties:
    - `mode`: `COUNT`, `EVALUATED`, `LENGTH`
    #### Outputs:
    - `#0 curve: Geometry = None`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeResampleCurve.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/operations/resample_curve.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeResampleCurve.html)
    """
    # selection = selection if self._selection is None else self.selection
    node = new_node(*nodes.GeometryNodeResampleCurve(mode, curve, selection, count, length))
    return node.outputs[0].Curve


def GeometryNodeReverseCurve(curve=None, selection=True):
    """The Reverse Curve node swaps the start and end of splines. The shape of the splines is not changed.
    #### Path
    - Curve > Operations > Reverse Curve Node
    #### Outputs:
    - `#0 curve: Geometry = None`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeReverseCurve.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/operations/reverse_curve.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeReverseCurve.html)
    """
    # selection = selection if self._selection is None else self.selection
    node = new_node(*nodes.GeometryNodeReverseCurve(curve, selection))
    return node.outputs[0].Curve


def GeometryNodeSubdivideCurve(curve=None, cuts=1):
    """The Subdivide Curve node adds more control points in between existing control points on the curve input. For Bézier and poly splines, the shape of the spline will not be changed at all.
    #### Path
    - Curve > Operations > Subdivide Curve Node
    #### Outputs:
    - `#0 curve: Geometry = None`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeSubdivideCurve.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/operations/subdivide_curve.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeSubdivideCurve.html)
    """
    node = new_node(*nodes.GeometryNodeSubdivideCurve(curve, cuts))
    return node.outputs[0].Curve


def GeometryNodeTrimCurve(mode='FACTOR', curve=None, selection=True, start=0.0, end=1.0, start_001=0.0, end_001=1.0):
    """The Trim Curve node shortens each spline in the curve by removing sections at the start and end of each spline.
    #### Path
    - Curve > Operations > Trim Curve Node
    #### Properties:
    - `mode`: `FACTOR`, `LENGTH`
    #### Outputs:
    - `#0 curve: Geometry = None`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeTrimCurve.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/operations/trim_curve.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeTrimCurve.html)
    """
    # selection = selection if self._selection is None else self.selection
    node = new_node(*nodes.GeometryNodeTrimCurve(mode, curve, selection, start, end, start_001, end_001))
    return node.outputs[0].Curve


def GeometryNodeCurveArc(mode='RADIUS', resolution=16, start=(-1.0, 0.0, 0.0), middle=(0.0, 2.0, 0.0), end=(1.0, 0.0, 0.0), radius=1.0, start_angle=math.radians(0.0), sweep_angle=math.radians(315.0), offset_angle=math.radians(0.0), connect_center=False, invert_arc=False):
    """The Arc node generates a poly spline arc. The node has two modes, Radius and Points.
    #### Path
    - Curve > Primitives > Arc Node
    #### Properties:
    - `mode`: `RADIUS`, `POINTS`
    #### Outputs:
    - `#0 curve: Geometry = None`
    - `#1 center: Vector = (0.0, 0.0, 0.0)`
    - `#2 normal: Vector = (0.0, 0.0, 0.0)`
    - `#3 radius: Float = 0.0`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeCurveArc.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/primitives/arc.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurveArc.html)
    """
    node = new_node(*nodes.GeometryNodeCurveArc(mode, resolution, start, middle, end, radius, start_angle, sweep_angle, offset_angle, connect_center, invert_arc))
    ret = typing.NamedTuple("GeometryNodeCurveArc", [("curve", Geometry), ("center", Vector), ("normal", Vector), ("radius", Float)])
    return ret(node.outputs[0].Curve, node.outputs[1].Vector, node.outputs[2].Vector, node.outputs[3].Float)
    return node.outputs[0].Curve, node.outputs[1].Vector, node.outputs[2].Vector, node.outputs[3].Float


def GeometryNodeCurvePrimitiveBezierSegment(mode='POSITION', resolution=16, start=(-1.0, 0.0, 0.0), start_handle=(-0.5, 0.5, 0.0), end_handle=(0.0, 0.0, 0.0), end=(1.0, 0.0, 0.0)):
    """The Bézier Segment node generates a 2D Bézier spline from the given control points and handles.
    #### Path
    - Curve > Primitives > Bézier Segment Node
    #### Properties:
    - `mode`: `POSITION`, `OFFSET`
    #### Outputs:
    - `#0 curve: Geometry = None`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeCurvePrimitiveBezierSegment.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/primitives/bezier_segment.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurvePrimitiveBezierSegment.html)
    """
    node = new_node(*nodes.GeometryNodeCurvePrimitiveBezierSegment(mode, resolution, start, start_handle, end_handle, end))
    return node.outputs[0].Curve


def GeometryNodeCurvePrimitiveCircle(mode='RADIUS', resolution=32, point_1=(-1.0, 0.0, 0.0), point_2=(0.0, 1.0, 0.0), point_3=(1.0, 0.0, 0.0), radius=1.0):
    """The Curve Circle node generates a poly spline circle.
    #### Path
    - Curve > Primitives > Curve Circle Node
    #### Properties:
    - `mode`: `RADIUS`, `POINTS`
    #### Outputs:
    - `#0 curve: Geometry = None`
    - `#1 center: Vector = (0.0, 0.0, 0.0)`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeCurvePrimitiveCircle.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/primitives/curve_circle.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurvePrimitiveCircle.html)
    """
    node = new_node(*nodes.GeometryNodeCurvePrimitiveCircle(mode, resolution, point_1, point_2, point_3, radius))
    ret = typing.NamedTuple("GeometryNodeCurvePrimitiveCircle", [("curve", Geometry), ("center", Vector)])
    return ret(node.outputs[0].Curve, node.outputs[1].Vector)
    return node.outputs[0].Curve, node.outputs[1].Vector


def GeometryNodeCurvePrimitiveLine(mode='POINTS', start=(0.0, 0.0, 0.0), end=(0.0, 0.0, 1.0), direction=(0.0, 0.0, 1.0), length=1.0):
    """The Curve Line node generates poly spline line.
    #### Path
    - Curve > Primitives > Curve Line Node
    #### Properties:
    - `mode`: `POINTS`, `DIRECTION`
    #### Outputs:
    - `#0 curve: Geometry = None`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeCurvePrimitiveLine.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/primitives/curve_line.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurvePrimitiveLine.html)
    """
    node = new_node(*nodes.GeometryNodeCurvePrimitiveLine(mode, start, end, direction, length))
    return node.outputs[0].Curve


def GeometryNodeCurveSpiral(resolution=32, rotations=2.0, start_radius=1.0, end_radius=2.0, height=2.0, reverse=False):
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


def GeometryNodeCurveQuadraticBezier(resolution=16, start=(-1.0, 0.0, 0.0), middle=(0.0, 2.0, 0.0), end=(1.0, 0.0, 0.0)):
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


def GeometryNodeCurvePrimitiveQuadrilateral(mode='RECTANGLE', width=2.0, height=2.0, bottom_width=4.0, top_width=2.0, offset=1.0, bottom_height=3.0, top_height=1.0, point_1=(-1.0, -1.0, 0.0), point_2=(1.0, -1.0, 0.0), point_3=(1.0, 1.0, 0.0), point_4=(-1.0, 1.0, 0.0)):
    """The Quadrilateral node generates a polygon with four points, with different modes.
    #### Path
    - Curve > Primitives > Quadrilateral Node
    #### Properties:
    - `mode`: `RECTANGLE`, `PARALLELOGRAM`, `TRAPEZOID`, `KITE`, `POINTS`
    #### Outputs:
    - `#0 curve: Geometry = None`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeCurvePrimitiveQuadrilateral.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/primitives/quadrilateral.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurvePrimitiveQuadrilateral.html)
    """
    node = new_node(*nodes.GeometryNodeCurvePrimitiveQuadrilateral(mode, width, height, bottom_width, top_width, offset, bottom_height, top_height, point_1, point_2, point_3, point_4))
    return node.outputs[0].Curve


def GeometryNodeCurveStar(points=8, inner_radius=1.0, outer_radius=2.0, twist=math.radians(0.0)):
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
    ret = typing.NamedTuple("GeometryNodeCurveStar", [("curve", Geometry), ("outer_points", Boolean)])
    return ret(node.outputs[0].Curve, node.outputs[1].Boolean)
    return node.outputs[0].Curve, node.outputs[1].Boolean


def GeometryNodeCurveOfPoint(point_index: "Integer"=None):
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
    return node.outputs[0].Integer, node.outputs[1].Integer


def GeometryNodeOffsetPointInCurve(point_index: "Integer"=None, offset=0):
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
    return node.outputs[0].Boolean, node.outputs[1].Integer


def GeometryNodePointsOfCurve(curve_index: "Integer"=None, weights=0.0, sort_index=0):
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
    return node.outputs[0].Integer, node.outputs[1].Integer


def GeometryNodeInstanceOnPoints(points=None, selection=True, instance=None, pick_instance=False, instance_index: "Integer"=None, rotation=(0.0, 0.0, 0.0), scale=(1.0, 1.0, 1.0)):
    """The Instance on Points node adds a reference to a geometry to each of the points present in the input geometry. Instances are a fast way to add the same geometry to a scene many times without duplicating the underlying data. The node works on any geometry type with a Point domain, including meshes, point clouds, and curve control points.
    #### Path
    - Instances > Instance on Points Node
    #### Outputs:
    - `#0 instances: Geometry = None`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeInstanceOnPoints.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/instance_on_points.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeInstanceOnPoints.html)
    """
    # selection = selection if self._selection is None else self.selection
    node = new_node(*nodes.GeometryNodeInstanceOnPoints(points, selection, instance, pick_instance, instance_index, rotation, scale))
    return node.outputs[0].Instances


def GeometryNodeInstancesToPoints(instances=None, selection=True, position: "Vector"=None, radius=0.05):
    """The Instances to Points node generates points at the origins of top-level instances. Attributes on the instance domain are moved to the point cloud points.
    #### Path
    - Instances > Instances to Points Node
    #### Outputs:
    - `#0 points: Geometry = None`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeInstancesToPoints.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/instances_to_points.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeInstancesToPoints.html)
    """
    # selection = selection if self._selection is None else self.selection
    node = new_node(*nodes.GeometryNodeInstancesToPoints(instances, selection, position, radius))
    return node.outputs[0].Points


def GeometryNodeRotateInstances(instances=None, selection=True, rotation=(0.0, 0.0, 0.0), pivot_point=(0.0, 0.0, 0.0), local_space=True):
    """The Rotate Instances node rotates geometry instances in local or global space.
    #### Path
    - Instances > Rotate Instances Node
    #### Outputs:
    - `#0 instances: Geometry = None`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeRotateInstances.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/rotate_instances.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeRotateInstances.html)
    """
    # selection = selection if self._selection is None else self.selection
    node = new_node(*nodes.GeometryNodeRotateInstances(instances, selection, rotation, pivot_point, local_space))
    return node.outputs[0].Instances


def GeometryNodeScaleInstances(instances=None, selection=True, scale=(1.0, 1.0, 1.0), center=(0.0, 0.0, 0.0), local_space=True):
    """The Scale Instances node scales geometry instances in local or global space.
    #### Path
    - Instances > Scale Instances Node
    #### Outputs:
    - `#0 instances: Geometry = None`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeScaleInstances.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/scale_instances.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeScaleInstances.html)
    """
    # selection = selection if self._selection is None else self.selection
    node = new_node(*nodes.GeometryNodeScaleInstances(instances, selection, scale, center, local_space))
    return node.outputs[0].Instances


def GeometryNodeTranslateInstances(instances=None, selection=True, translation=(0.0, 0.0, 0.0), local_space=True):
    """The Translate Instances node moves top-level geometry instances in local or global space.
    #### Path
    - Instances > Translate Instances Node
    #### Outputs:
    - `#0 instances: Geometry = None`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeTranslateInstances.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/translate_instances.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeTranslateInstances.html)
    """
    # selection = selection if self._selection is None else self.selection
    node = new_node(*nodes.GeometryNodeTranslateInstances(instances, selection, translation, local_space))
    return node.outputs[0].Instances


def GeometryNodeRealizeInstances(legacy_behavior=False, geometry=None):
    """The Realize Instances node makes any instances (efficient duplicates of the same geometry) into real geometry data. This makes it possible to affect each instance individually, whereas without this node, the exact same changes are applied to every instance of the same geometry. However, performance can become much worse when the input contains many instances of complex geometry, which is a fundamental limitation when procedurally processing geometry.
    #### Path
    - Instances > Realize Instances Node
    #### Outputs:
    - `#0 geometry: Geometry = None`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeRealizeInstances.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances/realize_instances.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeRealizeInstances.html)
    """
    node = new_node(*nodes.GeometryNodeRealizeInstances(legacy_behavior, geometry))
    return node.outputs[0].Geometry


def GeometryNodeInputInstanceRotation():
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


def GeometryNodeInputInstanceScale():
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


def GeometryNodeInputMeshEdgeAngle():
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
    return node.outputs[0].Float, node.outputs[1].Float


def GeometryNodeInputMeshEdgeNeighbors():
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


def GeometryNodeInputMeshEdgeVertices():
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
    ret = typing.NamedTuple("GeometryNodeInputMeshEdgeVertices", [("vertex_index_1", Integer), ("vertex_index_2", Integer), ("position_1", Vector), ("position_2", Vector)])
    return ret(node.outputs[0].Integer, node.outputs[1].Integer, node.outputs[2].Vector, node.outputs[3].Vector)
    return node.outputs[0].Integer, node.outputs[1].Integer, node.outputs[2].Vector, node.outputs[3].Vector


def GeometryNodeEdgesToFaceGroups(boundary_edges=True):
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


def GeometryNodeInputMeshFaceArea():
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


def GeometryNodeInputMeshFaceNeighbors():
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
    return node.outputs[0].Integer, node.outputs[1].Integer


def GeometryNodeMeshFaceSetBoundaries(face_set=0):
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


def GeometryNodeInputMeshFaceIsPlanar(threshold=0.01):
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


def GeometryNodeInputShadeSmooth():
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


def GeometryNodeInputMeshIsland():
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
    return node.outputs[0].Integer, node.outputs[1].Integer


def GeometryNodeInputShortestEdgePaths(end_vertex=False, edge_cost=1.0):
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
    return node.outputs[0].Integer, node.outputs[1].Float


def GeometryNodeInputMeshVertexNeighbors():
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
    return node.outputs[0].Integer, node.outputs[1].Integer


def GeometryNodeSampleNearestSurface(data_type='FLOAT', mesh=None, value_float=0.0, value_int=0, value_vector=(0.0, 0.0, 0.0), value_color=(0.0, 0.0, 0.0, 0.0), value_bool=False, sample_position: "Vector"=None):
    """The Sample Nearest Surface node finds values at the closest points on the surface of a source mesh geometry. Non-face attributes are interpolated across the surface.
    #### Path
    - Mesh > Sample > Sample Nearest Surface Node
    #### Properties:
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
    node = new_node(*nodes.GeometryNodeSampleNearestSurface(data_type, mesh, value_float, value_int, value_vector, value_color, value_bool, sample_position))
    ret = typing.NamedTuple("GeometryNodeSampleNearestSurface", [("value", Float), ("value", Integer), ("value", Vector), ("value", Color), ("value", Boolean)])
    return ret(node.outputs[0].Float, node.outputs[1].Integer, node.outputs[2].Vector, node.outputs[3].Color, node.outputs[4].Boolean)
    return node.outputs[0].Float, node.outputs[1].Integer, node.outputs[2].Vector, node.outputs[3].Color, node.outputs[4].Boolean


def GeometryNodeSampleUVSurface(data_type='FLOAT', mesh=None, value_float=0.0, value_int=0, value_vector=(0.0, 0.0, 0.0), value_color=(0.0, 0.0, 0.0, 0.0), value_bool=False, source_uv_map=(0.0, 0.0, 0.0), sample_uv=(0.0, 0.0, 0.0)):
    """The Sample UV Surface node finds values on a mesh’s surface at specific UV locations. Internally the process is a “reverse UV lookup” from a location in 2D space. The node then finds the face that corresponds to each UV coordinate, and the location within that face.
    #### Path
    - Mesh > Sample > Sample UV Surface Node
    #### Properties:
    - `data_type`: `FLOAT`, `INT`, `FLOAT_VECTOR`, `FLOAT_COLOR`, `BOOLEAN`
    #### Outputs:
    - `#0 value_float: Float = 0.0`
    - `#1 value_int: Integer = 0`
    - `#2 value_vector: Vector = (0.0, 0.0, 0.0)`
    - `#3 value_color: Color = (0.0, 0.0, 0.0, 0.0)`
    - `#4 value_bool: Boolean = False`
    - `#5 is_valid: Boolean = False`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeSampleUVSurface.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/sample/sample_uv_surface.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeSampleUVSurface.html)
    """
    node = new_node(*nodes.GeometryNodeSampleUVSurface(data_type, mesh, value_float, value_int, value_vector, value_color, value_bool, source_uv_map, sample_uv))
    ret = typing.NamedTuple("GeometryNodeSampleUVSurface", [("value", Float), ("value", Integer), ("value", Vector), ("value", Color), ("value", Boolean), ("is_valid", Boolean)])
    return ret(node.outputs[0].Float, node.outputs[1].Integer, node.outputs[2].Vector, node.outputs[3].Color, node.outputs[4].Boolean, node.outputs[5].Boolean)
    return node.outputs[0].Float, node.outputs[1].Integer, node.outputs[2].Vector, node.outputs[3].Color, node.outputs[4].Boolean, node.outputs[5].Boolean


def GeometryNodeSetShadeSmooth(geometry=None, selection=True, shade_smooth=True):
    """The Set Shade Smooth node controls whether the mesh’s faces look smooth in the viewport and renders. The input node for this data is the Is Shade Smooth node.
    #### Path
    - Mesh > Write > Set Shade Smooth Node
    #### Outputs:
    - `#0 geometry: Geometry = None`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeSetShadeSmooth.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/write/set_shade_smooth.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetShadeSmooth.html)
    """
    # selection = selection if self._selection is None else self.selection
    node = new_node(*nodes.GeometryNodeSetShadeSmooth(geometry, selection, shade_smooth))
    return node.outputs[0].Geometry


def GeometryNodeDualMesh(mesh=None, keep_boundaries=False):
    """The Dual Mesh Node converts a mesh into it’s dual, i.e. faces are turned into vertices and vertices are turned into faces. This also means that attributes which were on the face domain are transferred to the point domain in the dual mesh.
    #### Path
    - Mesh > Operations > Dual Mesh Node
    #### Outputs:
    - `#0 dual_mesh: Geometry = None`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeDualMesh.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/operations/dual_mesh.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeDualMesh.html)
    """
    node = new_node(*nodes.GeometryNodeDualMesh(mesh, keep_boundaries))
    return node.outputs[0].Geometry


def GeometryNodeEdgePathsToCurves(mesh=None, start_vertices=True, next_vertex_index=-1):
    """The Edge Paths to Curves node output curves that follow paths across mesh edges.
    #### Path
    - Mesh > Operations > Edge Paths to Curves Node
    #### Outputs:
    - `#0 curves: Geometry = None`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeEdgePathsToCurves.png)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/operations/edge_paths_to_curves.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeEdgePathsToCurves.html)
    """
    node = new_node(*nodes.GeometryNodeEdgePathsToCurves(mesh, start_vertices, next_vertex_index))
    return node.outputs[0].Geometry


def GeometryNodeEdgePathsToSelection(start_vertices=True, next_vertex_index=-1):
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


def GeometryNodeExtrudeMesh(mode='FACES', mesh=None, selection=True, offset: "Vector"=None, offset_scale=1.0, individual=True):
    """The Extrude Mesh Node generates new vertices, edges, or faces, on selected geometry and transforms them based on an offset.
    #### Path
    - Mesh > Operations > Extrude Mesh Node
    #### Properties:
    - `mode`: `FACES`, `VERTICES`, `EDGES`
    #### Outputs:
    - `#0 mesh: Geometry = None`
    - `#1 top: Boolean = False`
    - `#2 side: Boolean = False`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeExtrudeMesh.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/operations/extrude_mesh.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeExtrudeMesh.html)
    """
    # selection = selection if self._selection is None else self.selection
    node = new_node(*nodes.GeometryNodeExtrudeMesh(mode, mesh, selection, offset, offset_scale, individual))
    ret = typing.NamedTuple("GeometryNodeExtrudeMesh", [("mesh", Geometry), ("top", Boolean), ("side", Boolean)])
    return ret(node.outputs[0].Mesh, node.outputs[1].Boolean, node.outputs[2].Boolean)
    return node.outputs[0].Mesh, node.outputs[1].Boolean, node.outputs[2].Boolean


def GeometryNodeFlipFaces(mesh=None, selection=True):
    """The Flip Faces Node reverses the order of the vertices and edges of each selected face. The most common use of this node is to flip the normals of a face. Any face corner domain attributes of selected faces are also reversed.
    #### Path
    - Mesh > Operations > Flip Faces Node
    #### Outputs:
    - `#0 mesh: Geometry = None`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeFlipFaces.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/operations/flip_faces.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeFlipFaces.html)
    """
    # selection = selection if self._selection is None else self.selection
    node = new_node(*nodes.GeometryNodeFlipFaces(mesh, selection))
    return node.outputs[0].Mesh


def GeometryNodeMeshBoolean(operation='DIFFERENCE', mesh_1=None, mesh_2=None, self_intersection=False, hole_tolerant=False):
    """The Mesh Boolean Node allows you to cut, subtract, and join the geometry of two inputs. This node offers the same operations as the Boolean modifier.
    #### Path
    - Mesh > Operations > Mesh Boolean Node
    #### Properties:
    - `operation`: `DIFFERENCE`, `INTERSECT`, `UNION`
    #### Outputs:
    - `#0 mesh: Geometry = None`
    - `#1 intersecting_edges: Boolean = False`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeMeshBoolean.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/operations/mesh_boolean.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshBoolean.html)
    """
    node = new_node(*nodes.GeometryNodeMeshBoolean(operation, mesh_1, mesh_2, self_intersection, hole_tolerant))
    ret = typing.NamedTuple("GeometryNodeMeshBoolean", [("mesh", Geometry), ("intersecting_edges", Boolean)])
    return ret(node.outputs[0].Mesh, node.outputs[1].Boolean)
    return node.outputs[0].Mesh, node.outputs[1].Boolean


def GeometryNodeMeshToCurve(mesh=None, selection=True):
    """The Mesh to Curve node generates a curve from a mesh. The result is a poly spline, with a point for every selected vertex on the mesh. Any intersection of more than two selected edges will cause a break in the spline. Meaning that if a the mesh has grid-like topology and a continuous spline is desired, the Selection input is very important.
    #### Path
    - Mesh > Operations > Mesh to Curve Node
    #### Outputs:
    - `#0 curve: Geometry = None`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeMeshToCurve.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/operations/mesh_to_curve.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshToCurve.html)
    """
    # selection = selection if self._selection is None else self.selection
    node = new_node(*nodes.GeometryNodeMeshToCurve(mesh, selection))
    return node.outputs[0].Curve


def GeometryNodeMeshToPoints(mode='VERTICES', mesh=None, selection=True, position: "Vector"=None, radius=0.05):
    """The Mesh to Points node generates a point cloud from a mesh.
    #### Path
    - Mesh > Operations > Mesh to Points Node
    #### Properties:
    - `mode`: `VERTICES`, `EDGES`, `FACES`, `CORNERS`
    #### Outputs:
    - `#0 points: Geometry = None`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeMeshToPoints.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/operations/mesh_to_points.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshToPoints.html)
    """
    # selection = selection if self._selection is None else self.selection
    node = new_node(*nodes.GeometryNodeMeshToPoints(mode, mesh, selection, position, radius))
    return node.outputs[0].Points


def GeometryNodeMeshToVolume(resolution_mode='VOXEL_AMOUNT', mesh=None, density=1.0, voxel_size=0.3, voxel_amount=64.0, exterior_band_width=0.1, interior_band_width=0.0, fill_volume=True):
    """The Mesh to Volume node creates a fog volumes based on the shape of a mesh. The volume is created with a grid of the name “density”.
    #### Path
    - Mesh > Operations > Mesh to Volume Node
    #### Properties:
    - `resolution_mode`: `VOXEL_AMOUNT`, `VOXEL_SIZE`
    #### Outputs:
    - `#0 volume: Geometry = None`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeMeshToVolume.png)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/operations/mesh_to_volume.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshToVolume.html)
    """
    node = new_node(*nodes.GeometryNodeMeshToVolume(resolution_mode, mesh, density, voxel_size, voxel_amount, exterior_band_width, interior_band_width, fill_volume))
    return node.outputs[0].Volume


def GeometryNodeScaleElements(domain='FACE', scale_mode='UNIFORM', geometry=None, selection=True, scale=1.0, center: "Vector"=None, axis=(1.0, 0.0, 0.0)):
    """The Scale Elements Node scales groups of connected edges and faces. When multiple selected faces/edges share the same vertices, they are scaled together. The center and scaling factor is averaged in this case.
    #### Path
    - Mesh > Operations > Scale Elements Node
    #### Properties:
    - `domain`: `FACE`, `EDGE`
    - `scale_mode`: `UNIFORM`, `SINGLE_AXIS`
    #### Outputs:
    - `#0 geometry: Geometry = None`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeScaleElements.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/operations/scale_elements.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeScaleElements.html)
    """
    # selection = selection if self._selection is None else self.selection
    node = new_node(*nodes.GeometryNodeScaleElements(domain, scale_mode, geometry, selection, scale, center, axis))
    return node.outputs[0].Geometry


def GeometryNodeSplitEdges(mesh=None, selection=True):
    """Like the Edge Split Modifier, the Split Edges node splits and duplicates edges within a mesh, breaking ‘links’ between faces around those split edges.
    #### Path
    - Mesh > Operations > Split Edges Node
    #### Outputs:
    - `#0 mesh: Geometry = None`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeSplitEdges.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/operations/split_edges.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeSplitEdges.html)
    """
    # selection = selection if self._selection is None else self.selection
    node = new_node(*nodes.GeometryNodeSplitEdges(mesh, selection))
    return node.outputs[0].Mesh


def GeometryNodeSubdivideMesh(mesh=None, level=1):
    """The Subdivide Mesh node adds new faces to mesh geometry using a simple interpolation for deformation.
    #### Path
    - Mesh > Operations > Subdivide Mesh Node
    #### Outputs:
    - `#0 mesh: Geometry = None`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeSubdivideMesh.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/operations/subdivide_mesh.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeSubdivideMesh.html)
    """
    node = new_node(*nodes.GeometryNodeSubdivideMesh(mesh, level))
    return node.outputs[0].Mesh


def GeometryNodeSubdivisionSurface(boundary_smooth='ALL', uv_smooth='PRESERVE_BOUNDARIES', mesh=None, level=1, edge_crease=0.0, vertex_crease=0.0):
    """The Subdivision Surface node adds new faces to mesh geometry using a Catmull-Clark subdivision method.
    #### Path
    - Mesh > Operations > Subdivision Surface Node
    #### Properties:
    - `boundary_smooth`: `ALL`, `PRESERVE_CORNERS`
    - `uv_smooth`: `PRESERVE_BOUNDARIES`, `NONE`, `PRESERVE_CORNERS`, `PRESERVE_CORNERS_AND_JUNCTIONS`, `PRESERVE_CORNERS_JUNCTIONS_AND_CONCAVE`, `SMOOTH_ALL`
    #### Outputs:
    - `#0 mesh: Geometry = None`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeSubdivisionSurface.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/operations/subdivision_surface.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeSubdivisionSurface.html)
    """
    node = new_node(*nodes.GeometryNodeSubdivisionSurface(boundary_smooth, uv_smooth, mesh, level, edge_crease, vertex_crease))
    return node.outputs[0].Mesh


def GeometryNodeTriangulate(ngon_method='BEAUTY', quad_method='SHORTEST_DIAGONAL', mesh=None, selection=True, minimum_vertices=4):
    """The Triangulate node converts all faces in a mesh (quads and n-gons) to triangular faces. It functions the same as the Triangulate tool in Edit Mode.
    #### Path
    - Mesh > Operations > Triangulate Node
    #### Properties:
    - `ngon_method`: `BEAUTY`, `CLIP`
    - `quad_method`: `SHORTEST_DIAGONAL`, `BEAUTY`, `FIXED`, `FIXED_ALTERNATE`, `LONGEST_DIAGONAL`
    #### Outputs:
    - `#0 mesh: Geometry = None`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeTriangulate.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/operations/triangulate.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeTriangulate.html)
    """
    # selection = selection if self._selection is None else self.selection
    node = new_node(*nodes.GeometryNodeTriangulate(ngon_method, quad_method, mesh, selection, minimum_vertices))
    return node.outputs[0].Mesh


def GeometryNodeMeshCone(fill_type='NGON', vertices=32, side_segments=1, fill_segments=1, radius_top=0.0, radius_bottom=1.0, depth=2.0):
    """The Cone node generates a cone mesh that is optionally truncated.
    #### Path
    - Mesh > Primitives > Cone Node
    #### Properties:
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
    ret = typing.NamedTuple("GeometryNodeMeshCone", [("mesh", Geometry), ("top", Boolean), ("bottom", Boolean), ("side", Boolean), ("uv_map", Vector)])
    return ret(node.outputs[0].Mesh, node.outputs[1].Boolean, node.outputs[2].Boolean, node.outputs[3].Boolean, node.outputs[4].Vector)
    return node.outputs[0].Mesh, node.outputs[1].Boolean, node.outputs[2].Boolean, node.outputs[3].Boolean, node.outputs[4].Vector


def GeometryNodeMeshCube(size=(1.0, 1.0, 1.0), vertices_x=2, vertices_y=2, vertices_z=2):
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
    ret = typing.NamedTuple("GeometryNodeMeshCube", [("mesh", Geometry), ("uv_map", Vector)])
    return ret(node.outputs[0].Mesh, node.outputs[1].Vector)
    return node.outputs[0].Mesh, node.outputs[1].Vector


def GeometryNodeMeshCylinder(fill_type='NGON', vertices=32, side_segments=1, fill_segments=1, radius=1.0, depth=2.0):
    """The Cylinder node generates a cylinder mesh. It is similar to the Cone node but always uses the same radius for the circles at the top and bottom.
    #### Path
    - Mesh > Primitives > Cylinder Node
    #### Properties:
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
    ret = typing.NamedTuple("GeometryNodeMeshCylinder", [("mesh", Geometry), ("top", Boolean), ("side", Boolean), ("bottom", Boolean), ("uv_map", Vector)])
    return ret(node.outputs[0].Mesh, node.outputs[1].Boolean, node.outputs[2].Boolean, node.outputs[3].Boolean, node.outputs[4].Vector)
    return node.outputs[0].Mesh, node.outputs[1].Boolean, node.outputs[2].Boolean, node.outputs[3].Boolean, node.outputs[4].Vector


def GeometryNodeMeshGrid(size_x=1.0, size_y=1.0, vertices_x=3, vertices_y=3):
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
    ret = typing.NamedTuple("GeometryNodeMeshGrid", [("mesh", Geometry), ("uv_map", Vector)])
    return ret(node.outputs[0].Mesh, node.outputs[1].Vector)
    return node.outputs[0].Mesh, node.outputs[1].Vector


def GeometryNodeMeshIcoSphere(radius=1.0, subdivisions=1):
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
    ret = typing.NamedTuple("GeometryNodeMeshIcoSphere", [("mesh", Geometry), ("uv_map", Vector)])
    return ret(node.outputs[0].Mesh, node.outputs[1].Vector)
    return node.outputs[0].Mesh, node.outputs[1].Vector


def GeometryNodeMeshCircle(fill_type='NONE', vertices=32, radius=1.0):
    """The Mesh Circle node generates a circular ring of edges that is optionally filled with faces.
    #### Path
    - Mesh > Primitives > Mesh Circle Node
    #### Properties:
    - `fill_type`: `NONE`, `NGON`, `TRIANGLE_FAN`
    #### Outputs:
    - `#0 mesh: Geometry = None`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeMeshCircle.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/primitives/mesh_circle.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshCircle.html)
    """
    node = new_node(*nodes.GeometryNodeMeshCircle(fill_type, vertices, radius))
    return node.outputs[0].Mesh


def GeometryNodeMeshLine(count_mode='TOTAL', mode='OFFSET', count=10, resolution=1.0, start_location=(0.0, 0.0, 0.0), offset=(0.0, 0.0, 1.0)):
    """The Mesh Line node generates vertices in a line and connects them with edges.
    #### Path
    - Mesh > Primitives > Mesh Line Node
    #### Properties:
    - `count_mode`: `TOTAL`, `RESOLUTION`
    - `mode`: `OFFSET`, `END_POINTS`
    #### Outputs:
    - `#0 mesh: Geometry = None`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeMeshLine.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/primitives/mesh_line.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeMeshLine.html)
    """
    node = new_node(*nodes.GeometryNodeMeshLine(count_mode, mode, count, resolution, start_location, offset))
    return node.outputs[0].Mesh


def GeometryNodeMeshUVSphere(segments=32, rings=16, radius=1.0):
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
    ret = typing.NamedTuple("GeometryNodeMeshUVSphere", [("mesh", Geometry), ("uv_map", Vector)])
    return ret(node.outputs[0].Mesh, node.outputs[1].Vector)
    return node.outputs[0].Mesh, node.outputs[1].Vector


def GeometryNodeCornersOfFace(face_index: "Integer"=None, weights=0.0, sort_index=0):
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
    return node.outputs[0].Integer, node.outputs[1].Integer


def GeometryNodeCornersOfVertex(vertex_index: "Integer"=None, weights=0.0, sort_index=0):
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
    return node.outputs[0].Integer, node.outputs[1].Integer


def GeometryNodeEdgesOfCorner(corner_index: "Integer"=None):
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
    return node.outputs[0].Integer, node.outputs[1].Integer


def GeometryNodeEdgesOfVertex(vertex_index: "Integer"=None, weights=0.0, sort_index=0):
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
    return node.outputs[0].Integer, node.outputs[1].Integer


def GeometryNodeFaceOfCorner(corner_index: "Integer"=None):
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
    return node.outputs[0].Integer, node.outputs[1].Integer


def GeometryNodeOffsetCornerInFace(corner_index: "Integer"=None, offset=0):
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


def GeometryNodeVertexOfCorner(corner_index: "Integer"=None):
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


def GeometryNodeUVPackIslands(uv=(0.0, 0.0, 0.0), selection=True, margin=0.001, rotate=True):
    """The Pack UV Islands Node scales islands of a UV map and moves them so they fill the UV space as much as possible.
    #### Path
    - Mesh > UV > Pack UV Islands Node
    #### Outputs:
    - `#0 uv: Vector = (0.0, 0.0, 0.0)`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryUVPackIslands.png)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/uv/pack_uv_islands.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeUVPackIslands.html)
    """
    # selection = selection if self._selection is None else self.selection
    node = new_node(*nodes.GeometryNodeUVPackIslands(uv, selection, margin, rotate))
    return node.outputs[0].Vector


def GeometryNodeUVUnwrap(method='ANGLE_BASED', selection=True, seam=False, margin=0.001, fill_holes=True):
    """The UV Unwrap Node generates a UV map islands based on a selection of seam edges. The node implicitly performs a Pack Islands operation upon completion, because the results may not be generally useful otherwise.
    #### Path
    - Mesh > UV > UV Unwrap Node
    #### Properties:
    - `method`: `ANGLE_BASED`, `CONFORMAL`
    #### Outputs:
    - `#0 uv: Vector = (0.0, 0.0, 0.0)`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryUVUnrwap.png)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/mesh/uv/uv_unwrap.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeUVUnwrap.html)
    """
    # selection = selection if self._selection is None else self.selection
    node = new_node(*nodes.GeometryNodeUVUnwrap(method, selection, seam, margin, fill_holes))
    return node.outputs[0].Vector


def GeometryNodeDistributePointsInVolume(mode='DENSITY_RANDOM', volume=None, density=1.0, seed=0, spacing=(0.3, 0.3, 0.3), threshold=0.1):
    """The Distribute Points in Volume node creates points inside of volume grids. The node has two basic modes of operation: distributing points randomly, or in a regular grid. Both methods operate on all of the float grids in the volume.
    #### Path
    - Point > Distribute Points in Volume
    #### Properties:
    - `mode`: `DENSITY_RANDOM`, `DENSITY_GRID`
    #### Outputs:
    - `#0 points: Geometry = None`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeDistributePointsInVolume.png)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/distribute_points_in_volume.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeDistributePointsInVolume.html)
    """
    node = new_node(*nodes.GeometryNodeDistributePointsInVolume(mode, volume, density, seed, spacing, threshold))
    return node.outputs[0].Points


def GeometryNodeDistributePointsOnFaces(distribute_method='RANDOM', use_legacy_normal=False, mesh=None, selection=True, distance_min=0.0, density_max=10.0, density=10.0, density_factor=1.0, seed=0):
    """The Distribute Points on Faces node places points on the surface of the input geometry object. Point, corner, and polygon attributes of the input geometry are transferred to the generated points. That includes vertex weights and UV maps. Additionally, the node has Normal and Rotation outputs.
    #### Path
    - Point > Distribute Points on Faces
    #### Properties:
    - `distribute_method`: `RANDOM`, `POISSON`
    #### Outputs:
    - `#0 points: Geometry = None`
    - `#1 normal: Vector = (0.0, 0.0, 0.0)`
    - `#2 rotation: Vector = (0.0, 0.0, 0.0)`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeDistributePointsOnFaces.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/distribute_points_on_faces.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeDistributePointsOnFaces.html)
    """
    # selection = selection if self._selection is None else self.selection
    node = new_node(*nodes.GeometryNodeDistributePointsOnFaces(distribute_method, use_legacy_normal, mesh, selection, distance_min, density_max, density, density_factor, seed))
    ret = typing.NamedTuple("GeometryNodeDistributePointsOnFaces", [("points", Geometry), ("normal", Vector), ("rotation", Vector)])
    return ret(node.outputs[0].Points, node.outputs[1].Vector, node.outputs[2].Vector)
    return node.outputs[0].Points, node.outputs[1].Vector, node.outputs[2].Vector


def GeometryNodePoints(count=1, position=(0.0, 0.0, 0.0), radius=0.1):
    """The Points node generate a point cloud with positions and radii defined by fields.
    #### Path
    - Point > Points Node
    #### Outputs:
    - `#0 geometry: Geometry = None`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodePoints.png)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/points.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodePoints.html)
    """
    node = new_node(*nodes.GeometryNodePoints(count, position, radius))
    return node.outputs[0].Geometry


def GeometryNodePointsToVertices(points=None, selection=True):
    """The Points to Vertices node generate a mesh vertex in the output geometry for each point cloud point in the input geometry.
    #### Path
    - Point > Points to Vertices Node
    #### Outputs:
    - `#0 mesh: Geometry = None`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodePointsToVertices.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/points_to_vertices.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodePointsToVertices.html)
    """
    # selection = selection if self._selection is None else self.selection
    node = new_node(*nodes.GeometryNodePointsToVertices(points, selection))
    return node.outputs[0].Mesh


def GeometryNodePointsToVolume(resolution_mode='VOXEL_AMOUNT', points=None, density=1.0, voxel_size=0.3, voxel_amount=64.0, radius=0.5):
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
    node = new_node(*nodes.GeometryNodePointsToVolume(resolution_mode, points, density, voxel_size, voxel_amount, radius))
    return node.outputs[0].Volume


def GeometryNodeSetPointRadius(points=None, selection=True, radius=0.05):
    """The Set Point Radius node controls the size each selected point cloud point should display with in the viewport.
    #### Path
    - Point > Set Point Radius Node
    #### Outputs:
    - `#0 points: Geometry = None`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeSetPointRadius.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/point/set_point_radius.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetPointRadius.html)
    """
    # selection = selection if self._selection is None else self.selection
    node = new_node(*nodes.GeometryNodeSetPointRadius(points, selection, radius))
    return node.outputs[0].Points


def GeometryNodeVolumeCube(density=1.0, background=0.0, min=(-1.0, -1.0, -1.0), max=(1.0, 1.0, 1.0), resolution_x=32, resolution_y=32, resolution_z=32):
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


def GeometryNodeVolumeToMesh(resolution_mode='GRID', volume=None, voxel_size=0.3, voxel_amount=64.0, threshold=0.1, adaptivity=0.0):
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
    node = new_node(*nodes.GeometryNodeVolumeToMesh(resolution_mode, volume, voxel_size, voxel_amount, threshold, adaptivity))
    return node.outputs[0].Mesh


def GeometryNodeReplaceMaterial(geometry=None, old=None, new=None):
    """The Replace Material node swaps one material with another. Replacing a material with this node is more efficient than creating a selection of all faces with the old material with the Material Selection Node and then using the Set Material Node.
    #### Path
    - Material > Replace Material Node
    #### Outputs:
    - `#0 geometry: Geometry = None`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeReplaceMaterial.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/replace_material.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeReplaceMaterial.html)
    """
    node = new_node(*nodes.GeometryNodeReplaceMaterial(geometry, old, new))
    return node.outputs[0].Geometry


def GeometryNodeInputMaterialIndex():
    """The Material Index node outputs which material in the list of materials of the geometry each element corresponds to. Currently the node supports mesh data, where material_index is a built-in attribute on faces.
    #### Path
    - Material > Material Index Node
    #### Outputs:
    - `#0 material_index: Integer = 0`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeInputMaterialIndex.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/material_index.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMaterialIndex.html)
    """
    node = new_node(*nodes.GeometryNodeInputMaterialIndex())
    return node.outputs[0].Integer


def GeometryNodeMaterialSelection(material=None):
    """The Material Selection node provides a selection for meshes that use this material. Since the material_index is stored on each face, the output will be implicitly interpolated to a different domain when necessary. For example, every vertex connected to a selected face will be selected.
    #### Path
    - Material > Material Selection Node
    #### Outputs:
    - `#0 selection: Boolean = False`

    ![](https://docs.blender.org/manual/en/latest/_images/modeling_geometry-nodes_material_material-selection_node.png)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/material_selection.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeMaterialSelection.html)
    """
    node = new_node(*nodes.GeometryNodeMaterialSelection(material))
    return node.outputs[0].Boolean


def GeometryNodeSetMaterial(geometry=None, selection=True, material=None):
    """The Set Material changes the material assignment in the specified selection, by adjusting the material_index attribute. If the material is already used on the geometry, the existing material index will be reused.
    #### Path
    - Material > Set Material Node
    #### Outputs:
    - `#0 geometry: Geometry = None`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeSetMaterial.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/set_material.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetMaterial.html)
    """
    # selection = selection if self._selection is None else self.selection
    node = new_node(*nodes.GeometryNodeSetMaterial(geometry, selection, material))
    return node.outputs[0].Geometry


def GeometryNodeSetMaterialIndex(geometry=None, selection=True, material_index=0):
    """The Set Material Index node sets the material index for a geometry.
    #### Path
    - Material > Set Material Index Node
    #### Outputs:
    - `#0 geometry: Geometry = None`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeSetMaterialIndex.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/set_material_index.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeSetMaterialIndex.html)
    """
    # selection = selection if self._selection is None else self.selection
    node = new_node(*nodes.GeometryNodeSetMaterialIndex(geometry, selection, material_index))
    return node.outputs[0].Geometry


def ShaderNodeTexBrick(color_mapping=None, offset=0.5, offset_frequency=2, squash=1.0, squash_frequency=2, texture_mapping=None, vector: "Vector"=None, color1=(0.8, 0.8, 0.8, 1.0), color2=(0.2, 0.2, 0.2, 1.0), mortar=(0.0, 0.0, 0.0, 1.0), scale=5.0, mortar_size=0.02, mortar_smooth=0.1, bias=0.0, brick_width=0.5, row_height=0.25):
    """The Brick Texture is used to add a procedural texture producing bricks.
    #### Path
    - Texture > Brick Texture Node
    #### Outputs:
    - `#0 color: Color = (0.0, 0.0, 0.0, 0.0)`
    - `#1 fac: Float = 0.0`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeTexBrick.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/brick.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexBrick.html)
    """
    node = new_node(*nodes.ShaderNodeTexBrick(color_mapping, offset, offset_frequency, squash, squash_frequency, texture_mapping, vector, color1, color2, mortar, scale, mortar_size, mortar_smooth, bias, brick_width, row_height))
    ret = typing.NamedTuple("ShaderNodeTexBrick", [("color", Color), ("fac", Float)])
    return ret(node.outputs[0].Color, node.outputs[1].Float)
    return node.outputs[0].Color, node.outputs[1].Float


def ShaderNodeTexChecker(color_mapping=None, texture_mapping=None, vector: "Vector"=None, color1=(0.8, 0.8, 0.8, 1.0), color2=(0.2, 0.2, 0.2, 1.0), scale=5.0):
    """The Checker Texture is used to add a checkerboard texture.
    #### Path
    - Texture > Checker Texture Node
    #### Outputs:
    - `#0 color: Color = (0.0, 0.0, 0.0, 0.0)`
    - `#1 fac: Float = 0.0`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeTexChecker.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/checker.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexChecker.html)
    """
    node = new_node(*nodes.ShaderNodeTexChecker(color_mapping, texture_mapping, vector, color1, color2, scale))
    ret = typing.NamedTuple("ShaderNodeTexChecker", [("color", Color), ("fac", Float)])
    return ret(node.outputs[0].Color, node.outputs[1].Float)
    return node.outputs[0].Color, node.outputs[1].Float


def ShaderNodeTexGradient(gradient_type='LINEAR', color_mapping=None, texture_mapping=None, vector: "Vector"=None):
    """The Gradient Texture node generates interpolated color and intensity values based on the input vector.
    #### Path
    - Texture > Gradient Texture Node
    #### Properties:
    - `gradient_type`: `LINEAR`, `QUADRATIC`, `EASING`, `DIAGONAL`, `SPHERICAL`, `QUADRATIC_SPHERE`, `RADIAL`
    #### Outputs:
    - `#0 color: Color = (0.0, 0.0, 0.0, 0.0)`
    - `#1 fac: Float = 0.0`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeTexGradient.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/gradient.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexGradient.html)
    """
    node = new_node(*nodes.ShaderNodeTexGradient(gradient_type, color_mapping, texture_mapping, vector))
    ret = typing.NamedTuple("ShaderNodeTexGradient", [("color", Color), ("fac", Float)])
    return ret(node.outputs[0].Color, node.outputs[1].Float)
    return node.outputs[0].Color, node.outputs[1].Float


def GeometryNodeImageTexture(extension='REPEAT', interpolation='Linear', image=None, vector: "Vector"=None, frame=0):
    """The Image Texture node is used to add an image file as a texture. The image data is sampled with the input Vector and outputs a Color and Alpha value.
    #### Path
    - Texture > Image Texture Node
    #### Properties:
    - `extension`: `REPEAT`, `EXTEND`, `CLIP`, `MIRROR`
    - `interpolation`: `Linear`, `Closest`, `Cubic`
    #### Outputs:
    - `#0 color: Color = (0.0, 0.0, 0.0, 0.0)`
    - `#1 alpha: Float = 0.0`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeImageTexture.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/image.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeImageTexture.html)
    """
    node = new_node(*nodes.GeometryNodeImageTexture(extension, interpolation, image, vector, frame))
    ret = typing.NamedTuple("GeometryNodeImageTexture", [("color", Color), ("alpha", Float)])
    return ret(node.outputs[0].Color, node.outputs[1].Float)
    return node.outputs[0].Color, node.outputs[1].Float


def ShaderNodeTexMagic(color_mapping=None, texture_mapping=None, turbulence_depth=2, vector: "Vector"=None, scale=5.0, distortion=1.0):
    """The Magic Texture node is used to add a psychedelic color texture.
    #### Path
    - Texture > Magic Texture Node
    #### Outputs:
    - `#0 color: Color = (0.0, 0.0, 0.0, 0.0)`
    - `#1 fac: Float = 0.0`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeTexMagic.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/magic.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexMagic.html)
    """
    node = new_node(*nodes.ShaderNodeTexMagic(color_mapping, texture_mapping, turbulence_depth, vector, scale, distortion))
    ret = typing.NamedTuple("ShaderNodeTexMagic", [("color", Color), ("fac", Float)])
    return ret(node.outputs[0].Color, node.outputs[1].Float)
    return node.outputs[0].Color, node.outputs[1].Float


def ShaderNodeTexMusgrave(musgrave_dimensions='3D', musgrave_type='FBM', color_mapping=None, texture_mapping=None, vector: "Vector"=None, w=0.0, scale=5.0, detail=2.0, dimension=2.0, lacunarity=2.0, offset=0.0, gain=1.0):
    """The Musgrave Texture node evaluates a fractal Perlin noise at the input texture coordinates. Unlike the Noise Texture, which is also a fractal Perlin noise, the Musgrave Texture allows greater control over how octaves are combined.
    #### Path
    - Texture > Musgrave Texture Node
    #### Properties:
    - `musgrave_dimensions`: `3D`, `1D`, `2D`, `4D`
    - `musgrave_type`: `FBM`, `MULTIFRACTAL`, `RIDGED_MULTIFRACTAL`, `HYBRID_MULTIFRACTAL`, `HETERO_TERRAIN`
    #### Outputs:
    - `#0 fac: Float = 0.0`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeTexMusgrave.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/musgrave.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexMusgrave.html)
    """
    node = new_node(*nodes.ShaderNodeTexMusgrave(musgrave_dimensions, musgrave_type, color_mapping, texture_mapping, vector, w, scale, detail, dimension, lacunarity, offset, gain))
    return node.outputs[0].Float


def ShaderNodeTexNoise(noise_dimensions='3D', color_mapping=None, texture_mapping=None, vector: "Vector"=None, w=0.0, scale=5.0, detail=2.0, roughness=0.5, distortion=0.0):
    """The Noise Texture node evaluates a fractal Perlin noise at the input texture coordinates.
    #### Path
    - Texture > Noise Texture Node
    #### Properties:
    - `noise_dimensions`: `3D`, `1D`, `2D`, `4D`
    #### Outputs:
    - `#0 fac: Float = 0.0`
    - `#1 color: Color = (0.0, 0.0, 0.0, 0.0)`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeTexNoise.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/noise.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexNoise.html)
    """
    node = new_node(*nodes.ShaderNodeTexNoise(noise_dimensions, color_mapping, texture_mapping, vector, w, scale, detail, roughness, distortion))
    ret = typing.NamedTuple("ShaderNodeTexNoise", [("fac", Float), ("color", Color)])
    return ret(node.outputs[0].Float, node.outputs[1].Color)
    return node.outputs[0].Float, node.outputs[1].Color


def ShaderNodeTexVoronoi(distance='EUCLIDEAN', feature='F1', voronoi_dimensions='3D', color_mapping=None, texture_mapping=None, vector: "Vector"=None, w=0.0, scale=5.0, smoothness=1.0, exponent=0.5, randomness=1.0):
    """The Voronoi Texture node evaluates a Worley Noise at the input texture coordinates.
    #### Path
    - Texture > Voronoi Texture Node
    #### Properties:
    - `distance`: `EUCLIDEAN`, `MANHATTAN`, `CHEBYCHEV`, `MINKOWSKI`
    - `feature`: `F1`, `F2`, `SMOOTH_F1`, `DISTANCE_TO_EDGE`, `N_SPHERE_RADIUS`
    - `voronoi_dimensions`: `3D`, `1D`, `2D`, `4D`
    #### Outputs:
    - `#0 distance: Float = 0.0`
    - `#1 color: Color = (0.0, 0.0, 0.0, 0.0)`
    - `#2 position: Vector = (0.0, 0.0, 0.0)`
    - `#3 w: Float = 0.0`
    - `#4 radius: Float = 0.0`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeTexVoronoi.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/voronoi.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexVoronoi.html)
    """
    node = new_node(*nodes.ShaderNodeTexVoronoi(distance, feature, voronoi_dimensions, color_mapping, texture_mapping, vector, w, scale, smoothness, exponent, randomness))
    ret = typing.NamedTuple("ShaderNodeTexVoronoi", [("distance", Float), ("color", Color), ("position", Vector), ("w", Float), ("radius", Float)])
    return ret(node.outputs[0].Float, node.outputs[1].Color, node.outputs[2].Vector, node.outputs[3].Float, node.outputs[4].Float)
    return node.outputs[0].Float, node.outputs[1].Color, node.outputs[2].Vector, node.outputs[3].Float, node.outputs[4].Float


def ShaderNodeTexWave(bands_direction='X', rings_direction='X', wave_profile='SIN', wave_type='BANDS', color_mapping=None, texture_mapping=None, vector: "Vector"=None, scale=5.0, distortion=0.0, detail=2.0, detail_scale=1.0, detail_roughness=0.5, phase_offset=0.0):
    """The Wave Texture node adds procedural bands or rings with noise distortion.
    #### Path
    - Texture > Wave Texture Node
    #### Properties:
    - `bands_direction`: `X`, `Y`, `Z`, `DIAGONAL`
    - `rings_direction`: `X`, `Y`, `Z`, `SPHERICAL`
    - `wave_profile`: `SIN`, `SAW`, `TRI`
    - `wave_type`: `BANDS`, `RINGS`
    #### Outputs:
    - `#0 color: Color = (0.0, 0.0, 0.0, 0.0)`
    - `#1 fac: Float = 0.0`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeTexWave.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/wave.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexWave.html)
    """
    node = new_node(*nodes.ShaderNodeTexWave(bands_direction, rings_direction, wave_profile, wave_type, color_mapping, texture_mapping, vector, scale, distortion, detail, detail_scale, detail_roughness, phase_offset))
    ret = typing.NamedTuple("ShaderNodeTexWave", [("color", Color), ("fac", Float)])
    return ret(node.outputs[0].Color, node.outputs[1].Float)
    return node.outputs[0].Color, node.outputs[1].Float


def ShaderNodeTexWhiteNoise(noise_dimensions='3D', vector: "Vector"=None, w=0.0):
    """The White Noise Texture node returns a random number based on an input Seed. The seed can be a number, a 2D vector, a 3D vector, or a 4D vector; depending on the Dimensions property. The output number ranges between zero and one.
    #### Path
    - Texture > White Noise Texture Node
    #### Properties:
    - `noise_dimensions`: `3D`, `1D`, `2D`, `4D`
    #### Outputs:
    - `#0 value: Float = 0.0`
    - `#1 color: Color = (0.0, 0.0, 0.0, 0.0)`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeTexWhiteNoise.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/white_noise.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexWhiteNoise.html)
    """
    node = new_node(*nodes.ShaderNodeTexWhiteNoise(noise_dimensions, vector, w))
    ret = typing.NamedTuple("ShaderNodeTexWhiteNoise", [("value", Float), ("color", Color)])
    return ret(node.outputs[0].Float, node.outputs[1].Color)
    return node.outputs[0].Float, node.outputs[1].Color


def ShaderNodeValToRGB(color_ramp=None, fac=0.5):
    """The Color Ramp Node is used for mapping values to colors with the use of a gradient.
    #### Path
    - Utilities > Color > Color Ramp Node
    #### Outputs:
    - `#0 color: Color = (0.0, 0.0, 0.0, 0.0)`
    - `#1 alpha: Float = 0.0`

    ![](https://docs.blender.org/manual/en/latest/_images/compositing_node-types_CompositorNodeValToRGB.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/color/color_ramp.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeValToRGB.html)
    """
    node = new_node(*nodes.ShaderNodeValToRGB(color_ramp, fac))
    ret = typing.NamedTuple("ShaderNodeValToRGB", [("color", Color), ("alpha", Float)])
    return ret(node.outputs[0].Color, node.outputs[1].Float)
    return node.outputs[0].Color, node.outputs[1].Float


def FunctionNodeCombineColor(mode='RGB', red=0.0, green=0.0, blue=0.0, alpha=1.0):
    """The Combine Color Node combines an image from its composite color channels. The node can combine multiple Color Models depending on the Mode property.
    #### Path
    - Utilities > Color > Combine Color Node
    #### Properties:
    - `mode`: `RGB`, `HSV`, `HSL`
    #### Outputs:
    - `#0 color: Color = (0.0, 0.0, 0.0, 0.0)`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_FunctionNodeCombineColor.png)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/color/combine_color.html) [[API]](https://docs.blender.org/api/current/bpy.types.FunctionNodeCombineColor.html)
    """
    node = new_node(*nodes.FunctionNodeCombineColor(mode, red, green, blue, alpha))
    return node.outputs[0].Color


def ShaderNodeMix(blend_type='MIX', data_type='FLOAT', factor_mode='UNIFORM', clamp_factor=True, clamp_result=False, factor_float=0.5, factor_vector=(0.5, 0.5, 0.5), a_float=0.0, b_float=0.0, a_vector=(0.0, 0.0, 0.0), b_vector=(0.0, 0.0, 0.0), a_color=(0.5, 0.5, 0.5, 1.0), b_color=(0.5, 0.5, 0.5, 1.0)):
    """The Mix Node mixes images by working on the individual and corresponding pixels of the two input images. Called “Mix Color” in the shader, geometry, and texture context.
    #### Path
    - Utilities > Color > Mix Node
    #### Properties:
    - `blend_type`: `MIX`, `DARKEN`, `MULTIPLY`, `BURN`, `LIGHTEN`, `SCREEN`, `DODGE`, `ADD`, `OVERLAY`, `SOFT_LIGHT`, `LINEAR_LIGHT`, `DIFFERENCE`, `EXCLUSION`, `SUBTRACT`, `DIVIDE`, `HUE`, `SATURATION`, `COLOR`, `VALUE`
    - `data_type`: `FLOAT`, `VECTOR`, `RGBA`
    - `factor_mode`: `UNIFORM`, `NON_UNIFORM`
    #### Outputs:
    - `#0 result_float: Float = 0.0`
    - `#1 result_vector: Vector = (0.0, 0.0, 0.0)`
    - `#2 result_color: Color = (0.0, 0.0, 0.0, 0.0)`

    ![](https://docs.blender.org/manual/en/latest/_images/compositing_node-types_CompositorNodeMixRGB.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/color/mix_rgb.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html)
    """
    node = new_node(*nodes.ShaderNodeMix(blend_type, data_type, factor_mode, clamp_factor, clamp_result, factor_float, factor_vector, a_float, b_float, a_vector, b_vector, a_color, b_color))
    ret = typing.NamedTuple("ShaderNodeMix", [("result", Float), ("result", Vector), ("result", Color)])
    return ret(node.outputs[0].Float, node.outputs[1].Vector, node.outputs[2].Color)
    return node.outputs[0].Float, node.outputs[1].Vector, node.outputs[2].Color


def ShaderNodeRGBCurve(mapping=None, fac=1.0, color=(1.0, 1.0, 1.0, 1.0)):
    """The RGB Curves Node allows color corrections for each color channel and levels adjustments in the compositing context.
    #### Path
    - Utilities > Color > RGB Curves Node
    #### Outputs:
    - `#0 color: Color = (0.0, 0.0, 0.0, 0.0)`

    ![](https://docs.blender.org/manual/en/latest/_images/compositing_node-types_CompositorNodeCurveRGB.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/color/rgb_curves.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeRGBCurve.html)
    """
    node = new_node(*nodes.ShaderNodeRGBCurve(mapping, fac, color))
    return node.outputs[0].Color


def FunctionNodeSeparateColor(mode='RGB', color=(1.0, 1.0, 1.0, 1.0)):
    """The Separate Color Node splits an image into its composite color channels. The node can output multiple Color Models depending on the Mode property.
    #### Path
    - Utilities > Color > Separate Color Node
    #### Properties:
    - `mode`: `RGB`, `HSV`, `HSL`
    #### Outputs:
    - `#0 red: Float = 0.0`
    - `#1 green: Float = 0.0`
    - `#2 blue: Float = 0.0`
    - `#3 alpha: Float = 0.0`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_FunctionNodeSeparateColor.png)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/color/separate_color.html) [[API]](https://docs.blender.org/api/current/bpy.types.FunctionNodeSeparateColor.html)
    """
    node = new_node(*nodes.FunctionNodeSeparateColor(mode, color))
    ret = typing.NamedTuple("FunctionNodeSeparateColor", [("red", Float), ("green", Float), ("blue", Float), ("alpha", Float)])
    return ret(node.outputs[0].Float, node.outputs[1].Float, node.outputs[2].Float, node.outputs[3].Float)
    return node.outputs[0].Float, node.outputs[1].Float, node.outputs[2].Float, node.outputs[3].Float


def GeometryNodeStringJoin(delimiter='', strings=''):
    """The Join Strings node combines any number of input strings into the output string. The order of the result depends on the vertical ordering of the inputs in the multi-input socket.
    #### Path
    - Utilities > Text > Join Strings Node
    #### Outputs:
    - `#0 string: String = ""`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeStringJoin.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/text/join_strings.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeStringJoin.html)
    """
    node = new_node(*nodes.GeometryNodeStringJoin(delimiter, strings))
    return node.outputs[0].String


def FunctionNodeReplaceString(string='', find='', replace=''):
    """The Replace String node replaces a string segment with another.
    #### Path
    - Utilities > Text > Replace String Node
    #### Outputs:
    - `#0 string: String = ""`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_FunctionNodeReplaceString.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/text/replace_string.html) [[API]](https://docs.blender.org/api/current/bpy.types.FunctionNodeReplaceString.html)
    """
    node = new_node(*nodes.FunctionNodeReplaceString(string, find, replace))
    return node.outputs[0].String


def FunctionNodeSliceString(string='', position=0, length=10):
    """The Slice String node extracts a string segment from a larger string.
    #### Path
    - Utilities > Text > Slice String Node
    #### Outputs:
    - `#0 string: String = ""`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_FunctionNodeSliceString.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/text/slice_string.html) [[API]](https://docs.blender.org/api/current/bpy.types.FunctionNodeSliceString.html)
    """
    node = new_node(*nodes.FunctionNodeSliceString(string, position, length))
    return node.outputs[0].String


def FunctionNodeInputSpecialCharacters():
    """The Special Characters node is used to output string characters that can’t be typed directly with the keyboard.
    #### Path
    - Utilities > Text > Special Characters Node
    #### Outputs:
    - `#0 line_break: String = ""`
    - `#1 tab: String = ""`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_FunctionNodeInputSpecialCharacters.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/text/special_characters.html) [[API]](https://docs.blender.org/api/current/bpy.types.FunctionNodeInputSpecialCharacters.html)
    """
    node = new_node(*nodes.FunctionNodeInputSpecialCharacters())
    ret = typing.NamedTuple("FunctionNodeInputSpecialCharacters", [("line_break", String), ("tab", String)])
    return ret(node.outputs[0].String, node.outputs[1].String)
    return node.outputs[0].String, node.outputs[1].String


def FunctionNodeStringLength(string=''):
    """The String Length node outputs the number of characters in the input string.
    #### Path
    - Utilities > Text > String Length Node
    #### Outputs:
    - `#0 length: Integer = 0`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_FunctionNodeStringLength.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/text/string_length.html) [[API]](https://docs.blender.org/api/current/bpy.types.FunctionNodeStringLength.html)
    """
    node = new_node(*nodes.FunctionNodeStringLength(string))
    return node.outputs[0].Integer


def GeometryNodeStringToCurves(align_x='LEFT', align_y='TOP_BASELINE', overflow='OVERFLOW', pivot_mode='BOTTOM_LEFT', font=None, string='', size=1.0, character_spacing=1.0, word_spacing=1.0, line_spacing=1.0, text_box_width=0.0, text_box_height=0.0):
    """The String to Curves converts a string to curve instances. Each unique character used in the string is converted to a curve once, and further uses of that character are more instances of the same geometry.
    #### Path
    - Utilities > Text > String to Curves Node
    #### Properties:
    - `align_x`: `LEFT`, `CENTER`, `RIGHT`, `JUSTIFY`, `FLUSH`
    - `align_y`: `TOP_BASELINE`, `TOP`, `MIDDLE`, `BOTTOM_BASELINE`, `BOTTOM`
    - `overflow`: `OVERFLOW`, `SCALE_TO_FIT`, `TRUNCATE`
    - `pivot_mode`: `BOTTOM_LEFT`, `MIDPOINT`, `TOP_LEFT`, `TOP_CENTER`, `TOP_RIGHT`, `BOTTOM_CENTER`, `BOTTOM_RIGHT`
    #### Outputs:
    - `#0 curve_instances: Geometry = None`
    - `#1 remainder: String = ""`
    - `#2 line: Integer = 0`
    - `#3 pivot_point: Vector = (0.0, 0.0, 0.0)`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeStringToCurves.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/text/string_to_curves.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeStringToCurves.html)
    """
    node = new_node(*nodes.GeometryNodeStringToCurves(align_x, align_y, overflow, pivot_mode, font, string, size, character_spacing, word_spacing, line_spacing, text_box_width, text_box_height))
    ret = typing.NamedTuple("GeometryNodeStringToCurves", [("curve_instances", Geometry), ("remainder", String), ("line", Integer), ("pivot_point", Vector)])
    return ret(node.outputs[0].Geometry, node.outputs[1].String, node.outputs[2].Integer, node.outputs[3].Vector)
    return node.outputs[0].Geometry, node.outputs[1].String, node.outputs[2].Integer, node.outputs[3].Vector


def FunctionNodeValueToString(value=0.0, decimals=0):
    """The Value to String node generates string representation of the input value.
    #### Path
    - Utilities > Text > Value to String Node
    #### Outputs:
    - `#0 string: String = ""`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_FunctionNodeValueToString.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/text/value_to_string.html) [[API]](https://docs.blender.org/api/current/bpy.types.FunctionNodeValueToString.html)
    """
    node = new_node(*nodes.FunctionNodeValueToString(value, decimals))
    return node.outputs[0].String


def ShaderNodeCombineXYZ(x=0.0, y=0.0, z=0.0):
    """The Combine XYZ Node combines a vector from its individual components.
    #### Path
    - Utilities > Vector > Combine XYZ Node
    #### Outputs:
    - `#0 vector: Vector = (0.0, 0.0, 0.0)`

    ![](https://docs.blender.org/manual/en/latest/_images/compositing_node-types_CompositorNodeCombineXYZ.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/combine_xyz.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeCombineXYZ.html)
    """
    node = new_node(*nodes.ShaderNodeCombineXYZ(x, y, z))
    return node.outputs[0].Vector


def ShaderNodeSeparateXYZ(vector=(0.0, 0.0, 0.0)):
    """The Separate XYZ Node splits a vector into its individual components.
    #### Path
    - Utilities > Vector > Separate XYZ Node
    #### Outputs:
    - `#0 x: Float = 0.0`
    - `#1 y: Float = 0.0`
    - `#2 z: Float = 0.0`

    ![](https://docs.blender.org/manual/en/latest/_images/compositing_node-types_CompositorNodeSeparateXYZ.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/separate_xyz.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeSeparateXYZ.html)
    """
    node = new_node(*nodes.ShaderNodeSeparateXYZ(vector))
    ret = typing.NamedTuple("ShaderNodeSeparateXYZ", [("x", Float), ("y", Float), ("z", Float)])
    return ret(node.outputs[0].Float, node.outputs[1].Float, node.outputs[2].Float)
    return node.outputs[0].Float, node.outputs[1].Float, node.outputs[2].Float


def ShaderNodeVectorCurve(mapping=None, fac=1.0, vector=(0.0, 0.0, 0.0)):
    """The Vector Curves node maps an input vector components to a curve.
    #### Path
    - Utilities > Vector > Vector Curves Node
    #### Outputs:
    - `#0 vector: Vector = (0.0, 0.0, 0.0)`

    ![](https://docs.blender.org/manual/en/latest/_images/compositing_node-types_CompositorNodeCurveVec.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_curves.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorCurve.html)
    """
    node = new_node(*nodes.ShaderNodeVectorCurve(mapping, fac, vector))
    return node.outputs[0].Vector


def ShaderNodeVectorMath(operation='ADD', vector=(0.0, 0.0, 0.0), vector_001=(0.0, 0.0, 0.0), vector_002=(0.0, 0.0, 0.0), scale=1.0):
    """The Vector Math node performs the selected math operation on the input vectors.
    #### Path
    - Utilities > Vector > Vector Math Node
    #### Properties:
    - `operation`: `ADD`, `SUBTRACT`, `MULTIPLY`, `DIVIDE`, `MULTIPLY_ADD`, `CROSS_PRODUCT`, `PROJECT`, `REFLECT`, `REFRACT`, `FACEFORWARD`, `DOT_PRODUCT`, `DISTANCE`, `LENGTH`, `SCALE`, `NORMALIZE`, `ABSOLUTE`, `MINIMUM`, `MAXIMUM`, `FLOOR`, `CEIL`, `FRACTION`, `MODULO`, `WRAP`, `SNAP`, `SINE`, `COSINE`, `TANGENT`
    #### Outputs:
    - `#0 vector: Vector = (0.0, 0.0, 0.0)`
    - `#1 value: Float = 0.0`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeVectorMath.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_math.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)
    """
    node = new_node(*nodes.ShaderNodeVectorMath(operation, vector, vector_001, vector_002, scale))
    ret = typing.NamedTuple("ShaderNodeVectorMath", [("vector", Vector), ("value", Float)])
    return ret(node.outputs[0].Vector, node.outputs[1].Float)
    return node.outputs[0].Vector, node.outputs[1].Float


def ShaderNodeVectorRotate(rotation_type='AXIS_ANGLE', invert=False, vector=(0.0, 0.0, 0.0), center=(0.0, 0.0, 0.0), axis=(0.0, 0.0, 1.0), angle=math.radians(0.0), rotation=(0.0, 0.0, 0.0)):
    """The Vector Rotate Node provides the ability to rotate a vector around a pivot point (Center).
    #### Path
    - Utilities > Vector > Vector Rotate Node
    #### Properties:
    - `rotation_type`: `AXIS_ANGLE`, `X_AXIS`, `Y_AXIS`, `Z_AXIS`, `EULER_XYZ`
    #### Outputs:
    - `#0 vector: Vector = (0.0, 0.0, 0.0)`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeVectorRotate.png)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_rotate.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorRotate.html)
    """
    node = new_node(*nodes.ShaderNodeVectorRotate(rotation_type, invert, vector, center, axis, angle, rotation))
    return node.outputs[0].Vector


def GeometryNodeAccumulateField(data_type='FLOAT', domain='POINT', value_vector=(1.0, 1.0, 1.0), value_float=1.0, value_int=1, group_index=0):
    """The Accumulate Field node counts a running total of its input values, in the order defined by the geometry’s indices. The node’s essential operation is just addition, but instead of only outputting the final total, it outputs the current value at every element.
    #### Path
    - Utilities > Field > Accumulate Field Node
    #### Properties:
    - `data_type`: `FLOAT`, `INT`, `FLOAT_VECTOR`
    - `domain`: `POINT`, `EDGE`, `FACE`, `CORNER`, `CURVE`, `INSTANCE`
    #### Outputs:
    - `#0 leading_vector: Vector = (0.0, 0.0, 0.0)`
    - `#1 leading_float: Float = 0.0`
    - `#2 leading_int: Integer = 0`
    - `#3 trailing_vector: Vector = (0.0, 0.0, 0.0)`
    - `#4 trailing_float: Float = 0.0`
    - `#5 trailing_int: Integer = 0`
    - `#6 total_vector: Vector = (0.0, 0.0, 0.0)`
    - `#7 total_float: Float = 0.0`
    - `#8 total_int: Integer = 0`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeAccumulateField.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/field/accumulate_field.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeAccumulateField.html)
    """
    node = new_node(*nodes.GeometryNodeAccumulateField(data_type, domain, value_vector, value_float, value_int, group_index))
    ret = typing.NamedTuple("GeometryNodeAccumulateField", [("leading", Vector), ("leading", Float), ("leading", Integer), ("trailing", Vector), ("trailing", Float), ("trailing", Integer), ("total", Vector), ("total", Float), ("total", Integer)])
    return ret(node.outputs[0].Vector, node.outputs[1].Float, node.outputs[2].Integer, node.outputs[3].Vector, node.outputs[4].Float, node.outputs[5].Integer, node.outputs[6].Vector, node.outputs[7].Float, node.outputs[8].Integer)
    return node.outputs[0].Vector, node.outputs[1].Float, node.outputs[2].Integer, node.outputs[3].Vector, node.outputs[4].Float, node.outputs[5].Integer, node.outputs[6].Vector, node.outputs[7].Float, node.outputs[8].Integer


def GeometryNodeFieldAtIndex(data_type='FLOAT', domain='POINT', index=0, value_float=0.0, value_int=0, value_vector=(0.0, 0.0, 0.0), value_color=(0.0, 0.0, 0.0, 0.0), value_bool=False):
    """The Evaluate at Index node allows accessing data of other elements in the context geometry. It is similar to the Sample Index Node. The main difference is that this node does not require a geometry input, because the geometry from the field context is used.
    #### Path
    - Utilities > Field > Evaluate at Index Node
    #### Properties:
    - `data_type`: `FLOAT`, `INT`, `FLOAT_VECTOR`, `FLOAT_COLOR`, `BOOLEAN`
    - `domain`: `POINT`, `EDGE`, `FACE`, `CORNER`, `CURVE`, `INSTANCE`
    #### Outputs:
    - `#0 value_float: Float = 0.0`
    - `#1 value_int: Integer = 0`
    - `#2 value_vector: Vector = (0.0, 0.0, 0.0)`
    - `#3 value_color: Color = (0.0, 0.0, 0.0, 0.0)`
    - `#4 value_bool: Boolean = False`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeFieldAtIndex.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/field/evaluate_at_index.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeFieldAtIndex.html)
    """
    node = new_node(*nodes.GeometryNodeFieldAtIndex(data_type, domain, index, value_float, value_int, value_vector, value_color, value_bool))
    ret = typing.NamedTuple("GeometryNodeFieldAtIndex", [("value", Float), ("value", Integer), ("value", Vector), ("value", Color), ("value", Boolean)])
    return ret(node.outputs[0].Float, node.outputs[1].Integer, node.outputs[2].Vector, node.outputs[3].Color, node.outputs[4].Boolean)
    return node.outputs[0].Float, node.outputs[1].Integer, node.outputs[2].Vector, node.outputs[3].Color, node.outputs[4].Boolean


def GeometryNodeFieldOnDomain(data_type='FLOAT', domain='POINT', value_float=0.0, value_int=0, value_vector=(0.0, 0.0, 0.0), value_color=(0.0, 0.0, 0.0, 0.0), value_bool=False):
    """The Evaluate on Domain allows evaluating a field for a different attribute domain than the domain from the field context. For example, the face index could be used instead of the face corner index, when setting the values of a UV Map
    #### Path
    - Utilities > Field > Evaluate on Domain Node
    #### Properties:
    - `data_type`: `FLOAT`, `INT`, `FLOAT_VECTOR`, `FLOAT_COLOR`, `BOOLEAN`
    - `domain`: `POINT`, `EDGE`, `FACE`, `CORNER`, `CURVE`, `INSTANCE`
    #### Outputs:
    - `#0 value_float: Float = 0.0`
    - `#1 value_int: Integer = 0`
    - `#2 value_vector: Vector = (0.0, 0.0, 0.0)`
    - `#3 value_color: Color = (0.0, 0.0, 0.0, 0.0)`
    - `#4 value_bool: Boolean = False`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeInterpolateDomain.png)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/field/evaluate_on_domain.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeFieldOnDomain.html)
    """
    node = new_node(*nodes.GeometryNodeFieldOnDomain(data_type, domain, value_float, value_int, value_vector, value_color, value_bool))
    ret = typing.NamedTuple("GeometryNodeFieldOnDomain", [("value", Float), ("value", Integer), ("value", Vector), ("value", Color), ("value", Boolean)])
    return ret(node.outputs[0].Float, node.outputs[1].Integer, node.outputs[2].Vector, node.outputs[3].Color, node.outputs[4].Boolean)
    return node.outputs[0].Float, node.outputs[1].Integer, node.outputs[2].Vector, node.outputs[3].Color, node.outputs[4].Boolean


def FunctionNodeBooleanMath(operation='AND', boolean=False, boolean_001=False):
    """The Boolean Math node performs a basic logical operation on its inputs.
    #### Path
    - Utilities > Math > Boolean Math Node
    #### Properties:
    - `operation`: `AND`, `OR`, `NOT`, `NAND`, `NOR`, `XNOR`, `XOR`, `IMPLY`, `NIMPLY`
    #### Outputs:
    - `#0 boolean: Boolean = False`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_FunctionNodeBooleanMath.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/boolean_math.html) [[API]](https://docs.blender.org/api/current/bpy.types.FunctionNodeBooleanMath.html)
    """
    node = new_node(*nodes.FunctionNodeBooleanMath(operation, boolean, boolean_001))
    return node.outputs[0].Boolean


def ShaderNodeClamp(clamp_type='MINMAX', value=1.0, min=0.0, max=1.0):
    """The Clamp node clamps a value between a minimum and a maximum.
    #### Path
    - Utilities > Math > Clamp Node
    #### Properties:
    - `clamp_type`: `MINMAX`, `RANGE`
    #### Outputs:
    - `#0 result: Float = 0.0`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeClamp.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/clamp.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeClamp.html)
    """
    node = new_node(*nodes.ShaderNodeClamp(clamp_type, value, min, max))
    return node.outputs[0].Float


def FunctionNodeCompare(data_type='FLOAT', mode='ELEMENT', operation='GREATER_THAN', a=0.0, b=0.0, a_int=0, b_int=0, a_vec3=(0.0, 0.0, 0.0), b_vec3=(0.0, 0.0, 0.0), a_col=(0.0, 0.0, 0.0, 0.0), b_col=(0.0, 0.0, 0.0, 0.0), a_str='', b_str='', c=0.9, angle=math.radians(5.0), epsilon=0.001):
    """The Compare node takes two inputs and does an operation to determine whether they are similar. The node can work on all generic data types, and has modes for vectors that contain more complex comparisons, which can help to reduce the number of necessary nodes, and make a node tree more readable.
    #### Path
    - Utilities > Math > Compare Node
    #### Properties:
    - `data_type`: `FLOAT`, `INT`, `VECTOR`, `STRING`, `RGBA`
    - `mode`: `ELEMENT`, `LENGTH`, `AVERAGE`, `DOT_PRODUCT`, `DIRECTION`
    - `operation`: `GREATER_THAN`, `LESS_THAN`, `LESS_EQUAL`, `GREATER_EQUAL`, `EQUAL`, `NOT_EQUAL`
    #### Outputs:
    - `#0 result: Boolean = False`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_FunctionNodeCompare.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/compare.html) [[API]](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)
    """
    node = new_node(*nodes.FunctionNodeCompare(data_type, mode, operation, a, b, a_int, b_int, a_vec3, b_vec3, a_col, b_col, a_str, b_str, c, angle, epsilon))
    return node.outputs[0].Boolean


def ShaderNodeFloatCurve(mapping=None, factor=1.0, value=1.0):
    """The Float Curve node maps an input float to a curve and outputs a float value.
    #### Path
    - Utilities > Math > Float Curve
    #### Outputs:
    - `#0 value: Float = 0.0`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeFloatCurve.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/float_curve.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeFloatCurve.html)
    """
    node = new_node(*nodes.ShaderNodeFloatCurve(mapping, factor, value))
    return node.outputs[0].Float


def FunctionNodeFloatToInt(rounding_mode='ROUND', float=0.0):
    """The Float To Integer node takes a single floating point number input and converts it to an integer with a choice of methods.
    #### Path
    - Utilities > Math > Float To Integer Node
    #### Properties:
    - `rounding_mode`: `ROUND`, `FLOOR`, `CEILING`, `TRUNCATE`
    #### Outputs:
    - `#0 integer: Integer = 0`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_FunctionNodeFloatToInt.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/float_to_integer.html) [[API]](https://docs.blender.org/api/current/bpy.types.FunctionNodeFloatToInt.html)
    """
    node = new_node(*nodes.FunctionNodeFloatToInt(rounding_mode, float))
    return node.outputs[0].Integer


def ShaderNodeMapRange(data_type='FLOAT', interpolation_type='LINEAR', clamp=True, value=1.0, from_min=0.0, from_max=1.0, to_min=0.0, to_max=1.0, steps=4.0, vector=(0.0, 0.0, 0.0), from_min_float3=(0.0, 0.0, 0.0), from_max_float3=(1.0, 1.0, 1.0), to_min_float3=(0.0, 0.0, 0.0), to_max_float3=(1.0, 1.0, 1.0), steps_float3=(4.0, 4.0, 4.0)):
    """The Map Range node remaps a value from a range to a target range.
    #### Path
    - Utilities > Math > Map Range Node
    #### Properties:
    - `data_type`: `FLOAT`, `FLOAT_VECTOR`
    - `interpolation_type`: `LINEAR`, `STEPPED`, `SMOOTHSTEP`, `SMOOTHERSTEP`
    #### Outputs:
    - `#0 result: Float = 0.0`
    - `#1 vector: Vector = (0.0, 0.0, 0.0)`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeMapRange.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/map_range.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeMapRange.html)
    """
    node = new_node(*nodes.ShaderNodeMapRange(data_type, interpolation_type, clamp, value, from_min, from_max, to_min, to_max, steps, vector, from_min_float3, from_max_float3, to_min_float3, to_max_float3, steps_float3))
    ret = typing.NamedTuple("ShaderNodeMapRange", [("result", Float), ("vector", Vector)])
    return ret(node.outputs[0].Float, node.outputs[1].Vector)
    return node.outputs[0].Float, node.outputs[1].Vector


def ShaderNodeMath(operation='ADD', use_clamp=False, value=0.5, value_001=0.5, value_002=0.5):
    """The Math Node performs math operations.
    #### Path
    - Utilities > Math > Math Node
    #### Properties:
    - `operation`: `ADD`, `SUBTRACT`, `MULTIPLY`, `DIVIDE`, `MULTIPLY_ADD`, `POWER`, `LOGARITHM`, `SQRT`, `INVERSE_SQRT`, `ABSOLUTE`, `EXPONENT`, `MINIMUM`, `MAXIMUM`, `LESS_THAN`, `GREATER_THAN`, `SIGN`, `COMPARE`, `SMOOTH_MIN`, `SMOOTH_MAX`, `ROUND`, `FLOOR`, `CEIL`, `TRUNC`, `FRACT`, `MODULO`, `WRAP`, `SNAP`, `PINGPONG`, `SINE`, `COSINE`, `TANGENT`, `ARCSINE`, `ARCCOSINE`, `ARCTANGENT`, `ARCTAN2`, `SINH`, `COSH`, `TANH`, `RADIANS`, `DEGREES`
    #### Outputs:
    - `#0 value: Float = 0.0`

    ![](https://docs.blender.org/manual/en/latest/_images/compositing_node-types_CompositorNodeMath.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/math.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
    """
    node = new_node(*nodes.ShaderNodeMath(operation, use_clamp, value, value_001, value_002))
    return node.outputs[0].Float


def ShaderNodeMix(blend_type='MIX', data_type='FLOAT', factor_mode='UNIFORM', clamp_factor=True, clamp_result=False, factor_float=0.5, factor_vector=(0.5, 0.5, 0.5), a_float=0.0, b_float=0.0, a_vector=(0.0, 0.0, 0.0), b_vector=(0.0, 0.0, 0.0), a_color=(0.5, 0.5, 0.5, 1.0), b_color=(0.5, 0.5, 0.5, 1.0)):
    """The Mix Node mixes values, colors and vectors inputs using a factor to control the amount of interpolation. The Color mode has additional blending modes.
    #### Path
    - Utilities > Math > Mix Node
    #### Properties:
    - `blend_type`: `MIX`, `DARKEN`, `MULTIPLY`, `BURN`, `LIGHTEN`, `SCREEN`, `DODGE`, `ADD`, `OVERLAY`, `SOFT_LIGHT`, `LINEAR_LIGHT`, `DIFFERENCE`, `EXCLUSION`, `SUBTRACT`, `DIVIDE`, `HUE`, `SATURATION`, `COLOR`, `VALUE`
    - `data_type`: `FLOAT`, `VECTOR`, `RGBA`
    - `factor_mode`: `UNIFORM`, `NON_UNIFORM`
    #### Outputs:
    - `#0 result_float: Float = 0.0`
    - `#1 result_vector: Vector = (0.0, 0.0, 0.0)`
    - `#2 result_color: Color = (0.0, 0.0, 0.0, 0.0)`

    ![](https://docs.blender.org/manual/en/latest/_images/render_shader-nodes_shader_mix_node.jpg)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/mix.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html)
    """
    node = new_node(*nodes.ShaderNodeMix(blend_type, data_type, factor_mode, clamp_factor, clamp_result, factor_float, factor_vector, a_float, b_float, a_vector, b_vector, a_color, b_color))
    ret = typing.NamedTuple("ShaderNodeMix", [("result", Float), ("result", Vector), ("result", Color)])
    return ret(node.outputs[0].Float, node.outputs[1].Vector, node.outputs[2].Color)
    return node.outputs[0].Float, node.outputs[1].Vector, node.outputs[2].Color


def FunctionNodeAlignEulerToVector(axis='X', pivot_axis='AUTO', rotation=(0.0, 0.0, 0.0), factor=1.0, vector=(0.0, 0.0, 1.0)):
    """The Align Euler to Vector node rotates an Euler rotation into the given direction.
    #### Path
    - Utilities > Rotation > Align Euler to Vector Node
    #### Properties:
    - `axis`: `X`, `Y`, `Z`
    - `pivot_axis`: `AUTO`, `X`, `Y`, `Z`
    #### Outputs:
    - `#0 rotation: Vector = (0.0, 0.0, 0.0)`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_FunctionNodeAlignEulerToVector.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/rotation/align_euler_to_vector.html) [[API]](https://docs.blender.org/api/current/bpy.types.FunctionNodeAlignEulerToVector.html)
    """
    node = new_node(*nodes.FunctionNodeAlignEulerToVector(axis, pivot_axis, rotation, factor, vector))
    return node.outputs[0].Vector


def FunctionNodeRotateEuler(space='OBJECT', type='EULER', rotation=(0.0, 0.0, 0.0), rotate_by=(0.0, 0.0, 0.0), axis=(0.0, 0.0, 1.0), angle=math.radians(0.0)):
    """The Rotate Euler node rotates an Euler rotation.
    #### Path
    - Utilities > Rotation > Rotate Euler Node
    #### Properties:
    - `space`: `OBJECT`, `LOCAL`
    - `type`: `EULER`, `AXIS_ANGLE`
    #### Outputs:
    - `#0 rotation: Vector = (0.0, 0.0, 0.0)`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_FunctionNodeRotateEuler.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/rotation/rotate_euler.html) [[API]](https://docs.blender.org/api/current/bpy.types.FunctionNodeRotateEuler.html)
    """
    node = new_node(*nodes.FunctionNodeRotateEuler(space, type, rotation, rotate_by, axis, angle))
    return node.outputs[0].Vector


def FunctionNodeRandomValue(data_type='FLOAT', min=(0.0, 0.0, 0.0), max=(1.0, 1.0, 1.0), min_001=0.0, max_001=1.0, min_002=0, max_002=100, probability=0.5, id: "Integer"=None, seed=0):
    """The Random Value node outputs a white noise like value as a Float, Integer, Vector, or Boolean field.
    #### Path
    - Utilities > Random Value Node
    #### Properties:
    - `data_type`: `FLOAT`, `INT`, `FLOAT_VECTOR`, `BOOLEAN`
    #### Outputs:
    - `#0 value: Vector = (0.0, 0.0, 0.0)`
    - `#1 value_001: Float = 0.0`
    - `#2 value_002: Integer = 0`
    - `#3 value_003: Boolean = False`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_FunctionNodeRandomValue.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/random_value.html) [[API]](https://docs.blender.org/api/current/bpy.types.FunctionNodeRandomValue.html)
    """
    node = new_node(*nodes.FunctionNodeRandomValue(data_type, min, max, min_001, max_001, min_002, max_002, probability, id, seed))
    ret = typing.NamedTuple("FunctionNodeRandomValue", [("value", Vector), ("value", Float), ("value", Integer), ("value", Boolean)])
    return ret(node.outputs[0].Vector, node.outputs[1].Float, node.outputs[2].Integer, node.outputs[3].Boolean)
    return node.outputs[0].Vector, node.outputs[1].Float, node.outputs[2].Integer, node.outputs[3].Boolean


def GeometryNodeSwitch(input_type='GEOMETRY', switch=False, switch_001=False, false=0.0, true=0.0, false_001=0, true_001=0, false_002=False, true_002=True, false_003=(0.0, 0.0, 0.0), true_003=(0.0, 0.0, 0.0), false_004=(0.8, 0.8, 0.8, 1.0), true_004=(0.8, 0.8, 0.8, 1.0), false_005='', true_005='', false_006=None, true_006=None, false_007=None, true_007=None, false_008=None, true_008=None, false_009=None, true_009=None, false_010=None, true_010=None, false_011=None, true_011=None):
    """The Switch node outputs one of two inputs depending on a condition. Only the input that is passed through the node is computed.
    #### Path
    - Utilities > Switch Node
    #### Properties:
    - `input_type`: `GEOMETRY`, `FLOAT`, `INT`, `BOOLEAN`, `VECTOR`, `STRING`, `RGBA`, `OBJECT`, `IMAGE`, `COLLECTION`, `TEXTURE`, `MATERIAL`
    #### Outputs:
    - `#0 output: Float = 0.0`
    - `#1 output_001: Integer = 0`
    - `#2 output_002: Boolean = False`
    - `#3 output_003: Vector = (0.0, 0.0, 0.0)`
    - `#4 output_004: Color = (0.0, 0.0, 0.0, 0.0)`
    - `#5 output_005: String = ""`
    - `#6 output_006: Geometry = None`
    - `#7 output_007: Object = None`
    - `#8 output_008: Collection = None`
    - `#9 output_009: Texture = None`
    - `#10 output_010: Material = None`
    - `#11 output_011: Image = None`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeSwitch.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/switch.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeSwitch.html)
    """
    node = new_node(*nodes.GeometryNodeSwitch(input_type, switch, switch_001, false, true, false_001, true_001, false_002, true_002, false_003, true_003, false_004, true_004, false_005, true_005, false_006, true_006, false_007, true_007, false_008, true_008, false_009, true_009, false_010, true_010, false_011, true_011))
    ret = typing.NamedTuple("GeometryNodeSwitch", [("output", Float), ("output", Integer), ("output", Boolean), ("output", Vector), ("output", Color), ("output", String), ("output", Geometry), ("output", Object), ("output", Collection), ("output", Texture), ("output", Material), ("output", Image)])
    return ret(node.outputs[0].Float, node.outputs[1].Integer, node.outputs[2].Boolean, node.outputs[3].Vector, node.outputs[4].Color, node.outputs[5].String, node.outputs[6].Geometry, node.outputs[7].Object, node.outputs[8].Collection, node.outputs[9].Texture, node.outputs[10].Material, node.outputs[11].Image)
    return node.outputs[0].Float, node.outputs[1].Integer, node.outputs[2].Boolean, node.outputs[3].Vector, node.outputs[4].Color, node.outputs[5].String, node.outputs[6].Geometry, node.outputs[7].Object, node.outputs[8].Collection, node.outputs[9].Texture, node.outputs[10].Material, node.outputs[11].Image


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
    