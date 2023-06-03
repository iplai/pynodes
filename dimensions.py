NODE_DIMS = {
    "FunctionNodeAlignEulerToVector": {
        "params_enum": {
            "axis": ('X', 'Y', 'Z'),
            "pivot_axis": ('AUTO', 'X', 'Y', 'Z')
        },
        "dimensions": (140, 234)
    },
    "FunctionNodeBooleanMath": {
        "params_enum": {
            "operation": ('AND', 'OR', 'NOT', 'NAND', 'NOR', 'XNOR', 'XOR', 'IMPLY', 'NIMPLY')
        },
        "dimensions": (140, 127),
        "dimensions_2": (140, 107)
    },
    "FunctionNodeCombineColor": {
        "params_enum": {
            "mode": ('RGB', 'HSV', 'HSL')
        },
        "dimensions": (140, 171)
    },
    "FunctionNodeCompare": {
        "params_enum": {
            "data_type": ('FLOAT', 'INT', 'VECTOR', 'STRING', 'RGBA'),
            "mode": ('ELEMENT', 'LENGTH', 'AVERAGE', 'DOT_PRODUCT', 'DIRECTION'),
            "operation": ('LESS_THAN', 'LESS_EQUAL', 'GREATER_THAN', 'GREATER_EQUAL', 'EQUAL', 'NOT_EQUAL')
        },
        "dimensions": (140, 154),
        "dimensions_0_0_4": (140, 174),
        "dimensions_0_0_5": (140, 174),
        "dimensions_0_1_4": (140, 174),
        "dimensions_0_1_5": (140, 174),
        "dimensions_0_2_4": (140, 174),
        "dimensions_0_2_5": (140, 174),
        "dimensions_0_3_4": (140, 174),
        "dimensions_0_3_5": (140, 174),
        "dimensions_0_4_4": (140, 174),
        "dimensions_0_4_5": (140, 174),
        "dimensions_2_0_0": (140, 299),
        "dimensions_2_0_1": (140, 299),
        "dimensions_2_0_2": (140, 299),
        "dimensions_2_0_3": (140, 299),
        "dimensions_2_0_4": (140, 319),
        "dimensions_2_0_5": (140, 319),
        "dimensions_2_1_0": (140, 299),
        "dimensions_2_1_1": (140, 299),
        "dimensions_2_1_2": (140, 299),
        "dimensions_2_1_3": (140, 299),
        "dimensions_2_1_4": (140, 319),
        "dimensions_2_1_5": (140, 319),
        "dimensions_2_2_0": (140, 299),
        "dimensions_2_2_1": (140, 299),
        "dimensions_2_2_2": (140, 299),
        "dimensions_2_2_3": (140, 299),
        "dimensions_2_2_4": (140, 319),
        "dimensions_2_2_5": (140, 319),
        "dimensions_2_3_0": (140, 321),
        "dimensions_2_3_1": (140, 321),
        "dimensions_2_3_2": (140, 321),
        "dimensions_2_3_3": (140, 321),
        "dimensions_2_3_4": (140, 341),
        "dimensions_2_3_5": (140, 341),
        "dimensions_2_4_0": (140, 321),
        "dimensions_2_4_1": (140, 321),
        "dimensions_2_4_2": (140, 321),
        "dimensions_2_4_3": (140, 321),
        "dimensions_2_4_4": (140, 341),
        "dimensions_2_4_5": (140, 341),
        "dimensions_4_0_4": (140, 174),
        "dimensions_4_0_5": (140, 174),
        "dimensions_4_1_4": (140, 174),
        "dimensions_4_1_5": (140, 174),
        "dimensions_4_2_4": (140, 174),
        "dimensions_4_2_5": (140, 174),
        "dimensions_4_3_4": (140, 174),
        "dimensions_4_3_5": (140, 174),
        "dimensions_4_4_4": (140, 174),
        "dimensions_4_4_5": (140, 174)
    },
    "FunctionNodeFloatToInt": {
        "params_enum": {
            "rounding_mode": ('ROUND', 'FLOOR', 'CEILING', 'TRUNCATE')
        },
        "dimensions": (140, 105)
    },
    "FunctionNodeInputBool": {
        "dimensions": (140, 80)
    },
    "FunctionNodeInputColor": {
        "dimensions": (140, 185)
    },
    "FunctionNodeInputInt": {
        "dimensions": (140, 80)
    },
    "FunctionNodeInputSpecialCharacters": {
        "dimensions": (140, 72)
    },
    "FunctionNodeInputString": {
        "dimensions": (140, 80)
    },
    "FunctionNodeInputVector": {
        "dimensions": (140, 120)
    },
    "FunctionNodeRandomValue": {
        "params_enum": {
            "data_type": ('FLOAT', 'INT', 'FLOAT_VECTOR', 'BOOLEAN')
        },
        "dimensions": (140, 173),
        "dimensions_2": (140, 293),
        "dimensions_3": (140, 149)
    },
    "FunctionNodeReplaceString": {
        "dimensions": (140, 119)
    },
    "FunctionNodeRotateEuler": {
        "params_enum": {
            "space": ('OBJECT', 'LOCAL')
        },
        "dimensions": (140, 214)
    },
    "FunctionNodeSeparateColor": {
        "params_enum": {
            "mode": ('RGB', 'HSV', 'HSL')
        },
        "dimensions": (140, 171)
    },
    "FunctionNodeSliceString": {
        "dimensions": (140, 119)
    },
    "FunctionNodeStringLength": {
        "dimensions": (140, 75)
    },
    "FunctionNodeValueToString": {
        "dimensions": (140, 97)
    },
    "GeometryNodeAccumulateField": {
        "params_enum": {
            "data_type": ('FLOAT', 'INT', 'FLOAT_VECTOR'),
            "domain": ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')
        },
        "dimensions": (140, 198),
        "dimensions_1_0": (140, 196),
        "dimensions_1_1": (140, 196),
        "dimensions_1_2": (140, 196),
        "dimensions_1_3": (140, 196),
        "dimensions_1_4": (140, 196),
        "dimensions_1_5": (140, 196),
        "dimensions_2_0": (140, 258),
        "dimensions_2_1": (140, 258),
        "dimensions_2_2": (140, 258),
        "dimensions_2_3": (140, 258),
        "dimensions_2_4": (140, 258),
        "dimensions_2_5": (140, 258)
    },
    "GeometryNodeAttributeDomainSize": {
        "params_enum": {
            "component": ('MESH', 'POINTCLOUD', 'CURVE', 'INSTANCES')
        },
        "dimensions": (140, 173),
        "dimensions_1": (140, 107),
        "dimensions_2": (140, 129),
        "dimensions_3": (140, 105)
    },
    "GeometryNodeAttributeStatistic": {
        "params_enum": {
            "data_type": ('FLOAT', 'FLOAT_VECTOR'),
            "domain": ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')
        },
        "dimensions": (140, 332),
        "dimensions_1_0": (140, 328),
        "dimensions_1_1": (140, 328),
        "dimensions_1_2": (140, 328),
        "dimensions_1_3": (140, 328),
        "dimensions_1_4": (140, 328),
        "dimensions_1_5": (140, 328)
    },
    "GeometryNodeBlurAttribute": {
        "params_enum": {
            "data_type": ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR')
        },
        "dimensions": (140, 151),
        "dimensions_3": (140, 149)
    },
    "GeometryNodeBoundBox": {
        "dimensions": (140, 119)
    },
    "GeometryNodeCaptureAttribute": {
        "params_enum": {
            "data_type": ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN'),
            "domain": ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')
        },
        "dimensions": (140, 178),
        "dimensions_1_0": (140, 174),
        "dimensions_1_1": (140, 174),
        "dimensions_1_2": (140, 174),
        "dimensions_1_3": (140, 174),
        "dimensions_1_4": (140, 174),
        "dimensions_1_5": (140, 174),
        "dimensions_2_0": (140, 238),
        "dimensions_2_1": (140, 238),
        "dimensions_2_2": (140, 238),
        "dimensions_2_3": (140, 238),
        "dimensions_2_4": (140, 238),
        "dimensions_2_5": (140, 238)
    },
    "GeometryNodeCollectionInfo": {
        "params_enum": {
            "transform_space": ('ORIGINAL', 'RELATIVE')
        },
        "dimensions": (140, 149)
    },
    "GeometryNodeConvexHull": {
        "dimensions": (140, 75)
    },
    "GeometryNodeCornersOfFace": {
        "dimensions": (140, 141)
    },
    "GeometryNodeCornersOfVertex": {
        "dimensions": (140, 141)
    },
    "GeometryNodeCurveArc": {
        "params_enum": {
            "mode": ('POINTS', 'RADIUS')
        },
        "dimensions": (140, 217),
        "dimensions_0": (140, 483)
    },
    "GeometryNodeCurveEndpointSelection": {
        "dimensions": (140, 97)
    },
    "GeometryNodeCurveHandleTypeSelection": {
        "params_enum": {
            "handle_type": ('FREE', 'AUTO', 'VECTOR', 'ALIGN')
        },
        "dimensions": (140, 105)
    },
    "GeometryNodeCurveLength": {
        "dimensions": (140, 75)
    },
    "GeometryNodeCurveOfPoint": {
        "dimensions": (140, 97)
    },
    "GeometryNodeCurvePrimitiveBezierSegment": {
        "params_enum": {
            "mode": ('POSITION', 'OFFSET')
        },
        "dimensions": (140, 433)
    },
    "GeometryNodeCurvePrimitiveCircle": {
        "params_enum": {
            "mode": ('POINTS', 'RADIUS')
        },
        "dimensions": (140, 129),
        "dimensions_0": (140, 375)
    },
    "GeometryNodeCurvePrimitiveLine": {
        "params_enum": {
            "mode": ('POINTS', 'DIRECTION')
        },
        "dimensions": (140, 249),
        "dimensions_1": (140, 269)
    },
    "GeometryNodeCurvePrimitiveQuadrilateral": {
        "params_enum": {
            "mode": ('RECTANGLE', 'PARALLELOGRAM', 'TRAPEZOID', 'KITE', 'POINTS')
        },
        "dimensions": (140, 129),
        "dimensions_1": (140, 151),
        "dimensions_2": (140, 173),
        "dimensions_3": (140, 151),
        "dimensions_4": (140, 411)
    },
    "GeometryNodeCurveQuadraticBezier": {
        "dimensions": (140, 321)
    },
    "GeometryNodeCurveSetHandles": {
        "params_enum": {
            "handle_type": ('FREE', 'AUTO', 'VECTOR', 'ALIGN')
        },
        "dimensions": (140, 152)
    },
    "GeometryNodeCurveSpiral": {
        "dimensions": (140, 185)
    },
    "GeometryNodeCurveSplineType": {
        "params_enum": {
            "spline_type": ('CATMULL_ROM', 'POLY', 'BEZIER', 'NURBS')
        },
        "dimensions": (140, 127)
    },
    "GeometryNodeCurveStar": {
        "dimensions": (140, 163)
    },
    "GeometryNodeCurveToMesh": {
        "dimensions": (140, 119)
    },
    "GeometryNodeCurveToPoints": {
        "params_enum": {
            "mode": ('EVALUATED', 'COUNT', 'LENGTH')
        },
        "dimensions": (140, 195),
        "dimensions_0": (140, 173),
        "dimensions_2": (140, 193)
    },
    "GeometryNodeDeformCurvesOnSurface": {
        "dimensions": (170, 75)
    },
    "GeometryNodeDeleteGeometry": {
        "params_enum": {
            "domain": ('POINT', 'EDGE', 'FACE', 'CURVE', 'INSTANCE'),
            "mode": ('ALL', 'EDGE_FACE', 'ONLY_FACE')
        },
        "dimensions": (140, 152),
        "dimensions_3_0": (140, 127),
        "dimensions_3_1": (140, 127),
        "dimensions_3_2": (140, 127),
        "dimensions_4_0": (140, 127),
        "dimensions_4_1": (140, 127),
        "dimensions_4_2": (140, 127)
    },
    "GeometryNodeDistributePointsInVolume": {
        "params_enum": {
            "mode": ('DENSITY_RANDOM', 'DENSITY_GRID')
        },
        "dimensions": (170, 151),
        "dimensions_1": (170, 209)
    },
    "GeometryNodeDistributePointsOnFaces": {
        "params_enum": {
            "distribute_method": ('RANDOM', 'POISSON')
        },
        "dimensions": (170, 215),
        "dimensions_1": (170, 259)
    },
    "GeometryNodeDualMesh": {
        "dimensions": (140, 97)
    },
    "GeometryNodeDuplicateElements": {
        "params_enum": {
            "domain": ('POINT', 'EDGE', 'FACE', 'SPLINE', 'INSTANCE')
        },
        "dimensions": (140, 171)
    },
    "GeometryNodeEdgePathsToCurves": {
        "dimensions": (140, 119)
    },
    "GeometryNodeEdgePathsToSelection": {
        "dimensions": (150, 97)
    },
    "GeometryNodeEdgesOfCorner": {
        "dimensions": (140, 97)
    },
    "GeometryNodeEdgesOfVertex": {
        "dimensions": (140, 141)
    },
    "GeometryNodeEdgesToFaceGroups": {
        "dimensions": (140, 75)
    },
    "GeometryNodeExtrudeMesh": {
        "params_enum": {
            "mode": ('VERTICES', 'EDGES', 'FACES')
        },
        "dimensions": (140, 237),
        "dimensions_0": (140, 217),
        "dimensions_1": (140, 217)
    },
    "GeometryNodeFaceOfCorner": {
        "dimensions": (140, 97)
    },
    "GeometryNodeFieldAtIndex": {
        "params_enum": {
            "data_type": ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN'),
            "domain": ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')
        },
        "dimensions": (140, 156),
        "dimensions_4_0": (140, 152),
        "dimensions_4_1": (140, 152),
        "dimensions_4_2": (140, 152),
        "dimensions_4_3": (140, 152),
        "dimensions_4_4": (140, 152),
        "dimensions_4_5": (140, 152)
    },
    "GeometryNodeFieldOnDomain": {
        "params_enum": {
            "data_type": ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN'),
            "domain": ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')
        },
        "dimensions": (140, 134),
        "dimensions_2_0": (140, 194),
        "dimensions_2_1": (140, 194),
        "dimensions_2_2": (140, 194),
        "dimensions_2_3": (140, 194),
        "dimensions_2_4": (140, 194),
        "dimensions_2_5": (140, 194),
        "dimensions_4_0": (140, 130),
        "dimensions_4_1": (140, 130),
        "dimensions_4_2": (140, 130),
        "dimensions_4_3": (140, 130),
        "dimensions_4_4": (140, 130),
        "dimensions_4_5": (140, 130)
    },
    "GeometryNodeFillCurve": {
        "params_enum": {
            "mode": ('TRIANGLES', 'NGONS')
        },
        "dimensions": (140, 105)
    },
    "GeometryNodeFilletCurve": {
        "params_enum": {
            "mode": ('BEZIER', 'POLY')
        },
        "dimensions": (140, 149),
        "dimensions_1": (140, 171)
    },
    "GeometryNodeFlipFaces": {
        "dimensions": (140, 97)
    },
    "GeometryNodeGeometryToInstance": {
        "dimensions": (160, 75)
    },
    "GeometryNodeGroup": {
        "dimensions": (140, 50)
    },
    "GeometryNodeImageInfo": {
        "dimensions": (240, 185)
    },
    "GeometryNodeImageTexture": {
        "params_enum": {
            "extension": ('REPEAT', 'EXTEND', 'CLIP', 'MIRROR'),
            "interpolation": ('Linear', 'Closest', 'Cubic')
        },
        "dimensions": (240, 196)
    },
    "GeometryNodeInputCurveHandlePositions": {
        "dimensions": (150, 97)
    },
    "GeometryNodeInputCurveTilt": {
        "dimensions": (140, 50)
    },
    "GeometryNodeInputID": {
        "dimensions": (140, 50)
    },
    "GeometryNodeInputImage": {
        "dimensions": (240, 80)
    },
    "GeometryNodeInputIndex": {
        "dimensions": (140, 50)
    },
    "GeometryNodeInputInstanceRotation": {
        "dimensions": (140, 50)
    },
    "GeometryNodeInputInstanceScale": {
        "dimensions": (140, 50)
    },
    "GeometryNodeInputMaterial": {
        "dimensions": (140, 80)
    },
    "GeometryNodeInputMaterialIndex": {
        "dimensions": (140, 50)
    },
    "GeometryNodeInputMeshEdgeAngle": {
        "dimensions": (140, 72)
    },
    "GeometryNodeInputMeshEdgeNeighbors": {
        "dimensions": (140, 50)
    },
    "GeometryNodeInputMeshEdgeVertices": {
        "dimensions": (140, 116)
    },
    "GeometryNodeInputMeshFaceArea": {
        "dimensions": (140, 50)
    },
    "GeometryNodeInputMeshFaceIsPlanar": {
        "dimensions": (140, 75)
    },
    "GeometryNodeInputMeshFaceNeighbors": {
        "dimensions": (150, 72)
    },
    "GeometryNodeInputMeshIsland": {
        "dimensions": (140, 72)
    },
    "GeometryNodeInputMeshVertexNeighbors": {
        "dimensions": (140, 72)
    },
    "GeometryNodeInputNamedAttribute": {
        "params_enum": {
            "data_type": ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN')
        },
        "dimensions": (140, 127)
    },
    "GeometryNodeInputNormal": {
        "dimensions": (140, 50)
    },
    "GeometryNodeInputPosition": {
        "dimensions": (140, 50)
    },
    "GeometryNodeInputRadius": {
        "dimensions": (140, 50)
    },
    "GeometryNodeInputSceneTime": {
        "dimensions": (140, 72)
    },
    "GeometryNodeInputShadeSmooth": {
        "dimensions": (140, 50)
    },
    "GeometryNodeInputShortestEdgePaths": {
        "dimensions": (140, 119)
    },
    "GeometryNodeInputSplineCyclic": {
        "dimensions": (140, 50)
    },
    "GeometryNodeInputSplineResolution": {
        "dimensions": (140, 50)
    },
    "GeometryNodeInputTangent": {
        "dimensions": (140, 50)
    },
    "GeometryNodeInstanceOnPoints": {
        "dimensions": (140, 327)
    },
    "GeometryNodeInstancesToPoints": {
        "dimensions": (140, 141)
    },
    "GeometryNodeInterpolateCurves": {
        "dimensions": (140, 251)
    },
    "GeometryNodeIsViewport": {
        "dimensions": (140, 50)
    },
    "GeometryNodeJoinGeometry": {
        "dimensions": (140, 75)
    },
    "GeometryNodeMaterialSelection": {
        "dimensions": (140, 75)
    },
    "GeometryNodeMergeByDistance": {
        "params_enum": {
            "mode": ('ALL', 'CONNECTED')
        },
        "dimensions": (140, 149)
    },
    "GeometryNodeMeshBoolean": {
        "params_enum": {
            "operation": ('INTERSECT', 'UNION', 'DIFFERENCE')
        },
        "dimensions": (140, 193),
        "dimensions_0": (140, 171),
        "dimensions_1": (140, 171)
    },
    "GeometryNodeMeshCircle": {
        "params_enum": {
            "fill_type": ('NONE', 'NGON', 'TRIANGLE_FAN')
        },
        "dimensions": (140, 127)
    },
    "GeometryNodeMeshCone": {
        "params_enum": {
            "fill_type": ('NONE', 'NGON', 'TRIANGLE_FAN')
        },
        "dimensions": (140, 303),
        "dimensions_0": (140, 281)
    },
    "GeometryNodeMeshCube": {
        "dimensions": (140, 223)
    },
    "GeometryNodeMeshCylinder": {
        "params_enum": {
            "fill_type": ('NONE', 'NGON', 'TRIANGLE_FAN')
        },
        "dimensions": (140, 281),
        "dimensions_0": (140, 259)
    },
    "GeometryNodeMeshFaceSetBoundaries": {
        "dimensions": (150, 75)
    },
    "GeometryNodeMeshGrid": {
        "dimensions": (140, 163)
    },
    "GeometryNodeMeshIcoSphere": {
        "dimensions": (140, 119)
    },
    "GeometryNodeMeshLine": {
        "params_enum": {
            "count_mode": ('TOTAL', 'RESOLUTION'),
            "mode": ('OFFSET', 'END_POINTS')
        },
        "dimensions": (140, 269),
        "dimensions_0_1": (140, 294),
        "dimensions_1_1": (140, 294)
    },
    "GeometryNodeMeshToCurve": {
        "dimensions": (140, 97)
    },
    "GeometryNodeMeshToPoints": {
        "params_enum": {
            "mode": ('VERTICES', 'EDGES', 'FACES', 'CORNERS')
        },
        "dimensions": (140, 171)
    },
    "GeometryNodeMeshToVolume": {
        "params_enum": {
            "resolution_mode": ('VOXEL_AMOUNT', 'VOXEL_SIZE')
        },
        "dimensions": (200, 215)
    },
    "GeometryNodeMeshUVSphere": {
        "dimensions": (140, 141)
    },
    "GeometryNodeObjectInfo": {
        "params_enum": {
            "transform_space": ('ORIGINAL', 'RELATIVE')
        },
        "dimensions": (140, 193)
    },
    "GeometryNodeOffsetCornerInFace": {
        "dimensions": (140, 97)
    },
    "GeometryNodeOffsetPointInCurve": {
        "dimensions": (140, 119)
    },
    "GeometryNodePoints": {
        "dimensions": (140, 179)
    },
    "GeometryNodePointsOfCurve": {
        "dimensions": (140, 141)
    },
    "GeometryNodePointsToVertices": {
        "dimensions": (140, 97)
    },
    "GeometryNodePointsToVolume": {
        "params_enum": {
            "resolution_mode": ('VOXEL_AMOUNT', 'VOXEL_SIZE')
        },
        "dimensions": (170, 171)
    },
    "GeometryNodeProximity": {
        "params_enum": {
            "target_element": ('POINTS', 'EDGES', 'FACES')
        },
        "dimensions": (140, 149)
    },
    "GeometryNodeRaycast": {
        "params_enum": {
            "data_type": ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN'),
            "mapping": ('INTERPOLATED', 'NEAREST')
        },
        "dimensions": (150, 368),
        "dimensions_1_0": (150, 366),
        "dimensions_1_1": (150, 366)
    },
    "GeometryNodeRealizeInstances": {
        "dimensions": (140, 75)
    },
    "GeometryNodeRemoveAttribute": {
        "dimensions": (170, 97)
    },
    "GeometryNodeReplaceMaterial": {
        "dimensions": (140, 119)
    },
    "GeometryNodeResampleCurve": {
        "params_enum": {
            "mode": ('EVALUATED', 'COUNT', 'LENGTH')
        },
        "dimensions": (140, 151),
        "dimensions_0": (140, 129),
        "dimensions_2": (140, 149)
    },
    "GeometryNodeReverseCurve": {
        "dimensions": (140, 97)
    },
    "GeometryNodeRotateInstances": {
        "dimensions": (140, 283)
    },
    "GeometryNodeSampleCurve": {
        "params_enum": {
            "data_type": ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN'),
            "mode": ('FACTOR', 'LENGTH')
        },
        "dimensions": (140, 287)
    },
    "GeometryNodeSampleIndex": {
        "params_enum": {
            "data_type": ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN'),
            "domain": ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')
        },
        "dimensions": (140, 201),
        "dimensions_4_0": (140, 199),
        "dimensions_4_1": (140, 199),
        "dimensions_4_2": (140, 199),
        "dimensions_4_3": (140, 199),
        "dimensions_4_4": (140, 199),
        "dimensions_4_5": (140, 199)
    },
    "GeometryNodeSampleNearest": {
        "params_enum": {
            "domain": ('POINT', 'EDGE', 'FACE', 'CORNER')
        },
        "dimensions": (140, 127)
    },
    "GeometryNodeSampleNearestSurface": {
        "params_enum": {
            "data_type": ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN')
        },
        "dimensions": (150, 151),
        "dimensions_4": (150, 149)
    },
    "GeometryNodeSampleUVSurface": {
        "params_enum": {
            "data_type": ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN')
        },
        "dimensions": (140, 253)
    },
    "GeometryNodeScaleElements": {
        "params_enum": {
            "domain": ('FACE', 'EDGE'),
            "scale_mode": ('UNIFORM', 'SINGLE_AXIS')
        },
        "dimensions": (140, 198),
        "dimensions_0_1": (140, 278),
        "dimensions_1_1": (140, 278)
    },
    "GeometryNodeScaleInstances": {
        "dimensions": (140, 283)
    },
    "GeometryNodeSelfObject": {
        "dimensions": (140, 50)
    },
    "GeometryNodeSeparateComponents": {
        "dimensions": (140, 163)
    },
    "GeometryNodeSeparateGeometry": {
        "params_enum": {
            "domain": ('POINT', 'EDGE', 'FACE', 'CURVE', 'INSTANCE')
        },
        "dimensions": (140, 149)
    },
    "GeometryNodeSetCurveHandlePositions": {
        "params_enum": {
            "mode": ('LEFT', 'RIGHT')
        },
        "dimensions": (140, 231)
    },
    "GeometryNodeSetCurveNormal": {
        "params_enum": {
            "mode": ('MINIMUM_TWIST', 'Z_UP')
        },
        "dimensions": (140, 127)
    },
    "GeometryNodeSetCurveRadius": {
        "dimensions": (140, 119)
    },
    "GeometryNodeSetCurveTilt": {
        "dimensions": (140, 119)
    },
    "GeometryNodeSetID": {
        "dimensions": (140, 119)
    },
    "GeometryNodeSetMaterial": {
        "dimensions": (140, 119)
    },
    "GeometryNodeSetMaterialIndex": {
        "dimensions": (140, 119)
    },
    "GeometryNodeSetPointRadius": {
        "dimensions": (140, 119)
    },
    "GeometryNodeSetPosition": {
        "dimensions": (140, 201)
    },
    "GeometryNodeSetShadeSmooth": {
        "dimensions": (140, 119)
    },
    "GeometryNodeSetSplineCyclic": {
        "dimensions": (140, 119)
    },
    "GeometryNodeSetSplineResolution": {
        "dimensions": (140, 119)
    },
    "GeometryNodeSplineLength": {
        "dimensions": (140, 72)
    },
    "GeometryNodeSplineParameter": {
        "dimensions": (140, 94)
    },
    "GeometryNodeSplitEdges": {
        "dimensions": (140, 97)
    },
    "GeometryNodeStoreNamedAttribute": {
        "params_enum": {
            "data_type": ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BYTE_COLOR', 'BOOLEAN', 'FLOAT2'),
            "domain": ('POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')
        },
        "dimensions": (140, 198),
        "dimensions_1_0": (140, 196),
        "dimensions_1_1": (140, 196),
        "dimensions_1_2": (140, 196),
        "dimensions_1_3": (140, 196),
        "dimensions_1_4": (140, 196),
        "dimensions_1_5": (140, 196),
        "dimensions_2_0": (140, 258),
        "dimensions_2_1": (140, 258),
        "dimensions_2_2": (140, 258),
        "dimensions_2_3": (140, 258),
        "dimensions_2_4": (140, 258),
        "dimensions_2_5": (140, 258),
        "dimensions_6_0": (140, 258),
        "dimensions_6_1": (140, 258),
        "dimensions_6_2": (140, 258),
        "dimensions_6_3": (140, 258),
        "dimensions_6_4": (140, 258),
        "dimensions_6_5": (140, 258)
    },
    "GeometryNodeStringJoin": {
        "dimensions": (140, 97)
    },
    "GeometryNodeStringToCurves": {
        "params_enum": {
            "align_x": ('LEFT', 'CENTER', 'RIGHT', 'JUSTIFY', 'FLUSH'),
            "align_y": ('TOP', 'TOP_BASELINE', 'MIDDLE', 'BOTTOM_BASELINE', 'BOTTOM'),
            "overflow": ('OVERFLOW', 'SCALE_TO_FIT', 'TRUNCATE'),
            "pivot_mode": ('MIDPOINT', 'TOP_LEFT', 'TOP_CENTER', 'TOP_RIGHT', 'BOTTOM_LEFT', 'BOTTOM_CENTER', 'BOTTOM_RIGHT')
        },
        "dimensions": (190, 361),
        "dimensions_0_0_1_0": (190, 381),
        "dimensions_0_0_1_1": (190, 381),
        "dimensions_0_0_1_2": (190, 381),
        "dimensions_0_0_1_3": (190, 381),
        "dimensions_0_0_1_4": (190, 381),
        "dimensions_0_0_1_5": (190, 381),
        "dimensions_0_0_1_6": (190, 381),
        "dimensions_0_0_2_0": (190, 403),
        "dimensions_0_0_2_1": (190, 403),
        "dimensions_0_0_2_2": (190, 403),
        "dimensions_0_0_2_3": (190, 403),
        "dimensions_0_0_2_4": (190, 403),
        "dimensions_0_0_2_5": (190, 403),
        "dimensions_0_0_2_6": (190, 403),
        "dimensions_0_1_1_0": (190, 381),
        "dimensions_0_1_1_1": (190, 381),
        "dimensions_0_1_1_2": (190, 381),
        "dimensions_0_1_1_3": (190, 381),
        "dimensions_0_1_1_4": (190, 381),
        "dimensions_0_1_1_5": (190, 381),
        "dimensions_0_1_1_6": (190, 381),
        "dimensions_0_1_2_0": (190, 403),
        "dimensions_0_1_2_1": (190, 403),
        "dimensions_0_1_2_2": (190, 403),
        "dimensions_0_1_2_3": (190, 403),
        "dimensions_0_1_2_4": (190, 403),
        "dimensions_0_1_2_5": (190, 403),
        "dimensions_0_1_2_6": (190, 403),
        "dimensions_0_2_1_0": (190, 381),
        "dimensions_0_2_1_1": (190, 381),
        "dimensions_0_2_1_2": (190, 381),
        "dimensions_0_2_1_3": (190, 381),
        "dimensions_0_2_1_4": (190, 381),
        "dimensions_0_2_1_5": (190, 381),
        "dimensions_0_2_1_6": (190, 381),
        "dimensions_0_2_2_0": (190, 403),
        "dimensions_0_2_2_1": (190, 403),
        "dimensions_0_2_2_2": (190, 403),
        "dimensions_0_2_2_3": (190, 403),
        "dimensions_0_2_2_4": (190, 403),
        "dimensions_0_2_2_5": (190, 403),
        "dimensions_0_2_2_6": (190, 403),
        "dimensions_0_3_1_0": (190, 381),
        "dimensions_0_3_1_1": (190, 381),
        "dimensions_0_3_1_2": (190, 381),
        "dimensions_0_3_1_3": (190, 381),
        "dimensions_0_3_1_4": (190, 381),
        "dimensions_0_3_1_5": (190, 381),
        "dimensions_0_3_1_6": (190, 381),
        "dimensions_0_3_2_0": (190, 403),
        "dimensions_0_3_2_1": (190, 403),
        "dimensions_0_3_2_2": (190, 403),
        "dimensions_0_3_2_3": (190, 403),
        "dimensions_0_3_2_4": (190, 403),
        "dimensions_0_3_2_5": (190, 403),
        "dimensions_0_3_2_6": (190, 403),
        "dimensions_0_4_1_0": (190, 381),
        "dimensions_0_4_1_1": (190, 381),
        "dimensions_0_4_1_2": (190, 381),
        "dimensions_0_4_1_3": (190, 381),
        "dimensions_0_4_1_4": (190, 381),
        "dimensions_0_4_1_5": (190, 381),
        "dimensions_0_4_1_6": (190, 381),
        "dimensions_0_4_2_0": (190, 403),
        "dimensions_0_4_2_1": (190, 403),
        "dimensions_0_4_2_2": (190, 403),
        "dimensions_0_4_2_3": (190, 403),
        "dimensions_0_4_2_4": (190, 403),
        "dimensions_0_4_2_5": (190, 403),
        "dimensions_0_4_2_6": (190, 403),
        "dimensions_1_0_1_0": (190, 381),
        "dimensions_1_0_1_1": (190, 381),
        "dimensions_1_0_1_2": (190, 381),
        "dimensions_1_0_1_3": (190, 381),
        "dimensions_1_0_1_4": (190, 381),
        "dimensions_1_0_1_5": (190, 381),
        "dimensions_1_0_1_6": (190, 381),
        "dimensions_1_0_2_0": (190, 403),
        "dimensions_1_0_2_1": (190, 403),
        "dimensions_1_0_2_2": (190, 403),
        "dimensions_1_0_2_3": (190, 403),
        "dimensions_1_0_2_4": (190, 403),
        "dimensions_1_0_2_5": (190, 403),
        "dimensions_1_0_2_6": (190, 403),
        "dimensions_1_1_1_0": (190, 381),
        "dimensions_1_1_1_1": (190, 381),
        "dimensions_1_1_1_2": (190, 381),
        "dimensions_1_1_1_3": (190, 381),
        "dimensions_1_1_1_4": (190, 381),
        "dimensions_1_1_1_5": (190, 381),
        "dimensions_1_1_1_6": (190, 381),
        "dimensions_1_1_2_0": (190, 403),
        "dimensions_1_1_2_1": (190, 403),
        "dimensions_1_1_2_2": (190, 403),
        "dimensions_1_1_2_3": (190, 403),
        "dimensions_1_1_2_4": (190, 403),
        "dimensions_1_1_2_5": (190, 403),
        "dimensions_1_1_2_6": (190, 403),
        "dimensions_1_2_1_0": (190, 381),
        "dimensions_1_2_1_1": (190, 381),
        "dimensions_1_2_1_2": (190, 381),
        "dimensions_1_2_1_3": (190, 381),
        "dimensions_1_2_1_4": (190, 381),
        "dimensions_1_2_1_5": (190, 381),
        "dimensions_1_2_1_6": (190, 381),
        "dimensions_1_2_2_0": (190, 403),
        "dimensions_1_2_2_1": (190, 403),
        "dimensions_1_2_2_2": (190, 403),
        "dimensions_1_2_2_3": (190, 403),
        "dimensions_1_2_2_4": (190, 403),
        "dimensions_1_2_2_5": (190, 403),
        "dimensions_1_2_2_6": (190, 403),
        "dimensions_1_3_1_0": (190, 381),
        "dimensions_1_3_1_1": (190, 381),
        "dimensions_1_3_1_2": (190, 381),
        "dimensions_1_3_1_3": (190, 381),
        "dimensions_1_3_1_4": (190, 381),
        "dimensions_1_3_1_5": (190, 381),
        "dimensions_1_3_1_6": (190, 381),
        "dimensions_1_3_2_0": (190, 403),
        "dimensions_1_3_2_1": (190, 403),
        "dimensions_1_3_2_2": (190, 403),
        "dimensions_1_3_2_3": (190, 403),
        "dimensions_1_3_2_4": (190, 403),
        "dimensions_1_3_2_5": (190, 403),
        "dimensions_1_3_2_6": (190, 403),
        "dimensions_1_4_1_0": (190, 381),
        "dimensions_1_4_1_1": (190, 381),
        "dimensions_1_4_1_2": (190, 381),
        "dimensions_1_4_1_3": (190, 381),
        "dimensions_1_4_1_4": (190, 381),
        "dimensions_1_4_1_5": (190, 381),
        "dimensions_1_4_1_6": (190, 381),
        "dimensions_1_4_2_0": (190, 403),
        "dimensions_1_4_2_1": (190, 403),
        "dimensions_1_4_2_2": (190, 403),
        "dimensions_1_4_2_3": (190, 403),
        "dimensions_1_4_2_4": (190, 403),
        "dimensions_1_4_2_5": (190, 403),
        "dimensions_1_4_2_6": (190, 403),
        "dimensions_2_0_1_0": (190, 381),
        "dimensions_2_0_1_1": (190, 381),
        "dimensions_2_0_1_2": (190, 381),
        "dimensions_2_0_1_3": (190, 381),
        "dimensions_2_0_1_4": (190, 381),
        "dimensions_2_0_1_5": (190, 381),
        "dimensions_2_0_1_6": (190, 381),
        "dimensions_2_0_2_0": (190, 403),
        "dimensions_2_0_2_1": (190, 403),
        "dimensions_2_0_2_2": (190, 403),
        "dimensions_2_0_2_3": (190, 403),
        "dimensions_2_0_2_4": (190, 403),
        "dimensions_2_0_2_5": (190, 403),
        "dimensions_2_0_2_6": (190, 403),
        "dimensions_2_1_1_0": (190, 381),
        "dimensions_2_1_1_1": (190, 381),
        "dimensions_2_1_1_2": (190, 381),
        "dimensions_2_1_1_3": (190, 381),
        "dimensions_2_1_1_4": (190, 381),
        "dimensions_2_1_1_5": (190, 381),
        "dimensions_2_1_1_6": (190, 381),
        "dimensions_2_1_2_0": (190, 403),
        "dimensions_2_1_2_1": (190, 403),
        "dimensions_2_1_2_2": (190, 403),
        "dimensions_2_1_2_3": (190, 403),
        "dimensions_2_1_2_4": (190, 403),
        "dimensions_2_1_2_5": (190, 403),
        "dimensions_2_1_2_6": (190, 403),
        "dimensions_2_2_1_0": (190, 381),
        "dimensions_2_2_1_1": (190, 381),
        "dimensions_2_2_1_2": (190, 381),
        "dimensions_2_2_1_3": (190, 381),
        "dimensions_2_2_1_4": (190, 381),
        "dimensions_2_2_1_5": (190, 381),
        "dimensions_2_2_1_6": (190, 381),
        "dimensions_2_2_2_0": (190, 403),
        "dimensions_2_2_2_1": (190, 403),
        "dimensions_2_2_2_2": (190, 403),
        "dimensions_2_2_2_3": (190, 403),
        "dimensions_2_2_2_4": (190, 403),
        "dimensions_2_2_2_5": (190, 403),
        "dimensions_2_2_2_6": (190, 403),
        "dimensions_2_3_1_0": (190, 381),
        "dimensions_2_3_1_1": (190, 381),
        "dimensions_2_3_1_2": (190, 381),
        "dimensions_2_3_1_3": (190, 381),
        "dimensions_2_3_1_4": (190, 381),
        "dimensions_2_3_1_5": (190, 381),
        "dimensions_2_3_1_6": (190, 381),
        "dimensions_2_3_2_0": (190, 403),
        "dimensions_2_3_2_1": (190, 403),
        "dimensions_2_3_2_2": (190, 403),
        "dimensions_2_3_2_3": (190, 403),
        "dimensions_2_3_2_4": (190, 403),
        "dimensions_2_3_2_5": (190, 403),
        "dimensions_2_3_2_6": (190, 403),
        "dimensions_2_4_1_0": (190, 381),
        "dimensions_2_4_1_1": (190, 381),
        "dimensions_2_4_1_2": (190, 381),
        "dimensions_2_4_1_3": (190, 381),
        "dimensions_2_4_1_4": (190, 381),
        "dimensions_2_4_1_5": (190, 381),
        "dimensions_2_4_1_6": (190, 381),
        "dimensions_2_4_2_0": (190, 403),
        "dimensions_2_4_2_1": (190, 403),
        "dimensions_2_4_2_2": (190, 403),
        "dimensions_2_4_2_3": (190, 403),
        "dimensions_2_4_2_4": (190, 403),
        "dimensions_2_4_2_5": (190, 403),
        "dimensions_2_4_2_6": (190, 403),
        "dimensions_3_0_1_0": (190, 381),
        "dimensions_3_0_1_1": (190, 381),
        "dimensions_3_0_1_2": (190, 381),
        "dimensions_3_0_1_3": (190, 381),
        "dimensions_3_0_1_4": (190, 381),
        "dimensions_3_0_1_5": (190, 381),
        "dimensions_3_0_1_6": (190, 381),
        "dimensions_3_0_2_0": (190, 403),
        "dimensions_3_0_2_1": (190, 403),
        "dimensions_3_0_2_2": (190, 403),
        "dimensions_3_0_2_3": (190, 403),
        "dimensions_3_0_2_4": (190, 403),
        "dimensions_3_0_2_5": (190, 403),
        "dimensions_3_0_2_6": (190, 403),
        "dimensions_3_1_1_0": (190, 381),
        "dimensions_3_1_1_1": (190, 381),
        "dimensions_3_1_1_2": (190, 381),
        "dimensions_3_1_1_3": (190, 381),
        "dimensions_3_1_1_4": (190, 381),
        "dimensions_3_1_1_5": (190, 381),
        "dimensions_3_1_1_6": (190, 381),
        "dimensions_3_1_2_0": (190, 403),
        "dimensions_3_1_2_1": (190, 403),
        "dimensions_3_1_2_2": (190, 403),
        "dimensions_3_1_2_3": (190, 403),
        "dimensions_3_1_2_4": (190, 403),
        "dimensions_3_1_2_5": (190, 403),
        "dimensions_3_1_2_6": (190, 403),
        "dimensions_3_2_1_0": (190, 381),
        "dimensions_3_2_1_1": (190, 381),
        "dimensions_3_2_1_2": (190, 381),
        "dimensions_3_2_1_3": (190, 381),
        "dimensions_3_2_1_4": (190, 381),
        "dimensions_3_2_1_5": (190, 381),
        "dimensions_3_2_1_6": (190, 381),
        "dimensions_3_2_2_0": (190, 403),
        "dimensions_3_2_2_1": (190, 403),
        "dimensions_3_2_2_2": (190, 403),
        "dimensions_3_2_2_3": (190, 403),
        "dimensions_3_2_2_4": (190, 403),
        "dimensions_3_2_2_5": (190, 403),
        "dimensions_3_2_2_6": (190, 403),
        "dimensions_3_3_1_0": (190, 381),
        "dimensions_3_3_1_1": (190, 381),
        "dimensions_3_3_1_2": (190, 381),
        "dimensions_3_3_1_3": (190, 381),
        "dimensions_3_3_1_4": (190, 381),
        "dimensions_3_3_1_5": (190, 381),
        "dimensions_3_3_1_6": (190, 381),
        "dimensions_3_3_2_0": (190, 403),
        "dimensions_3_3_2_1": (190, 403),
        "dimensions_3_3_2_2": (190, 403),
        "dimensions_3_3_2_3": (190, 403),
        "dimensions_3_3_2_4": (190, 403),
        "dimensions_3_3_2_5": (190, 403),
        "dimensions_3_3_2_6": (190, 403),
        "dimensions_3_4_1_0": (190, 381),
        "dimensions_3_4_1_1": (190, 381),
        "dimensions_3_4_1_2": (190, 381),
        "dimensions_3_4_1_3": (190, 381),
        "dimensions_3_4_1_4": (190, 381),
        "dimensions_3_4_1_5": (190, 381),
        "dimensions_3_4_1_6": (190, 381),
        "dimensions_3_4_2_0": (190, 403),
        "dimensions_3_4_2_1": (190, 403),
        "dimensions_3_4_2_2": (190, 403),
        "dimensions_3_4_2_3": (190, 403),
        "dimensions_3_4_2_4": (190, 403),
        "dimensions_3_4_2_5": (190, 403),
        "dimensions_3_4_2_6": (190, 403),
        "dimensions_4_0_1_0": (190, 381),
        "dimensions_4_0_1_1": (190, 381),
        "dimensions_4_0_1_2": (190, 381),
        "dimensions_4_0_1_3": (190, 381),
        "dimensions_4_0_1_4": (190, 381),
        "dimensions_4_0_1_5": (190, 381),
        "dimensions_4_0_1_6": (190, 381),
        "dimensions_4_0_2_0": (190, 403),
        "dimensions_4_0_2_1": (190, 403),
        "dimensions_4_0_2_2": (190, 403),
        "dimensions_4_0_2_3": (190, 403),
        "dimensions_4_0_2_4": (190, 403),
        "dimensions_4_0_2_5": (190, 403),
        "dimensions_4_0_2_6": (190, 403),
        "dimensions_4_1_1_0": (190, 381),
        "dimensions_4_1_1_1": (190, 381),
        "dimensions_4_1_1_2": (190, 381),
        "dimensions_4_1_1_3": (190, 381),
        "dimensions_4_1_1_4": (190, 381),
        "dimensions_4_1_1_5": (190, 381),
        "dimensions_4_1_1_6": (190, 381),
        "dimensions_4_1_2_0": (190, 403),
        "dimensions_4_1_2_1": (190, 403),
        "dimensions_4_1_2_2": (190, 403),
        "dimensions_4_1_2_3": (190, 403),
        "dimensions_4_1_2_4": (190, 403),
        "dimensions_4_1_2_5": (190, 403),
        "dimensions_4_1_2_6": (190, 403),
        "dimensions_4_2_1_0": (190, 381),
        "dimensions_4_2_1_1": (190, 381),
        "dimensions_4_2_1_2": (190, 381),
        "dimensions_4_2_1_3": (190, 381),
        "dimensions_4_2_1_4": (190, 381),
        "dimensions_4_2_1_5": (190, 381),
        "dimensions_4_2_1_6": (190, 381),
        "dimensions_4_2_2_0": (190, 403),
        "dimensions_4_2_2_1": (190, 403),
        "dimensions_4_2_2_2": (190, 403),
        "dimensions_4_2_2_3": (190, 403),
        "dimensions_4_2_2_4": (190, 403),
        "dimensions_4_2_2_5": (190, 403),
        "dimensions_4_2_2_6": (190, 403),
        "dimensions_4_3_1_0": (190, 381),
        "dimensions_4_3_1_1": (190, 381),
        "dimensions_4_3_1_2": (190, 381),
        "dimensions_4_3_1_3": (190, 381),
        "dimensions_4_3_1_4": (190, 381),
        "dimensions_4_3_1_5": (190, 381),
        "dimensions_4_3_1_6": (190, 381),
        "dimensions_4_3_2_0": (190, 403),
        "dimensions_4_3_2_1": (190, 403),
        "dimensions_4_3_2_2": (190, 403),
        "dimensions_4_3_2_3": (190, 403),
        "dimensions_4_3_2_4": (190, 403),
        "dimensions_4_3_2_5": (190, 403),
        "dimensions_4_3_2_6": (190, 403),
        "dimensions_4_4_1_0": (190, 381),
        "dimensions_4_4_1_1": (190, 381),
        "dimensions_4_4_1_2": (190, 381),
        "dimensions_4_4_1_3": (190, 381),
        "dimensions_4_4_1_4": (190, 381),
        "dimensions_4_4_1_5": (190, 381),
        "dimensions_4_4_1_6": (190, 381),
        "dimensions_4_4_2_0": (190, 403),
        "dimensions_4_4_2_1": (190, 403),
        "dimensions_4_4_2_2": (190, 403),
        "dimensions_4_4_2_3": (190, 403),
        "dimensions_4_4_2_4": (190, 403),
        "dimensions_4_4_2_5": (190, 403),
        "dimensions_4_4_2_6": (190, 403)
    },
    "GeometryNodeSubdivideCurve": {
        "dimensions": (140, 97)
    },
    "GeometryNodeSubdivideMesh": {
        "dimensions": (140, 97)
    },
    "GeometryNodeSubdivisionSurface": {
        "params_enum": {
            "boundary_smooth": ('PRESERVE_CORNERS', 'ALL'),
            "uv_smooth": ('NONE', 'PRESERVE_CORNERS', 'PRESERVE_CORNERS_AND_JUNCTIONS', 'PRESERVE_CORNERS_JUNCTIONS_AND_CONCAVE', 'PRESERVE_BOUNDARIES', 'SMOOTH_ALL')
        },
        "dimensions": (150, 196)
    },
    "GeometryNodeSwitch": {
        "params_enum": {
            "input_type": ('FLOAT', 'INT', 'BOOLEAN', 'VECTOR', 'STRING', 'RGBA', 'OBJECT', 'IMAGE', 'GEOMETRY', 'COLLECTION', 'TEXTURE', 'MATERIAL')
        },
        "dimensions": (140, 153),
        "dimensions_3": (140, 273),
        "dimensions_7": (140, 149)
    },
    "GeometryNodeTransform": {
        "dimensions": (140, 321)
    },
    "GeometryNodeTranslateInstances": {
        "dimensions": (140, 201)
    },
    "GeometryNodeTriangulate": {
        "params_enum": {
            "ngon_method": ('BEAUTY', 'CLIP'),
            "quad_method": ('BEAUTY', 'FIXED', 'FIXED_ALTERNATE', 'SHORTEST_DIAGONAL', 'LONGEST_DIAGONAL')
        },
        "dimensions": (140, 174)
    },
    "GeometryNodeTrimCurve": {
        "params_enum": {
            "mode": ('FACTOR', 'LENGTH')
        },
        "dimensions": (140, 173),
        "dimensions_1": (140, 171)
    },
    "GeometryNodeUVPackIslands": {
        "dimensions": (140, 141)
    },
    "GeometryNodeUVUnwrap": {
        "params_enum": {
            "method": ('ANGLE_BASED', 'CONFORMAL')
        },
        "dimensions": (140, 171)
    },
    "GeometryNodeVertexOfCorner": {
        "dimensions": (140, 75)
    },
    "GeometryNodeViewer": {
        "params_enum": {
            "data_type": ('FLOAT', 'INT', 'FLOAT_VECTOR', 'FLOAT_COLOR', 'BOOLEAN'),
            "domain": ('AUTO', 'POINT', 'EDGE', 'FACE', 'CORNER', 'CURVE', 'INSTANCE')
        },
        "dimensions": (140, 99),
        "dimensions_4_0": (140, 97),
        "dimensions_4_1": (140, 97),
        "dimensions_4_2": (140, 97),
        "dimensions_4_3": (140, 97),
        "dimensions_4_4": (140, 97),
        "dimensions_4_5": (140, 97),
        "dimensions_4_6": (140, 97)
    },
    "GeometryNodeVolumeCube": {
        "dimensions": (140, 327)
    },
    "GeometryNodeVolumeToMesh": {
        "params_enum": {
            "resolution_mode": ('GRID', 'VOXEL_AMOUNT', 'VOXEL_SIZE')
        },
        "dimensions": (170, 149),
        "dimensions_1": (170, 171),
        "dimensions_2": (170, 171)
    },
    "NodeFrame": {
        "dimensions": (150, 100)
    },
    "NodeGroupInput": {
        "dimensions": (140, 94)
    },
    "NodeGroupOutput": {
        "dimensions": (140, 72)
    },
    "NodeReroute": {
        "dimensions": (16, 16)
    },
    "ShaderNodeClamp": {
        "params_enum": {
            "clamp_type": ('MINMAX', 'RANGE')
        },
        "dimensions": (140, 149)
    },
    "ShaderNodeCombineRGB": {
        "dimensions": (140, 119)
    },
    "ShaderNodeCombineXYZ": {
        "dimensions": (140, 119)
    },
    "ShaderNodeFloatCurve": {
        "dimensions": (240, 292)
    },
    "ShaderNodeMapRange": {
        "params_enum": {
            "data_type": ('FLOAT', 'FLOAT_VECTOR'),
            "interpolation_type": ('LINEAR', 'STEPPED', 'SMOOTHSTEP', 'SMOOTHERSTEP')
        },
        "dimensions": (140, 247),
        "dimensions_0_1": (140, 269),
        "dimensions_0_2": (140, 222),
        "dimensions_0_3": (140, 222),
        "dimensions_1_0": (140, 485),
        "dimensions_1_1": (140, 565),
        "dimensions_1_2": (140, 460),
        "dimensions_1_3": (140, 460)
    },
    "ShaderNodeMath": {
        "params_enum": {
            "operation": ('ADD', 'SUBTRACT', 'MULTIPLY', 'DIVIDE', 'MULTIPLY_ADD', 'POWER', 'LOGARITHM', 'SQRT', 'INVERSE_SQRT', 'ABSOLUTE', 'EXPONENT', 'MINIMUM', 'MAXIMUM', 'LESS_THAN', 'GREATER_THAN', 'SIGN', 'COMPARE', 'SMOOTH_MIN', 'SMOOTH_MAX', 'ROUND', 'FLOOR', 'CEIL', 'TRUNC', 'FRACT', 'MODULO', 'WRAP', 'SNAP', 'PINGPONG', 'SINE', 'COSINE', 'TANGENT', 'ARCSINE', 'ARCCOSINE', 'ARCTANGENT', 'ARCTAN2', 'SINH', 'COSH', 'TANH', 'RADIANS', 'DEGREES')
        },
        "dimensions": (140, 154),
        "dimensions_4": (140, 174),
        "dimensions_7": (140, 132),
        "dimensions_8": (140, 132),
        "dimensions_9": (140, 132),
        "dimensions_10": (140, 132),
        "dimensions_15": (140, 132),
        "dimensions_16": (140, 174),
        "dimensions_17": (140, 174),
        "dimensions_18": (140, 174),
        "dimensions_19": (140, 132),
        "dimensions_20": (140, 132),
        "dimensions_21": (140, 132),
        "dimensions_22": (140, 132),
        "dimensions_23": (140, 132),
        "dimensions_25": (140, 174),
        "dimensions_28": (140, 132),
        "dimensions_29": (140, 132),
        "dimensions_30": (140, 132),
        "dimensions_31": (140, 132),
        "dimensions_32": (140, 132),
        "dimensions_33": (140, 132),
        "dimensions_35": (140, 132),
        "dimensions_36": (140, 132),
        "dimensions_37": (140, 132),
        "dimensions_38": (140, 132),
        "dimensions_39": (140, 132)
    },
    "ShaderNodeMix": {
        "params_enum": {
            "blend_type": ('MIX', 'DARKEN', 'MULTIPLY', 'BURN', 'LIGHTEN', 'SCREEN', 'DODGE', 'ADD', 'OVERLAY', 'SOFT_LIGHT', 'LINEAR_LIGHT', 'DIFFERENCE', 'EXCLUSION', 'SUBTRACT', 'DIVIDE', 'HUE', 'SATURATION', 'COLOR', 'VALUE'),
            "data_type": ('FLOAT', 'VECTOR', 'RGBA'),
            "factor_mode": ('UNIFORM', 'NON_UNIFORM')
        },
        "dimensions": (140, 178),
        "dimensions_0_1_0": (140, 323),
        "dimensions_0_1_1": (140, 383),
        "dimensions_0_2_0": (140, 224),
        "dimensions_0_2_1": (140, 224),
        "dimensions_1_1_0": (140, 323),
        "dimensions_1_1_1": (140, 383),
        "dimensions_1_2_0": (140, 224),
        "dimensions_1_2_1": (140, 224),
        "dimensions_2_1_0": (140, 323),
        "dimensions_2_1_1": (140, 383),
        "dimensions_2_2_0": (140, 224),
        "dimensions_2_2_1": (140, 224),
        "dimensions_3_1_0": (140, 323),
        "dimensions_3_1_1": (140, 383),
        "dimensions_3_2_0": (140, 224),
        "dimensions_3_2_1": (140, 224),
        "dimensions_4_1_0": (140, 323),
        "dimensions_4_1_1": (140, 383),
        "dimensions_4_2_0": (140, 224),
        "dimensions_4_2_1": (140, 224),
        "dimensions_5_1_0": (140, 323),
        "dimensions_5_1_1": (140, 383),
        "dimensions_5_2_0": (140, 224),
        "dimensions_5_2_1": (140, 224),
        "dimensions_6_1_0": (140, 323),
        "dimensions_6_1_1": (140, 383),
        "dimensions_6_2_0": (140, 224),
        "dimensions_6_2_1": (140, 224),
        "dimensions_7_1_0": (140, 323),
        "dimensions_7_1_1": (140, 383),
        "dimensions_7_2_0": (140, 224),
        "dimensions_7_2_1": (140, 224),
        "dimensions_8_1_0": (140, 323),
        "dimensions_8_1_1": (140, 383),
        "dimensions_8_2_0": (140, 224),
        "dimensions_8_2_1": (140, 224),
        "dimensions_9_1_0": (140, 323),
        "dimensions_9_1_1": (140, 383),
        "dimensions_9_2_0": (140, 224),
        "dimensions_9_2_1": (140, 224),
        "dimensions_10_1_0": (140, 323),
        "dimensions_10_1_1": (140, 383),
        "dimensions_10_2_0": (140, 224),
        "dimensions_10_2_1": (140, 224),
        "dimensions_11_1_0": (140, 323),
        "dimensions_11_1_1": (140, 383),
        "dimensions_11_2_0": (140, 224),
        "dimensions_11_2_1": (140, 224),
        "dimensions_12_1_0": (140, 323),
        "dimensions_12_1_1": (140, 383),
        "dimensions_12_2_0": (140, 224),
        "dimensions_12_2_1": (140, 224),
        "dimensions_13_1_0": (140, 323),
        "dimensions_13_1_1": (140, 383),
        "dimensions_13_2_0": (140, 224),
        "dimensions_13_2_1": (140, 224),
        "dimensions_14_1_0": (140, 323),
        "dimensions_14_1_1": (140, 383),
        "dimensions_14_2_0": (140, 224),
        "dimensions_14_2_1": (140, 224),
        "dimensions_15_1_0": (140, 323),
        "dimensions_15_1_1": (140, 383),
        "dimensions_15_2_0": (140, 224),
        "dimensions_15_2_1": (140, 224),
        "dimensions_16_1_0": (140, 323),
        "dimensions_16_1_1": (140, 383),
        "dimensions_16_2_0": (140, 224),
        "dimensions_16_2_1": (140, 224),
        "dimensions_17_1_0": (140, 323),
        "dimensions_17_1_1": (140, 383),
        "dimensions_17_2_0": (140, 224),
        "dimensions_17_2_1": (140, 224),
        "dimensions_18_1_0": (140, 323),
        "dimensions_18_1_1": (140, 383),
        "dimensions_18_2_0": (140, 224),
        "dimensions_18_2_1": (140, 224)
    },
    "ShaderNodeMixRGB": {
        "params_enum": {
            "blend_type": ('MIX', 'DARKEN', 'MULTIPLY', 'BURN', 'LIGHTEN', 'SCREEN', 'DODGE', 'ADD', 'OVERLAY', 'SOFT_LIGHT', 'LINEAR_LIGHT', 'DIFFERENCE', 'EXCLUSION', 'SUBTRACT', 'DIVIDE', 'HUE', 'SATURATION', 'COLOR', 'VALUE')
        },
        "dimensions": (140, 171)
    },
    "ShaderNodeRGBCurve": {
        "dimensions": (240, 292)
    },
    "ShaderNodeSeparateRGB": {
        "dimensions": (140, 119)
    },
    "ShaderNodeSeparateXYZ": {
        "dimensions": (140, 179)
    },
    "ShaderNodeTexBrick": {
        "dimensions": (150, 390)
    },
    "ShaderNodeTexChecker": {
        "dimensions": (140, 163)
    },
    "ShaderNodeTexGradient": {
        "params_enum": {
            "gradient_type": ('LINEAR', 'QUADRATIC', 'EASING', 'DIAGONAL', 'SPHERICAL', 'QUADRATIC_SPHERE', 'RADIAL')
        },
        "dimensions": (140, 127)
    },
    "ShaderNodeTexMagic": {
        "dimensions": (140, 171)
    },
    "ShaderNodeTexMusgrave": {
        "params_enum": {
            "musgrave_dimensions": ('1D', '2D', '3D', '4D'),
            "musgrave_type": ('MULTIFRACTAL', 'RIDGED_MULTIFRACTAL', 'HYBRID_MULTIFRACTAL', 'FBM', 'HETERO_TERRAIN')
        },
        "dimensions": (150, 220),
        "dimensions_0_1": (150, 262),
        "dimensions_0_2": (150, 262),
        "dimensions_0_4": (150, 242),
        "dimensions_1_1": (150, 262),
        "dimensions_1_2": (150, 262),
        "dimensions_1_4": (150, 242),
        "dimensions_2_1": (150, 262),
        "dimensions_2_2": (150, 262),
        "dimensions_2_4": (150, 242),
        "dimensions_3_0": (150, 242),
        "dimensions_3_1": (150, 284),
        "dimensions_3_2": (150, 284),
        "dimensions_3_3": (150, 242),
        "dimensions_3_4": (150, 264)
    },
    "ShaderNodeTexNoise": {
        "params_enum": {
            "noise_dimensions": ('1D', '2D', '3D', '4D')
        },
        "dimensions": (140, 215),
        "dimensions_3": (140, 237)
    },
    "ShaderNodeTexVoronoi": {
        "params_enum": {
            "distance": ('EUCLIDEAN', 'MANHATTAN', 'CHEBYCHEV', 'MINKOWSKI'),
            "feature": ('F1', 'F2', 'SMOOTH_F1', 'DISTANCE_TO_EDGE', 'N_SPHERE_RADIUS'),
            "voronoi_dimensions": ('1D', '2D', '3D', '4D')
        },
        "dimensions": (140, 245),
        "dimensions_0_0_0": (140, 220),
        "dimensions_0_0_3": (140, 289),
        "dimensions_0_1_0": (140, 220),
        "dimensions_0_1_3": (140, 289),
        "dimensions_0_2_0": (140, 242),
        "dimensions_0_2_1": (140, 267),
        "dimensions_0_2_2": (140, 267),
        "dimensions_0_2_3": (140, 311),
        "dimensions_0_3_0": (140, 176),
        "dimensions_0_3_1": (140, 176),
        "dimensions_0_3_2": (140, 176),
        "dimensions_0_3_3": (140, 198),
        "dimensions_0_4_0": (140, 174),
        "dimensions_0_4_1": (140, 174),
        "dimensions_0_4_2": (140, 174),
        "dimensions_0_4_3": (140, 196),
        "dimensions_1_0_0": (140, 220),
        "dimensions_1_0_3": (140, 289),
        "dimensions_1_1_0": (140, 220),
        "dimensions_1_1_3": (140, 289),
        "dimensions_1_2_0": (140, 242),
        "dimensions_1_2_1": (140, 267),
        "dimensions_1_2_2": (140, 267),
        "dimensions_1_2_3": (140, 311),
        "dimensions_1_3_0": (140, 176),
        "dimensions_1_3_1": (140, 176),
        "dimensions_1_3_2": (140, 176),
        "dimensions_1_3_3": (140, 198),
        "dimensions_1_4_0": (140, 174),
        "dimensions_1_4_1": (140, 174),
        "dimensions_1_4_2": (140, 174),
        "dimensions_1_4_3": (140, 196),
        "dimensions_2_0_0": (140, 220),
        "dimensions_2_0_3": (140, 289),
        "dimensions_2_1_0": (140, 220),
        "dimensions_2_1_3": (140, 289),
        "dimensions_2_2_0": (140, 242),
        "dimensions_2_2_1": (140, 267),
        "dimensions_2_2_2": (140, 267),
        "dimensions_2_2_3": (140, 311),
        "dimensions_2_3_0": (140, 176),
        "dimensions_2_3_1": (140, 176),
        "dimensions_2_3_2": (140, 176),
        "dimensions_2_3_3": (140, 198),
        "dimensions_2_4_0": (140, 174),
        "dimensions_2_4_1": (140, 174),
        "dimensions_2_4_2": (140, 174),
        "dimensions_2_4_3": (140, 196),
        "dimensions_3_0_0": (140, 220),
        "dimensions_3_0_1": (140, 267),
        "dimensions_3_0_2": (140, 267),
        "dimensions_3_0_3": (140, 311),
        "dimensions_3_1_0": (140, 220),
        "dimensions_3_1_1": (140, 267),
        "dimensions_3_1_2": (140, 267),
        "dimensions_3_1_3": (140, 311),
        "dimensions_3_2_0": (140, 242),
        "dimensions_3_2_1": (140, 289),
        "dimensions_3_2_2": (140, 289),
        "dimensions_3_2_3": (140, 333),
        "dimensions_3_3_0": (140, 176),
        "dimensions_3_3_1": (140, 176),
        "dimensions_3_3_2": (140, 176),
        "dimensions_3_3_3": (140, 198),
        "dimensions_3_4_0": (140, 174),
        "dimensions_3_4_1": (140, 174),
        "dimensions_3_4_2": (140, 174),
        "dimensions_3_4_3": (140, 196)
    },
    "ShaderNodeTexWave": {
        "params_enum": {
            "bands_direction": ('X', 'Y', 'Z', 'DIAGONAL'),
            "rings_direction": ('X', 'Y', 'Z', 'SPHERICAL'),
            "wave_profile": ('SIN', 'SAW', 'TRI'),
            "wave_type": ('BANDS', 'RINGS')
        },
        "dimensions": (150, 309)
    },
    "ShaderNodeTexWhiteNoise": {
        "params_enum": {
            "noise_dimensions": ('1D', '2D', '3D', '4D')
        },
        "dimensions": (140, 129),
        "dimensions_0": (140, 127),
        "dimensions_3": (140, 149)
    },
    "ShaderNodeValToRGB": {
        "dimensions": (240, 212)
    },
    "ShaderNodeValue": {
        "dimensions": (140, 80)
    },
    "ShaderNodeVectorCurve": {
        "dimensions": (240, 352)
    },
    "ShaderNodeVectorMath": {
        "params_enum": {
            "operation": ('ADD', 'SUBTRACT', 'MULTIPLY', 'DIVIDE', 'MULTIPLY_ADD', 'CROSS_PRODUCT', 'PROJECT', 'REFLECT', 'REFRACT', 'FACEFORWARD', 'DOT_PRODUCT', 'DISTANCE', 'LENGTH', 'SCALE', 'NORMALIZE', 'ABSOLUTE', 'MINIMUM', 'MAXIMUM', 'FLOOR', 'CEIL', 'FRACTION', 'MODULO', 'WRAP', 'SNAP', 'SINE', 'COSINE', 'TANGENT')
        },
        "dimensions": (140, 251),
        "dimensions_4": (140, 333),
        "dimensions_8": (140, 271),
        "dimensions_9": (140, 333),
        "dimensions_10": (140, 249),
        "dimensions_11": (140, 249),
        "dimensions_12": (140, 167),
        "dimensions_13": (140, 189),
        "dimensions_14": (140, 169),
        "dimensions_15": (140, 169),
        "dimensions_18": (140, 169),
        "dimensions_19": (140, 169),
        "dimensions_20": (140, 169),
        "dimensions_22": (140, 333),
        "dimensions_24": (140, 169),
        "dimensions_25": (140, 169),
        "dimensions_26": (140, 169)
    },
    "ShaderNodeVectorRotate": {
        "params_enum": {
            "rotation_type": ('AXIS_ANGLE', 'X_AXIS', 'Y_AXIS', 'Z_AXIS', 'EULER_XYZ')
        },
        "dimensions": (140, 318),
        "dimensions_1": (140, 236),
        "dimensions_2": (140, 236),
        "dimensions_3": (140, 236),
        "dimensions_4": (140, 294)
    },
    "ShaderNodeAddShader": {
        "dimensions": (140, 97)
    },
    "ShaderNodeAmbientOcclusion": {
        "dimensions": (140, 221)
    },
    "ShaderNodeAttribute": {
        "params_enum": {
            "attribute_type": ('GEOMETRY', 'OBJECT', 'INSTANCER', 'VIEW_LAYER')
        },
        "dimensions": (140, 171)
    },
    "ShaderNodeBackground": {
        "dimensions": (140, 99)
    },
    "ShaderNodeBevel": {
        "dimensions": (140, 127)
    },
    "ShaderNodeBlackbody": {
        "dimensions": (150, 75)
    },
    "ShaderNodeBrightContrast": {
        "dimensions": (140, 119)
    },
    "ShaderNodeBsdfAnisotropic": {
        "params_enum": {
            "distribution": ('BECKMANN', 'GGX', 'MULTI_GGX', 'ASHIKHMIN_SHIRLEY')
        },
        "dimensions": (150, 217)
    },
    "ShaderNodeBsdfDiffuse": {
        "dimensions": (150, 121)
    },
    "ShaderNodeBsdfGlass": {
        "params_enum": {
            "distribution": ('SHARP', 'BECKMANN', 'GGX', 'MULTI_GGX')
        },
        "dimensions": (150, 173)
    },
    "ShaderNodeBsdfGlossy": {
        "params_enum": {
            "distribution": ('SHARP', 'BECKMANN', 'GGX', 'ASHIKHMIN_SHIRLEY', 'MULTI_GGX')
        },
        "dimensions": (150, 151)
    },
    "ShaderNodeBsdfHair": {
        "params_enum": {
            "component": ('Reflection', 'Transmission')
        },
        "dimensions": (150, 195)
    },
    "ShaderNodeBsdfHairPrincipled": {
        "params_enum": {
            "parametrization": ('ABSORPTION', 'MELANIN', 'COLOR')
        },
        "dimensions": (240, 261),
        "dimensions_0": (240, 321),
        "dimensions_1": (240, 327)
    },
    "ShaderNodeBsdfPrincipled": {
        "params_enum": {
            "distribution": ('GGX', 'MULTI_GGX'),
            "subsurface_method": ('BURLEY', 'RANDOM_WALK_FIXED_RADIUS', 'RANDOM_WALK')
        },
        "dimensions": (240, 660),
        "dimensions_0_0": (240, 616),
        "dimensions_1_0": (240, 594),
        "dimensions_1_1": (240, 638),
        "dimensions_1_2": (240, 638)
    },
    "ShaderNodeBsdfRefraction": {
        "params_enum": {
            "distribution": ('SHARP', 'BECKMANN', 'GGX')
        },
        "dimensions": (150, 173)
    },
    "ShaderNodeBsdfToon": {
        "params_enum": {
            "component": ('DIFFUSE', 'GLOSSY')
        },
        "dimensions": (150, 173)
    },
    "ShaderNodeBsdfTranslucent": {
        "dimensions": (140, 99)
    },
    "ShaderNodeBsdfTransparent": {
        "dimensions": (140, 77)
    },
    "ShaderNodeBsdfVelvet": {
        "dimensions": (140, 121)
    },
    "ShaderNodeBump": {
        "dimensions": (140, 171)
    },
    "ShaderNodeCameraData": {
        "dimensions": (140, 94)
    },
    "ShaderNodeCombineColor": {
        "params_enum": {
            "mode": ('RGB', 'HSV', 'HSL')
        },
        "dimensions": (140, 149)
    },
    "ShaderNodeCombineHSV": {
        "dimensions": (140, 119)
    },
    "ShaderNodeDisplacement": {
        "params_enum": {
            "space": ('OBJECT', 'WORLD')
        },
        "dimensions": (140, 171)
    },
    "ShaderNodeEeveeSpecular": {
        "dimensions": (140, 275)
    },
    "ShaderNodeEmission": {
        "dimensions": (140, 99)
    },
    "ShaderNodeFresnel": {
        "dimensions": (140, 97)
    },
    "ShaderNodeGamma": {
        "dimensions": (140, 97)
    },
    "ShaderNodeGroup": {
        "dimensions": (140, 50)
    },
    "ShaderNodeHairInfo": {
        "dimensions": (140, 160)
    },
    "ShaderNodeHoldout": {
        "dimensions": (140, 55)
    },
    "ShaderNodeHueSaturation": {
        "dimensions": (150, 163)
    },
    "ShaderNodeInvert": {
        "dimensions": (140, 97)
    },
    "ShaderNodeLayerWeight": {
        "dimensions": (140, 119)
    },
    "ShaderNodeLightFalloff": {
        "dimensions": (150, 141)
    },
    "ShaderNodeLightPath": {
        "dimensions": (140, 314)
    },
    "ShaderNodeMapping": {
        "params_enum": {
            "vector_type": ('POINT', 'TEXTURE', 'VECTOR', 'NORMAL')
        },
        "dimensions": (140, 411),
        "dimensions_2": (140, 329),
        "dimensions_3": (140, 329)
    },
    "ShaderNodeMixShader": {
        "dimensions": (140, 119)
    },
    "ShaderNodeNewGeometry": {
        "dimensions": (140, 226)
    },
    "ShaderNodeNormal": {
        "dimensions": (140, 207)
    },
    "ShaderNodeNormalMap": {
        "params_enum": {
            "space": ('TANGENT', 'OBJECT', 'WORLD', 'BLENDER_OBJECT', 'BLENDER_WORLD')
        },
        "dimensions": (150, 152),
        "dimensions_1": (150, 127),
        "dimensions_2": (150, 127),
        "dimensions_3": (150, 127),
        "dimensions_4": (150, 127)
    },
    "ShaderNodeObjectInfo": {
        "dimensions": (140, 160)
    },
    "ShaderNodeOutputAOV": {
        "dimensions": (140, 97)
    },
    "ShaderNodeOutputLight": {
        "params_enum": {
            "target": ('ALL', 'EEVEE', 'CYCLES')
        },
        "dimensions": (140, 75)
    },
    "ShaderNodeOutputLineStyle": {
        "params_enum": {
            "blend_type": ('MIX', 'DARKEN', 'MULTIPLY', 'BURN', 'LIGHTEN', 'SCREEN', 'DODGE', 'ADD', 'OVERLAY', 'SOFT_LIGHT', 'LINEAR_LIGHT', 'DIFFERENCE', 'EXCLUSION', 'SUBTRACT', 'DIVIDE', 'HUE', 'SATURATION', 'COLOR', 'VALUE'),
            "target": ('ALL', 'EEVEE', 'CYCLES')
        },
        "dimensions": (140, 163)
    },
    "ShaderNodeOutputMaterial": {
        "params_enum": {
            "target": ('ALL', 'EEVEE', 'CYCLES')
        },
        "dimensions": (140, 121)
    },
    "ShaderNodeOutputWorld": {
        "params_enum": {
            "target": ('ALL', 'EEVEE', 'CYCLES')
        },
        "dimensions": (140, 97)
    },
    "ShaderNodeParticleInfo": {
        "dimensions": (140, 204)
    },
    "ShaderNodePointInfo": {
        "dimensions": (140, 94)
    },
    "ShaderNodeRGB": {
        "dimensions": (140, 182)
    },
    "ShaderNodeRGBToBW": {
        "dimensions": (140, 75)
    },
    "ShaderNodeScript": {
        "params_enum": {
            "mode": ('INTERNAL', 'EXTERNAL')
        },
        "dimensions": (140, 75)
    },
    "ShaderNodeSeparateColor": {
        "params_enum": {
            "mode": ('RGB', 'HSV', 'HSL')
        },
        "dimensions": (140, 149)
    },
    "ShaderNodeSeparateHSV": {
        "dimensions": (140, 119)
    },
    "ShaderNodeShaderToRGB": {
        "dimensions": (140, 97)
    },
    "ShaderNodeSqueeze": {
        "dimensions": (140, 119)
    },
    "ShaderNodeSubsurfaceScattering": {
        "params_enum": {
            "falloff": ('BURLEY', 'RANDOM_WALK_FIXED_RADIUS', 'RANDOM_WALK')
        },
        "dimensions": (150, 217),
        "dimensions_0": (150, 173)
    },
    "ShaderNodeTangent": {
        "params_enum": {
            "axis": ('X', 'Y', 'Z'),
            "direction_type": ('RADIAL', 'UV_MAP')
        },
        "dimensions": (150, 80)
    },
    "ShaderNodeTexCoord": {
        "dimensions": (140, 237)
    },
    "ShaderNodeTexEnvironment": {
        "params_enum": {
            "interpolation": ('Linear', 'Closest', 'Cubic', 'Smart'),
            "projection": ('EQUIRECTANGULAR', 'MIRROR_BALL')
        },
        "dimensions": (240, 155)
    },
    "ShaderNodeTexIES": {
        "params_enum": {
            "mode": ('INTERNAL', 'EXTERNAL')
        },
        "dimensions": (140, 152)
    },
    "ShaderNodeTexImage": {
        "params_enum": {
            "extension": ('REPEAT', 'EXTEND', 'CLIP', 'MIRROR'),
            "interpolation": ('Linear', 'Closest', 'Cubic', 'Smart'),
            "projection": ('FLAT', 'BOX', 'SPHERE', 'TUBE')
        },
        "dimensions": (240, 202),
        "dimensions_0_0_1": (240, 227),
        "dimensions_0_1_1": (240, 227),
        "dimensions_0_2_1": (240, 227),
        "dimensions_0_3_1": (240, 227),
        "dimensions_1_0_1": (240, 227),
        "dimensions_1_1_1": (240, 227),
        "dimensions_1_2_1": (240, 227),
        "dimensions_1_3_1": (240, 227),
        "dimensions_2_0_1": (240, 227),
        "dimensions_2_1_1": (240, 227),
        "dimensions_2_2_1": (240, 227),
        "dimensions_2_3_1": (240, 227),
        "dimensions_3_0_1": (240, 227),
        "dimensions_3_1_1": (240, 227),
        "dimensions_3_2_1": (240, 227),
        "dimensions_3_3_1": (240, 227)
    },
    "ShaderNodeTexPointDensity": {
        "params_enum": {
            "interpolation": ('Closest', 'Linear', 'Cubic'),
            "particle_color_source": ('PARTICLE_AGE', 'PARTICLE_SPEED', 'PARTICLE_VELOCITY'),
            "point_source": ('PARTICLE_SYSTEM', 'OBJECT'),
            "space": ('OBJECT', 'WORLD'),
            "vertex_color_source": ('VERTEX_COLOR', 'VERTEX_WEIGHT', 'VERTEX_NORMAL')
        },
        "dimensions": (140, 277)
    },
    "ShaderNodeTexSky": {
        "params_enum": {
            "sky_type": ('PREETHAM', 'HOSEK_WILKIE', 'NISHITA')
        },
        "dimensions": (150, 315),
        "dimensions_0": (150, 195),
        "dimensions_1": (150, 220)
    },
    "ShaderNodeUVAlongStroke": {
        "dimensions": (140, 80)
    },
    "ShaderNodeUVMap": {
        "dimensions": (150, 105)
    },
    "ShaderNodeVectorDisplacement": {
        "params_enum": {
            "space": ('TANGENT', 'OBJECT', 'WORLD')
        },
        "dimensions": (140, 149)
    },
    "ShaderNodeVectorTransform": {
        "params_enum": {
            "convert_from": ('WORLD', 'OBJECT', 'CAMERA'),
            "convert_to": ('WORLD', 'OBJECT', 'CAMERA'),
            "vector_type": ('POINT', 'VECTOR', 'NORMAL')
        },
        "dimensions": (140, 215)
    },
    "ShaderNodeVertexColor": {
        "dimensions": (140, 102)
    },
    "ShaderNodeVolumeAbsorption": {
        "dimensions": (140, 99)
    },
    "ShaderNodeVolumeInfo": {
        "dimensions": (140, 116)
    },
    "ShaderNodeVolumePrincipled": {
        "dimensions": (240, 319)
    },
    "ShaderNodeVolumeScatter": {
        "dimensions": (140, 121)
    },
    "ShaderNodeWavelength": {
        "dimensions": (150, 75)
    },
    "ShaderNodeWireframe": {
        "dimensions": (140, 105)
    }
}
