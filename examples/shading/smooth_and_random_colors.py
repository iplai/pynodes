from pynodes import *


@tree
def random_color():
    """@material"""
    shader = BSDF.Principled()
    # a list with ten bright hex color strings
    bright_colors = ["#ff0000", "#ff8000", "#ffff00", "#80ff00", "#00ff00", "#00ff80", "#00ffff", "#0080ff", "#0000ff", "#8000ff"]
    shader['Base Color'] = shader.object_info.random.color_ramp_uniform(*bright_colors)
    shader['roughness'] = 0.1
    return shader


@tree
def geometry_nodes(mesh: Mesh):
    return MeshIcoSphere(subdivisions=3).mesh.on_points(MeshIcoSphere(subdivisions=2).mesh).set_shade_smooth().set_material("random_color")
