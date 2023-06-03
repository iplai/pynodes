from pynodes import *


@tree
def calculate_coord(p: Integer, q: Integer, ɸ: Float):
    δ = SceneTime().seconds * 2

    r = cos(q * ɸ + δ) + 2
    x = r * cos(p * ɸ + δ)
    y = r * sin(p * ɸ + δ)
    z = -sin(q * ɸ + δ)

    return CombineXYZ(x, y, z)


@tree
def merge_curve(curve: Curve):
    return curve.to_mesh().merge_by_distance().to_curve()


@tree
def torus_knot(
    resolution: Integer = 200,
    p: Integer = 3,
    q: Integer = 5,
    radius: Float = 0.2,
):
    circle = CurveCircle(resolution=resolution)

    ɸ = circle.parameter.factor.map_range(0, 1, 0, tau)

    position = calculate_coord(p, q, ɸ)

    circle.set_position(position=position)

    circle.store_named_attribute("factor", circle.parameter.factor)

    circle = merge_curve(circle)

    with frame("Make curve to mesh"):

        mesh = circle.to_mesh(profile_curve=CurveCircle(radius))

        mesh.set_material("Torus Knot")

    return mesh


@tree
def torus_knot():
    """@Material"""

    factor = Shader.attribute(name="factor").fac

    color = GradientTexture(vector=factor).color

    color = color.mix("#117f0f")

    shader = BSDF.Principled("MULTI_GGX", base_color=color)

    return shader


def load_font(name=None, file_name=None, windows=True):
    font = bpy.data.fonts.get(name)
    if font is not None:
        return font
    if windows:
        prefix = "C:\\Windows\\Fonts\\"
    else:
        prefix = "C:\\Users\\Administrator\\AppData\\Local\\Microsoft\\Windows\\Fonts\\"
    font = bpy.data.fonts.load(prefix + file_name, check_existing=True)
    print("Loaded", font.name)
    return font


font = load_font("Segoe UI Emoji Regular", "seguiemj.ttf")


@tree
def geometry_nodes(d: Float = ("延长", 0, 0, 10), fixed: Boolean = ("固定起点", True), reverse: Boolean = ("反向", False)):
    """伸缩大括号"""

    d = d / 2

    curve = StringToCurves("{", "CENTER", "MIDDLE", font=font).curve_instances

    curve = curve.transform((0, -0.01, 0)).realize_instances().Curve

    curve = curve.resample_evaluated()

    a = InputFloat(0.12)

    curve[curve.position.y > 0.15].set_position(offset=(0, d - a, 0))

    curve[curve.position.y < -0.15].set_position(offset=(0, -d + a, 0))

    d = d.switch(reverse, -d)

    curve.transform((0, InputFloat(0).switch(fixed, d), 0))

    return curve
