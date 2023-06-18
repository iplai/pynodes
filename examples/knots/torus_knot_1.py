from pynodes import *


@tree
def calculate_coord(p: Integer, q: Integer, ɸ: Float):
    δ = SceneTime().seconds * 2

    with frame("r"):
        r = cos(q * ɸ + δ) + 2

    with frame("x"):
        x = r * cos(p * ɸ + δ)

    with frame("y"):
        y = r * sin(p * ɸ + δ)

    with frame("z"):
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
