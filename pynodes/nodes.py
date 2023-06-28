import math, bpy


def GeometryNodeAttributeStatistic(data_type='FLOAT', domain='POINT', geometry=None, selection=True, attribute=0.0, attribute_001=(0.0, 0.0, 0.0)):
    """
    - `data_type`: `FLOAT`, `FLOAT_VECTOR`
    - `domain`: `POINT`, `EDGE`, `FACE`, `CORNER`, `CURVE`, `INSTANCE`
    #### Inputs:
    - `#0 geometry: Geometry = None`
    - `#1 selection: Boolean = True`
    - `#2 attribute: Float = 0.0`
    - `#3 attribute_001: Vector = (0.0, 0.0, 0.0)`
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
    """
    params_all = [('data_type', data_type, 'FLOAT'), ('domain', domain, 'POINT')]
    inputs_all = [(geometry, None), (selection, True), (attribute, 0.0), (attribute_001, (0.0, 0.0, 0.0))]
    return "GeometryNodeAttributeStatistic", params_all, inputs_all


def GeometryNodeAttributeDomainSize(component='MESH', geometry=None):
    """
    - `component`: `MESH`, `POINTCLOUD`, `CURVE`, `INSTANCES`
    #### Inputs:
    - `#0 geometry: Geometry = None`
    #### Outputs:
    - `#0 point_count: Integer = 0`
    - `#1 edge_count: Integer = 0`
    - `#2 face_count: Integer = 0`
    - `#3 face_corner_count: Integer = 0`
    - `#4 spline_count: Integer = 0`
    - `#5 instance_count: Integer = 0`
    """
    params_all = [('component', component, 'MESH')]
    inputs_all = [(geometry, None)]
    return "GeometryNodeAttributeDomainSize", params_all, inputs_all


def GeometryNodeBlurAttribute(data_type='FLOAT', value_float=0.0, value_int=0, value_vector=(0.0, 0.0, 0.0), value_color=(0.0, 0.0, 0.0, 0.0), iterations=1, weight=1.0):
    """
    - `data_type`: `FLOAT`, `INT`, `FLOAT_VECTOR`, `FLOAT_COLOR`
    #### Inputs:
    - `#0 value_float: Float = 0.0`
    - `#1 value_int: Integer = 0`
    - `#2 value_vector: Vector = (0.0, 0.0, 0.0)`
    - `#3 value_color: Color = (0.0, 0.0, 0.0, 0.0)`
    - `#4 iterations: Integer = 1`
    - `#5 weight: Float = 1.0`
    #### Outputs:
    - `#0 value_float: Float = 0.0`
    - `#1 value_int: Integer = 0`
    - `#2 value_vector: Vector = (0.0, 0.0, 0.0)`
    - `#3 value_color: Color = (0.0, 0.0, 0.0, 0.0)`
    """
    params_all = [('data_type', data_type, 'FLOAT')]
    inputs_all = [(value_float, 0.0), (value_int, 0), (value_vector, (0.0, 0.0, 0.0)), (value_color, (0.0, 0.0, 0.0, 0.0)), (iterations, 1), (weight, 1.0)]
    return "GeometryNodeBlurAttribute", params_all, inputs_all


def GeometryNodeCaptureAttribute(data_type='FLOAT', domain='POINT', geometry=None, value=(0.0, 0.0, 0.0), value_001=0.0, value_002=(0.0, 0.0, 0.0, 0.0), value_003=False, value_004=0):
    """
    - `data_type`: `FLOAT`, `INT`, `FLOAT_VECTOR`, `FLOAT_COLOR`, `BOOLEAN`
    - `domain`: `POINT`, `EDGE`, `FACE`, `CORNER`, `CURVE`, `INSTANCE`
    #### Inputs:
    - `#0 geometry: Geometry = None`
    - `#1 value: Vector = (0.0, 0.0, 0.0)`
    - `#2 value_001: Float = 0.0`
    - `#3 value_002: Color = (0.0, 0.0, 0.0, 0.0)`
    - `#4 value_003: Boolean = False`
    - `#5 value_004: Integer = 0`
    #### Outputs:
    - `#0 geometry: Geometry = None`
    - `#1 attribute: Vector = (0.0, 0.0, 0.0)`
    - `#2 attribute_001: Float = 0.0`
    - `#3 attribute_002: Color = (0.0, 0.0, 0.0, 0.0)`
    - `#4 attribute_003: Boolean = False`
    - `#5 attribute_004: Integer = 0`
    """
    params_all = [('data_type', data_type, 'FLOAT'), ('domain', domain, 'POINT')]
    inputs_all = [(geometry, None), (value, (0.0, 0.0, 0.0)), (value_001, 0.0), (value_002, (0.0, 0.0, 0.0, 0.0)), (value_003, False), (value_004, 0)]
    return "GeometryNodeCaptureAttribute", params_all, inputs_all


def GeometryNodeRemoveAttribute(geometry=None, name=''):
    """
    #### Inputs:
    - `#0 geometry: Geometry = None`
    - `#1 name: String = ''`
    #### Outputs:
    - `#0 geometry: Geometry = None`
    """
    params_all = []
    inputs_all = [(geometry, None), (name, '')]
    return "GeometryNodeRemoveAttribute", params_all, inputs_all


def GeometryNodeStoreNamedAttribute(data_type='FLOAT', domain='POINT', geometry=None, selection=True, name='', value_vector=(0.0, 0.0, 0.0), value_float=0.0, value_color=(0.0, 0.0, 0.0, 0.0), value_bool=False, value_int=0):
    """
    - `data_type`: `FLOAT`, `INT`, `FLOAT_VECTOR`, `FLOAT_COLOR`, `BYTE_COLOR`, `BOOLEAN`, `FLOAT2`
    - `domain`: `POINT`, `EDGE`, `FACE`, `CORNER`, `CURVE`, `INSTANCE`
    #### Inputs:
    - `#0 geometry: Geometry = None`
    - `#1 selection: Boolean = True`
    - `#2 name: String = ''`
    - `#3 value_vector: Vector = (0.0, 0.0, 0.0)`
    - `#4 value_float: Float = 0.0`
    - `#5 value_color: Color = (0.0, 0.0, 0.0, 0.0)`
    - `#6 value_bool: Boolean = False`
    - `#7 value_int: Integer = 0`
    #### Outputs:
    - `#0 geometry: Geometry = None`
    """
    params_all = [('data_type', data_type, 'FLOAT'), ('domain', domain, 'POINT')]
    inputs_all = [(geometry, None), (selection, True), (name, ''), (value_vector, (0.0, 0.0, 0.0)), (value_float, 0.0), (value_color, (0.0, 0.0, 0.0, 0.0)), (value_bool, False), (value_int, 0)]
    return "GeometryNodeStoreNamedAttribute", params_all, inputs_all


def FunctionNodeInputBool(boolean=False):
    """
    #### Outputs:
    - `#0 boolean: Boolean = False`
    """
    params_all = [('boolean', boolean, False)]
    inputs_all = []
    return "FunctionNodeInputBool", params_all, inputs_all


def FunctionNodeInputColor():
    """
    #### Outputs:
    - `#0 color: Color = (0.0, 0.0, 0.0, 0.0)`
    """
    params_all = []
    inputs_all = []
    return "FunctionNodeInputColor", params_all, inputs_all


def GeometryNodeInputImage(image=None):
    """
    #### Outputs:
    - `#0 image: Image = None`
    """
    params_all = [('image', image, None)]
    inputs_all = []
    return "GeometryNodeInputImage", params_all, inputs_all


def FunctionNodeInputInt(integer=0):
    """
    #### Outputs:
    - `#0 integer: Integer = 0`
    """
    params_all = [('integer', integer, 0)]
    inputs_all = []
    return "FunctionNodeInputInt", params_all, inputs_all


def GeometryNodeInputMaterial(material=None):
    """
    #### Outputs:
    - `#0 material: Material = None`
    """
    params_all = [('material', material, None)]
    inputs_all = []
    return "GeometryNodeInputMaterial", params_all, inputs_all


def FunctionNodeInputString(string=''):
    """
    #### Outputs:
    - `#0 string: String = ""`
    """
    params_all = [('string', string, '')]
    inputs_all = []
    return "FunctionNodeInputString", params_all, inputs_all


def ShaderNodeValue():
    """
    #### Outputs:
    - `#0 value: Float = 0.0`
    """
    params_all = []
    inputs_all = []
    return "ShaderNodeValue", params_all, inputs_all


def FunctionNodeInputVector(vector=(0.0, 0.0, 0.0)):
    """
    #### Outputs:
    - `#0 vector: Vector = (0.0, 0.0, 0.0)`
    """
    params_all = [('vector', vector, (0.0, 0.0, 0.0))]
    inputs_all = []
    return "FunctionNodeInputVector", params_all, inputs_all


def GeometryNodeCollectionInfo(transform_space='ORIGINAL', collection=None, separate_children=False, reset_children=False):
    """
    - `transform_space`: `ORIGINAL`, `RELATIVE`
    #### Inputs:
    - `#0 collection: Collection = None`
    - `#1 separate_children: Boolean = False`
    - `#2 reset_children: Boolean = False`
    #### Outputs:
    - `#0 instances: Geometry = None`
    """
    params_all = [('transform_space', transform_space, 'ORIGINAL')]
    inputs_all = [(collection, None), (separate_children, False), (reset_children, False)]
    return "GeometryNodeCollectionInfo", params_all, inputs_all


def GeometryNodeImageInfo(image=None, frame=0):
    """
    #### Inputs:
    - `#0 image: Image = None`
    - `#1 frame: Integer = 0`
    #### Outputs:
    - `#0 width: Integer = 0`
    - `#1 height: Integer = 0`
    - `#2 has_alpha: Boolean = False`
    - `#3 frame_count: Integer = 0`
    - `#4 fps: Float = 0.0`
    """
    params_all = []
    inputs_all = [(image, None), (frame, 0)]
    return "GeometryNodeImageInfo", params_all, inputs_all


def GeometryNodeIsViewport():
    """
    #### Outputs:
    - `#0 is_viewport: Boolean = False`
    """
    params_all = []
    inputs_all = []
    return "GeometryNodeIsViewport", params_all, inputs_all


def GeometryNodeObjectInfo(transform_space='ORIGINAL', object=None, as_instance=False):
    """
    - `transform_space`: `ORIGINAL`, `RELATIVE`
    #### Inputs:
    - `#0 object: Object = None`
    - `#1 as_instance: Boolean = False`
    #### Outputs:
    - `#0 location: Vector = (0.0, 0.0, 0.0)`
    - `#1 rotation: Vector = (0.0, 0.0, 0.0)`
    - `#2 scale: Vector = (0.0, 0.0, 0.0)`
    - `#3 geometry: Geometry = None`
    """
    params_all = [('transform_space', transform_space, 'ORIGINAL')]
    inputs_all = [(object, None), (as_instance, False)]
    return "GeometryNodeObjectInfo", params_all, inputs_all


def GeometryNodeSelfObject():
    """
    #### Outputs:
    - `#0 self_object: Object = None`
    """
    params_all = []
    inputs_all = []
    return "GeometryNodeSelfObject", params_all, inputs_all


def GeometryNodeViewer(data_type='FLOAT', domain='AUTO', geometry=None, value=0.0, value_001=(0.0, 0.0, 0.0), value_002=(0.0, 0.0, 0.0, 0.0), value_003=0, value_004=False):
    """
    - `data_type`: `FLOAT`, `INT`, `FLOAT_VECTOR`, `FLOAT_COLOR`, `BOOLEAN`
    - `domain`: `AUTO`, `POINT`, `EDGE`, `FACE`, `CORNER`, `CURVE`, `INSTANCE`
    #### Inputs:
    - `#0 geometry: Geometry = None`
    - `#1 value: Float = 0.0`
    - `#2 value_001: Vector = (0.0, 0.0, 0.0)`
    - `#3 value_002: Color = (0.0, 0.0, 0.0, 0.0)`
    - `#4 value_003: Integer = 0`
    - `#5 value_004: Boolean = False`
    """
    params_all = [('data_type', data_type, 'FLOAT'), ('domain', domain, 'AUTO')]
    inputs_all = [(geometry, None), (value, 0.0), (value_001, (0.0, 0.0, 0.0)), (value_002, (0.0, 0.0, 0.0, 0.0)), (value_003, 0), (value_004, False)]
    return "GeometryNodeViewer", params_all, inputs_all


def GeometryNodeInputID():
    """
    #### Outputs:
    - `#0 id: Integer = 0`
    """
    params_all = []
    inputs_all = []
    return "GeometryNodeInputID", params_all, inputs_all


def GeometryNodeInputIndex():
    """
    #### Outputs:
    - `#0 index: Integer = 0`
    """
    params_all = []
    inputs_all = []
    return "GeometryNodeInputIndex", params_all, inputs_all


def GeometryNodeInputNamedAttribute(data_type='FLOAT', name=''):
    """
    - `data_type`: `FLOAT`, `INT`, `FLOAT_VECTOR`, `FLOAT_COLOR`, `BOOLEAN`
    #### Inputs:
    - `#0 name: String = ''`
    #### Outputs:
    - `#0 attribute_vector: Vector = (0.0, 0.0, 0.0)`
    - `#1 attribute_float: Float = 0.0`
    - `#2 attribute_color: Color = (0.0, 0.0, 0.0, 0.0)`
    - `#3 attribute_bool: Boolean = False`
    - `#4 attribute_int: Integer = 0`
    - `#5 exists: Boolean = False`
    """
    params_all = [('data_type', data_type, 'FLOAT')]
    inputs_all = [(name, '')]
    return "GeometryNodeInputNamedAttribute", params_all, inputs_all


def GeometryNodeInputNormal():
    """
    #### Outputs:
    - `#0 normal: Vector = (0.0, 0.0, 0.0)`
    """
    params_all = []
    inputs_all = []
    return "GeometryNodeInputNormal", params_all, inputs_all


def GeometryNodeInputPosition():
    """
    #### Outputs:
    - `#0 position: Vector = (0.0, 0.0, 0.0)`
    """
    params_all = []
    inputs_all = []
    return "GeometryNodeInputPosition", params_all, inputs_all


def GeometryNodeInputRadius():
    """
    #### Outputs:
    - `#0 radius: Float = 1.0`
    """
    params_all = []
    inputs_all = []
    return "GeometryNodeInputRadius", params_all, inputs_all


def GeometryNodeSetID(geometry=None, selection=True, id=None):
    """
    #### Inputs:
    - `#0 geometry: Geometry = None`
    - `#1 selection: Boolean = True`
    - `#2 id: Integer = 0`
    #### Outputs:
    - `#0 geometry: Geometry = None`
    """
    params_all = []
    inputs_all = [(geometry, None), (selection, True), (id, None)]
    return "GeometryNodeSetID", params_all, inputs_all


def GeometryNodeSetPosition(geometry=None, selection=True, position=None, offset=(0.0, 0.0, 0.0)):
    """
    #### Inputs:
    - `#0 geometry: Geometry = None`
    - `#1 selection: Boolean = True`
    - `#2 position: Vector = (0.0, 0.0, 0.0)`
    - `#3 offset: Vector = (0.0, 0.0, 0.0)`
    #### Outputs:
    - `#0 geometry: Geometry = None`
    """
    params_all = []
    inputs_all = [(geometry, None), (selection, True), (position, None), (offset, (0.0, 0.0, 0.0))]
    return "GeometryNodeSetPosition", params_all, inputs_all


def GeometryNodeProximity(target_element='FACES', target=None, source_position=None):
    """
    - `target_element`: `FACES`, `POINTS`, `EDGES`
    #### Inputs:
    - `#0 target: Geometry = None`
    - `#1 source_position: Vector = (0.0, 0.0, 0.0)`
    #### Outputs:
    - `#0 position: Vector = (0.0, 0.0, 0.0)`
    - `#1 distance: Float = 0.0`
    """
    params_all = [('target_element', target_element, 'FACES')]
    inputs_all = [(target, None), (source_position, None)]
    return "GeometryNodeProximity", params_all, inputs_all


def GeometryNodeRaycast(data_type='FLOAT', mapping='INTERPOLATED', target_geometry=None, attribute=(0.0, 0.0, 0.0), attribute_001=0.0, attribute_002=(0.0, 0.0, 0.0, 0.0), attribute_003=False, attribute_004=0, source_position=None, ray_direction=(0.0, 0.0, -1.0), ray_length=100.0):
    """
    - `data_type`: `FLOAT`, `INT`, `FLOAT_VECTOR`, `FLOAT_COLOR`, `BOOLEAN`
    - `mapping`: `INTERPOLATED`, `NEAREST`
    #### Inputs:
    - `#0 target_geometry: Geometry = None`
    - `#1 attribute: Vector = (0.0, 0.0, 0.0)`
    - `#2 attribute_001: Float = 0.0`
    - `#3 attribute_002: Color = (0.0, 0.0, 0.0, 0.0)`
    - `#4 attribute_003: Boolean = False`
    - `#5 attribute_004: Integer = 0`
    - `#6 source_position: Vector = (0.0, 0.0, 0.0)`
    - `#7 ray_direction: Vector = (0.0, 0.0, -1.0)`
    - `#8 ray_length: Float = 100.0`
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
    """
    params_all = [('data_type', data_type, 'FLOAT'), ('mapping', mapping, 'INTERPOLATED')]
    inputs_all = [(target_geometry, None), (attribute, (0.0, 0.0, 0.0)), (attribute_001, 0.0), (attribute_002, (0.0, 0.0, 0.0, 0.0)), (attribute_003, False), (attribute_004, 0), (source_position, None), (ray_direction, (0.0, 0.0, -1.0)), (ray_length, 100.0)]
    return "GeometryNodeRaycast", params_all, inputs_all


def GeometryNodeSampleIndex(data_type='FLOAT', domain='POINT', clamp=False, geometry=None, value_float=0.0, value_int=0, value_vector=(0.0, 0.0, 0.0), value_color=(0.0, 0.0, 0.0, 0.0), value_bool=False, index=0):
    """
    - `data_type`: `FLOAT`, `INT`, `FLOAT_VECTOR`, `FLOAT_COLOR`, `BOOLEAN`
    - `domain`: `POINT`, `EDGE`, `FACE`, `CORNER`, `CURVE`, `INSTANCE`
    #### Inputs:
    - `#0 geometry: Geometry = None`
    - `#1 value_float: Float = 0.0`
    - `#2 value_int: Integer = 0`
    - `#3 value_vector: Vector = (0.0, 0.0, 0.0)`
    - `#4 value_color: Color = (0.0, 0.0, 0.0, 0.0)`
    - `#5 value_bool: Boolean = False`
    - `#6 index: Integer = 0`
    #### Outputs:
    - `#0 value_float: Float = 0.0`
    - `#1 value_int: Integer = 0`
    - `#2 value_vector: Vector = (0.0, 0.0, 0.0)`
    - `#3 value_color: Color = (0.0, 0.0, 0.0, 0.0)`
    - `#4 value_bool: Boolean = False`
    """
    params_all = [('data_type', data_type, 'FLOAT'), ('domain', domain, 'POINT'), ('clamp', clamp, False)]
    inputs_all = [(geometry, None), (value_float, 0.0), (value_int, 0), (value_vector, (0.0, 0.0, 0.0)), (value_color, (0.0, 0.0, 0.0, 0.0)), (value_bool, False), (index, 0)]
    return "GeometryNodeSampleIndex", params_all, inputs_all


def GeometryNodeSampleNearest(domain='POINT', geometry=None, sample_position=None):
    """
    - `domain`: `POINT`, `EDGE`, `FACE`, `CORNER`
    #### Inputs:
    - `#0 geometry: Geometry = None`
    - `#1 sample_position: Vector = (0.0, 0.0, 0.0)`
    #### Outputs:
    - `#0 index: Integer = 0`
    """
    params_all = [('domain', domain, 'POINT')]
    inputs_all = [(geometry, None), (sample_position, None)]
    return "GeometryNodeSampleNearest", params_all, inputs_all


def GeometryNodeBoundBox(geometry=None):
    """
    #### Inputs:
    - `#0 geometry: Geometry = None`
    #### Outputs:
    - `#0 bounding_box: Geometry = None`
    - `#1 min: Vector = (0.0, 0.0, 0.0)`
    - `#2 max: Vector = (0.0, 0.0, 0.0)`
    """
    params_all = []
    inputs_all = [(geometry, None)]
    return "GeometryNodeBoundBox", params_all, inputs_all


def GeometryNodeConvexHull(geometry=None):
    """
    #### Inputs:
    - `#0 geometry: Geometry = None`
    #### Outputs:
    - `#0 convex_hull: Geometry = None`
    """
    params_all = []
    inputs_all = [(geometry, None)]
    return "GeometryNodeConvexHull", params_all, inputs_all


def GeometryNodeDeleteGeometry(domain='POINT', mode='ALL', geometry=None, selection=True):
    """
    - `domain`: `POINT`, `EDGE`, `FACE`, `CURVE`, `INSTANCE`
    - `mode`: `ALL`, `EDGE_FACE`, `ONLY_FACE`
    #### Inputs:
    - `#0 geometry: Geometry = None`
    - `#1 selection: Boolean = True`
    #### Outputs:
    - `#0 geometry: Geometry = None`
    """
    params_all = [('domain', domain, 'POINT'), ('mode', mode, 'ALL')]
    inputs_all = [(geometry, None), (selection, True)]
    return "GeometryNodeDeleteGeometry", params_all, inputs_all


def GeometryNodeDuplicateElements(domain='POINT', geometry=None, selection=True, amount=1):
    """
    - `domain`: `POINT`, `EDGE`, `FACE`, `SPLINE`, `INSTANCE`
    #### Inputs:
    - `#0 geometry: Geometry = None`
    - `#1 selection: Boolean = True`
    - `#2 amount: Integer = 1`
    #### Outputs:
    - `#0 geometry: Geometry = None`
    - `#1 duplicate_index: Integer = 0`
    """
    params_all = [('domain', domain, 'POINT')]
    inputs_all = [(geometry, None), (selection, True), (amount, 1)]
    return "GeometryNodeDuplicateElements", params_all, inputs_all


def GeometryNodeMergeByDistance(mode='ALL', geometry=None, selection=True, distance=0.001):
    """
    - `mode`: `ALL`, `CONNECTED`
    #### Inputs:
    - `#0 geometry: Geometry = None`
    - `#1 selection: Boolean = True`
    - `#2 distance: Float = 0.001`
    #### Outputs:
    - `#0 geometry: Geometry = None`
    """
    params_all = [('mode', mode, 'ALL')]
    inputs_all = [(geometry, None), (selection, True), (distance, 0.001)]
    return "GeometryNodeMergeByDistance", params_all, inputs_all


def GeometryNodeTransform(geometry=None, translation=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(1.0, 1.0, 1.0)):
    """
    #### Inputs:
    - `#0 geometry: Geometry = None`
    - `#1 translation: Vector = (0.0, 0.0, 0.0)`
    - `#2 rotation: Vector = (0.0, 0.0, 0.0)`
    - `#3 scale: Vector = (1.0, 1.0, 1.0)`
    #### Outputs:
    - `#0 geometry: Geometry = None`
    """
    params_all = []
    inputs_all = [(geometry, None), (translation, (0.0, 0.0, 0.0)), (rotation, (0.0, 0.0, 0.0)), (scale, (1.0, 1.0, 1.0))]
    return "GeometryNodeTransform", params_all, inputs_all


def GeometryNodeSeparateComponents(geometry=None):
    """
    #### Inputs:
    - `#0 geometry: Geometry = None`
    #### Outputs:
    - `#0 mesh: Geometry = None`
    - `#1 point_cloud: Geometry = None`
    - `#2 curve: Geometry = None`
    - `#3 volume: Geometry = None`
    - `#4 instances: Geometry = None`
    """
    params_all = []
    inputs_all = [(geometry, None)]
    return "GeometryNodeSeparateComponents", params_all, inputs_all


def GeometryNodeSeparateGeometry(domain='POINT', geometry=None, selection=True):
    """
    - `domain`: `POINT`, `EDGE`, `FACE`, `CURVE`, `INSTANCE`
    #### Inputs:
    - `#0 geometry: Geometry = None`
    - `#1 selection: Boolean = True`
    #### Outputs:
    - `#0 selection: Geometry = None`
    - `#1 inverted: Geometry = None`
    """
    params_all = [('domain', domain, 'POINT')]
    inputs_all = [(geometry, None), (selection, True)]
    return "GeometryNodeSeparateGeometry", params_all, inputs_all


def GeometryNodeJoinGeometry(geometry=None):
    """
    #### Inputs:
    - `#0 geometry: Geometry = None`
    #### Outputs:
    - `#0 geometry: Geometry = None`
    """
    params_all = []
    inputs_all = [(geometry, None)]
    return "GeometryNodeJoinGeometry", params_all, inputs_all


def GeometryNodeGeometryToInstance(geometry=None):
    """
    #### Inputs:
    - `#0 geometry: Geometry = None`
    #### Outputs:
    - `#0 instances: Geometry = None`
    """
    params_all = []
    inputs_all = [(geometry, None)]
    return "GeometryNodeGeometryToInstance", params_all, inputs_all


def GeometryNodeInputCurveHandlePositions(relative=False):
    """
    #### Inputs:
    - `#0 relative: Boolean = False`
    #### Outputs:
    - `#0 left: Vector = (0.0, 0.0, 0.0)`
    - `#1 right: Vector = (0.0, 0.0, 0.0)`
    """
    params_all = []
    inputs_all = [(relative, False)]
    return "GeometryNodeInputCurveHandlePositions", params_all, inputs_all


def GeometryNodeCurveLength(curve=None):
    """
    #### Inputs:
    - `#0 curve: Geometry = None`
    #### Outputs:
    - `#0 length: Float = 0.0`
    """
    params_all = []
    inputs_all = [(curve, None)]
    return "GeometryNodeCurveLength", params_all, inputs_all


def GeometryNodeInputTangent():
    """
    #### Outputs:
    - `#0 tangent: Vector = (0.0, 0.0, 0.0)`
    """
    params_all = []
    inputs_all = []
    return "GeometryNodeInputTangent", params_all, inputs_all


def GeometryNodeInputCurveTilt():
    """
    #### Outputs:
    - `#0 tilt: Float = 0.0`
    """
    params_all = []
    inputs_all = []
    return "GeometryNodeInputCurveTilt", params_all, inputs_all


def GeometryNodeCurveEndpointSelection(start_size=1, end_size=1):
    """
    #### Inputs:
    - `#0 start_size: Integer = 1`
    - `#1 end_size: Integer = 1`
    #### Outputs:
    - `#0 selection: Boolean = False`
    """
    params_all = []
    inputs_all = [(start_size, 1), (end_size, 1)]
    return "GeometryNodeCurveEndpointSelection", params_all, inputs_all


def GeometryNodeCurveHandleTypeSelection(handle_type='AUTO', mode={'RIGHT', 'LEFT'}):
    """
    - `handle_type`: `AUTO`, `FREE`, `VECTOR`, `ALIGN`
    #### Outputs:
    - `#0 selection: Boolean = False`
    """
    params_all = [('handle_type', handle_type, 'AUTO'), ('mode', mode, {'RIGHT', 'LEFT'})]
    inputs_all = []
    return "GeometryNodeCurveHandleTypeSelection", params_all, inputs_all


def GeometryNodeInputSplineCyclic():
    """
    #### Outputs:
    - `#0 cyclic: Boolean = False`
    """
    params_all = []
    inputs_all = []
    return "GeometryNodeInputSplineCyclic", params_all, inputs_all


def GeometryNodeSplineLength():
    """
    #### Outputs:
    - `#0 length: Float = 0.0`
    - `#1 point_count: Integer = 0`
    """
    params_all = []
    inputs_all = []
    return "GeometryNodeSplineLength", params_all, inputs_all


def GeometryNodeSplineParameter():
    """
    #### Outputs:
    - `#0 factor: Float = 0.0`
    - `#1 length: Float = 0.0`
    - `#2 index: Integer = 0`
    """
    params_all = []
    inputs_all = []
    return "GeometryNodeSplineParameter", params_all, inputs_all


def GeometryNodeInputSplineResolution():
    """
    #### Outputs:
    - `#0 resolution: Integer = 0`
    """
    params_all = []
    inputs_all = []
    return "GeometryNodeInputSplineResolution", params_all, inputs_all


def GeometryNodeSampleCurve(data_type='FLOAT', mode='FACTOR', use_all_curves=False, curves=None, value_float=0.0, value_int=0, value_vector=(0.0, 0.0, 0.0), value_color=(0.0, 0.0, 0.0, 0.0), value_bool=False, factor=0.0, length=0.0, curve_index=0):
    """
    - `data_type`: `FLOAT`, `INT`, `FLOAT_VECTOR`, `FLOAT_COLOR`, `BOOLEAN`
    - `mode`: `FACTOR`, `LENGTH`
    #### Inputs:
    - `#0 curves: Geometry = None`
    - `#1 value_float: Float = 0.0`
    - `#2 value_int: Integer = 0`
    - `#3 value_vector: Vector = (0.0, 0.0, 0.0)`
    - `#4 value_color: Color = (0.0, 0.0, 0.0, 0.0)`
    - `#5 value_bool: Boolean = False`
    - `#6 factor: Float = 0.0`
    - `#7 length: Float = 0.0`
    - `#8 curve_index: Integer = 0`
    #### Outputs:
    - `#0 value_float: Float = 0.0`
    - `#1 value_int: Integer = 0`
    - `#2 value_vector: Vector = (0.0, 0.0, 0.0)`
    - `#3 value_color: Color = (0.0, 0.0, 0.0, 0.0)`
    - `#4 value_bool: Boolean = False`
    - `#5 position: Vector = (0.0, 0.0, 0.0)`
    - `#6 tangent: Vector = (0.0, 0.0, 0.0)`
    - `#7 normal: Vector = (0.0, 0.0, 0.0)`
    """
    params_all = [('data_type', data_type, 'FLOAT'), ('mode', mode, 'FACTOR'), ('use_all_curves', use_all_curves, False)]
    inputs_all = [(curves, None), (value_float, 0.0), (value_int, 0), (value_vector, (0.0, 0.0, 0.0)), (value_color, (0.0, 0.0, 0.0, 0.0)), (value_bool, False), (factor, 0.0), (length, 0.0), (curve_index, 0)]
    return "GeometryNodeSampleCurve", params_all, inputs_all


def GeometryNodeSetCurveNormal(mode='MINIMUM_TWIST', curve=None, selection=True):
    """
    - `mode`: `MINIMUM_TWIST`, `Z_UP`
    #### Inputs:
    - `#0 curve: Geometry = None`
    - `#1 selection: Boolean = True`
    #### Outputs:
    - `#0 curve: Geometry = None`
    """
    params_all = [('mode', mode, 'MINIMUM_TWIST')]
    inputs_all = [(curve, None), (selection, True)]
    return "GeometryNodeSetCurveNormal", params_all, inputs_all


def GeometryNodeSetCurveRadius(curve=None, selection=True, radius=0.005):
    """
    #### Inputs:
    - `#0 curve: Geometry = None`
    - `#1 selection: Boolean = True`
    - `#2 radius: Float = 0.005`
    #### Outputs:
    - `#0 curve: Geometry = None`
    """
    params_all = []
    inputs_all = [(curve, None), (selection, True), (radius, 0.005)]
    return "GeometryNodeSetCurveRadius", params_all, inputs_all


def GeometryNodeSetCurveTilt(curve=None, selection=True, tilt=math.radians(0.0)):
    """
    #### Inputs:
    - `#0 curve: Geometry = None`
    - `#1 selection: Boolean = True`
    - `#2 tilt: Float = math.radians(0.0)`
    #### Outputs:
    - `#0 curve: Geometry = None`
    """
    params_all = []
    inputs_all = [(curve, None), (selection, True), (tilt, math.radians(0.0))]
    return "GeometryNodeSetCurveTilt", params_all, inputs_all


def GeometryNodeSetCurveHandlePositions(mode='LEFT', curve=None, selection=True, position=None, offset=(0.0, 0.0, 0.0)):
    """
    - `mode`: `LEFT`, `RIGHT`
    #### Inputs:
    - `#0 curve: Geometry = None`
    - `#1 selection: Boolean = True`
    - `#2 position: Vector = (0.0, 0.0, 0.0)`
    - `#3 offset: Vector = (0.0, 0.0, 0.0)`
    #### Outputs:
    - `#0 curve: Geometry = None`
    """
    params_all = [('mode', mode, 'LEFT')]
    inputs_all = [(curve, None), (selection, True), (position, None), (offset, (0.0, 0.0, 0.0))]
    return "GeometryNodeSetCurveHandlePositions", params_all, inputs_all


def GeometryNodeCurveSetHandles(handle_type='AUTO', mode={'RIGHT', 'LEFT'}, curve=None, selection=True):
    """
    - `handle_type`: `AUTO`, `FREE`, `VECTOR`, `ALIGN`
    #### Inputs:
    - `#0 curve: Geometry = None`
    - `#1 selection: Boolean = True`
    #### Outputs:
    - `#0 curve: Geometry = None`
    """
    params_all = [('handle_type', handle_type, 'AUTO'), ('mode', mode, {'RIGHT', 'LEFT'})]
    inputs_all = [(curve, None), (selection, True)]
    return "GeometryNodeCurveSetHandles", params_all, inputs_all


def GeometryNodeSetSplineCyclic(geometry=None, selection=True, cyclic=False):
    """
    #### Inputs:
    - `#0 geometry: Geometry = None`
    - `#1 selection: Boolean = True`
    - `#2 cyclic: Boolean = False`
    #### Outputs:
    - `#0 geometry: Geometry = None`
    """
    params_all = []
    inputs_all = [(geometry, None), (selection, True), (cyclic, False)]
    return "GeometryNodeSetSplineCyclic", params_all, inputs_all


def GeometryNodeSetSplineResolution(geometry=None, selection=True, resolution=12):
    """
    #### Inputs:
    - `#0 geometry: Geometry = None`
    - `#1 selection: Boolean = True`
    - `#2 resolution: Integer = 12`
    #### Outputs:
    - `#0 geometry: Geometry = None`
    """
    params_all = []
    inputs_all = [(geometry, None), (selection, True), (resolution, 12)]
    return "GeometryNodeSetSplineResolution", params_all, inputs_all


def GeometryNodeCurveSplineType(spline_type='POLY', curve=None, selection=True):
    """
    - `spline_type`: `POLY`, `CATMULL_ROM`, `BEZIER`, `NURBS`
    #### Inputs:
    - `#0 curve: Geometry = None`
    - `#1 selection: Boolean = True`
    #### Outputs:
    - `#0 curve: Geometry = None`
    """
    params_all = [('spline_type', spline_type, 'POLY')]
    inputs_all = [(curve, None), (selection, True)]
    return "GeometryNodeCurveSplineType", params_all, inputs_all


def GeometryNodeCurveToMesh(curve=None, profile_curve=None, fill_caps=False):
    """
    #### Inputs:
    - `#0 curve: Geometry = None`
    - `#1 profile_curve: Geometry = None`
    - `#2 fill_caps: Boolean = False`
    #### Outputs:
    - `#0 mesh: Geometry = None`
    """
    params_all = []
    inputs_all = [(curve, None), (profile_curve, None), (fill_caps, False)]
    return "GeometryNodeCurveToMesh", params_all, inputs_all


def GeometryNodeCurveToPoints(mode='COUNT', curve=None, count=10, length=0.1):
    """
    - `mode`: `COUNT`, `EVALUATED`, `LENGTH`
    #### Inputs:
    - `#0 curve: Geometry = None`
    - `#1 count: Integer = 10`
    - `#2 length: Float = 0.1`
    #### Outputs:
    - `#0 points: Geometry = None`
    - `#1 tangent: Vector = (0.0, 0.0, 0.0)`
    - `#2 normal: Vector = (0.0, 0.0, 0.0)`
    - `#3 rotation: Vector = (0.0, 0.0, 0.0)`
    """
    params_all = [('mode', mode, 'COUNT')]
    inputs_all = [(curve, None), (count, 10), (length, 0.1)]
    return "GeometryNodeCurveToPoints", params_all, inputs_all


def GeometryNodeDeformCurvesOnSurface(curves=None):
    """
    #### Inputs:
    - `#0 curves: Geometry = None`
    #### Outputs:
    - `#0 curves: Geometry = None`
    """
    params_all = []
    inputs_all = [(curves, None)]
    return "GeometryNodeDeformCurvesOnSurface", params_all, inputs_all


def GeometryNodeFillCurve(mode='TRIANGLES', curve=None):
    """
    - `mode`: `TRIANGLES`, `NGONS`
    #### Inputs:
    - `#0 curve: Geometry = None`
    #### Outputs:
    - `#0 mesh: Geometry = None`
    """
    params_all = [('mode', mode, 'TRIANGLES')]
    inputs_all = [(curve, None)]
    return "GeometryNodeFillCurve", params_all, inputs_all


def GeometryNodeFilletCurve(mode='BEZIER', curve=None, count=1, radius=0.25, limit_radius=False):
    """
    - `mode`: `BEZIER`, `POLY`
    #### Inputs:
    - `#0 curve: Geometry = None`
    - `#1 count: Integer = 1`
    - `#2 radius: Float = 0.25`
    - `#3 limit_radius: Boolean = False`
    #### Outputs:
    - `#0 curve: Geometry = None`
    """
    params_all = [('mode', mode, 'BEZIER')]
    inputs_all = [(curve, None), (count, 1), (radius, 0.25), (limit_radius, False)]
    return "GeometryNodeFilletCurve", params_all, inputs_all


def GeometryNodeInterpolateCurves(guide_curves=None, guide_up=(0.0, 0.0, 0.0), guide_group_id=0, points=None, point_up=(0.0, 0.0, 0.0), point_group_id=0, max_neighbors=4):
    """
    #### Inputs:
    - `#0 guide_curves: Geometry = None`
    - `#1 guide_up: Vector = (0.0, 0.0, 0.0)`
    - `#2 guide_group_id: Integer = 0`
    - `#3 points: Geometry = None`
    - `#4 point_up: Vector = (0.0, 0.0, 0.0)`
    - `#5 point_group_id: Integer = 0`
    - `#6 max_neighbors: Integer = 4`
    #### Outputs:
    - `#0 curves: Geometry = None`
    - `#1 closest_index: Integer = 0`
    - `#2 closest_weight: Float = 0.0`
    """
    params_all = []
    inputs_all = [(guide_curves, None), (guide_up, (0.0, 0.0, 0.0)), (guide_group_id, 0), (points, None), (point_up, (0.0, 0.0, 0.0)), (point_group_id, 0), (max_neighbors, 4)]
    return "GeometryNodeInterpolateCurves", params_all, inputs_all


def GeometryNodeResampleCurve(mode='COUNT', curve=None, selection=True, count=10, length=0.1):
    """
    - `mode`: `COUNT`, `EVALUATED`, `LENGTH`
    #### Inputs:
    - `#0 curve: Geometry = None`
    - `#1 selection: Boolean = True`
    - `#2 count: Integer = 10`
    - `#3 length: Float = 0.1`
    #### Outputs:
    - `#0 curve: Geometry = None`
    """
    params_all = [('mode', mode, 'COUNT')]
    inputs_all = [(curve, None), (selection, True), (count, 10), (length, 0.1)]
    return "GeometryNodeResampleCurve", params_all, inputs_all


def GeometryNodeReverseCurve(curve=None, selection=True):
    """
    #### Inputs:
    - `#0 curve: Geometry = None`
    - `#1 selection: Boolean = True`
    #### Outputs:
    - `#0 curve: Geometry = None`
    """
    params_all = []
    inputs_all = [(curve, None), (selection, True)]
    return "GeometryNodeReverseCurve", params_all, inputs_all


def GeometryNodeSubdivideCurve(curve=None, cuts=1):
    """
    #### Inputs:
    - `#0 curve: Geometry = None`
    - `#1 cuts: Integer = 1`
    #### Outputs:
    - `#0 curve: Geometry = None`
    """
    params_all = []
    inputs_all = [(curve, None), (cuts, 1)]
    return "GeometryNodeSubdivideCurve", params_all, inputs_all


def GeometryNodeTrimCurve(mode='FACTOR', curve=None, selection=True, start=0.0, end=1.0, start_001=0.0, end_001=1.0):
    """
    - `mode`: `FACTOR`, `LENGTH`
    #### Inputs:
    - `#0 curve: Geometry = None`
    - `#1 selection: Boolean = True`
    - `#2 start: Float = 0.0`
    - `#3 end: Float = 1.0`
    - `#4 start_001: Float = 0.0`
    - `#5 end_001: Float = 1.0`
    #### Outputs:
    - `#0 curve: Geometry = None`
    """
    params_all = [('mode', mode, 'FACTOR')]
    inputs_all = [(curve, None), (selection, True), (start, 0.0), (end, 1.0), (start_001, 0.0), (end_001, 1.0)]
    return "GeometryNodeTrimCurve", params_all, inputs_all


def GeometryNodeCurveArc(mode='RADIUS', resolution=16, start=(-1.0, 0.0, 0.0), middle=(0.0, 2.0, 0.0), end=(1.0, 0.0, 0.0), radius=1.0, start_angle=math.radians(0.0), sweep_angle=math.radians(315.0), offset_angle=math.radians(0.0), connect_center=False, invert_arc=False):
    """
    - `mode`: `RADIUS`, `POINTS`
    #### Inputs:
    - `#0 resolution: Integer = 16`
    - `#1 start: Vector = (-1.0, 0.0, 0.0)`
    - `#2 middle: Vector = (0.0, 2.0, 0.0)`
    - `#3 end: Vector = (1.0, 0.0, 0.0)`
    - `#4 radius: Float = 1.0`
    - `#5 start_angle: Float = math.radians(0.0)`
    - `#6 sweep_angle: Float = math.radians(315.0)`
    - `#7 offset_angle: Float = math.radians(0.0)`
    - `#8 connect_center: Boolean = False`
    - `#9 invert_arc: Boolean = False`
    #### Outputs:
    - `#0 curve: Geometry = None`
    - `#1 center: Vector = (0.0, 0.0, 0.0)`
    - `#2 normal: Vector = (0.0, 0.0, 0.0)`
    - `#3 radius: Float = 0.0`
    """
    params_all = [('mode', mode, 'RADIUS')]
    inputs_all = [(resolution, 16), (start, (-1.0, 0.0, 0.0)), (middle, (0.0, 2.0, 0.0)), (end, (1.0, 0.0, 0.0)), (radius, 1.0), (start_angle, math.radians(0.0)), (sweep_angle, math.radians(315.0)), (offset_angle, math.radians(0.0)), (connect_center, False), (invert_arc, False)]
    return "GeometryNodeCurveArc", params_all, inputs_all


def GeometryNodeCurvePrimitiveBezierSegment(mode='POSITION', resolution=16, start=(-1.0, 0.0, 0.0), start_handle=(-0.5, 0.5, 0.0), end_handle=(0.0, 0.0, 0.0), end=(1.0, 0.0, 0.0)):
    """
    - `mode`: `POSITION`, `OFFSET`
    #### Inputs:
    - `#0 resolution: Integer = 16`
    - `#1 start: Vector = (-1.0, 0.0, 0.0)`
    - `#2 start_handle: Vector = (-0.5, 0.5, 0.0)`
    - `#3 end_handle: Vector = (0.0, 0.0, 0.0)`
    - `#4 end: Vector = (1.0, 0.0, 0.0)`
    #### Outputs:
    - `#0 curve: Geometry = None`
    """
    params_all = [('mode', mode, 'POSITION')]
    inputs_all = [(resolution, 16), (start, (-1.0, 0.0, 0.0)), (start_handle, (-0.5, 0.5, 0.0)), (end_handle, (0.0, 0.0, 0.0)), (end, (1.0, 0.0, 0.0))]
    return "GeometryNodeCurvePrimitiveBezierSegment", params_all, inputs_all


def GeometryNodeCurvePrimitiveCircle(mode='RADIUS', resolution=32, point_1=(-1.0, 0.0, 0.0), point_2=(0.0, 1.0, 0.0), point_3=(1.0, 0.0, 0.0), radius=1.0):
    """
    - `mode`: `RADIUS`, `POINTS`
    #### Inputs:
    - `#0 resolution: Integer = 32`
    - `#1 point_1: Vector = (-1.0, 0.0, 0.0)`
    - `#2 point_2: Vector = (0.0, 1.0, 0.0)`
    - `#3 point_3: Vector = (1.0, 0.0, 0.0)`
    - `#4 radius: Float = 1.0`
    #### Outputs:
    - `#0 curve: Geometry = None`
    - `#1 center: Vector = (0.0, 0.0, 0.0)`
    """
    params_all = [('mode', mode, 'RADIUS')]
    inputs_all = [(resolution, 32), (point_1, (-1.0, 0.0, 0.0)), (point_2, (0.0, 1.0, 0.0)), (point_3, (1.0, 0.0, 0.0)), (radius, 1.0)]
    return "GeometryNodeCurvePrimitiveCircle", params_all, inputs_all


def GeometryNodeCurvePrimitiveLine(mode='POINTS', start=(0.0, 0.0, 0.0), end=(0.0, 0.0, 1.0), direction=(0.0, 0.0, 1.0), length=1.0):
    """
    - `mode`: `POINTS`, `DIRECTION`
    #### Inputs:
    - `#0 start: Vector = (0.0, 0.0, 0.0)`
    - `#1 end: Vector = (0.0, 0.0, 1.0)`
    - `#2 direction: Vector = (0.0, 0.0, 1.0)`
    - `#3 length: Float = 1.0`
    #### Outputs:
    - `#0 curve: Geometry = None`
    """
    params_all = [('mode', mode, 'POINTS')]
    inputs_all = [(start, (0.0, 0.0, 0.0)), (end, (0.0, 0.0, 1.0)), (direction, (0.0, 0.0, 1.0)), (length, 1.0)]
    return "GeometryNodeCurvePrimitiveLine", params_all, inputs_all


def GeometryNodeCurveSpiral(resolution=32, rotations=2.0, start_radius=1.0, end_radius=2.0, height=2.0, reverse=False):
    """
    #### Inputs:
    - `#0 resolution: Integer = 32`
    - `#1 rotations: Float = 2.0`
    - `#2 start_radius: Float = 1.0`
    - `#3 end_radius: Float = 2.0`
    - `#4 height: Float = 2.0`
    - `#5 reverse: Boolean = False`
    #### Outputs:
    - `#0 curve: Geometry = None`
    """
    params_all = []
    inputs_all = [(resolution, 32), (rotations, 2.0), (start_radius, 1.0), (end_radius, 2.0), (height, 2.0), (reverse, False)]
    return "GeometryNodeCurveSpiral", params_all, inputs_all


def GeometryNodeCurveQuadraticBezier(resolution=16, start=(-1.0, 0.0, 0.0), middle=(0.0, 2.0, 0.0), end=(1.0, 0.0, 0.0)):
    """
    #### Inputs:
    - `#0 resolution: Integer = 16`
    - `#1 start: Vector = (-1.0, 0.0, 0.0)`
    - `#2 middle: Vector = (0.0, 2.0, 0.0)`
    - `#3 end: Vector = (1.0, 0.0, 0.0)`
    #### Outputs:
    - `#0 curve: Geometry = None`
    """
    params_all = []
    inputs_all = [(resolution, 16), (start, (-1.0, 0.0, 0.0)), (middle, (0.0, 2.0, 0.0)), (end, (1.0, 0.0, 0.0))]
    return "GeometryNodeCurveQuadraticBezier", params_all, inputs_all


def GeometryNodeCurvePrimitiveQuadrilateral(mode='RECTANGLE', width=2.0, height=2.0, bottom_width=4.0, top_width=2.0, offset=1.0, bottom_height=3.0, top_height=1.0, point_1=(-1.0, -1.0, 0.0), point_2=(1.0, -1.0, 0.0), point_3=(1.0, 1.0, 0.0), point_4=(-1.0, 1.0, 0.0)):
    """
    - `mode`: `RECTANGLE`, `PARALLELOGRAM`, `TRAPEZOID`, `KITE`, `POINTS`
    #### Inputs:
    - `#0 width: Float = 2.0`
    - `#1 height: Float = 2.0`
    - `#2 bottom_width: Float = 4.0`
    - `#3 top_width: Float = 2.0`
    - `#4 offset: Float = 1.0`
    - `#5 bottom_height: Float = 3.0`
    - `#6 top_height: Float = 1.0`
    - `#7 point_1: Vector = (-1.0, -1.0, 0.0)`
    - `#8 point_2: Vector = (1.0, -1.0, 0.0)`
    - `#9 point_3: Vector = (1.0, 1.0, 0.0)`
    - `#10 point_4: Vector = (-1.0, 1.0, 0.0)`
    #### Outputs:
    - `#0 curve: Geometry = None`
    """
    params_all = [('mode', mode, 'RECTANGLE')]
    inputs_all = [(width, 2.0), (height, 2.0), (bottom_width, 4.0), (top_width, 2.0), (offset, 1.0), (bottom_height, 3.0), (top_height, 1.0), (point_1, (-1.0, -1.0, 0.0)), (point_2, (1.0, -1.0, 0.0)), (point_3, (1.0, 1.0, 0.0)), (point_4, (-1.0, 1.0, 0.0))]
    return "GeometryNodeCurvePrimitiveQuadrilateral", params_all, inputs_all


def GeometryNodeCurveStar(points=8, inner_radius=1.0, outer_radius=2.0, twist=math.radians(0.0)):
    """
    #### Inputs:
    - `#0 points: Integer = 8`
    - `#1 inner_radius: Float = 1.0`
    - `#2 outer_radius: Float = 2.0`
    - `#3 twist: Float = math.radians(0.0)`
    #### Outputs:
    - `#0 curve: Geometry = None`
    - `#1 outer_points: Boolean = False`
    """
    params_all = []
    inputs_all = [(points, 8), (inner_radius, 1.0), (outer_radius, 2.0), (twist, math.radians(0.0))]
    return "GeometryNodeCurveStar", params_all, inputs_all


def GeometryNodeCurveOfPoint(point_index=None):
    """
    #### Inputs:
    - `#0 point_index: Integer = 0`
    #### Outputs:
    - `#0 curve_index: Integer = 0`
    - `#1 index_in_curve: Integer = 0`
    """
    params_all = []
    inputs_all = [(point_index, None)]
    return "GeometryNodeCurveOfPoint", params_all, inputs_all


def GeometryNodeOffsetPointInCurve(point_index=None, offset=0):
    """
    #### Inputs:
    - `#0 point_index: Integer = 0`
    - `#1 offset: Integer = 0`
    #### Outputs:
    - `#0 is_valid_offset: Boolean = False`
    - `#1 point_index: Integer = 0`
    """
    params_all = []
    inputs_all = [(point_index, None), (offset, 0)]
    return "GeometryNodeOffsetPointInCurve", params_all, inputs_all


def GeometryNodePointsOfCurve(curve_index=None, weights=0.0, sort_index=0):
    """
    #### Inputs:
    - `#0 curve_index: Integer = 0`
    - `#1 weights: Float = 0.0`
    - `#2 sort_index: Integer = 0`
    #### Outputs:
    - `#0 point_index: Integer = 0`
    - `#1 total: Integer = 0`
    """
    params_all = []
    inputs_all = [(curve_index, None), (weights, 0.0), (sort_index, 0)]
    return "GeometryNodePointsOfCurve", params_all, inputs_all


def GeometryNodeInstanceOnPoints(points=None, selection=True, instance=None, pick_instance=False, instance_index=None, rotation=(0.0, 0.0, 0.0), scale=(1.0, 1.0, 1.0)):
    """
    #### Inputs:
    - `#0 points: Geometry = None`
    - `#1 selection: Boolean = True`
    - `#2 instance: Geometry = None`
    - `#3 pick_instance: Boolean = False`
    - `#4 instance_index: Integer = 0`
    - `#5 rotation: Vector = (0.0, 0.0, 0.0)`
    - `#6 scale: Vector = (1.0, 1.0, 1.0)`
    #### Outputs:
    - `#0 instances: Geometry = None`
    """
    params_all = []
    inputs_all = [(points, None), (selection, True), (instance, None), (pick_instance, False), (instance_index, None), (rotation, (0.0, 0.0, 0.0)), (scale, (1.0, 1.0, 1.0))]
    return "GeometryNodeInstanceOnPoints", params_all, inputs_all


def GeometryNodeInstancesToPoints(instances=None, selection=True, position=None, radius=0.05):
    """
    #### Inputs:
    - `#0 instances: Geometry = None`
    - `#1 selection: Boolean = True`
    - `#2 position: Vector = (0.0, 0.0, 0.0)`
    - `#3 radius: Float = 0.05`
    #### Outputs:
    - `#0 points: Geometry = None`
    """
    params_all = []
    inputs_all = [(instances, None), (selection, True), (position, None), (radius, 0.05)]
    return "GeometryNodeInstancesToPoints", params_all, inputs_all


def GeometryNodeRotateInstances(instances=None, selection=True, rotation=(0.0, 0.0, 0.0), pivot_point=(0.0, 0.0, 0.0), local_space=True):
    """
    #### Inputs:
    - `#0 instances: Geometry = None`
    - `#1 selection: Boolean = True`
    - `#2 rotation: Vector = (0.0, 0.0, 0.0)`
    - `#3 pivot_point: Vector = (0.0, 0.0, 0.0)`
    - `#4 local_space: Boolean = True`
    #### Outputs:
    - `#0 instances: Geometry = None`
    """
    params_all = []
    inputs_all = [(instances, None), (selection, True), (rotation, (0.0, 0.0, 0.0)), (pivot_point, (0.0, 0.0, 0.0)), (local_space, True)]
    return "GeometryNodeRotateInstances", params_all, inputs_all


def GeometryNodeScaleInstances(instances=None, selection=True, scale=(1.0, 1.0, 1.0), center=(0.0, 0.0, 0.0), local_space=True):
    """
    #### Inputs:
    - `#0 instances: Geometry = None`
    - `#1 selection: Boolean = True`
    - `#2 scale: Vector = (1.0, 1.0, 1.0)`
    - `#3 center: Vector = (0.0, 0.0, 0.0)`
    - `#4 local_space: Boolean = True`
    #### Outputs:
    - `#0 instances: Geometry = None`
    """
    params_all = []
    inputs_all = [(instances, None), (selection, True), (scale, (1.0, 1.0, 1.0)), (center, (0.0, 0.0, 0.0)), (local_space, True)]
    return "GeometryNodeScaleInstances", params_all, inputs_all


def GeometryNodeTranslateInstances(instances=None, selection=True, translation=(0.0, 0.0, 0.0), local_space=True):
    """
    #### Inputs:
    - `#0 instances: Geometry = None`
    - `#1 selection: Boolean = True`
    - `#2 translation: Vector = (0.0, 0.0, 0.0)`
    - `#3 local_space: Boolean = True`
    #### Outputs:
    - `#0 instances: Geometry = None`
    """
    params_all = []
    inputs_all = [(instances, None), (selection, True), (translation, (0.0, 0.0, 0.0)), (local_space, True)]
    return "GeometryNodeTranslateInstances", params_all, inputs_all


def GeometryNodeRealizeInstances(legacy_behavior=False, geometry=None):
    """
    #### Inputs:
    - `#0 geometry: Geometry = None`
    #### Outputs:
    - `#0 geometry: Geometry = None`
    """
    params_all = [('legacy_behavior', legacy_behavior, False)]
    inputs_all = [(geometry, None)]
    return "GeometryNodeRealizeInstances", params_all, inputs_all


def GeometryNodeInputInstanceRotation():
    """
    #### Outputs:
    - `#0 rotation: Vector = (0.0, 0.0, 0.0)`
    """
    params_all = []
    inputs_all = []
    return "GeometryNodeInputInstanceRotation", params_all, inputs_all


def GeometryNodeInputInstanceScale():
    """
    #### Outputs:
    - `#0 scale: Vector = (0.0, 0.0, 0.0)`
    """
    params_all = []
    inputs_all = []
    return "GeometryNodeInputInstanceScale", params_all, inputs_all


def GeometryNodeInputMeshEdgeAngle():
    """
    #### Outputs:
    - `#0 unsigned_angle: Float = 0.0`
    - `#1 signed_angle: Float = 0.0`
    """
    params_all = []
    inputs_all = []
    return "GeometryNodeInputMeshEdgeAngle", params_all, inputs_all


def GeometryNodeInputMeshEdgeNeighbors():
    """
    #### Outputs:
    - `#0 face_count: Integer = 0`
    """
    params_all = []
    inputs_all = []
    return "GeometryNodeInputMeshEdgeNeighbors", params_all, inputs_all


def GeometryNodeInputMeshEdgeVertices():
    """
    #### Outputs:
    - `#0 vertex_index_1: Integer = 0`
    - `#1 vertex_index_2: Integer = 0`
    - `#2 position_1: Vector = (0.0, 0.0, 0.0)`
    - `#3 position_2: Vector = (0.0, 0.0, 0.0)`
    """
    params_all = []
    inputs_all = []
    return "GeometryNodeInputMeshEdgeVertices", params_all, inputs_all


def GeometryNodeEdgesToFaceGroups(boundary_edges=True):
    """
    #### Inputs:
    - `#0 boundary_edges: Boolean = True`
    #### Outputs:
    - `#0 face_group_id: Integer = 0`
    """
    params_all = []
    inputs_all = [(boundary_edges, True)]
    return "GeometryNodeEdgesToFaceGroups", params_all, inputs_all


def GeometryNodeInputMeshFaceArea():
    """
    #### Outputs:
    - `#0 area: Float = 0.0`
    """
    params_all = []
    inputs_all = []
    return "GeometryNodeInputMeshFaceArea", params_all, inputs_all


def GeometryNodeInputMeshFaceNeighbors():
    """
    #### Outputs:
    - `#0 vertex_count: Integer = 0`
    - `#1 face_count: Integer = 0`
    """
    params_all = []
    inputs_all = []
    return "GeometryNodeInputMeshFaceNeighbors", params_all, inputs_all


def GeometryNodeMeshFaceSetBoundaries(face_set=0):
    """
    #### Inputs:
    - `#0 face_set: Integer = 0`
    #### Outputs:
    - `#0 boundary_edges: Boolean = False`
    """
    params_all = []
    inputs_all = [(face_set, 0)]
    return "GeometryNodeMeshFaceSetBoundaries", params_all, inputs_all


def GeometryNodeInputMeshFaceIsPlanar(threshold=0.01):
    """
    #### Inputs:
    - `#0 threshold: Float = 0.01`
    #### Outputs:
    - `#0 planar: Boolean = False`
    """
    params_all = []
    inputs_all = [(threshold, 0.01)]
    return "GeometryNodeInputMeshFaceIsPlanar", params_all, inputs_all


def GeometryNodeInputShadeSmooth():
    """
    #### Outputs:
    - `#0 smooth: Boolean = False`
    """
    params_all = []
    inputs_all = []
    return "GeometryNodeInputShadeSmooth", params_all, inputs_all


def GeometryNodeInputMeshIsland():
    """
    #### Outputs:
    - `#0 island_index: Integer = 0`
    - `#1 island_count: Integer = 0`
    """
    params_all = []
    inputs_all = []
    return "GeometryNodeInputMeshIsland", params_all, inputs_all


def GeometryNodeInputShortestEdgePaths(end_vertex=False, edge_cost=1.0):
    """
    #### Inputs:
    - `#0 end_vertex: Boolean = False`
    - `#1 edge_cost: Float = 1.0`
    #### Outputs:
    - `#0 next_vertex_index: Integer = 0`
    - `#1 total_cost: Float = 0.0`
    """
    params_all = []
    inputs_all = [(end_vertex, False), (edge_cost, 1.0)]
    return "GeometryNodeInputShortestEdgePaths", params_all, inputs_all


def GeometryNodeInputMeshVertexNeighbors():
    """
    #### Outputs:
    - `#0 vertex_count: Integer = 0`
    - `#1 face_count: Integer = 0`
    """
    params_all = []
    inputs_all = []
    return "GeometryNodeInputMeshVertexNeighbors", params_all, inputs_all


def GeometryNodeSampleNearestSurface(data_type='FLOAT', mesh=None, value_float=0.0, value_int=0, value_vector=(0.0, 0.0, 0.0), value_color=(0.0, 0.0, 0.0, 0.0), value_bool=False, sample_position=None):
    """
    - `data_type`: `FLOAT`, `INT`, `FLOAT_VECTOR`, `FLOAT_COLOR`, `BOOLEAN`
    #### Inputs:
    - `#0 mesh: Geometry = None`
    - `#1 value_float: Float = 0.0`
    - `#2 value_int: Integer = 0`
    - `#3 value_vector: Vector = (0.0, 0.0, 0.0)`
    - `#4 value_color: Color = (0.0, 0.0, 0.0, 0.0)`
    - `#5 value_bool: Boolean = False`
    - `#6 sample_position: Vector = (0.0, 0.0, 0.0)`
    #### Outputs:
    - `#0 value_float: Float = 0.0`
    - `#1 value_int: Integer = 0`
    - `#2 value_vector: Vector = (0.0, 0.0, 0.0)`
    - `#3 value_color: Color = (0.0, 0.0, 0.0, 0.0)`
    - `#4 value_bool: Boolean = False`
    """
    params_all = [('data_type', data_type, 'FLOAT')]
    inputs_all = [(mesh, None), (value_float, 0.0), (value_int, 0), (value_vector, (0.0, 0.0, 0.0)), (value_color, (0.0, 0.0, 0.0, 0.0)), (value_bool, False), (sample_position, None)]
    return "GeometryNodeSampleNearestSurface", params_all, inputs_all


def GeometryNodeSampleUVSurface(data_type='FLOAT', mesh=None, value_float=0.0, value_int=0, value_vector=(0.0, 0.0, 0.0), value_color=(0.0, 0.0, 0.0, 0.0), value_bool=False, source_uv_map=(0.0, 0.0, 0.0), sample_uv=(0.0, 0.0, 0.0)):
    """
    - `data_type`: `FLOAT`, `INT`, `FLOAT_VECTOR`, `FLOAT_COLOR`, `BOOLEAN`
    #### Inputs:
    - `#0 mesh: Geometry = None`
    - `#1 value_float: Float = 0.0`
    - `#2 value_int: Integer = 0`
    - `#3 value_vector: Vector = (0.0, 0.0, 0.0)`
    - `#4 value_color: Color = (0.0, 0.0, 0.0, 0.0)`
    - `#5 value_bool: Boolean = False`
    - `#6 source_uv_map: Vector = (0.0, 0.0, 0.0)`
    - `#7 sample_uv: Vector = (0.0, 0.0, 0.0)`
    #### Outputs:
    - `#0 value_float: Float = 0.0`
    - `#1 value_int: Integer = 0`
    - `#2 value_vector: Vector = (0.0, 0.0, 0.0)`
    - `#3 value_color: Color = (0.0, 0.0, 0.0, 0.0)`
    - `#4 value_bool: Boolean = False`
    - `#5 is_valid: Boolean = False`
    """
    params_all = [('data_type', data_type, 'FLOAT')]
    inputs_all = [(mesh, None), (value_float, 0.0), (value_int, 0), (value_vector, (0.0, 0.0, 0.0)), (value_color, (0.0, 0.0, 0.0, 0.0)), (value_bool, False), (source_uv_map, (0.0, 0.0, 0.0)), (sample_uv, (0.0, 0.0, 0.0))]
    return "GeometryNodeSampleUVSurface", params_all, inputs_all


def GeometryNodeSetShadeSmooth(geometry=None, selection=True, shade_smooth=True):
    """
    #### Inputs:
    - `#0 geometry: Geometry = None`
    - `#1 selection: Boolean = True`
    - `#2 shade_smooth: Boolean = True`
    #### Outputs:
    - `#0 geometry: Geometry = None`
    """
    params_all = []
    inputs_all = [(geometry, None), (selection, True), (shade_smooth, True)]
    return "GeometryNodeSetShadeSmooth", params_all, inputs_all


def GeometryNodeDualMesh(mesh=None, keep_boundaries=False):
    """
    #### Inputs:
    - `#0 mesh: Geometry = None`
    - `#1 keep_boundaries: Boolean = False`
    #### Outputs:
    - `#0 dual_mesh: Geometry = None`
    """
    params_all = []
    inputs_all = [(mesh, None), (keep_boundaries, False)]
    return "GeometryNodeDualMesh", params_all, inputs_all


def GeometryNodeEdgePathsToCurves(mesh=None, start_vertices=True, next_vertex_index=-1):
    """
    #### Inputs:
    - `#0 mesh: Geometry = None`
    - `#1 start_vertices: Boolean = True`
    - `#2 next_vertex_index: Integer = -1`
    #### Outputs:
    - `#0 curves: Geometry = None`
    """
    params_all = []
    inputs_all = [(mesh, None), (start_vertices, True), (next_vertex_index, -1)]
    return "GeometryNodeEdgePathsToCurves", params_all, inputs_all


def GeometryNodeEdgePathsToSelection(start_vertices=True, next_vertex_index=-1):
    """
    #### Inputs:
    - `#0 start_vertices: Boolean = True`
    - `#1 next_vertex_index: Integer = -1`
    #### Outputs:
    - `#0 selection: Boolean = False`
    """
    params_all = []
    inputs_all = [(start_vertices, True), (next_vertex_index, -1)]
    return "GeometryNodeEdgePathsToSelection", params_all, inputs_all


def GeometryNodeExtrudeMesh(mode='FACES', mesh=None, selection=True, offset=None, offset_scale=1.0, individual=True):
    """
    - `mode`: `FACES`, `VERTICES`, `EDGES`
    #### Inputs:
    - `#0 mesh: Geometry = None`
    - `#1 selection: Boolean = True`
    - `#2 offset: Vector = (0.0, 0.0, 0.0)`
    - `#3 offset_scale: Float = 1.0`
    - `#4 individual: Boolean = True`
    #### Outputs:
    - `#0 mesh: Geometry = None`
    - `#1 top: Boolean = False`
    - `#2 side: Boolean = False`
    """
    params_all = [('mode', mode, 'FACES')]
    inputs_all = [(mesh, None), (selection, True), (offset, None), (offset_scale, 1.0), (individual, True)]
    return "GeometryNodeExtrudeMesh", params_all, inputs_all


def GeometryNodeFlipFaces(mesh=None, selection=True):
    """
    #### Inputs:
    - `#0 mesh: Geometry = None`
    - `#1 selection: Boolean = True`
    #### Outputs:
    - `#0 mesh: Geometry = None`
    """
    params_all = []
    inputs_all = [(mesh, None), (selection, True)]
    return "GeometryNodeFlipFaces", params_all, inputs_all


def GeometryNodeMeshBoolean(operation='DIFFERENCE', mesh_1=None, mesh_2=None, self_intersection=False, hole_tolerant=False):
    """
    - `operation`: `DIFFERENCE`, `INTERSECT`, `UNION`
    #### Inputs:
    - `#0 mesh_1: Geometry = None`
    - `#1 mesh_2: Geometry = None`
    - `#2 self_intersection: Boolean = False`
    - `#3 hole_tolerant: Boolean = False`
    #### Outputs:
    - `#0 mesh: Geometry = None`
    - `#1 intersecting_edges: Boolean = False`
    """
    params_all = [('operation', operation, 'DIFFERENCE')]
    inputs_all = [(mesh_1, None), (mesh_2, None), (self_intersection, False), (hole_tolerant, False)]
    return "GeometryNodeMeshBoolean", params_all, inputs_all


def GeometryNodeMeshToCurve(mesh=None, selection=True):
    """
    #### Inputs:
    - `#0 mesh: Geometry = None`
    - `#1 selection: Boolean = True`
    #### Outputs:
    - `#0 curve: Geometry = None`
    """
    params_all = []
    inputs_all = [(mesh, None), (selection, True)]
    return "GeometryNodeMeshToCurve", params_all, inputs_all


def GeometryNodeMeshToPoints(mode='VERTICES', mesh=None, selection=True, position=None, radius=0.05):
    """
    - `mode`: `VERTICES`, `EDGES`, `FACES`, `CORNERS`
    #### Inputs:
    - `#0 mesh: Geometry = None`
    - `#1 selection: Boolean = True`
    - `#2 position: Vector = (0.0, 0.0, 0.0)`
    - `#3 radius: Float = 0.05`
    #### Outputs:
    - `#0 points: Geometry = None`
    """
    params_all = [('mode', mode, 'VERTICES')]
    inputs_all = [(mesh, None), (selection, True), (position, None), (radius, 0.05)]
    return "GeometryNodeMeshToPoints", params_all, inputs_all


def GeometryNodeMeshToVolume(resolution_mode='VOXEL_AMOUNT', mesh=None, density=1.0, voxel_size=0.3, voxel_amount=64.0, exterior_band_width=0.1, interior_band_width=0.0, fill_volume=True):
    """
    - `resolution_mode`: `VOXEL_AMOUNT`, `VOXEL_SIZE`
    #### Inputs:
    - `#0 mesh: Geometry = None`
    - `#1 density: Float = 1.0`
    - `#2 voxel_size: Float = 0.3`
    - `#3 voxel_amount: Float = 64.0`
    - `#4 exterior_band_width: Float = 0.1`
    - `#5 interior_band_width: Float = 0.0`
    - `#6 fill_volume: Boolean = True`
    #### Outputs:
    - `#0 volume: Geometry = None`
    """
    params_all = [('resolution_mode', resolution_mode, 'VOXEL_AMOUNT')]
    inputs_all = [(mesh, None), (density, 1.0), (voxel_size, 0.3), (voxel_amount, 64.0), (exterior_band_width, 0.1), (interior_band_width, 0.0), (fill_volume, True)]
    return "GeometryNodeMeshToVolume", params_all, inputs_all


def GeometryNodeScaleElements(domain='FACE', scale_mode='UNIFORM', geometry=None, selection=True, scale=1.0, center=None, axis=(1.0, 0.0, 0.0)):
    """
    - `domain`: `FACE`, `EDGE`
    - `scale_mode`: `UNIFORM`, `SINGLE_AXIS`
    #### Inputs:
    - `#0 geometry: Geometry = None`
    - `#1 selection: Boolean = True`
    - `#2 scale: Float = 1.0`
    - `#3 center: Vector = (0.0, 0.0, 0.0)`
    - `#4 axis: Vector = (1.0, 0.0, 0.0)`
    #### Outputs:
    - `#0 geometry: Geometry = None`
    """
    params_all = [('domain', domain, 'FACE'), ('scale_mode', scale_mode, 'UNIFORM')]
    inputs_all = [(geometry, None), (selection, True), (scale, 1.0), (center, None), (axis, (1.0, 0.0, 0.0))]
    return "GeometryNodeScaleElements", params_all, inputs_all


def GeometryNodeSplitEdges(mesh=None, selection=True):
    """
    #### Inputs:
    - `#0 mesh: Geometry = None`
    - `#1 selection: Boolean = True`
    #### Outputs:
    - `#0 mesh: Geometry = None`
    """
    params_all = []
    inputs_all = [(mesh, None), (selection, True)]
    return "GeometryNodeSplitEdges", params_all, inputs_all


def GeometryNodeSubdivideMesh(mesh=None, level=1):
    """
    #### Inputs:
    - `#0 mesh: Geometry = None`
    - `#1 level: Integer = 1`
    #### Outputs:
    - `#0 mesh: Geometry = None`
    """
    params_all = []
    inputs_all = [(mesh, None), (level, 1)]
    return "GeometryNodeSubdivideMesh", params_all, inputs_all


def GeometryNodeSubdivisionSurface(boundary_smooth='ALL', uv_smooth='PRESERVE_BOUNDARIES', mesh=None, level=1, edge_crease=0.0, vertex_crease=0.0):
    """
    - `boundary_smooth`: `ALL`, `PRESERVE_CORNERS`
    - `uv_smooth`: `PRESERVE_BOUNDARIES`, `NONE`, `PRESERVE_CORNERS`, `PRESERVE_CORNERS_AND_JUNCTIONS`, `PRESERVE_CORNERS_JUNCTIONS_AND_CONCAVE`, `SMOOTH_ALL`
    #### Inputs:
    - `#0 mesh: Geometry = None`
    - `#1 level: Integer = 1`
    - `#2 edge_crease: Float = 0.0`
    - `#3 vertex_crease: Float = 0.0`
    #### Outputs:
    - `#0 mesh: Geometry = None`
    """
    params_all = [('boundary_smooth', boundary_smooth, 'ALL'), ('uv_smooth', uv_smooth, 'PRESERVE_BOUNDARIES')]
    inputs_all = [(mesh, None), (level, 1), (edge_crease, 0.0), (vertex_crease, 0.0)]
    return "GeometryNodeSubdivisionSurface", params_all, inputs_all


def GeometryNodeTriangulate(ngon_method='BEAUTY', quad_method='SHORTEST_DIAGONAL', mesh=None, selection=True, minimum_vertices=4):
    """
    - `ngon_method`: `BEAUTY`, `CLIP`
    - `quad_method`: `SHORTEST_DIAGONAL`, `BEAUTY`, `FIXED`, `FIXED_ALTERNATE`, `LONGEST_DIAGONAL`
    #### Inputs:
    - `#0 mesh: Geometry = None`
    - `#1 selection: Boolean = True`
    - `#2 minimum_vertices: Integer = 4`
    #### Outputs:
    - `#0 mesh: Geometry = None`
    """
    params_all = [('ngon_method', ngon_method, 'BEAUTY'), ('quad_method', quad_method, 'SHORTEST_DIAGONAL')]
    inputs_all = [(mesh, None), (selection, True), (minimum_vertices, 4)]
    return "GeometryNodeTriangulate", params_all, inputs_all


def GeometryNodeMeshCone(fill_type='NGON', vertices=32, side_segments=1, fill_segments=1, radius_top=0.0, radius_bottom=1.0, depth=2.0):
    """
    - `fill_type`: `NGON`, `NONE`, `TRIANGLE_FAN`
    #### Inputs:
    - `#0 vertices: Integer = 32`
    - `#1 side_segments: Integer = 1`
    - `#2 fill_segments: Integer = 1`
    - `#3 radius_top: Float = 0.0`
    - `#4 radius_bottom: Float = 1.0`
    - `#5 depth: Float = 2.0`
    #### Outputs:
    - `#0 mesh: Geometry = None`
    - `#1 top: Boolean = False`
    - `#2 bottom: Boolean = False`
    - `#3 side: Boolean = False`
    - `#4 uv_map: Vector = (0.0, 0.0, 0.0)`
    """
    params_all = [('fill_type', fill_type, 'NGON')]
    inputs_all = [(vertices, 32), (side_segments, 1), (fill_segments, 1), (radius_top, 0.0), (radius_bottom, 1.0), (depth, 2.0)]
    return "GeometryNodeMeshCone", params_all, inputs_all


def GeometryNodeMeshCube(size=(1.0, 1.0, 1.0), vertices_x=2, vertices_y=2, vertices_z=2):
    """
    #### Inputs:
    - `#0 size: Vector = (1.0, 1.0, 1.0)`
    - `#1 vertices_x: Integer = 2`
    - `#2 vertices_y: Integer = 2`
    - `#3 vertices_z: Integer = 2`
    #### Outputs:
    - `#0 mesh: Geometry = None`
    - `#1 uv_map: Vector = (0.0, 0.0, 0.0)`
    """
    params_all = []
    inputs_all = [(size, (1.0, 1.0, 1.0)), (vertices_x, 2), (vertices_y, 2), (vertices_z, 2)]
    return "GeometryNodeMeshCube", params_all, inputs_all


def GeometryNodeMeshCylinder(fill_type='NGON', vertices=32, side_segments=1, fill_segments=1, radius=1.0, depth=2.0):
    """
    - `fill_type`: `NGON`, `NONE`, `TRIANGLE_FAN`
    #### Inputs:
    - `#0 vertices: Integer = 32`
    - `#1 side_segments: Integer = 1`
    - `#2 fill_segments: Integer = 1`
    - `#3 radius: Float = 1.0`
    - `#4 depth: Float = 2.0`
    #### Outputs:
    - `#0 mesh: Geometry = None`
    - `#1 top: Boolean = False`
    - `#2 side: Boolean = False`
    - `#3 bottom: Boolean = False`
    - `#4 uv_map: Vector = (0.0, 0.0, 0.0)`
    """
    params_all = [('fill_type', fill_type, 'NGON')]
    inputs_all = [(vertices, 32), (side_segments, 1), (fill_segments, 1), (radius, 1.0), (depth, 2.0)]
    return "GeometryNodeMeshCylinder", params_all, inputs_all


def GeometryNodeMeshGrid(size_x=1.0, size_y=1.0, vertices_x=3, vertices_y=3):
    """
    #### Inputs:
    - `#0 size_x: Float = 1.0`
    - `#1 size_y: Float = 1.0`
    - `#2 vertices_x: Integer = 3`
    - `#3 vertices_y: Integer = 3`
    #### Outputs:
    - `#0 mesh: Geometry = None`
    - `#1 uv_map: Vector = (0.0, 0.0, 0.0)`
    """
    params_all = []
    inputs_all = [(size_x, 1.0), (size_y, 1.0), (vertices_x, 3), (vertices_y, 3)]
    return "GeometryNodeMeshGrid", params_all, inputs_all


def GeometryNodeMeshIcoSphere(radius=1.0, subdivisions=1):
    """
    #### Inputs:
    - `#0 radius: Float = 1.0`
    - `#1 subdivisions: Integer = 1`
    #### Outputs:
    - `#0 mesh: Geometry = None`
    - `#1 uv_map: Vector = (0.0, 0.0, 0.0)`
    """
    params_all = []
    inputs_all = [(radius, 1.0), (subdivisions, 1)]
    return "GeometryNodeMeshIcoSphere", params_all, inputs_all


def GeometryNodeMeshCircle(fill_type='NONE', vertices=32, radius=1.0):
    """
    - `fill_type`: `NONE`, `NGON`, `TRIANGLE_FAN`
    #### Inputs:
    - `#0 vertices: Integer = 32`
    - `#1 radius: Float = 1.0`
    #### Outputs:
    - `#0 mesh: Geometry = None`
    """
    params_all = [('fill_type', fill_type, 'NONE')]
    inputs_all = [(vertices, 32), (radius, 1.0)]
    return "GeometryNodeMeshCircle", params_all, inputs_all


def GeometryNodeMeshLine(count_mode='TOTAL', mode='OFFSET', count=10, resolution=1.0, start_location=(0.0, 0.0, 0.0), offset=(0.0, 0.0, 1.0)):
    """
    - `count_mode`: `TOTAL`, `RESOLUTION`
    - `mode`: `OFFSET`, `END_POINTS`
    #### Inputs:
    - `#0 count: Integer = 10`
    - `#1 resolution: Float = 1.0`
    - `#2 start_location: Vector = (0.0, 0.0, 0.0)`
    - `#3 offset: Vector = (0.0, 0.0, 1.0)`
    #### Outputs:
    - `#0 mesh: Geometry = None`
    """
    params_all = [('count_mode', count_mode, 'TOTAL'), ('mode', mode, 'OFFSET')]
    inputs_all = [(count, 10), (resolution, 1.0), (start_location, (0.0, 0.0, 0.0)), (offset, (0.0, 0.0, 1.0))]
    return "GeometryNodeMeshLine", params_all, inputs_all


def GeometryNodeMeshUVSphere(segments=32, rings=16, radius=1.0):
    """
    #### Inputs:
    - `#0 segments: Integer = 32`
    - `#1 rings: Integer = 16`
    - `#2 radius: Float = 1.0`
    #### Outputs:
    - `#0 mesh: Geometry = None`
    - `#1 uv_map: Vector = (0.0, 0.0, 0.0)`
    """
    params_all = []
    inputs_all = [(segments, 32), (rings, 16), (radius, 1.0)]
    return "GeometryNodeMeshUVSphere", params_all, inputs_all


def GeometryNodeCornersOfFace(face_index=None, weights=0.0, sort_index=0):
    """
    #### Inputs:
    - `#0 face_index: Integer = 0`
    - `#1 weights: Float = 0.0`
    - `#2 sort_index: Integer = 0`
    #### Outputs:
    - `#0 corner_index: Integer = 0`
    - `#1 total: Integer = 0`
    """
    params_all = []
    inputs_all = [(face_index, None), (weights, 0.0), (sort_index, 0)]
    return "GeometryNodeCornersOfFace", params_all, inputs_all


def GeometryNodeCornersOfVertex(vertex_index=None, weights=0.0, sort_index=0):
    """
    #### Inputs:
    - `#0 vertex_index: Integer = 0`
    - `#1 weights: Float = 0.0`
    - `#2 sort_index: Integer = 0`
    #### Outputs:
    - `#0 corner_index: Integer = 0`
    - `#1 total: Integer = 0`
    """
    params_all = []
    inputs_all = [(vertex_index, None), (weights, 0.0), (sort_index, 0)]
    return "GeometryNodeCornersOfVertex", params_all, inputs_all


def GeometryNodeEdgesOfCorner(corner_index=None):
    """
    #### Inputs:
    - `#0 corner_index: Integer = 0`
    #### Outputs:
    - `#0 next_edge_index: Integer = 0`
    - `#1 previous_edge_index: Integer = 0`
    """
    params_all = []
    inputs_all = [(corner_index, None)]
    return "GeometryNodeEdgesOfCorner", params_all, inputs_all


def GeometryNodeEdgesOfVertex(vertex_index=None, weights=0.0, sort_index=0):
    """
    #### Inputs:
    - `#0 vertex_index: Integer = 0`
    - `#1 weights: Float = 0.0`
    - `#2 sort_index: Integer = 0`
    #### Outputs:
    - `#0 edge_index: Integer = 0`
    - `#1 total: Integer = 0`
    """
    params_all = []
    inputs_all = [(vertex_index, None), (weights, 0.0), (sort_index, 0)]
    return "GeometryNodeEdgesOfVertex", params_all, inputs_all


def GeometryNodeFaceOfCorner(corner_index=None):
    """
    #### Inputs:
    - `#0 corner_index: Integer = 0`
    #### Outputs:
    - `#0 face_index: Integer = 0`
    - `#1 index_in_face: Integer = 0`
    """
    params_all = []
    inputs_all = [(corner_index, None)]
    return "GeometryNodeFaceOfCorner", params_all, inputs_all


def GeometryNodeOffsetCornerInFace(corner_index=None, offset=0):
    """
    #### Inputs:
    - `#0 corner_index: Integer = 0`
    - `#1 offset: Integer = 0`
    #### Outputs:
    - `#0 corner_index: Integer = 0`
    """
    params_all = []
    inputs_all = [(corner_index, None), (offset, 0)]
    return "GeometryNodeOffsetCornerInFace", params_all, inputs_all


def GeometryNodeVertexOfCorner(corner_index=None):
    """
    #### Inputs:
    - `#0 corner_index: Integer = 0`
    #### Outputs:
    - `#0 vertex_index: Integer = 0`
    """
    params_all = []
    inputs_all = [(corner_index, None)]
    return "GeometryNodeVertexOfCorner", params_all, inputs_all


def GeometryNodeUVPackIslands(uv=(0.0, 0.0, 0.0), selection=True, margin=0.001, rotate=True):
    """
    #### Inputs:
    - `#0 uv: Vector = (0.0, 0.0, 0.0)`
    - `#1 selection: Boolean = True`
    - `#2 margin: Float = 0.001`
    - `#3 rotate: Boolean = True`
    #### Outputs:
    - `#0 uv: Vector = (0.0, 0.0, 0.0)`
    """
    params_all = []
    inputs_all = [(uv, (0.0, 0.0, 0.0)), (selection, True), (margin, 0.001), (rotate, True)]
    return "GeometryNodeUVPackIslands", params_all, inputs_all


def GeometryNodeUVUnwrap(method='ANGLE_BASED', selection=True, seam=False, margin=0.001, fill_holes=True):
    """
    - `method`: `ANGLE_BASED`, `CONFORMAL`
    #### Inputs:
    - `#0 selection: Boolean = True`
    - `#1 seam: Boolean = False`
    - `#2 margin: Float = 0.001`
    - `#3 fill_holes: Boolean = True`
    #### Outputs:
    - `#0 uv: Vector = (0.0, 0.0, 0.0)`
    """
    params_all = [('method', method, 'ANGLE_BASED')]
    inputs_all = [(selection, True), (seam, False), (margin, 0.001), (fill_holes, True)]
    return "GeometryNodeUVUnwrap", params_all, inputs_all


def GeometryNodeDistributePointsInVolume(mode='DENSITY_RANDOM', volume=None, density=1.0, seed=0, spacing=(0.3, 0.3, 0.3), threshold=0.1):
    """
    - `mode`: `DENSITY_RANDOM`, `DENSITY_GRID`
    #### Inputs:
    - `#0 volume: Geometry = None`
    - `#1 density: Float = 1.0`
    - `#2 seed: Integer = 0`
    - `#3 spacing: Vector = (0.3, 0.3, 0.3)`
    - `#4 threshold: Float = 0.1`
    #### Outputs:
    - `#0 points: Geometry = None`
    """
    params_all = [('mode', mode, 'DENSITY_RANDOM')]
    inputs_all = [(volume, None), (density, 1.0), (seed, 0), (spacing, (0.3, 0.3, 0.3)), (threshold, 0.1)]
    return "GeometryNodeDistributePointsInVolume", params_all, inputs_all


def GeometryNodeDistributePointsOnFaces(distribute_method='RANDOM', use_legacy_normal=False, mesh=None, selection=True, distance_min=0.0, density_max=10.0, density=10.0, density_factor=1.0, seed=0):
    """
    - `distribute_method`: `RANDOM`, `POISSON`
    #### Inputs:
    - `#0 mesh: Geometry = None`
    - `#1 selection: Boolean = True`
    - `#2 distance_min: Float = 0.0`
    - `#3 density_max: Float = 10.0`
    - `#4 density: Float = 10.0`
    - `#5 density_factor: Float = 1.0`
    - `#6 seed: Integer = 0`
    #### Outputs:
    - `#0 points: Geometry = None`
    - `#1 normal: Vector = (0.0, 0.0, 0.0)`
    - `#2 rotation: Vector = (0.0, 0.0, 0.0)`
    """
    params_all = [('distribute_method', distribute_method, 'RANDOM'), ('use_legacy_normal', use_legacy_normal, False)]
    inputs_all = [(mesh, None), (selection, True), (distance_min, 0.0), (density_max, 10.0), (density, 10.0), (density_factor, 1.0), (seed, 0)]
    return "GeometryNodeDistributePointsOnFaces", params_all, inputs_all


def GeometryNodePoints(count=1, position=(0.0, 0.0, 0.0), radius=0.1):
    """
    #### Inputs:
    - `#0 count: Integer = 1`
    - `#1 position: Vector = (0.0, 0.0, 0.0)`
    - `#2 radius: Float = 0.1`
    #### Outputs:
    - `#0 geometry: Geometry = None`
    """
    params_all = []
    inputs_all = [(count, 1), (position, (0.0, 0.0, 0.0)), (radius, 0.1)]
    return "GeometryNodePoints", params_all, inputs_all


def GeometryNodePointsToVertices(points=None, selection=True):
    """
    #### Inputs:
    - `#0 points: Geometry = None`
    - `#1 selection: Boolean = True`
    #### Outputs:
    - `#0 mesh: Geometry = None`
    """
    params_all = []
    inputs_all = [(points, None), (selection, True)]
    return "GeometryNodePointsToVertices", params_all, inputs_all


def GeometryNodePointsToVolume(resolution_mode='VOXEL_AMOUNT', points=None, density=1.0, voxel_size=0.3, voxel_amount=64.0, radius=0.5):
    """
    - `resolution_mode`: `VOXEL_AMOUNT`, `VOXEL_SIZE`
    #### Inputs:
    - `#0 points: Geometry = None`
    - `#1 density: Float = 1.0`
    - `#2 voxel_size: Float = 0.3`
    - `#3 voxel_amount: Float = 64.0`
    - `#4 radius: Float = 0.5`
    #### Outputs:
    - `#0 volume: Geometry = None`
    """
    params_all = [('resolution_mode', resolution_mode, 'VOXEL_AMOUNT')]
    inputs_all = [(points, None), (density, 1.0), (voxel_size, 0.3), (voxel_amount, 64.0), (radius, 0.5)]
    return "GeometryNodePointsToVolume", params_all, inputs_all


def GeometryNodeSetPointRadius(points=None, selection=True, radius=0.05):
    """
    #### Inputs:
    - `#0 points: Geometry = None`
    - `#1 selection: Boolean = True`
    - `#2 radius: Float = 0.05`
    #### Outputs:
    - `#0 points: Geometry = None`
    """
    params_all = []
    inputs_all = [(points, None), (selection, True), (radius, 0.05)]
    return "GeometryNodeSetPointRadius", params_all, inputs_all


def GeometryNodeVolumeCube(density=1.0, background=0.0, min=(-1.0, -1.0, -1.0), max=(1.0, 1.0, 1.0), resolution_x=32, resolution_y=32, resolution_z=32):
    """
    #### Inputs:
    - `#0 density: Float = 1.0`
    - `#1 background: Float = 0.0`
    - `#2 min: Vector = (-1.0, -1.0, -1.0)`
    - `#3 max: Vector = (1.0, 1.0, 1.0)`
    - `#4 resolution_x: Integer = 32`
    - `#5 resolution_y: Integer = 32`
    - `#6 resolution_z: Integer = 32`
    #### Outputs:
    - `#0 volume: Geometry = None`
    """
    params_all = []
    inputs_all = [(density, 1.0), (background, 0.0), (min, (-1.0, -1.0, -1.0)), (max, (1.0, 1.0, 1.0)), (resolution_x, 32), (resolution_y, 32), (resolution_z, 32)]
    return "GeometryNodeVolumeCube", params_all, inputs_all


def GeometryNodeVolumeToMesh(resolution_mode='GRID', volume=None, voxel_size=0.3, voxel_amount=64.0, threshold=0.1, adaptivity=0.0):
    """
    - `resolution_mode`: `GRID`, `VOXEL_AMOUNT`, `VOXEL_SIZE`
    #### Inputs:
    - `#0 volume: Geometry = None`
    - `#1 voxel_size: Float = 0.3`
    - `#2 voxel_amount: Float = 64.0`
    - `#3 threshold: Float = 0.1`
    - `#4 adaptivity: Float = 0.0`
    #### Outputs:
    - `#0 mesh: Geometry = None`
    """
    params_all = [('resolution_mode', resolution_mode, 'GRID')]
    inputs_all = [(volume, None), (voxel_size, 0.3), (voxel_amount, 64.0), (threshold, 0.1), (adaptivity, 0.0)]
    return "GeometryNodeVolumeToMesh", params_all, inputs_all


def GeometryNodeReplaceMaterial(geometry=None, old=None, new=None):
    """
    #### Inputs:
    - `#0 geometry: Geometry = None`
    - `#1 old: Material = None`
    - `#2 new: Material = None`
    #### Outputs:
    - `#0 geometry: Geometry = None`
    """
    params_all = []
    inputs_all = [(geometry, None), (old, None), (new, None)]
    return "GeometryNodeReplaceMaterial", params_all, inputs_all


def GeometryNodeInputMaterialIndex():
    """
    #### Outputs:
    - `#0 material_index: Integer = 0`
    """
    params_all = []
    inputs_all = []
    return "GeometryNodeInputMaterialIndex", params_all, inputs_all


def GeometryNodeMaterialSelection(material=None):
    """
    #### Inputs:
    - `#0 material: Material = None`
    #### Outputs:
    - `#0 selection: Boolean = False`
    """
    params_all = []
    inputs_all = [(material, None)]
    return "GeometryNodeMaterialSelection", params_all, inputs_all


def GeometryNodeSetMaterial(geometry=None, selection=True, material=None):
    """
    #### Inputs:
    - `#0 geometry: Geometry = None`
    - `#1 selection: Boolean = True`
    - `#2 material: Material = None`
    #### Outputs:
    - `#0 geometry: Geometry = None`
    """
    params_all = []
    inputs_all = [(geometry, None), (selection, True), (material, None)]
    return "GeometryNodeSetMaterial", params_all, inputs_all


def GeometryNodeSetMaterialIndex(geometry=None, selection=True, material_index=0):
    """
    #### Inputs:
    - `#0 geometry: Geometry = None`
    - `#1 selection: Boolean = True`
    - `#2 material_index: Integer = 0`
    #### Outputs:
    - `#0 geometry: Geometry = None`
    """
    params_all = []
    inputs_all = [(geometry, None), (selection, True), (material_index, 0)]
    return "GeometryNodeSetMaterialIndex", params_all, inputs_all


def ShaderNodeTexBrick(color_mapping=None, offset=0.5, offset_frequency=2, squash=1.0, squash_frequency=2, texture_mapping=None, vector=None, color1=(0.8, 0.8, 0.8, 1.0), color2=(0.2, 0.2, 0.2, 1.0), mortar=(0.0, 0.0, 0.0, 1.0), scale=5.0, mortar_size=0.02, mortar_smooth=0.1, bias=0.0, brick_width=0.5, row_height=0.25):
    """
    #### Inputs:
    - `#0 vector: Vector = (0.0, 0.0, 0.0)`
    - `#1 color1: Color = (0.8, 0.8, 0.8, 1.0)`
    - `#2 color2: Color = (0.2, 0.2, 0.2, 1.0)`
    - `#3 mortar: Color = (0.0, 0.0, 0.0, 1.0)`
    - `#4 scale: Float = 5.0`
    - `#5 mortar_size: Float = 0.02`
    - `#6 mortar_smooth: Float = 0.1`
    - `#7 bias: Float = 0.0`
    - `#8 brick_width: Float = 0.5`
    - `#9 row_height: Float = 0.25`
    #### Outputs:
    - `#0 color: Color = (0.0, 0.0, 0.0, 0.0)`
    - `#1 fac: Float = 0.0`
    """
    params_all = [('color_mapping', color_mapping, None), ('offset', offset, 0.5), ('offset_frequency', offset_frequency, 2), ('squash', squash, 1.0), ('squash_frequency', squash_frequency, 2), ('texture_mapping', texture_mapping, None)]
    inputs_all = [(vector, None), (color1, (0.8, 0.8, 0.8, 1.0)), (color2, (0.2, 0.2, 0.2, 1.0)), (mortar, (0.0, 0.0, 0.0, 1.0)), (scale, 5.0), (mortar_size, 0.02), (mortar_smooth, 0.1), (bias, 0.0), (brick_width, 0.5), (row_height, 0.25)]
    return "ShaderNodeTexBrick", params_all, inputs_all


def ShaderNodeTexChecker(color_mapping=None, texture_mapping=None, vector=None, color1=(0.8, 0.8, 0.8, 1.0), color2=(0.2, 0.2, 0.2, 1.0), scale=5.0):
    """
    #### Inputs:
    - `#0 vector: Vector = (0.0, 0.0, 0.0)`
    - `#1 color1: Color = (0.8, 0.8, 0.8, 1.0)`
    - `#2 color2: Color = (0.2, 0.2, 0.2, 1.0)`
    - `#3 scale: Float = 5.0`
    #### Outputs:
    - `#0 color: Color = (0.0, 0.0, 0.0, 0.0)`
    - `#1 fac: Float = 0.0`
    """
    params_all = [('color_mapping', color_mapping, None), ('texture_mapping', texture_mapping, None)]
    inputs_all = [(vector, None), (color1, (0.8, 0.8, 0.8, 1.0)), (color2, (0.2, 0.2, 0.2, 1.0)), (scale, 5.0)]
    return "ShaderNodeTexChecker", params_all, inputs_all


def ShaderNodeTexGradient(gradient_type='LINEAR', color_mapping=None, texture_mapping=None, vector=None):
    """
    - `gradient_type`: `LINEAR`, `QUADRATIC`, `EASING`, `DIAGONAL`, `SPHERICAL`, `QUADRATIC_SPHERE`, `RADIAL`
    #### Inputs:
    - `#0 vector: Vector = (0.0, 0.0, 0.0)`
    #### Outputs:
    - `#0 color: Color = (0.0, 0.0, 0.0, 0.0)`
    - `#1 fac: Float = 0.0`
    """
    params_all = [('gradient_type', gradient_type, 'LINEAR'), ('color_mapping', color_mapping, None), ('texture_mapping', texture_mapping, None)]
    inputs_all = [(vector, None)]
    return "ShaderNodeTexGradient", params_all, inputs_all


def GeometryNodeImageTexture(extension='REPEAT', interpolation='Linear', image=None, vector=None, frame=0):
    """
    - `extension`: `REPEAT`, `EXTEND`, `CLIP`, `MIRROR`
    - `interpolation`: `Linear`, `Closest`, `Cubic`
    #### Inputs:
    - `#0 image: Image = None`
    - `#1 vector: Vector = (0.0, 0.0, 0.0)`
    - `#2 frame: Integer = 0`
    #### Outputs:
    - `#0 color: Color = (0.0, 0.0, 0.0, 0.0)`
    - `#1 alpha: Float = 0.0`
    """
    params_all = [('extension', extension, 'REPEAT'), ('interpolation', interpolation, 'Linear')]
    inputs_all = [(image, None), (vector, None), (frame, 0)]
    return "GeometryNodeImageTexture", params_all, inputs_all


def ShaderNodeTexMagic(color_mapping=None, texture_mapping=None, turbulence_depth=2, vector=None, scale=5.0, distortion=1.0):
    """
    #### Inputs:
    - `#0 vector: Vector = (0.0, 0.0, 0.0)`
    - `#1 scale: Float = 5.0`
    - `#2 distortion: Float = 1.0`
    #### Outputs:
    - `#0 color: Color = (0.0, 0.0, 0.0, 0.0)`
    - `#1 fac: Float = 0.0`
    """
    params_all = [('color_mapping', color_mapping, None), ('texture_mapping', texture_mapping, None), ('turbulence_depth', turbulence_depth, 2)]
    inputs_all = [(vector, None), (scale, 5.0), (distortion, 1.0)]
    return "ShaderNodeTexMagic", params_all, inputs_all


def ShaderNodeTexMusgrave(musgrave_dimensions='3D', musgrave_type='FBM', color_mapping=None, texture_mapping=None, vector=None, w=0.0, scale=5.0, detail=2.0, dimension=2.0, lacunarity=2.0, offset=0.0, gain=1.0):
    """
    - `musgrave_dimensions`: `3D`, `1D`, `2D`, `4D`
    - `musgrave_type`: `FBM`, `MULTIFRACTAL`, `RIDGED_MULTIFRACTAL`, `HYBRID_MULTIFRACTAL`, `HETERO_TERRAIN`
    #### Inputs:
    - `#0 vector: Vector = (0.0, 0.0, 0.0)`
    - `#1 w: Float = 0.0`
    - `#2 scale: Float = 5.0`
    - `#3 detail: Float = 2.0`
    - `#4 dimension: Float = 2.0`
    - `#5 lacunarity: Float = 2.0`
    - `#6 offset: Float = 0.0`
    - `#7 gain: Float = 1.0`
    #### Outputs:
    - `#0 fac: Float = 0.0`
    """
    params_all = [('musgrave_dimensions', musgrave_dimensions, '3D'), ('musgrave_type', musgrave_type, 'FBM'), ('color_mapping', color_mapping, None), ('texture_mapping', texture_mapping, None)]
    inputs_all = [(vector, None), (w, 0.0), (scale, 5.0), (detail, 2.0), (dimension, 2.0), (lacunarity, 2.0), (offset, 0.0), (gain, 1.0)]
    return "ShaderNodeTexMusgrave", params_all, inputs_all


def ShaderNodeTexNoise(noise_dimensions='3D', color_mapping=None, texture_mapping=None, vector=None, w=0.0, scale=5.0, detail=2.0, roughness=0.5, distortion=0.0):
    """
    - `noise_dimensions`: `3D`, `1D`, `2D`, `4D`
    #### Inputs:
    - `#0 vector: Vector = (0.0, 0.0, 0.0)`
    - `#1 w: Float = 0.0`
    - `#2 scale: Float = 5.0`
    - `#3 detail: Float = 2.0`
    - `#4 roughness: Float = 0.5`
    - `#5 distortion: Float = 0.0`
    #### Outputs:
    - `#0 fac: Float = 0.0`
    - `#1 color: Color = (0.0, 0.0, 0.0, 0.0)`
    """
    params_all = [('noise_dimensions', noise_dimensions, '3D'), ('color_mapping', color_mapping, None), ('texture_mapping', texture_mapping, None)]
    inputs_all = [(vector, None), (w, 0.0), (scale, 5.0), (detail, 2.0), (roughness, 0.5), (distortion, 0.0)]
    return "ShaderNodeTexNoise", params_all, inputs_all


def ShaderNodeTexVoronoi(distance='EUCLIDEAN', feature='F1', voronoi_dimensions='3D', color_mapping=None, texture_mapping=None, vector=None, w=0.0, scale=5.0, smoothness=1.0, exponent=0.5, randomness=1.0):
    """
    - `distance`: `EUCLIDEAN`, `MANHATTAN`, `CHEBYCHEV`, `MINKOWSKI`
    - `feature`: `F1`, `F2`, `SMOOTH_F1`, `DISTANCE_TO_EDGE`, `N_SPHERE_RADIUS`
    - `voronoi_dimensions`: `3D`, `1D`, `2D`, `4D`
    #### Inputs:
    - `#0 vector: Vector = (0.0, 0.0, 0.0)`
    - `#1 w: Float = 0.0`
    - `#2 scale: Float = 5.0`
    - `#3 smoothness: Float = 1.0`
    - `#4 exponent: Float = 0.5`
    - `#5 randomness: Float = 1.0`
    #### Outputs:
    - `#0 distance: Float = 0.0`
    - `#1 color: Color = (0.0, 0.0, 0.0, 0.0)`
    - `#2 position: Vector = (0.0, 0.0, 0.0)`
    - `#3 w: Float = 0.0`
    - `#4 radius: Float = 0.0`
    """
    params_all = [('distance', distance, 'EUCLIDEAN'), ('feature', feature, 'F1'), ('voronoi_dimensions', voronoi_dimensions, '3D'), ('color_mapping', color_mapping, None), ('texture_mapping', texture_mapping, None)]
    inputs_all = [(vector, None), (w, 0.0), (scale, 5.0), (smoothness, 1.0), (exponent, 0.5), (randomness, 1.0)]
    return "ShaderNodeTexVoronoi", params_all, inputs_all


def ShaderNodeTexWave(bands_direction='X', rings_direction='X', wave_profile='SIN', wave_type='BANDS', color_mapping=None, texture_mapping=None, vector=None, scale=5.0, distortion=0.0, detail=2.0, detail_scale=1.0, detail_roughness=0.5, phase_offset=0.0):
    """
    - `bands_direction`: `X`, `Y`, `Z`, `DIAGONAL`
    - `rings_direction`: `X`, `Y`, `Z`, `SPHERICAL`
    - `wave_profile`: `SIN`, `SAW`, `TRI`
    - `wave_type`: `BANDS`, `RINGS`
    #### Inputs:
    - `#0 vector: Vector = (0.0, 0.0, 0.0)`
    - `#1 scale: Float = 5.0`
    - `#2 distortion: Float = 0.0`
    - `#3 detail: Float = 2.0`
    - `#4 detail_scale: Float = 1.0`
    - `#5 detail_roughness: Float = 0.5`
    - `#6 phase_offset: Float = 0.0`
    #### Outputs:
    - `#0 color: Color = (0.0, 0.0, 0.0, 0.0)`
    - `#1 fac: Float = 0.0`
    """
    params_all = [('bands_direction', bands_direction, 'X'), ('rings_direction', rings_direction, 'X'), ('wave_profile', wave_profile, 'SIN'), ('wave_type', wave_type, 'BANDS'), ('color_mapping', color_mapping, None), ('texture_mapping', texture_mapping, None)]
    inputs_all = [(vector, None), (scale, 5.0), (distortion, 0.0), (detail, 2.0), (detail_scale, 1.0), (detail_roughness, 0.5), (phase_offset, 0.0)]
    return "ShaderNodeTexWave", params_all, inputs_all


def ShaderNodeTexWhiteNoise(noise_dimensions='3D', vector=None, w=0.0):
    """
    - `noise_dimensions`: `3D`, `1D`, `2D`, `4D`
    #### Inputs:
    - `#0 vector: Vector = (0.0, 0.0, 0.0)`
    - `#1 w: Float = 0.0`
    #### Outputs:
    - `#0 value: Float = 0.0`
    - `#1 color: Color = (0.0, 0.0, 0.0, 0.0)`
    """
    params_all = [('noise_dimensions', noise_dimensions, '3D')]
    inputs_all = [(vector, None), (w, 0.0)]
    return "ShaderNodeTexWhiteNoise", params_all, inputs_all


def ShaderNodeValToRGB(color_ramp=None, fac=0.5):
    """
    #### Inputs:
    - `#0 fac: Float = 0.5`
    #### Outputs:
    - `#0 color: Color = (0.0, 0.0, 0.0, 0.0)`
    - `#1 alpha: Float = 0.0`
    """
    params_all = [('color_ramp', color_ramp, None)]
    inputs_all = [(fac, 0.5)]
    return "ShaderNodeValToRGB", params_all, inputs_all


def FunctionNodeCombineColor(mode='RGB', red=0.0, green=0.0, blue=0.0, alpha=1.0):
    """
    - `mode`: `RGB`, `HSV`, `HSL`
    #### Inputs:
    - `#0 red: Float = 0.0`
    - `#1 green: Float = 0.0`
    - `#2 blue: Float = 0.0`
    - `#3 alpha: Float = 1.0`
    #### Outputs:
    - `#0 color: Color = (0.0, 0.0, 0.0, 0.0)`
    """
    params_all = [('mode', mode, 'RGB')]
    inputs_all = [(red, 0.0), (green, 0.0), (blue, 0.0), (alpha, 1.0)]
    return "FunctionNodeCombineColor", params_all, inputs_all


def ShaderNodeMix(blend_type='MIX', data_type='FLOAT', factor_mode='UNIFORM', clamp_factor=True, clamp_result=False, factor_float=0.5, factor_vector=(0.5, 0.5, 0.5), a_float=0.0, b_float=0.0, a_vector=(0.0, 0.0, 0.0), b_vector=(0.0, 0.0, 0.0), a_color=(0.5, 0.5, 0.5, 1.0), b_color=(0.5, 0.5, 0.5, 1.0)):
    """
    - `blend_type`: `MIX`, `DARKEN`, `MULTIPLY`, `BURN`, `LIGHTEN`, `SCREEN`, `DODGE`, `ADD`, `OVERLAY`, `SOFT_LIGHT`, `LINEAR_LIGHT`, `DIFFERENCE`, `EXCLUSION`, `SUBTRACT`, `DIVIDE`, `HUE`, `SATURATION`, `COLOR`, `VALUE`
    - `data_type`: `FLOAT`, `VECTOR`, `RGBA`
    - `factor_mode`: `UNIFORM`, `NON_UNIFORM`
    #### Inputs:
    - `#0 factor_float: Float = 0.5`
    - `#1 factor_vector: Vector = (0.5, 0.5, 0.5)`
    - `#2 a_float: Float = 0.0`
    - `#3 b_float: Float = 0.0`
    - `#4 a_vector: Vector = (0.0, 0.0, 0.0)`
    - `#5 b_vector: Vector = (0.0, 0.0, 0.0)`
    - `#6 a_color: Color = (0.5, 0.5, 0.5, 1.0)`
    - `#7 b_color: Color = (0.5, 0.5, 0.5, 1.0)`
    #### Outputs:
    - `#0 result_float: Float = 0.0`
    - `#1 result_vector: Vector = (0.0, 0.0, 0.0)`
    - `#2 result_color: Color = (0.0, 0.0, 0.0, 0.0)`
    """
    params_all = [('blend_type', blend_type, 'MIX'), ('data_type', data_type, 'FLOAT'), ('factor_mode', factor_mode, 'UNIFORM'), ('clamp_factor', clamp_factor, True), ('clamp_result', clamp_result, False)]
    inputs_all = [(factor_float, 0.5), (factor_vector, (0.5, 0.5, 0.5)), (a_float, 0.0), (b_float, 0.0), (a_vector, (0.0, 0.0, 0.0)), (b_vector, (0.0, 0.0, 0.0)), (a_color, (0.5, 0.5, 0.5, 1.0)), (b_color, (0.5, 0.5, 0.5, 1.0))]
    return "ShaderNodeMix", params_all, inputs_all


def ShaderNodeRGBCurve(mapping=None, fac=1.0, color=(1.0, 1.0, 1.0, 1.0)):
    """
    #### Inputs:
    - `#0 fac: Float = 1.0`
    - `#1 color: Color = (1.0, 1.0, 1.0, 1.0)`
    #### Outputs:
    - `#0 color: Color = (0.0, 0.0, 0.0, 0.0)`
    """
    params_all = [('mapping', mapping, None)]
    inputs_all = [(fac, 1.0), (color, (1.0, 1.0, 1.0, 1.0))]
    return "ShaderNodeRGBCurve", params_all, inputs_all


def FunctionNodeSeparateColor(mode='RGB', color=(1.0, 1.0, 1.0, 1.0)):
    """
    - `mode`: `RGB`, `HSV`, `HSL`
    #### Inputs:
    - `#0 color: Color = (1.0, 1.0, 1.0, 1.0)`
    #### Outputs:
    - `#0 red: Float = 0.0`
    - `#1 green: Float = 0.0`
    - `#2 blue: Float = 0.0`
    - `#3 alpha: Float = 0.0`
    """
    params_all = [('mode', mode, 'RGB')]
    inputs_all = [(color, (1.0, 1.0, 1.0, 1.0))]
    return "FunctionNodeSeparateColor", params_all, inputs_all


def GeometryNodeStringJoin(delimiter='', strings=''):
    """
    #### Inputs:
    - `#0 delimiter: String = ''`
    - `#1 strings: String = ''`
    #### Outputs:
    - `#0 string: String = ""`
    """
    params_all = []
    inputs_all = [(delimiter, ''), (strings, '')]
    return "GeometryNodeStringJoin", params_all, inputs_all


def FunctionNodeReplaceString(string='', find='', replace=''):
    """
    #### Inputs:
    - `#0 string: String = ''`
    - `#1 find: String = ''`
    - `#2 replace: String = ''`
    #### Outputs:
    - `#0 string: String = ""`
    """
    params_all = []
    inputs_all = [(string, ''), (find, ''), (replace, '')]
    return "FunctionNodeReplaceString", params_all, inputs_all


def FunctionNodeSliceString(string='', position=0, length=10):
    """
    #### Inputs:
    - `#0 string: String = ''`
    - `#1 position: Integer = 0`
    - `#2 length: Integer = 10`
    #### Outputs:
    - `#0 string: String = ""`
    """
    params_all = []
    inputs_all = [(string, ''), (position, 0), (length, 10)]
    return "FunctionNodeSliceString", params_all, inputs_all


def FunctionNodeInputSpecialCharacters():
    """
    #### Outputs:
    - `#0 line_break: String = ""`
    - `#1 tab: String = ""`
    """
    params_all = []
    inputs_all = []
    return "FunctionNodeInputSpecialCharacters", params_all, inputs_all


def FunctionNodeStringLength(string=''):
    """
    #### Inputs:
    - `#0 string: String = ''`
    #### Outputs:
    - `#0 length: Integer = 0`
    """
    params_all = []
    inputs_all = [(string, '')]
    return "FunctionNodeStringLength", params_all, inputs_all


def GeometryNodeStringToCurves(align_x='LEFT', align_y='TOP_BASELINE', overflow='OVERFLOW', pivot_mode='BOTTOM_LEFT', font=None, string='', size=1.0, character_spacing=1.0, word_spacing=1.0, line_spacing=1.0, text_box_width=0.0, text_box_height=0.0):
    """
    - `align_x`: `LEFT`, `CENTER`, `RIGHT`, `JUSTIFY`, `FLUSH`
    - `align_y`: `TOP_BASELINE`, `TOP`, `MIDDLE`, `BOTTOM_BASELINE`, `BOTTOM`
    - `overflow`: `OVERFLOW`, `SCALE_TO_FIT`, `TRUNCATE`
    - `pivot_mode`: `BOTTOM_LEFT`, `MIDPOINT`, `TOP_LEFT`, `TOP_CENTER`, `TOP_RIGHT`, `BOTTOM_CENTER`, `BOTTOM_RIGHT`
    #### Inputs:
    - `#0 string: String = ''`
    - `#1 size: Float = 1.0`
    - `#2 character_spacing: Float = 1.0`
    - `#3 word_spacing: Float = 1.0`
    - `#4 line_spacing: Float = 1.0`
    - `#5 text_box_width: Float = 0.0`
    - `#6 text_box_height: Float = 0.0`
    #### Outputs:
    - `#0 curve_instances: Geometry = None`
    - `#1 remainder: String = ""`
    - `#2 line: Integer = 0`
    - `#3 pivot_point: Vector = (0.0, 0.0, 0.0)`
    """
    params_all = [('align_x', align_x, 'LEFT'), ('align_y', align_y, 'TOP_BASELINE'), ('overflow', overflow, 'OVERFLOW'), ('pivot_mode', pivot_mode, 'BOTTOM_LEFT'), ('font', font, None)]
    inputs_all = [(string, ''), (size, 1.0), (character_spacing, 1.0), (word_spacing, 1.0), (line_spacing, 1.0), (text_box_width, 0.0), (text_box_height, 0.0)]
    return "GeometryNodeStringToCurves", params_all, inputs_all


def FunctionNodeValueToString(value=0.0, decimals=0):
    """
    #### Inputs:
    - `#0 value: Float = 0.0`
    - `#1 decimals: Integer = 0`
    #### Outputs:
    - `#0 string: String = ""`
    """
    params_all = []
    inputs_all = [(value, 0.0), (decimals, 0)]
    return "FunctionNodeValueToString", params_all, inputs_all


def ShaderNodeCombineXYZ(x=0.0, y=0.0, z=0.0):
    """
    #### Inputs:
    - `#0 x: Float = 0.0`
    - `#1 y: Float = 0.0`
    - `#2 z: Float = 0.0`
    #### Outputs:
    - `#0 vector: Vector = (0.0, 0.0, 0.0)`
    """
    params_all = []
    inputs_all = [(x, 0.0), (y, 0.0), (z, 0.0)]
    return "ShaderNodeCombineXYZ", params_all, inputs_all


def ShaderNodeSeparateXYZ(vector=(0.0, 0.0, 0.0)):
    """
    #### Inputs:
    - `#0 vector: Vector = (0.0, 0.0, 0.0)`
    #### Outputs:
    - `#0 x: Float = 0.0`
    - `#1 y: Float = 0.0`
    - `#2 z: Float = 0.0`
    """
    params_all = []
    inputs_all = [(vector, (0.0, 0.0, 0.0))]
    return "ShaderNodeSeparateXYZ", params_all, inputs_all


def ShaderNodeVectorCurve(mapping=None, fac=1.0, vector=(0.0, 0.0, 0.0)):
    """
    #### Inputs:
    - `#0 fac: Float = 1.0`
    - `#1 vector: Vector = (0.0, 0.0, 0.0)`
    #### Outputs:
    - `#0 vector: Vector = (0.0, 0.0, 0.0)`
    """
    params_all = [('mapping', mapping, None)]
    inputs_all = [(fac, 1.0), (vector, (0.0, 0.0, 0.0))]
    return "ShaderNodeVectorCurve", params_all, inputs_all


def ShaderNodeVectorMath(operation='ADD', vector=(0.0, 0.0, 0.0), vector_001=(0.0, 0.0, 0.0), vector_002=(0.0, 0.0, 0.0), scale=1.0):
    """
    - `operation`: `ADD`, `SUBTRACT`, `MULTIPLY`, `DIVIDE`, `MULTIPLY_ADD`, `CROSS_PRODUCT`, `PROJECT`, `REFLECT`, `REFRACT`, `FACEFORWARD`, `DOT_PRODUCT`, `DISTANCE`, `LENGTH`, `SCALE`, `NORMALIZE`, `ABSOLUTE`, `MINIMUM`, `MAXIMUM`, `FLOOR`, `CEIL`, `FRACTION`, `MODULO`, `WRAP`, `SNAP`, `SINE`, `COSINE`, `TANGENT`
    #### Inputs:
    - `#0 vector: Vector = (0.0, 0.0, 0.0)`
    - `#1 vector_001: Vector = (0.0, 0.0, 0.0)`
    - `#2 vector_002: Vector = (0.0, 0.0, 0.0)`
    - `#3 scale: Float = 1.0`
    #### Outputs:
    - `#0 vector: Vector = (0.0, 0.0, 0.0)`
    - `#1 value: Float = 0.0`
    """
    params_all = [('operation', operation, 'ADD')]
    inputs_all = [(vector, (0.0, 0.0, 0.0)), (vector_001, (0.0, 0.0, 0.0)), (vector_002, (0.0, 0.0, 0.0)), (scale, 1.0)]
    return "ShaderNodeVectorMath", params_all, inputs_all


def ShaderNodeVectorRotate(rotation_type='AXIS_ANGLE', invert=False, vector=(0.0, 0.0, 0.0), center=(0.0, 0.0, 0.0), axis=(0.0, 0.0, 1.0), angle=math.radians(0.0), rotation=(0.0, 0.0, 0.0)):
    """
    - `rotation_type`: `AXIS_ANGLE`, `X_AXIS`, `Y_AXIS`, `Z_AXIS`, `EULER_XYZ`
    #### Inputs:
    - `#0 vector: Vector = (0.0, 0.0, 0.0)`
    - `#1 center: Vector = (0.0, 0.0, 0.0)`
    - `#2 axis: Vector = (0.0, 0.0, 1.0)`
    - `#3 angle: Float = math.radians(0.0)`
    - `#4 rotation: Vector = (0.0, 0.0, 0.0)`
    #### Outputs:
    - `#0 vector: Vector = (0.0, 0.0, 0.0)`
    """
    params_all = [('rotation_type', rotation_type, 'AXIS_ANGLE'), ('invert', invert, False)]
    inputs_all = [(vector, (0.0, 0.0, 0.0)), (center, (0.0, 0.0, 0.0)), (axis, (0.0, 0.0, 1.0)), (angle, math.radians(0.0)), (rotation, (0.0, 0.0, 0.0))]
    return "ShaderNodeVectorRotate", params_all, inputs_all


def GeometryNodeAccumulateField(data_type='FLOAT', domain='POINT', value_vector=(1.0, 1.0, 1.0), value_float=1.0, value_int=1, group_index=0):
    """
    - `data_type`: `FLOAT`, `INT`, `FLOAT_VECTOR`
    - `domain`: `POINT`, `EDGE`, `FACE`, `CORNER`, `CURVE`, `INSTANCE`
    #### Inputs:
    - `#0 value_vector: Vector = (1.0, 1.0, 1.0)`
    - `#1 value_float: Float = 1.0`
    - `#2 value_int: Integer = 1`
    - `#3 group_index: Integer = 0`
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
    """
    params_all = [('data_type', data_type, 'FLOAT'), ('domain', domain, 'POINT')]
    inputs_all = [(value_vector, (1.0, 1.0, 1.0)), (value_float, 1.0), (value_int, 1), (group_index, 0)]
    return "GeometryNodeAccumulateField", params_all, inputs_all


def GeometryNodeFieldAtIndex(data_type='FLOAT', domain='POINT', index=0, value_float=0.0, value_int=0, value_vector=(0.0, 0.0, 0.0), value_color=(0.0, 0.0, 0.0, 0.0), value_bool=False):
    """
    - `data_type`: `FLOAT`, `INT`, `FLOAT_VECTOR`, `FLOAT_COLOR`, `BOOLEAN`
    - `domain`: `POINT`, `EDGE`, `FACE`, `CORNER`, `CURVE`, `INSTANCE`
    #### Inputs:
    - `#0 index: Integer = 0`
    - `#1 value_float: Float = 0.0`
    - `#2 value_int: Integer = 0`
    - `#3 value_vector: Vector = (0.0, 0.0, 0.0)`
    - `#4 value_color: Color = (0.0, 0.0, 0.0, 0.0)`
    - `#5 value_bool: Boolean = False`
    #### Outputs:
    - `#0 value_float: Float = 0.0`
    - `#1 value_int: Integer = 0`
    - `#2 value_vector: Vector = (0.0, 0.0, 0.0)`
    - `#3 value_color: Color = (0.0, 0.0, 0.0, 0.0)`
    - `#4 value_bool: Boolean = False`
    """
    params_all = [('data_type', data_type, 'FLOAT'), ('domain', domain, 'POINT')]
    inputs_all = [(index, 0), (value_float, 0.0), (value_int, 0), (value_vector, (0.0, 0.0, 0.0)), (value_color, (0.0, 0.0, 0.0, 0.0)), (value_bool, False)]
    return "GeometryNodeFieldAtIndex", params_all, inputs_all


def GeometryNodeFieldOnDomain(data_type='FLOAT', domain='POINT', value_float=0.0, value_int=0, value_vector=(0.0, 0.0, 0.0), value_color=(0.0, 0.0, 0.0, 0.0), value_bool=False):
    """
    - `data_type`: `FLOAT`, `INT`, `FLOAT_VECTOR`, `FLOAT_COLOR`, `BOOLEAN`
    - `domain`: `POINT`, `EDGE`, `FACE`, `CORNER`, `CURVE`, `INSTANCE`
    #### Inputs:
    - `#0 value_float: Float = 0.0`
    - `#1 value_int: Integer = 0`
    - `#2 value_vector: Vector = (0.0, 0.0, 0.0)`
    - `#3 value_color: Color = (0.0, 0.0, 0.0, 0.0)`
    - `#4 value_bool: Boolean = False`
    #### Outputs:
    - `#0 value_float: Float = 0.0`
    - `#1 value_int: Integer = 0`
    - `#2 value_vector: Vector = (0.0, 0.0, 0.0)`
    - `#3 value_color: Color = (0.0, 0.0, 0.0, 0.0)`
    - `#4 value_bool: Boolean = False`
    """
    params_all = [('data_type', data_type, 'FLOAT'), ('domain', domain, 'POINT')]
    inputs_all = [(value_float, 0.0), (value_int, 0), (value_vector, (0.0, 0.0, 0.0)), (value_color, (0.0, 0.0, 0.0, 0.0)), (value_bool, False)]
    return "GeometryNodeFieldOnDomain", params_all, inputs_all


def FunctionNodeBooleanMath(operation='AND', boolean=False, boolean_001=False):
    """
    - `operation`: `AND`, `OR`, `NOT`, `NAND`, `NOR`, `XNOR`, `XOR`, `IMPLY`, `NIMPLY`
    #### Inputs:
    - `#0 boolean: Boolean = False`
    - `#1 boolean_001: Boolean = False`
    #### Outputs:
    - `#0 boolean: Boolean = False`
    """
    params_all = [('operation', operation, 'AND')]
    inputs_all = [(boolean, False), (boolean_001, False)]
    return "FunctionNodeBooleanMath", params_all, inputs_all


def ShaderNodeClamp(clamp_type='MINMAX', value=1.0, min=0.0, max=1.0):
    """
    - `clamp_type`: `MINMAX`, `RANGE`
    #### Inputs:
    - `#0 value: Float = 1.0`
    - `#1 min: Float = 0.0`
    - `#2 max: Float = 1.0`
    #### Outputs:
    - `#0 result: Float = 0.0`
    """
    params_all = [('clamp_type', clamp_type, 'MINMAX')]
    inputs_all = [(value, 1.0), (min, 0.0), (max, 1.0)]
    return "ShaderNodeClamp", params_all, inputs_all


def FunctionNodeCompare(data_type='FLOAT', mode='ELEMENT', operation='GREATER_THAN', a=0.0, b=0.0, a_int=0, b_int=0, a_vec3=(0.0, 0.0, 0.0), b_vec3=(0.0, 0.0, 0.0), a_col=(0.0, 0.0, 0.0, 0.0), b_col=(0.0, 0.0, 0.0, 0.0), a_str='', b_str='', c=0.9, angle=math.radians(5.0), epsilon=0.001):
    """
    - `data_type`: `FLOAT`, `INT`, `VECTOR`, `STRING`, `RGBA`
    - `mode`: `ELEMENT`, `LENGTH`, `AVERAGE`, `DOT_PRODUCT`, `DIRECTION`
    - `operation`: `GREATER_THAN`, `LESS_THAN`, `LESS_EQUAL`, `GREATER_EQUAL`, `EQUAL`, `NOT_EQUAL`
    #### Inputs:
    - `#0 a: Float = 0.0`
    - `#1 b: Float = 0.0`
    - `#2 a_int: Integer = 0`
    - `#3 b_int: Integer = 0`
    - `#4 a_vec3: Vector = (0.0, 0.0, 0.0)`
    - `#5 b_vec3: Vector = (0.0, 0.0, 0.0)`
    - `#6 a_col: Color = (0.0, 0.0, 0.0, 0.0)`
    - `#7 b_col: Color = (0.0, 0.0, 0.0, 0.0)`
    - `#8 a_str: String = ''`
    - `#9 b_str: String = ''`
    - `#10 c: Float = 0.9`
    - `#11 angle: Float = math.radians(5.0)`
    - `#12 epsilon: Float = 0.001`
    #### Outputs:
    - `#0 result: Boolean = False`
    """
    params_all = [('data_type', data_type, 'FLOAT'), ('mode', mode, 'ELEMENT'), ('operation', operation, 'GREATER_THAN')]
    inputs_all = [(a, 0.0), (b, 0.0), (a_int, 0), (b_int, 0), (a_vec3, (0.0, 0.0, 0.0)), (b_vec3, (0.0, 0.0, 0.0)), (a_col, (0.0, 0.0, 0.0, 0.0)), (b_col, (0.0, 0.0, 0.0, 0.0)), (a_str, ''), (b_str, ''), (c, 0.9), (angle, math.radians(5.0)), (epsilon, 0.001)]
    return "FunctionNodeCompare", params_all, inputs_all


def ShaderNodeFloatCurve(mapping=None, factor=1.0, value=1.0):
    """
    #### Inputs:
    - `#0 factor: Float = 1.0`
    - `#1 value: Float = 1.0`
    #### Outputs:
    - `#0 value: Float = 0.0`
    """
    params_all = [('mapping', mapping, None)]
    inputs_all = [(factor, 1.0), (value, 1.0)]
    return "ShaderNodeFloatCurve", params_all, inputs_all


def FunctionNodeFloatToInt(rounding_mode='ROUND', float=0.0):
    """
    - `rounding_mode`: `ROUND`, `FLOOR`, `CEILING`, `TRUNCATE`
    #### Inputs:
    - `#0 float: Float = 0.0`
    #### Outputs:
    - `#0 integer: Integer = 0`
    """
    params_all = [('rounding_mode', rounding_mode, 'ROUND')]
    inputs_all = [(float, 0.0)]
    return "FunctionNodeFloatToInt", params_all, inputs_all


def ShaderNodeMapRange(data_type='FLOAT', interpolation_type='LINEAR', clamp=True, value=1.0, from_min=0.0, from_max=1.0, to_min=0.0, to_max=1.0, steps=4.0, vector=(0.0, 0.0, 0.0), from_min_float3=(0.0, 0.0, 0.0), from_max_float3=(1.0, 1.0, 1.0), to_min_float3=(0.0, 0.0, 0.0), to_max_float3=(1.0, 1.0, 1.0), steps_float3=(4.0, 4.0, 4.0)):
    """
    - `data_type`: `FLOAT`, `FLOAT_VECTOR`
    - `interpolation_type`: `LINEAR`, `STEPPED`, `SMOOTHSTEP`, `SMOOTHERSTEP`
    #### Inputs:
    - `#0 value: Float = 1.0`
    - `#1 from_min: Float = 0.0`
    - `#2 from_max: Float = 1.0`
    - `#3 to_min: Float = 0.0`
    - `#4 to_max: Float = 1.0`
    - `#5 steps: Float = 4.0`
    - `#6 vector: Vector = (0.0, 0.0, 0.0)`
    - `#7 from_min_float3: Vector = (0.0, 0.0, 0.0)`
    - `#8 from_max_float3: Vector = (1.0, 1.0, 1.0)`
    - `#9 to_min_float3: Vector = (0.0, 0.0, 0.0)`
    - `#10 to_max_float3: Vector = (1.0, 1.0, 1.0)`
    - `#11 steps_float3: Vector = (4.0, 4.0, 4.0)`
    #### Outputs:
    - `#0 result: Float = 0.0`
    - `#1 vector: Vector = (0.0, 0.0, 0.0)`
    """
    params_all = [('data_type', data_type, 'FLOAT'), ('interpolation_type', interpolation_type, 'LINEAR'), ('clamp', clamp, True)]
    inputs_all = [(value, 1.0), (from_min, 0.0), (from_max, 1.0), (to_min, 0.0), (to_max, 1.0), (steps, 4.0), (vector, (0.0, 0.0, 0.0)), (from_min_float3, (0.0, 0.0, 0.0)), (from_max_float3, (1.0, 1.0, 1.0)), (to_min_float3, (0.0, 0.0, 0.0)), (to_max_float3, (1.0, 1.0, 1.0)), (steps_float3, (4.0, 4.0, 4.0))]
    return "ShaderNodeMapRange", params_all, inputs_all


def ShaderNodeMath(operation='ADD', use_clamp=False, value=0.5, value_001=0.5, value_002=0.5):
    """
    - `operation`: `ADD`, `SUBTRACT`, `MULTIPLY`, `DIVIDE`, `MULTIPLY_ADD`, `POWER`, `LOGARITHM`, `SQRT`, `INVERSE_SQRT`, `ABSOLUTE`, `EXPONENT`, `MINIMUM`, `MAXIMUM`, `LESS_THAN`, `GREATER_THAN`, `SIGN`, `COMPARE`, `SMOOTH_MIN`, `SMOOTH_MAX`, `ROUND`, `FLOOR`, `CEIL`, `TRUNC`, `FRACT`, `MODULO`, `WRAP`, `SNAP`, `PINGPONG`, `SINE`, `COSINE`, `TANGENT`, `ARCSINE`, `ARCCOSINE`, `ARCTANGENT`, `ARCTAN2`, `SINH`, `COSH`, `TANH`, `RADIANS`, `DEGREES`
    #### Inputs:
    - `#0 value: Float = 0.5`
    - `#1 value_001: Float = 0.5`
    - `#2 value_002: Float = 0.5`
    #### Outputs:
    - `#0 value: Float = 0.0`
    """
    params_all = [('operation', operation, 'ADD'), ('use_clamp', use_clamp, False)]
    inputs_all = [(value, 0.5), (value_001, 0.5), (value_002, 0.5)]
    return "ShaderNodeMath", params_all, inputs_all


def FunctionNodeAlignEulerToVector(axis='X', pivot_axis='AUTO', rotation=(0.0, 0.0, 0.0), factor=1.0, vector=(0.0, 0.0, 1.0)):
    """
    - `axis`: `X`, `Y`, `Z`
    - `pivot_axis`: `AUTO`, `X`, `Y`, `Z`
    #### Inputs:
    - `#0 rotation: Vector = (0.0, 0.0, 0.0)`
    - `#1 factor: Float = 1.0`
    - `#2 vector: Vector = (0.0, 0.0, 1.0)`
    #### Outputs:
    - `#0 rotation: Vector = (0.0, 0.0, 0.0)`
    """
    params_all = [('axis', axis, 'X'), ('pivot_axis', pivot_axis, 'AUTO')]
    inputs_all = [(rotation, (0.0, 0.0, 0.0)), (factor, 1.0), (vector, (0.0, 0.0, 1.0))]
    return "FunctionNodeAlignEulerToVector", params_all, inputs_all


def FunctionNodeRotateEuler(space='OBJECT', type='EULER', rotation=(0.0, 0.0, 0.0), rotate_by=(0.0, 0.0, 0.0), axis=(0.0, 0.0, 1.0), angle=math.radians(0.0)):
    """
    - `space`: `OBJECT`, `LOCAL`
    - `type`: `EULER`, `AXIS_ANGLE`
    #### Inputs:
    - `#0 rotation: Vector = (0.0, 0.0, 0.0)`
    - `#1 rotate_by: Vector = (0.0, 0.0, 0.0)`
    - `#2 axis: Vector = (0.0, 0.0, 1.0)`
    - `#3 angle: Float = math.radians(0.0)`
    #### Outputs:
    - `#0 rotation: Vector = (0.0, 0.0, 0.0)`
    """
    params_all = [('space', space, 'OBJECT'), ('type', type, 'EULER')]
    inputs_all = [(rotation, (0.0, 0.0, 0.0)), (rotate_by, (0.0, 0.0, 0.0)), (axis, (0.0, 0.0, 1.0)), (angle, math.radians(0.0))]
    return "FunctionNodeRotateEuler", params_all, inputs_all


def FunctionNodeRandomValue(data_type='FLOAT', min=(0.0, 0.0, 0.0), max=(1.0, 1.0, 1.0), min_001=0.0, max_001=1.0, min_002=0, max_002=100, probability=0.5, id=None, seed=0):
    """
    - `data_type`: `FLOAT`, `INT`, `FLOAT_VECTOR`, `BOOLEAN`
    #### Inputs:
    - `#0 min: Vector = (0.0, 0.0, 0.0)`
    - `#1 max: Vector = (1.0, 1.0, 1.0)`
    - `#2 min_001: Float = 0.0`
    - `#3 max_001: Float = 1.0`
    - `#4 min_002: Integer = 0`
    - `#5 max_002: Integer = 100`
    - `#6 probability: Float = 0.5`
    - `#7 id: Integer = 0`
    - `#8 seed: Integer = 0`
    #### Outputs:
    - `#0 value: Vector = (0.0, 0.0, 0.0)`
    - `#1 value_001: Float = 0.0`
    - `#2 value_002: Integer = 0`
    - `#3 value_003: Boolean = False`
    """
    params_all = [('data_type', data_type, 'FLOAT')]
    inputs_all = [(min, (0.0, 0.0, 0.0)), (max, (1.0, 1.0, 1.0)), (min_001, 0.0), (max_001, 1.0), (min_002, 0), (max_002, 100), (probability, 0.5), (id, None), (seed, 0)]
    return "FunctionNodeRandomValue", params_all, inputs_all


def GeometryNodeSwitch(input_type='GEOMETRY', switch=False, switch_001=False, false=0.0, true=0.0, false_001=0, true_001=0, false_002=False, true_002=True, false_003=(0.0, 0.0, 0.0), true_003=(0.0, 0.0, 0.0), false_004=(0.8, 0.8, 0.8, 1.0), true_004=(0.8, 0.8, 0.8, 1.0), false_005='', true_005='', false_006=None, true_006=None, false_007=None, true_007=None, false_008=None, true_008=None, false_009=None, true_009=None, false_010=None, true_010=None, false_011=None, true_011=None):
    """
    - `input_type`: `GEOMETRY`, `FLOAT`, `INT`, `BOOLEAN`, `VECTOR`, `STRING`, `RGBA`, `OBJECT`, `IMAGE`, `COLLECTION`, `TEXTURE`, `MATERIAL`
    #### Inputs:
    - `#0 switch: Boolean = False`
    - `#1 switch_001: Boolean = False`
    - `#2 false: Float = 0.0`
    - `#3 true: Float = 0.0`
    - `#4 false_001: Integer = 0`
    - `#5 true_001: Integer = 0`
    - `#6 false_002: Boolean = False`
    - `#7 true_002: Boolean = True`
    - `#8 false_003: Vector = (0.0, 0.0, 0.0)`
    - `#9 true_003: Vector = (0.0, 0.0, 0.0)`
    - `#10 false_004: Color = (0.8, 0.8, 0.8, 1.0)`
    - `#11 true_004: Color = (0.8, 0.8, 0.8, 1.0)`
    - `#12 false_005: String = ''`
    - `#13 true_005: String = ''`
    - `#14 false_006: Geometry = None`
    - `#15 true_006: Geometry = None`
    - `#16 false_007: Object = None`
    - `#17 true_007: Object = None`
    - `#18 false_008: Collection = None`
    - `#19 true_008: Collection = None`
    - `#20 false_009: Texture = None`
    - `#21 true_009: Texture = None`
    - `#22 false_010: Material = None`
    - `#23 true_010: Material = None`
    - `#24 false_011: Image = None`
    - `#25 true_011: Image = None`
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
    """
    params_all = [('input_type', input_type, 'GEOMETRY')]
    inputs_all = [(switch, False), (switch_001, False), (false, 0.0), (true, 0.0), (false_001, 0), (true_001, 0), (false_002, False), (true_002, True), (false_003, (0.0, 0.0, 0.0)), (true_003, (0.0, 0.0, 0.0)), (false_004, (0.8, 0.8, 0.8, 1.0)), (true_004, (0.8, 0.8, 0.8, 1.0)), (false_005, ''), (true_005, ''), (false_006, None), (true_006, None), (false_007, None), (true_007, None), (false_008, None), (true_008, None), (false_009, None), (true_009, None), (false_010, None), (true_010, None), (false_011, None), (true_011, None)]
    return "GeometryNodeSwitch", params_all, inputs_all


def ShaderNodeAmbientOcclusion(inside=False, only_local=False, samples=16, color=(1.0, 1.0, 1.0, 1.0), distance=1.0, normal=(0.0, 0.0, 0.0)):
    """
    #### Inputs:
    - `#0 color: Color = (1.0, 1.0, 1.0, 1.0)`
    - `#1 distance: Float = 1.0`
    - `#2 normal: Vector = (0.0, 0.0, 0.0)`
    #### Outputs:
    - `#0 color: Color = (0.0, 0.0, 0.0, 0.0)`
    - `#1 ao: Float = 0.0`
    """
    params_all = [('inside', inside, False), ('only_local', only_local, False), ('samples', samples, 16)]
    inputs_all = [(color, (1.0, 1.0, 1.0, 1.0)), (distance, 1.0), (normal, (0.0, 0.0, 0.0))]
    return "ShaderNodeAmbientOcclusion", params_all, inputs_all


def ShaderNodeAttribute(attribute_type='GEOMETRY', attribute_name=''):
    """
    - `attribute_type`: `GEOMETRY`, `OBJECT`, `INSTANCER`, `VIEW_LAYER`
    #### Outputs:
    - `#0 color: Color = (0.0, 0.0, 0.0, 0.0)`
    - `#1 vector: Vector = (0.0, 0.0, 0.0)`
    - `#2 fac: Float = 0.0`
    - `#3 alpha: Float = 0.0`
    """
    params_all = [('attribute_type', attribute_type, 'GEOMETRY'), ('attribute_name', attribute_name, '')]
    inputs_all = []
    return "ShaderNodeAttribute", params_all, inputs_all


def ShaderNodeBevel(samples=4, radius=0.05, normal=(0.0, 0.0, 0.0)):
    """
    #### Inputs:
    - `#0 radius: Float = 0.05`
    - `#1 normal: Vector = (0.0, 0.0, 0.0)`
    #### Outputs:
    - `#0 normal: Vector = (0.0, 0.0, 0.0)`
    """
    params_all = [('samples', samples, 4)]
    inputs_all = [(radius, 0.05), (normal, (0.0, 0.0, 0.0))]
    return "ShaderNodeBevel", params_all, inputs_all


def ShaderNodeCameraData():
    """
    #### Outputs:
    - `#0 view_vector: Vector = (0.0, 0.0, 0.0)`
    - `#1 view_z_depth: Float = 0.0`
    - `#2 view_distance: Float = 0.0`
    """
    params_all = []
    inputs_all = []
    return "ShaderNodeCameraData", params_all, inputs_all


def ShaderNodeFresnel(ior=1.45, normal=(0.0, 0.0, 0.0)):
    """
    #### Inputs:
    - `#0 ior: Float = 1.45`
    - `#1 normal: Vector = (0.0, 0.0, 0.0)`
    #### Outputs:
    - `#0 fac: Float = 0.0`
    """
    params_all = []
    inputs_all = [(ior, 1.45), (normal, (0.0, 0.0, 0.0))]
    return "ShaderNodeFresnel", params_all, inputs_all


def ShaderNodeNewGeometry():
    """
    #### Outputs:
    - `#0 position: Vector = (0.0, 0.0, 0.0)`
    - `#1 normal: Vector = (0.0, 0.0, 0.0)`
    - `#2 tangent: Vector = (0.0, 0.0, 0.0)`
    - `#3 true_normal: Vector = (0.0, 0.0, 0.0)`
    - `#4 incoming: Vector = (0.0, 0.0, 0.0)`
    - `#5 parametric: Vector = (0.0, 0.0, 0.0)`
    - `#6 backfacing: Float = 0.0`
    - `#7 pointiness: Float = 0.0`
    - `#8 random_per_island: Float = 0.0`
    """
    params_all = []
    inputs_all = []
    return "ShaderNodeNewGeometry", params_all, inputs_all


def ShaderNodeHairInfo():
    """
    #### Outputs:
    - `#0 is_strand: Float = 0.0`
    - `#1 intercept: Float = 0.0`
    - `#2 length: Float = 0.0`
    - `#3 thickness: Float = 0.0`
    - `#4 tangent_normal: Vector = (0.0, 0.0, 0.0)`
    - `#5 random: Float = 0.0`
    """
    params_all = []
    inputs_all = []
    return "ShaderNodeHairInfo", params_all, inputs_all


def ShaderNodeLayerWeight(blend=0.5, normal=(0.0, 0.0, 0.0)):
    """
    #### Inputs:
    - `#0 blend: Float = 0.5`
    - `#1 normal: Vector = (0.0, 0.0, 0.0)`
    #### Outputs:
    - `#0 fresnel: Float = 0.0`
    - `#1 facing: Float = 0.0`
    """
    params_all = []
    inputs_all = [(blend, 0.5), (normal, (0.0, 0.0, 0.0))]
    return "ShaderNodeLayerWeight", params_all, inputs_all


def ShaderNodeLightPath():
    """
    #### Outputs:
    - `#0 is_camera_ray: Float = 0.0`
    - `#1 is_shadow_ray: Float = 0.0`
    - `#2 is_diffuse_ray: Float = 0.0`
    - `#3 is_glossy_ray: Float = 0.0`
    - `#4 is_singular_ray: Float = 0.0`
    - `#5 is_reflection_ray: Float = 0.0`
    - `#6 is_transmission_ray: Float = 0.0`
    - `#7 ray_length: Float = 0.0`
    - `#8 ray_depth: Float = 0.0`
    - `#9 diffuse_depth: Float = 0.0`
    - `#10 glossy_depth: Float = 0.0`
    - `#11 transparent_depth: Float = 0.0`
    - `#12 transmission_depth: Float = 0.0`
    """
    params_all = []
    inputs_all = []
    return "ShaderNodeLightPath", params_all, inputs_all


def ShaderNodeObjectInfo():
    """
    #### Outputs:
    - `#0 location: Vector = (0.0, 0.0, 0.0)`
    - `#1 color: Color = (0.0, 0.0, 0.0, 0.0)`
    - `#2 alpha: Float = 0.0`
    - `#3 object_index: Float = 0.0`
    - `#4 material_index: Float = 0.0`
    - `#5 random: Float = 0.0`
    """
    params_all = []
    inputs_all = []
    return "ShaderNodeObjectInfo", params_all, inputs_all


def ShaderNodeParticleInfo():
    """
    #### Outputs:
    - `#0 index: Float = 0.0`
    - `#1 random: Float = 0.0`
    - `#2 age: Float = 0.0`
    - `#3 lifetime: Float = 0.0`
    - `#4 location: Vector = (0.0, 0.0, 0.0)`
    - `#5 size: Float = 0.0`
    - `#6 velocity: Vector = (0.0, 0.0, 0.0)`
    - `#7 angular_velocity: Vector = (0.0, 0.0, 0.0)`
    """
    params_all = []
    inputs_all = []
    return "ShaderNodeParticleInfo", params_all, inputs_all


def ShaderNodePointInfo():
    """
    #### Outputs:
    - `#0 position: Vector = (0.0, 0.0, 0.0)`
    - `#1 radius: Float = 0.0`
    - `#2 random: Float = 0.0`
    """
    params_all = []
    inputs_all = []
    return "ShaderNodePointInfo", params_all, inputs_all


def ShaderNodeRGB():
    """
    #### Outputs:
    - `#0 color: Color = (0.5, 0.5, 0.5, 1.0)`
    """
    params_all = []
    inputs_all = []
    return "ShaderNodeRGB", params_all, inputs_all


def ShaderNodeTangent(axis='Z', direction_type='RADIAL', uv_map=''):
    """
    - `axis`: `Z`, `X`, `Y`
    - `direction_type`: `RADIAL`, `UV_MAP`
    #### Outputs:
    - `#0 tangent: Vector = (0.0, 0.0, 0.0)`
    """
    params_all = [('axis', axis, 'Z'), ('direction_type', direction_type, 'RADIAL'), ('uv_map', uv_map, '')]
    inputs_all = []
    return "ShaderNodeTangent", params_all, inputs_all


def ShaderNodeTexCoord(from_instancer=False, object=None):
    """
    #### Outputs:
    - `#0 generated: Vector = (0.0, 0.0, 0.0)`
    - `#1 normal: Vector = (0.0, 0.0, 0.0)`
    - `#2 uv: Vector = (0.0, 0.0, 0.0)`
    - `#3 object: Vector = (0.0, 0.0, 0.0)`
    - `#4 camera: Vector = (0.0, 0.0, 0.0)`
    - `#5 window: Vector = (0.0, 0.0, 0.0)`
    - `#6 reflection: Vector = (0.0, 0.0, 0.0)`
    """
    params_all = [('from_instancer', from_instancer, False), ('object', object, None)]
    inputs_all = []
    return "ShaderNodeTexCoord", params_all, inputs_all


def ShaderNodeUVMap(from_instancer=False, uv_map=''):
    """
    #### Outputs:
    - `#0 uv: Vector = (0.0, 0.0, 0.0)`
    """
    params_all = [('from_instancer', from_instancer, False), ('uv_map', uv_map, '')]
    inputs_all = []
    return "ShaderNodeUVMap", params_all, inputs_all


def ShaderNodeVertexColor(layer_name=''):
    """
    #### Outputs:
    - `#0 color: Color = (0.0, 0.0, 0.0, 0.0)`
    - `#1 alpha: Float = 0.0`
    """
    params_all = [('layer_name', layer_name, '')]
    inputs_all = []
    return "ShaderNodeVertexColor", params_all, inputs_all


def ShaderNodeVolumeInfo():
    """
    #### Outputs:
    - `#0 color: Color = (0.0, 0.0, 0.0, 0.0)`
    - `#1 density: Float = 0.0`
    - `#2 flame: Float = 0.0`
    - `#3 temperature: Float = 0.0`
    """
    params_all = []
    inputs_all = []
    return "ShaderNodeVolumeInfo", params_all, inputs_all


def ShaderNodeWireframe(use_pixel_size=False, size=0.01):
    """
    #### Inputs:
    - `#0 size: Float = 0.01`
    #### Outputs:
    - `#0 fac: Float = 0.0`
    """
    params_all = [('use_pixel_size', use_pixel_size, False)]
    inputs_all = [(size, 0.01)]
    return "ShaderNodeWireframe", params_all, inputs_all


def ShaderNodeOutputAOV(color=(0.0, 0.0, 0.0, 1.0), value=0.0):
    """
    #### Inputs:
    - `#0 color: Color = (0.0, 0.0, 0.0, 1.0)`
    - `#1 value: Float = 0.0`
    """
    params_all = []
    inputs_all = [(color, (0.0, 0.0, 0.0, 1.0)), (value, 0.0)]
    return "ShaderNodeOutputAOV", params_all, inputs_all


def ShaderNodeOutputMaterial(target='ALL', is_active_output=True, surface=None, volume=None, displacement=(0.0, 0.0, 0.0), thickness=0.0):
    """
    - `target`: `ALL`, `EEVEE`, `CYCLES`
    #### Inputs:
    - `#0 surface: Shader = None`
    - `#1 volume: Shader = None`
    - `#2 displacement: Vector = (0.0, 0.0, 0.0)`
    - `#3 thickness: Float = 0.0`
    """
    params_all = [('target', target, 'ALL'), ('is_active_output', is_active_output, True)]
    inputs_all = [(surface, None), (volume, None), (displacement, (0.0, 0.0, 0.0)), (thickness, 0.0)]
    return "ShaderNodeOutputMaterial", params_all, inputs_all


def ShaderNodeOutputLight(target='ALL', is_active_output=True, surface=None):
    """
    - `target`: `ALL`, `EEVEE`, `CYCLES`
    #### Inputs:
    - `#0 surface: Shader = None`
    """
    params_all = [('target', target, 'ALL'), ('is_active_output', is_active_output, True)]
    inputs_all = [(surface, None)]
    return "ShaderNodeOutputLight", params_all, inputs_all


def ShaderNodeOutputWorld(target='ALL', is_active_output=True, surface=None, volume=None):
    """
    - `target`: `ALL`, `EEVEE`, `CYCLES`
    #### Inputs:
    - `#0 surface: Shader = None`
    - `#1 volume: Shader = None`
    """
    params_all = [('target', target, 'ALL'), ('is_active_output', is_active_output, True)]
    inputs_all = [(surface, None), (volume, None)]
    return "ShaderNodeOutputWorld", params_all, inputs_all


def ShaderNodeAddShader(shader=None, shader_001=None):
    """
    #### Inputs:
    - `#0 shader: Shader = None`
    - `#1 shader_001: Shader = None`
    #### Outputs:
    - `#0 shader: Shader = None`
    """
    params_all = []
    inputs_all = [(shader, None), (shader_001, None)]
    return "ShaderNodeAddShader", params_all, inputs_all


def ShaderNodeBsdfAnisotropic(distribution='GGX', color=(0.8, 0.8, 0.8, 1.0), roughness=0.5, anisotropy=0.5, rotation=0.0, normal=(0.0, 0.0, 0.0), tangent=(0.0, 0.0, 0.0), weight=0.0):
    """
    - `distribution`: `GGX`, `BECKMANN`, `MULTI_GGX`, `ASHIKHMIN_SHIRLEY`
    #### Inputs:
    - `#0 color: Color = (0.8, 0.8, 0.8, 1.0)`
    - `#1 roughness: Float = 0.5`
    - `#2 anisotropy: Float = 0.5`
    - `#3 rotation: Float = 0.0`
    - `#4 normal: Vector = (0.0, 0.0, 0.0)`
    - `#5 tangent: Vector = (0.0, 0.0, 0.0)`
    - `#6 weight: Float = 0.0`
    #### Outputs:
    - `#0 bsdf: Shader = None`
    """
    params_all = [('distribution', distribution, 'GGX')]
    inputs_all = [(color, (0.8, 0.8, 0.8, 1.0)), (roughness, 0.5), (anisotropy, 0.5), (rotation, 0.0), (normal, (0.0, 0.0, 0.0)), (tangent, (0.0, 0.0, 0.0)), (weight, 0.0)]
    return "ShaderNodeBsdfAnisotropic", params_all, inputs_all


def ShaderNodeBackground(color=(0.8, 0.8, 0.8, 1.0), strength=1.0, weight=0.0):
    """
    #### Inputs:
    - `#0 color: Color = (0.8, 0.8, 0.8, 1.0)`
    - `#1 strength: Float = 1.0`
    - `#2 weight: Float = 0.0`
    #### Outputs:
    - `#0 background: Shader = None`
    """
    params_all = []
    inputs_all = [(color, (0.8, 0.8, 0.8, 1.0)), (strength, 1.0), (weight, 0.0)]
    return "ShaderNodeBackground", params_all, inputs_all


def ShaderNodeBsdfDiffuse(color=(0.8, 0.8, 0.8, 1.0), roughness=0.0, normal=(0.0, 0.0, 0.0), weight=0.0):
    """
    #### Inputs:
    - `#0 color: Color = (0.8, 0.8, 0.8, 1.0)`
    - `#1 roughness: Float = 0.0`
    - `#2 normal: Vector = (0.0, 0.0, 0.0)`
    - `#3 weight: Float = 0.0`
    #### Outputs:
    - `#0 bsdf: Shader = None`
    """
    params_all = []
    inputs_all = [(color, (0.8, 0.8, 0.8, 1.0)), (roughness, 0.0), (normal, (0.0, 0.0, 0.0)), (weight, 0.0)]
    return "ShaderNodeBsdfDiffuse", params_all, inputs_all


def ShaderNodeEmission(color=(1.0, 1.0, 1.0, 1.0), strength=1.0, weight=0.0):
    """
    #### Inputs:
    - `#0 color: Color = (1.0, 1.0, 1.0, 1.0)`
    - `#1 strength: Float = 1.0`
    - `#2 weight: Float = 0.0`
    #### Outputs:
    - `#0 emission: Shader = None`
    """
    params_all = []
    inputs_all = [(color, (1.0, 1.0, 1.0, 1.0)), (strength, 1.0), (weight, 0.0)]
    return "ShaderNodeEmission", params_all, inputs_all


def ShaderNodeBsdfGlass(distribution='BECKMANN', color=(1.0, 1.0, 1.0, 1.0), roughness=0.0, ior=1.45, normal=(0.0, 0.0, 0.0), weight=0.0):
    """
    - `distribution`: `BECKMANN`, `SHARP`, `GGX`, `MULTI_GGX`
    #### Inputs:
    - `#0 color: Color = (1.0, 1.0, 1.0, 1.0)`
    - `#1 roughness: Float = 0.0`
    - `#2 ior: Float = 1.45`
    - `#3 normal: Vector = (0.0, 0.0, 0.0)`
    - `#4 weight: Float = 0.0`
    #### Outputs:
    - `#0 bsdf: Shader = None`
    """
    params_all = [('distribution', distribution, 'BECKMANN')]
    inputs_all = [(color, (1.0, 1.0, 1.0, 1.0)), (roughness, 0.0), (ior, 1.45), (normal, (0.0, 0.0, 0.0)), (weight, 0.0)]
    return "ShaderNodeBsdfGlass", params_all, inputs_all


def ShaderNodeBsdfGlossy(distribution='GGX', color=(0.8, 0.8, 0.8, 1.0), roughness=0.5, normal=(0.0, 0.0, 0.0), weight=0.0):
    """
    - `distribution`: `GGX`, `SHARP`, `BECKMANN`, `ASHIKHMIN_SHIRLEY`, `MULTI_GGX`
    #### Inputs:
    - `#0 color: Color = (0.8, 0.8, 0.8, 1.0)`
    - `#1 roughness: Float = 0.5`
    - `#2 normal: Vector = (0.0, 0.0, 0.0)`
    - `#3 weight: Float = 0.0`
    #### Outputs:
    - `#0 bsdf: Shader = None`
    """
    params_all = [('distribution', distribution, 'GGX')]
    inputs_all = [(color, (0.8, 0.8, 0.8, 1.0)), (roughness, 0.5), (normal, (0.0, 0.0, 0.0)), (weight, 0.0)]
    return "ShaderNodeBsdfGlossy", params_all, inputs_all


def ShaderNodeBsdfHair(component='Reflection', color=(0.8, 0.8, 0.8, 1.0), offset=math.radians(0.0), roughnessu=0.1, roughnessv=1.0, tangent=(0.0, 0.0, 0.0), weight=0.0):
    """
    - `component`: `Reflection`, `Transmission`
    #### Inputs:
    - `#0 color: Color = (0.8, 0.8, 0.8, 1.0)`
    - `#1 offset: Float = math.radians(0.0)`
    - `#2 roughnessu: Float = 0.1`
    - `#3 roughnessv: Float = 1.0`
    - `#4 tangent: Vector = (0.0, 0.0, 0.0)`
    - `#5 weight: Float = 0.0`
    #### Outputs:
    - `#0 bsdf: Shader = None`
    """
    params_all = [('component', component, 'Reflection')]
    inputs_all = [(color, (0.8, 0.8, 0.8, 1.0)), (offset, math.radians(0.0)), (roughnessu, 0.1), (roughnessv, 1.0), (tangent, (0.0, 0.0, 0.0)), (weight, 0.0)]
    return "ShaderNodeBsdfHair", params_all, inputs_all


def ShaderNodeHoldout(weight=0.0):
    """
    #### Inputs:
    - `#0 weight: Float = 0.0`
    #### Outputs:
    - `#0 holdout: Shader = None`
    """
    params_all = []
    inputs_all = [(weight, 0.0)]
    return "ShaderNodeHoldout", params_all, inputs_all


def ShaderNodeMixShader(fac=0.5, shader=None, shader_001=None):
    """
    #### Inputs:
    - `#0 fac: Float = 0.5`
    - `#1 shader: Shader = None`
    - `#2 shader_001: Shader = None`
    #### Outputs:
    - `#0 shader: Shader = None`
    """
    params_all = []
    inputs_all = [(fac, 0.5), (shader, None), (shader_001, None)]
    return "ShaderNodeMixShader", params_all, inputs_all


def ShaderNodeBsdfPrincipled(distribution='GGX', subsurface_method='RANDOM_WALK', base_color=(0.8, 0.8, 0.8, 1.0), subsurface=0.0, subsurface_radius=(1.0, 0.2, 0.1), subsurface_color=(0.8, 0.8, 0.8, 1.0), subsurface_ior=1.4, subsurface_anisotropy=0.0, metallic=0.0, specular=0.5, specular_tint=0.0, roughness=0.5, anisotropic=0.0, anisotropic_rotation=0.0, sheen=0.0, sheen_tint=0.5, clearcoat=0.0, clearcoat_roughness=0.03, ior=1.45, transmission=0.0, transmission_roughness=0.0, emission=(0.0, 0.0, 0.0, 1.0), emission_strength=1.0, alpha=1.0, normal=(0.0, 0.0, 0.0), clearcoat_normal=(0.0, 0.0, 0.0), tangent=(0.0, 0.0, 0.0), weight=0.0):
    """
    - `distribution`: `GGX`, `MULTI_GGX`
    - `subsurface_method`: `RANDOM_WALK`, `BURLEY`, `RANDOM_WALK_FIXED_RADIUS`
    #### Inputs:
    - `#0 base_color: Color = (0.8, 0.8, 0.8, 1.0)`
    - `#1 subsurface: Float = 0.0`
    - `#2 subsurface_radius: Vector = (1.0, 0.2, 0.1)`
    - `#3 subsurface_color: Color = (0.8, 0.8, 0.8, 1.0)`
    - `#4 subsurface_ior: Float = 1.4`
    - `#5 subsurface_anisotropy: Float = 0.0`
    - `#6 metallic: Float = 0.0`
    - `#7 specular: Float = 0.5`
    - `#8 specular_tint: Float = 0.0`
    - `#9 roughness: Float = 0.5`
    - `#10 anisotropic: Float = 0.0`
    - `#11 anisotropic_rotation: Float = 0.0`
    - `#12 sheen: Float = 0.0`
    - `#13 sheen_tint: Float = 0.5`
    - `#14 clearcoat: Float = 0.0`
    - `#15 clearcoat_roughness: Float = 0.03`
    - `#16 ior: Float = 1.45`
    - `#17 transmission: Float = 0.0`
    - `#18 transmission_roughness: Float = 0.0`
    - `#19 emission: Color = (0.0, 0.0, 0.0, 1.0)`
    - `#20 emission_strength: Float = 1.0`
    - `#21 alpha: Float = 1.0`
    - `#22 normal: Vector = (0.0, 0.0, 0.0)`
    - `#23 clearcoat_normal: Vector = (0.0, 0.0, 0.0)`
    - `#24 tangent: Vector = (0.0, 0.0, 0.0)`
    - `#25 weight: Float = 0.0`
    #### Outputs:
    - `#0 bsdf: Shader = None`
    """
    params_all = [('distribution', distribution, 'GGX'), ('subsurface_method', subsurface_method, 'RANDOM_WALK')]
    inputs_all = [(base_color, (0.8, 0.8, 0.8, 1.0)), (subsurface, 0.0), (subsurface_radius, (1.0, 0.2, 0.1)), (subsurface_color, (0.8, 0.8, 0.8, 1.0)), (subsurface_ior, 1.4), (subsurface_anisotropy, 0.0), (metallic, 0.0), (specular, 0.5), (specular_tint, 0.0), (roughness, 0.5), (anisotropic, 0.0), (anisotropic_rotation, 0.0), (sheen, 0.0),
                  (sheen_tint, 0.5), (clearcoat, 0.0), (clearcoat_roughness, 0.03), (ior, 1.45), (transmission, 0.0), (transmission_roughness, 0.0), (emission, (0.0, 0.0, 0.0, 1.0)), (emission_strength, 1.0), (alpha, 1.0), (normal, (0.0, 0.0, 0.0)), (clearcoat_normal, (0.0, 0.0, 0.0)), (tangent, (0.0, 0.0, 0.0)), (weight, 0.0)]
    return "ShaderNodeBsdfPrincipled", params_all, inputs_all


def ShaderNodeBsdfHairPrincipled(parametrization='COLOR', color=(0.018, 0.006, 0.002, 1.0), melanin=0.8, melanin_redness=1.0, tint=(1.0, 1.0, 1.0, 1.0), absorption_coefficient=(0.246, 0.52, 1.365), roughness=0.3, radial_roughness=0.3, coat=0.0, ior=1.55, offset=math.radians(2.0), random_color=0.0, random_roughness=0.0, random=0.0, weight=0.0):
    """
    - `parametrization`: `COLOR`, `ABSORPTION`, `MELANIN`
    #### Inputs:
    - `#0 color: Color = (0.018, 0.006, 0.002, 1.0)`
    - `#1 melanin: Float = 0.8`
    - `#2 melanin_redness: Float = 1.0`
    - `#3 tint: Color = (1.0, 1.0, 1.0, 1.0)`
    - `#4 absorption_coefficient: Vector = (0.246, 0.52, 1.365)`
    - `#5 roughness: Float = 0.3`
    - `#6 radial_roughness: Float = 0.3`
    - `#7 coat: Float = 0.0`
    - `#8 ior: Float = 1.55`
    - `#9 offset: Float = math.radians(2.0)`
    - `#10 random_color: Float = 0.0`
    - `#11 random_roughness: Float = 0.0`
    - `#12 random: Float = 0.0`
    - `#13 weight: Float = 0.0`
    #### Outputs:
    - `#0 bsdf: Shader = None`
    """
    params_all = [('parametrization', parametrization, 'COLOR')]
    inputs_all = [(color, (0.018, 0.006, 0.002, 1.0)), (melanin, 0.8), (melanin_redness, 1.0), (tint, (1.0, 1.0, 1.0, 1.0)), (absorption_coefficient, (0.246, 0.52, 1.365)), (roughness, 0.3), (radial_roughness, 0.3), (coat, 0.0), (ior, 1.55), (offset, math.radians(2.0)), (random_color, 0.0), (random_roughness, 0.0), (random, 0.0), (weight, 0.0)]
    return "ShaderNodeBsdfHairPrincipled", params_all, inputs_all


def ShaderNodeVolumePrincipled(color=(0.5, 0.5, 0.5, 1.0), color_attribute='', density=1.0, density_attribute='density', anisotropy=0.0, absorption_color=(0.0, 0.0, 0.0, 1.0), emission_strength=0.0, emission_color=(1.0, 1.0, 1.0, 1.0), blackbody_intensity=0.0, blackbody_tint=(1.0, 1.0, 1.0, 1.0), temperature=1000.0, temperature_attribute='temperature', weight=0.0):
    """
    #### Inputs:
    - `#0 color: Color = (0.5, 0.5, 0.5, 1.0)`
    - `#1 color_attribute: String = ''`
    - `#2 density: Float = 1.0`
    - `#3 density_attribute: String = 'density'`
    - `#4 anisotropy: Float = 0.0`
    - `#5 absorption_color: Color = (0.0, 0.0, 0.0, 1.0)`
    - `#6 emission_strength: Float = 0.0`
    - `#7 emission_color: Color = (1.0, 1.0, 1.0, 1.0)`
    - `#8 blackbody_intensity: Float = 0.0`
    - `#9 blackbody_tint: Color = (1.0, 1.0, 1.0, 1.0)`
    - `#10 temperature: Float = 1000.0`
    - `#11 temperature_attribute: String = 'temperature'`
    - `#12 weight: Float = 0.0`
    #### Outputs:
    - `#0 volume: Shader = None`
    """
    params_all = []
    inputs_all = [(color, (0.5, 0.5, 0.5, 1.0)), (color_attribute, ''), (density, 1.0), (density_attribute, 'density'), (anisotropy, 0.0), (absorption_color, (0.0, 0.0, 0.0, 1.0)), (emission_strength, 0.0), (emission_color, (1.0, 1.0, 1.0, 1.0)), (blackbody_intensity, 0.0), (blackbody_tint, (1.0, 1.0, 1.0, 1.0)), (temperature, 1000.0), (temperature_attribute, 'temperature'), (weight, 0.0)]
    return "ShaderNodeVolumePrincipled", params_all, inputs_all


def ShaderNodeBsdfRefraction(distribution='BECKMANN', color=(1.0, 1.0, 1.0, 1.0), roughness=0.0, ior=1.45, normal=(0.0, 0.0, 0.0), weight=0.0):
    """
    - `distribution`: `BECKMANN`, `SHARP`, `GGX`
    #### Inputs:
    - `#0 color: Color = (1.0, 1.0, 1.0, 1.0)`
    - `#1 roughness: Float = 0.0`
    - `#2 ior: Float = 1.45`
    - `#3 normal: Vector = (0.0, 0.0, 0.0)`
    - `#4 weight: Float = 0.0`
    #### Outputs:
    - `#0 bsdf: Shader = None`
    """
    params_all = [('distribution', distribution, 'BECKMANN')]
    inputs_all = [(color, (1.0, 1.0, 1.0, 1.0)), (roughness, 0.0), (ior, 1.45), (normal, (0.0, 0.0, 0.0)), (weight, 0.0)]
    return "ShaderNodeBsdfRefraction", params_all, inputs_all


def ShaderNodeEeveeSpecular(base_color=(0.8, 0.8, 0.8, 1.0), specular=(0.03, 0.03, 0.03, 1.0), roughness=0.2, emissive_color=(0.0, 0.0, 0.0, 1.0), transparency=0.0, normal=(0.0, 0.0, 0.0), clear_coat=0.0, clear_coat_roughness=0.0, clear_coat_normal=(0.0, 0.0, 0.0), ambient_occlusion=0.0, weight=0.0):
    """
    #### Inputs:
    - `#0 base_color: Color = (0.8, 0.8, 0.8, 1.0)`
    - `#1 specular: Color = (0.03, 0.03, 0.03, 1.0)`
    - `#2 roughness: Float = 0.2`
    - `#3 emissive_color: Color = (0.0, 0.0, 0.0, 1.0)`
    - `#4 transparency: Float = 0.0`
    - `#5 normal: Vector = (0.0, 0.0, 0.0)`
    - `#6 clear_coat: Float = 0.0`
    - `#7 clear_coat_roughness: Float = 0.0`
    - `#8 clear_coat_normal: Vector = (0.0, 0.0, 0.0)`
    - `#9 ambient_occlusion: Float = 0.0`
    - `#10 weight: Float = 0.0`
    #### Outputs:
    - `#0 bsdf: Shader = None`
    """
    params_all = []
    inputs_all = [(base_color, (0.8, 0.8, 0.8, 1.0)), (specular, (0.03, 0.03, 0.03, 1.0)), (roughness, 0.2), (emissive_color, (0.0, 0.0, 0.0, 1.0)), (transparency, 0.0), (normal, (0.0, 0.0, 0.0)), (clear_coat, 0.0), (clear_coat_roughness, 0.0), (clear_coat_normal, (0.0, 0.0, 0.0)), (ambient_occlusion, 0.0), (weight, 0.0)]
    return "ShaderNodeEeveeSpecular", params_all, inputs_all


def ShaderNodeSubsurfaceScattering(falloff='RANDOM_WALK', color=(0.8, 0.8, 0.8, 1.0), scale=1.0, radius=(1.0, 0.2, 0.1), ior=1.4, anisotropy=0.0, normal=(0.0, 0.0, 0.0), weight=0.0):
    """
    - `falloff`: `RANDOM_WALK`, `BURLEY`, `RANDOM_WALK_FIXED_RADIUS`
    #### Inputs:
    - `#0 color: Color = (0.8, 0.8, 0.8, 1.0)`
    - `#1 scale: Float = 1.0`
    - `#2 radius: Vector = (1.0, 0.2, 0.1)`
    - `#3 ior: Float = 1.4`
    - `#4 anisotropy: Float = 0.0`
    - `#5 normal: Vector = (0.0, 0.0, 0.0)`
    - `#6 weight: Float = 0.0`
    #### Outputs:
    - `#0 bssrdf: Shader = None`
    """
    params_all = [('falloff', falloff, 'RANDOM_WALK')]
    inputs_all = [(color, (0.8, 0.8, 0.8, 1.0)), (scale, 1.0), (radius, (1.0, 0.2, 0.1)), (ior, 1.4), (anisotropy, 0.0), (normal, (0.0, 0.0, 0.0)), (weight, 0.0)]
    return "ShaderNodeSubsurfaceScattering", params_all, inputs_all


def ShaderNodeBsdfToon(component='DIFFUSE', color=(0.8, 0.8, 0.8, 1.0), size=0.5, smooth=0.0, normal=(0.0, 0.0, 0.0), weight=0.0):
    """
    - `component`: `DIFFUSE`, `GLOSSY`
    #### Inputs:
    - `#0 color: Color = (0.8, 0.8, 0.8, 1.0)`
    - `#1 size: Float = 0.5`
    - `#2 smooth: Float = 0.0`
    - `#3 normal: Vector = (0.0, 0.0, 0.0)`
    - `#4 weight: Float = 0.0`
    #### Outputs:
    - `#0 bsdf: Shader = None`
    """
    params_all = [('component', component, 'DIFFUSE')]
    inputs_all = [(color, (0.8, 0.8, 0.8, 1.0)), (size, 0.5), (smooth, 0.0), (normal, (0.0, 0.0, 0.0)), (weight, 0.0)]
    return "ShaderNodeBsdfToon", params_all, inputs_all


def ShaderNodeBsdfTranslucent(color=(0.8, 0.8, 0.8, 1.0), normal=(0.0, 0.0, 0.0), weight=0.0):
    """
    #### Inputs:
    - `#0 color: Color = (0.8, 0.8, 0.8, 1.0)`
    - `#1 normal: Vector = (0.0, 0.0, 0.0)`
    - `#2 weight: Float = 0.0`
    #### Outputs:
    - `#0 bsdf: Shader = None`
    """
    params_all = []
    inputs_all = [(color, (0.8, 0.8, 0.8, 1.0)), (normal, (0.0, 0.0, 0.0)), (weight, 0.0)]
    return "ShaderNodeBsdfTranslucent", params_all, inputs_all


def ShaderNodeBsdfTransparent(color=(1.0, 1.0, 1.0, 1.0), weight=0.0):
    """
    #### Inputs:
    - `#0 color: Color = (1.0, 1.0, 1.0, 1.0)`
    - `#1 weight: Float = 0.0`
    #### Outputs:
    - `#0 bsdf: Shader = None`
    """
    params_all = []
    inputs_all = [(color, (1.0, 1.0, 1.0, 1.0)), (weight, 0.0)]
    return "ShaderNodeBsdfTransparent", params_all, inputs_all


def ShaderNodeBsdfVelvet(color=(0.8, 0.8, 0.8, 1.0), sigma=1.0, normal=(0.0, 0.0, 0.0), weight=0.0):
    """
    #### Inputs:
    - `#0 color: Color = (0.8, 0.8, 0.8, 1.0)`
    - `#1 sigma: Float = 1.0`
    - `#2 normal: Vector = (0.0, 0.0, 0.0)`
    - `#3 weight: Float = 0.0`
    #### Outputs:
    - `#0 bsdf: Shader = None`
    """
    params_all = []
    inputs_all = [(color, (0.8, 0.8, 0.8, 1.0)), (sigma, 1.0), (normal, (0.0, 0.0, 0.0)), (weight, 0.0)]
    return "ShaderNodeBsdfVelvet", params_all, inputs_all


def ShaderNodeVolumeAbsorption(color=(0.8, 0.8, 0.8, 1.0), density=1.0, weight=0.0):
    """
    #### Inputs:
    - `#0 color: Color = (0.8, 0.8, 0.8, 1.0)`
    - `#1 density: Float = 1.0`
    - `#2 weight: Float = 0.0`
    #### Outputs:
    - `#0 volume: Shader = None`
    """
    params_all = []
    inputs_all = [(color, (0.8, 0.8, 0.8, 1.0)), (density, 1.0), (weight, 0.0)]
    return "ShaderNodeVolumeAbsorption", params_all, inputs_all


def ShaderNodeVolumeScatter(color=(0.8, 0.8, 0.8, 1.0), density=1.0, anisotropy=0.0, weight=0.0):
    """
    #### Inputs:
    - `#0 color: Color = (0.8, 0.8, 0.8, 1.0)`
    - `#1 density: Float = 1.0`
    - `#2 anisotropy: Float = 0.0`
    - `#3 weight: Float = 0.0`
    #### Outputs:
    - `#0 volume: Shader = None`
    """
    params_all = []
    inputs_all = [(color, (0.8, 0.8, 0.8, 1.0)), (density, 1.0), (anisotropy, 0.0), (weight, 0.0)]
    return "ShaderNodeVolumeScatter", params_all, inputs_all


def ShaderNodeTexEnvironment(interpolation='Linear', projection='EQUIRECTANGULAR', color_mapping=None, image=None, image_user=None, texture_mapping=None, vector=(0.0, 0.0, 0.0)):
    """
    - `interpolation`: `Linear`, `Closest`, `Cubic`, `Smart`
    - `projection`: `EQUIRECTANGULAR`, `MIRROR_BALL`
    #### Inputs:
    - `#0 vector: Vector = (0.0, 0.0, 0.0)`
    #### Outputs:
    - `#0 color: Color = (0.0, 0.0, 0.0, 0.0)`
    """
    params_all = [('interpolation', interpolation, 'Linear'), ('projection', projection, 'EQUIRECTANGULAR'), ('color_mapping', color_mapping, None), ('image', image, None), ('image_user', image_user, None), ('texture_mapping', texture_mapping, None)]
    inputs_all = [(vector, (0.0, 0.0, 0.0))]
    return "ShaderNodeTexEnvironment", params_all, inputs_all


def ShaderNodeTexIES(mode='INTERNAL', filepath='', ies=None, vector=(0.0, 0.0, 0.0), strength=1.0):
    """
    - `mode`: `INTERNAL`, `EXTERNAL`
    #### Inputs:
    - `#0 vector: Vector = (0.0, 0.0, 0.0)`
    - `#1 strength: Float = 1.0`
    #### Outputs:
    - `#0 fac: Float = 0.0`
    """
    params_all = [('mode', mode, 'INTERNAL'), ('filepath', filepath, ''), ('ies', ies, None)]
    inputs_all = [(vector, (0.0, 0.0, 0.0)), (strength, 1.0)]
    return "ShaderNodeTexIES", params_all, inputs_all


def ShaderNodeTexImage(extension='REPEAT', interpolation='Linear', projection='FLAT', color_mapping=None, image=None, image_user=None, projection_blend=0.0, texture_mapping=None, vector=(0.0, 0.0, 0.0)):
    """
    - `extension`: `REPEAT`, `EXTEND`, `CLIP`, `MIRROR`
    - `interpolation`: `Linear`, `Closest`, `Cubic`, `Smart`
    - `projection`: `FLAT`, `BOX`, `SPHERE`, `TUBE`
    #### Inputs:
    - `#0 vector: Vector = (0.0, 0.0, 0.0)`
    #### Outputs:
    - `#0 color: Color = (0.0, 0.0, 0.0, 0.0)`
    - `#1 alpha: Float = 0.0`
    """
    params_all = [('extension', extension, 'REPEAT'), ('interpolation', interpolation, 'Linear'), ('projection', projection, 'FLAT'), ('color_mapping', color_mapping, None), ('image', image, None), ('image_user', image_user, None), ('projection_blend', projection_blend, 0.0), ('texture_mapping', texture_mapping, None)]
    inputs_all = [(vector, (0.0, 0.0, 0.0))]
    return "ShaderNodeTexImage", params_all, inputs_all


def ShaderNodeTexPointDensity(interpolation='Linear', particle_color_source='PARTICLE_AGE', point_source='PARTICLE_SYSTEM', space='OBJECT', vertex_color_source='VERTEX_COLOR', object=None, particle_system=None, radius=0.3, resolution=100, vertex_attribute_name='', vector=(0.0, 0.0, 0.0)):
    """
    - `interpolation`: `Linear`, `Closest`, `Cubic`
    - `particle_color_source`: `PARTICLE_AGE`, `PARTICLE_SPEED`, `PARTICLE_VELOCITY`
    - `point_source`: `PARTICLE_SYSTEM`, `OBJECT`
    - `space`: `OBJECT`, `WORLD`
    - `vertex_color_source`: `VERTEX_COLOR`, `VERTEX_WEIGHT`, `VERTEX_NORMAL`
    #### Inputs:
    - `#0 vector: Vector = (0.0, 0.0, 0.0)`
    #### Outputs:
    - `#0 color: Color = (0.0, 0.0, 0.0, 0.0)`
    - `#1 density: Float = 0.0`
    """
    params_all = [('interpolation', interpolation, 'Linear'), ('particle_color_source', particle_color_source, 'PARTICLE_AGE'), ('point_source', point_source, 'PARTICLE_SYSTEM'), ('space', space, 'OBJECT'), ('vertex_color_source', vertex_color_source, 'VERTEX_COLOR'), ('object', object, None), ('particle_system', particle_system, None), ('radius', radius, 0.3), ('resolution', resolution, 100), ('vertex_attribute_name', vertex_attribute_name, '')]
    inputs_all = [(vector, (0.0, 0.0, 0.0))]
    return "ShaderNodeTexPointDensity", params_all, inputs_all


def ShaderNodeTexSky(sky_type='NISHITA', air_density=1.0, altitude=0.0, color_mapping=None, dust_density=1.0, ground_albedo=0.3, ozone_density=1.0, sun_direction=(0.0, 0.0, 1.0), sun_disc=True, sun_elevation=math.radians(15.0), sun_intensity=1.0, sun_rotation=0.0, sun_size=math.radians(0.545), texture_mapping=None, turbidity=2.2, vector=(0.0, 0.0, 0.0)):
    """
    - `sky_type`: `NISHITA`, `PREETHAM`, `HOSEK_WILKIE`
    #### Inputs:
    - `#0 vector: Vector = (0.0, 0.0, 0.0)`
    #### Outputs:
    - `#0 color: Color = (0.0, 0.0, 0.0, 0.0)`
    """
    params_all = [('sky_type', sky_type, 'NISHITA'), ('air_density', air_density, 1.0), ('altitude', altitude, 0.0), ('color_mapping', color_mapping, None), ('dust_density', dust_density, 1.0), ('ground_albedo', ground_albedo, 0.3), ('ozone_density', ozone_density, 1.0), ('sun_direction', sun_direction, (0.0, 0.0, 1.0)),
                  ('sun_disc', sun_disc, True), ('sun_elevation', sun_elevation, math.radians(15.0)), ('sun_intensity', sun_intensity, 1.0), ('sun_rotation', sun_rotation, 0.0), ('sun_size', sun_size, math.radians(0.545)), ('texture_mapping', texture_mapping, None), ('turbidity', turbidity, 2.2)]
    inputs_all = [(vector, (0.0, 0.0, 0.0))]
    return "ShaderNodeTexSky", params_all, inputs_all


def ShaderNodeBrightContrast(color=(1.0, 1.0, 1.0, 1.0), bright=0.0, contrast=0.0):
    """
    #### Inputs:
    - `#0 color: Color = (1.0, 1.0, 1.0, 1.0)`
    - `#1 bright: Float = 0.0`
    - `#2 contrast: Float = 0.0`
    #### Outputs:
    - `#0 color: Color = (0.0, 0.0, 0.0, 0.0)`
    """
    params_all = []
    inputs_all = [(color, (1.0, 1.0, 1.0, 1.0)), (bright, 0.0), (contrast, 0.0)]
    return "ShaderNodeBrightContrast", params_all, inputs_all


def ShaderNodeGamma(color=(1.0, 1.0, 1.0, 1.0), gamma=1.0):
    """
    #### Inputs:
    - `#0 color: Color = (1.0, 1.0, 1.0, 1.0)`
    - `#1 gamma: Float = 1.0`
    #### Outputs:
    - `#0 color: Color = (0.0, 0.0, 0.0, 0.0)`
    """
    params_all = []
    inputs_all = [(color, (1.0, 1.0, 1.0, 1.0)), (gamma, 1.0)]
    return "ShaderNodeGamma", params_all, inputs_all


def ShaderNodeHueSaturation(hue=0.5, saturation=1.0, value=1.0, fac=1.0, color=(0.8, 0.8, 0.8, 1.0)):
    """
    #### Inputs:
    - `#0 hue: Float = 0.5`
    - `#1 saturation: Float = 1.0`
    - `#2 value: Float = 1.0`
    - `#3 fac: Float = 1.0`
    - `#4 color: Color = (0.8, 0.8, 0.8, 1.0)`
    #### Outputs:
    - `#0 color: Color = (0.0, 0.0, 0.0, 0.0)`
    """
    params_all = []
    inputs_all = [(hue, 0.5), (saturation, 1.0), (value, 1.0), (fac, 1.0), (color, (0.8, 0.8, 0.8, 1.0))]
    return "ShaderNodeHueSaturation", params_all, inputs_all


def ShaderNodeInvert(fac=1.0, color=(0.0, 0.0, 0.0, 1.0)):
    """
    #### Inputs:
    - `#0 fac: Float = 1.0`
    - `#1 color: Color = (0.0, 0.0, 0.0, 1.0)`
    #### Outputs:
    - `#0 color: Color = (0.0, 0.0, 0.0, 0.0)`
    """
    params_all = []
    inputs_all = [(fac, 1.0), (color, (0.0, 0.0, 0.0, 1.0))]
    return "ShaderNodeInvert", params_all, inputs_all


def ShaderNodeLightFalloff(strength=100.0, smooth=0.0):
    """
    #### Inputs:
    - `#0 strength: Float = 100.0`
    - `#1 smooth: Float = 0.0`
    #### Outputs:
    - `#0 quadratic: Float = 0.0`
    - `#1 linear: Float = 0.0`
    - `#2 constant: Float = 0.0`
    """
    params_all = []
    inputs_all = [(strength, 100.0), (smooth, 0.0)]
    return "ShaderNodeLightFalloff", params_all, inputs_all


def ShaderNodeBump(invert=False, strength=1.0, distance=1.0, height=1.0, normal=(0.0, 0.0, 0.0)):
    """
    #### Inputs:
    - `#0 strength: Float = 1.0`
    - `#1 distance: Float = 1.0`
    - `#2 height: Float = 1.0`
    - `#3 normal: Vector = (0.0, 0.0, 0.0)`
    #### Outputs:
    - `#0 normal: Vector = (0.0, 0.0, 0.0)`
    """
    params_all = [('invert', invert, False)]
    inputs_all = [(strength, 1.0), (distance, 1.0), (height, 1.0), (normal, (0.0, 0.0, 0.0))]
    return "ShaderNodeBump", params_all, inputs_all


def ShaderNodeDisplacement(space='OBJECT', height=0.0, midlevel=0.5, scale=1.0, normal=(0.0, 0.0, 0.0)):
    """
    - `space`: `OBJECT`, `WORLD`
    #### Inputs:
    - `#0 height: Float = 0.0`
    - `#1 midlevel: Float = 0.5`
    - `#2 scale: Float = 1.0`
    - `#3 normal: Vector = (0.0, 0.0, 0.0)`
    #### Outputs:
    - `#0 displacement: Vector = (0.0, 0.0, 0.0)`
    """
    params_all = [('space', space, 'OBJECT')]
    inputs_all = [(height, 0.0), (midlevel, 0.5), (scale, 1.0), (normal, (0.0, 0.0, 0.0))]
    return "ShaderNodeDisplacement", params_all, inputs_all


def ShaderNodeMapping(vector_type='POINT', vector=(0.0, 0.0, 0.0), location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(1.0, 1.0, 1.0)):
    """
    - `vector_type`: `POINT`, `TEXTURE`, `VECTOR`, `NORMAL`
    #### Inputs:
    - `#0 vector: Vector = (0.0, 0.0, 0.0)`
    - `#1 location: Vector = (0.0, 0.0, 0.0)`
    - `#2 rotation: Vector = (0.0, 0.0, 0.0)`
    - `#3 scale: Vector = (1.0, 1.0, 1.0)`
    #### Outputs:
    - `#0 vector: Vector = (0.0, 0.0, 0.0)`
    """
    params_all = [('vector_type', vector_type, 'POINT')]
    inputs_all = [(vector, (0.0, 0.0, 0.0)), (location, (0.0, 0.0, 0.0)), (rotation, (0.0, 0.0, 0.0)), (scale, (1.0, 1.0, 1.0))]
    return "ShaderNodeMapping", params_all, inputs_all


def ShaderNodeNormal(normal=(0.0, 0.0, 1.0)):
    """
    #### Inputs:
    - `#0 normal: Vector = (0.0, 0.0, 1.0)`
    #### Outputs:
    - `#0 normal: Vector = (0.0, 0.0, 1.0)`
    - `#1 dot: Float = 0.0`
    """
    params_all = []
    inputs_all = [(normal, (0.0, 0.0, 1.0))]
    return "ShaderNodeNormal", params_all, inputs_all


def ShaderNodeNormalMap(space='TANGENT', uv_map='', strength=1.0, color=(0.5, 0.5, 1.0, 1.0)):
    """
    - `space`: `TANGENT`, `OBJECT`, `WORLD`, `BLENDER_OBJECT`, `BLENDER_WORLD`
    #### Inputs:
    - `#0 strength: Float = 1.0`
    - `#1 color: Color = (0.5, 0.5, 1.0, 1.0)`
    #### Outputs:
    - `#0 normal: Vector = (0.0, 0.0, 0.0)`
    """
    params_all = [('space', space, 'TANGENT'), ('uv_map', uv_map, '')]
    inputs_all = [(strength, 1.0), (color, (0.5, 0.5, 1.0, 1.0))]
    return "ShaderNodeNormalMap", params_all, inputs_all


def ShaderNodeVectorDisplacement(space='TANGENT', vector=(0.0, 0.0, 0.0, 0.0), midlevel=0.0, scale=1.0):
    """
    - `space`: `TANGENT`, `OBJECT`, `WORLD`
    #### Inputs:
    - `#0 vector: Color = (0.0, 0.0, 0.0, 0.0)`
    - `#1 midlevel: Float = 0.0`
    - `#2 scale: Float = 1.0`
    #### Outputs:
    - `#0 displacement: Vector = (0.0, 0.0, 0.0)`
    """
    params_all = [('space', space, 'TANGENT')]
    inputs_all = [(vector, (0.0, 0.0, 0.0, 0.0)), (midlevel, 0.0), (scale, 1.0)]
    return "ShaderNodeVectorDisplacement", params_all, inputs_all


def ShaderNodeVectorTransform(convert_from='WORLD', convert_to='OBJECT', vector_type='VECTOR', vector=(0.5, 0.5, 0.5)):
    """
    - `convert_from`: `WORLD`, `OBJECT`, `CAMERA`
    - `convert_to`: `OBJECT`, `WORLD`, `CAMERA`
    - `vector_type`: `VECTOR`, `POINT`, `NORMAL`
    #### Inputs:
    - `#0 vector: Vector = (0.5, 0.5, 0.5)`
    #### Outputs:
    - `#0 vector: Vector = (0.0, 0.0, 0.0)`
    """
    params_all = [('convert_from', convert_from, 'WORLD'), ('convert_to', convert_to, 'OBJECT'), ('vector_type', vector_type, 'VECTOR')]
    inputs_all = [(vector, (0.5, 0.5, 0.5))]
    return "ShaderNodeVectorTransform", params_all, inputs_all


def ShaderNodeBlackbody(temperature=1500.0):
    """
    #### Inputs:
    - `#0 temperature: Float = 1500.0`
    #### Outputs:
    - `#0 color: Color = (0.0, 0.0, 0.0, 0.0)`
    """
    params_all = []
    inputs_all = [(temperature, 1500.0)]
    return "ShaderNodeBlackbody", params_all, inputs_all


def ShaderNodeCombineColor(mode='RGB', red=0.0, green=0.0, blue=0.0):
    """
    - `mode`: `RGB`, `HSV`, `HSL`
    #### Inputs:
    - `#0 red: Float = 0.0`
    - `#1 green: Float = 0.0`
    - `#2 blue: Float = 0.0`
    #### Outputs:
    - `#0 color: Color = (0.0, 0.0, 0.0, 0.0)`
    """
    params_all = [('mode', mode, 'RGB')]
    inputs_all = [(red, 0.0), (green, 0.0), (blue, 0.0)]
    return "ShaderNodeCombineColor", params_all, inputs_all


def ShaderNodeRGBToBW(color=(0.5, 0.5, 0.5, 1.0)):
    """
    #### Inputs:
    - `#0 color: Color = (0.5, 0.5, 0.5, 1.0)`
    #### Outputs:
    - `#0 val: Float = 0.0`
    """
    params_all = []
    inputs_all = [(color, (0.5, 0.5, 0.5, 1.0))]
    return "ShaderNodeRGBToBW", params_all, inputs_all


def ShaderNodeSeparateColor(mode='RGB', color=(0.8, 0.8, 0.8, 1.0)):
    """
    - `mode`: `RGB`, `HSV`, `HSL`
    #### Inputs:
    - `#0 color: Color = (0.8, 0.8, 0.8, 1.0)`
    #### Outputs:
    - `#0 red: Float = 0.0`
    - `#1 green: Float = 0.0`
    - `#2 blue: Float = 0.0`
    """
    params_all = [('mode', mode, 'RGB')]
    inputs_all = [(color, (0.8, 0.8, 0.8, 1.0))]
    return "ShaderNodeSeparateColor", params_all, inputs_all


def ShaderNodeShaderToRGB(shader=None):
    """
    #### Inputs:
    - `#0 shader: Shader = None`
    #### Outputs:
    - `#0 color: Color = (0.0, 0.0, 0.0, 0.0)`
    - `#1 alpha: Float = 0.0`
    """
    params_all = []
    inputs_all = [(shader, None)]
    return "ShaderNodeShaderToRGB", params_all, inputs_all


def ShaderNodeWavelength(wavelength=500.0):
    """
    #### Inputs:
    - `#0 wavelength: Float = 500.0`
    #### Outputs:
    - `#0 color: Color = (0.0, 0.0, 0.0, 0.0)`
    """
    params_all = []
    inputs_all = [(wavelength, 500.0)]
    return "ShaderNodeWavelength", params_all, inputs_all


def ShaderNodeScript(mode="INTERNAL", script: bpy.types.Text = None):
    """
    - `mode`: `INTERNAL`, `EXTERNAL`
    """
    params_all = [("mode", mode, "INTERNAL"), ("script", script, None)]
    inputs_all = []
    return "ShaderNodeScript", params_all, inputs_all


def GeometryNodeInputSceneTime():
    """
    #### Outputs:
    - `#0 seconds: Float = 0.0`
    - `#1 frame: Float = 0.0`
    """
    params_all = []
    inputs_all = []
    return "GeometryNodeInputSceneTime", params_all, inputs_all


def GeometryNodeIndexOfNearest(position=None, group_id=0):
    """
    #### Inputs:
    - `#0 position: Vector = None`
    - `#1 group_id: Integer = 0`
    #### Outputs:
    - `#0 index: Integer = 0`
    - `#1 has_neighbor: Boolean = False`
    """
    params_all = []
    inputs_all = [(position, None), (group_id, 0)]
    return "GeometryNodeIndexOfNearest", params_all, inputs_all
