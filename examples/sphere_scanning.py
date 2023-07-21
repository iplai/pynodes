from pynodes import *


@tree
def sphere_scanning():
    w = SceneTime().seconds * 0.2
    color = MusgraveTexture("4D", w=w, scale=2.7).height.color_ramp_with_position([(0.1, 0), (0.15, 1)], interpolation="B_SPLINE")
    mesh = MeshUVSphere(126, 110, 1).mesh.triangulate().dual_mesh().split_edges().scale_elements(scale=color).\
        extrude_faces(offset_scale=color.Float.map_range(0, 1, -0.3, 0.1)).mesh.transform(rotation=(0, 0, SceneTime().seconds * 0.5))
    return mesh
