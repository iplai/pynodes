from pynodes import *

sin, cos = Float.sin, Float.cos


@tree
def calculate_coord(p: Integer, q: Integer, R: Float, r: Float, ɸ: Float):
    δ = SceneTime().seconds * 2

    a = ɸ * p + δ
    b = ɸ * q
    c = R + r * cos(b)

    x = c * cos(a)
    y = c * sin(a)
    z = sin(b)

    return CombineXYZ(x, y, z)


@tree
def torus_kont(
    resolution_ratio: Float = 10,
    p: Integer = 1,
    q: Integer = 3,
    R: Float = 5,
    r: Float = 1,
    profile_radius: Float = 0.5,
    n: Integer = (3, 3),
    keep_normal: Boolean = False
):

    with frame("Torus"):

        torus = CurveCircle(R, 64).to_mesh(CurveCircle(r / 5)).set_material("#c43131")

    with frame("Calculate curve resolution"):

        res = (R * tau * p + r * tau * q) * resolution_ratio

        circle = CurveCircle(resolution=res)

    with frame("Set curve normal"):

        circle.switch(keep_normal, circle.Curve.set_normal("Z_UP"))

    # with frame("Curve normal"):

        # circle = circle.set_tilt(circle.parameter.factor * pi)

    with frame("Set position of circle curve points"):

        ɸ = circle.parameter.factor.map_range(0, 1, 0, tau)

        circle.set_position(position=calculate_coord(p, q, R, r, ɸ))

    circle.store_named_attribute("factor", circle.parameter.factor)

    with frame("Make curve to mesh"):

        profile_circle = CurveCircle(resolution=n, radius=profile_radius)

        mesh = circle.to_mesh(profile_circle).set_shade_smooth(False).set_material("#5f97eb")

    return mesh + torus
