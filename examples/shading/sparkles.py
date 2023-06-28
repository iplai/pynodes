from pynodes import *
from pynodes.math import *


@tree
def sparkles_mat():
    """@Material"""

    shader = BSDF.Emission()

    noise_texture = WhiteNoiseTexture("1D", w=shader.object_info.random)

    image_texture = ImageTexture(vector=shader.attribute("uv_map").vector)

    shader['Color'] = noise_texture.color * 2

    shader['Strength'] = image_texture.color.Float * shader.attribute("a", "INSTANCER").fac.map_range(0.7, 1, 1, 0, "SMOOTHERSTEP")

    return shader.add_shader(BSDF.Transparent())


@tree
def sparkles():

    with frame("The value to store"):

        a = (SceneTime().seconds * 0.5 + RandomFloat(0, 10)).fract

    with frame("Position of the points"):

        pos = RandomVector((-1, -1, 0), (1, 1, 0)).normalize * a * 5

    with frame("Points"):

        points = InputPoints(100, position=pos).store_named_attribute("a", a)

    with frame("Scale of the sparkles"):

        scale = (sin(a * 16 + RandomFloat(0, 10)) * 0.5 + 0.5) * a.map_range(0, 0.9, 4, 0, interpolation_type="SMOOTHSTEP")

    with frame("Sparkles Mat"):

        grid = MeshGrid(1, 1, 2, 2)

        mesh = grid.mesh.store_named_attribute("uv_map", grid.uv_map).on_points(points, scale=scale).set_material("Sparkles Mat")

    return mesh


bpy.data.materials["Sparkles Mat"].blend_method = "BLEND"
