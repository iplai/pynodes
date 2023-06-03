from pynodes import *
from pynodes.colors import hex_color_to_rgba
from pynodes.utils import load_text

bpy.context.scene.view_settings.view_transform = "Standard"
bpy.data.scenes["Scene"].render.engine = "CYCLES"
bpy.data.scenes["Scene"].cycles.shading_system = True

import os
load_text(f"{os.getcwd()}/osl/castironcover.osl")
load_text(f"{os.getcwd()}/osl/checker.osl")
load_text(f"{os.getcwd()}/osl/noise.osl")
load_text(f"{os.getcwd()}/osl/colorname.osl")
load_text(f"{os.getcwd()}/osl/colorrange.osl")
load_text(f"{os.getcwd()}/osl/diamondplate.osl")
load_text(f"{os.getcwd()}/osl/dots.osl")
load_text(f"{os.getcwd()}/osl/droplet.osl")
load_text(f"{os.getcwd()}/osl/droplets.osl")


@tree
def castiron_cover():
    """@material"""

    with frame("Castiron Cover"):
        node = ShaderScript(script="castironcover.osl", vector=TextureCoord().uv, scale=1)
        factor = node['Fac'].Float

    with frame("Normal"):
        normal = (factor + NoiseTexture(scale=100).fac * 0.06).to_normal(distance=0.1)

    with frame("Diffuse and Glossy"):
        shader = MixShader(BSDF.Diffuse(color="#1b7cb4", normal=normal, roughness=0.4), BSDF.Glossy(normal=normal, roughness=0.3), 0.2)

    with frame("Switch Transparent"):
        shader = MixShader(shader, BSDF.Transparent(), factor.less_than(0.005))

    return shader


@tree
def checker_board():
    """@material"""

    node = ShaderScript(script="checker.osl", vector=TextureCoord().uv.mapping())

    return node["Color"]


@tree
def color_range():
    """@material"""

    node = ShaderScript(script="colorrange.osl", value=NoiseTexture().fac, low=0.4, high=0.5)

    return node["Color"]


@tree
def color_name():
    """@material"""
    with frame("Only CPU"):
        node = ShaderScript(script="colorname.osl", file_path=f"{os.getcwd()}/osl/colors.xml")

    return node["Color"]


@tree
def simple_noise():
    """@material"""

    node = ShaderScript(script="noise.osl", vector=TextureCoord().uv.mapping())

    return node["Color"]


@tree
def dots():
    """@material"""

    with frame("CPU only"):
        node = ShaderScript(script="dots.osl", pos=TextureCoord().object.mapping(), scale=1)

    factor, color = node['Fac'].Float, node['Color'].Color

    shader = MixShader(factor, color)

    with frame("Black background to Transparent"):
        shader = MixShader(shader, BSDF.Transparent(), factor.compare(0, 0))

    return shader


def set_color_ramp(socket: Socket):
    bnode: bpy.types.ShaderNodeValToRGB = socket.node.bnode
    color_ramp = bnode.color_ramp
    color_ramp.interpolation = "B_SPLINE"
    color_ramp.elements.new(0.199)
    color_ramp.elements[0].position = 0.063
    color_ramp.elements[2].position = 0.643
    color_ramp.elements[1].color = hex_color_to_rgba("#613B35")


@tree
def diamond_plate():
    """@material"""

    vector = TextureCoord().uv

    node = ShaderScript(script="diamondplate.osl", vector=vector, scale=16)

    factor, disp = node['Fac'].Float, node['Disp'].Float

    with frame("Factor to Color"):

        color = (factor + NoiseTexture(vector=vector, scale=100).fac * 0.3).to_color()

    set_color_ramp(color)

    with frame("Displacement to Normal"):

        normal = disp.to_normal(strength=0.51, distance=0.1)

    with frame("Mix Shader"):

        shader = MixShader(BSDF.Diffuse(color, 0.1, normal), BSDF.Anisotropic("BECKMANN", roughness=0.316, anisotropy=0.2), 0.4)

    return shader


@tree
def droplet_wrapper(pos: Vector, time: Float = (0.3, 0, 2), end_time: Float = 2, spread: Float = 1):
    """@shader"""

    node = ShaderScript(script="droplet.osl", pos=pos, time=time, end_time=end_time, spread=spread)

    return node.height


@tree
def water_droplet():
    """@material"""

    height = droplet_wrapper(pos=TextureCoord().uv.mapping())

    shader = BSDF.Glossy(normal=height.to_normal(strength=0.1, distance=0.1), roughness=0.0001)

    return shader


@tree
def droplets_wrapper(pos: Vector, drops: Integer = 3, time: Float = (0, 0, 10), end_time: Float = 10, spread: Float = 0.03):
    """@shader"""

    node = ShaderScript(script="droplets.osl", pos=pos, drops=drops, time=time, end_time=end_time, spread=spread)

    return node.height


@tree
def water_droplets():
    """@material"""

    height = droplets_wrapper(pos=TextureCoord().uv.mapping())

    shader = BSDF.Glossy(normal=height.to_normal(strength=0.1, distance=0.1), roughness=0.25)

    return shader


@tree
def world():
    """@world"""
    return Shader.Background()


from pynodes.scene import *

scene = Tree({
    O.plane @ "Castiron Cover": {
        Mat.slots: ["Castiron Cover"],
    },
    O.plane @ "Checker Board": {
        Mat.slots: ["Checker Board"],
    },
    O.plane @ "Simple Noise": {
        Mat.slots: ["Simple Noise"],
    },
    O.plane @ "Color Range": {
        Mat.slots: ["Color Range"],
    },
    O.plane @ "Diamond Plate": {
        Mat.slots: ["Diamond Plate"],
    },
    O.plane @ "Dots": {
        Mat.slots: ["Dots"],
    },
    O.plane @ "Water Droplet": {
        Mat.slots: ["Water Droplet"],
    },
}).load()
