from pynodes import *

bpy.data.scenes["Scene"].view_settings.view_transform = "Standard"


def set_color_ramp(socket: Socket):
    bnode: bpy.types.ShaderNodeValToRGB = socket.node.bnode
    color_ramp = bnode.color_ramp
    color_ramp.interpolation = "CONSTANT"
    ramp_steps = 8

    for _ in range(ramp_steps - 2):
        color_ramp.elements.new(0)

    for i in range(ramp_steps):
        element = color_ramp.elements[i]
        element.position = i / (ramp_steps - 1)
        c = rgb(245, 120, 193)
        c.v = (0.5 if i == 0 else i) / (ramp_steps - 1)
        element.color = *c, 1


@tree
def inner_faces_shader(color: Color):
    """@shader"""

    shader = BSDF.Transparent()

    shader = shader.mix(BSDF.Emission(color), fac=shader.geometry.backfacing)

    return shader


@tree
def inner_faces_shader_with_hole(color: Color, hole_y: Float = 0.5):
    """@shader"""

    geometry = ShaderGeometry()

    fac = geometry.backfacing + geometry.position.y.less_than(hole_y)

    shader = BSDF.Transparent().mix(BSDF.Emission(color), fac=fac)

    return shader


@tree
def ramped_diffuse_color():
    """@shader"""

    color = BSDF.Diffuse().to_rgb().color

    color = color.Float.float_curve(points=[(0, 0), (0.25, 0.2), (0.8, 0.85), (1, 1)])

    color = ColorRamp(fac=color).color

    set_color_ramp(color)

    return color


@tree
def ramped_diffuse_color():
    """@shader"""

    color = BSDF.Diffuse().to_rgb().color

    color = color.Float.float_curve(points=[(0, 0), (0.25, 0.2), (0.8, 0.85), (1, 1)])

    color = ColorRamp(fac=color).color

    set_color_ramp(color)

    return color


def set_color_ramp_2(socket: Socket):
    bnode: bpy.types.ShaderNodeValToRGB = socket.node.bnode
    color_ramp = bnode.color_ramp
    color_ramp.interpolation = "B_SPLINE"
    element = color_ramp.elements[0]
    element.position = 0.4
    element.color = *rgb(243, 136, 229), 1
    element = color_ramp.elements[1]
    element.position = 0.55
    element.color = *rgb(63, 50, 188), 1


@tree
def grandient_color():
    """@shader"""

    fac = Shader.texture_coord().uv.mapping(location=(0, 0.3, 0)).y

    color = ColorRamp(fac=fac).color

    set_color_ramp_2(color)

    return color


@tree
def toon():
    """@material"""

    color = ramped_diffuse_color()

    shader = BSDF.Principled(base_color=color)

    return shader


@tree
def toon_gradient():
    """@material"""

    color = grandient_color()

    shader = BSDF.Principled(base_color=color)

    return shader


@tree
def toon_inner():
    """@material"""

    color = ramped_diffuse_color()

    shader = inner_faces_shader_with_hole(color)

    return shader


@tree
def glass_shader():
    """@shader"""
    fac = BSDF.Glossy(roughness=0.214, color=(1, 1, 1, 1)).to_rgb().color.Float.color_ramp().color.Float

    shader = BSDF.Transparent()

    shader = shader.mix(shader.mix(BSDF.Diffuse()), fac=fac)

    return shader


@tree
def glass():
    """@material"""
    return glass_shader()


bpy.data.materials["Toon Inner"].blend_method = "CLIP"
bpy.data.materials["Toon"].blend_method = "CLIP"
