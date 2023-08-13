from pynodes import *
from pynodes.math import *


@tree
def calculate_coord(p: Integer, q: Integer, R: Float, r: Float, ɸ: Float):

    a = ɸ * p
    b = ɸ * q
    c = R + r * cos(b)

    x = c * sin(a)
    y = c * cos(a)
    z = sin(b) * r

    return CombineXYZ(x, y, z)


@tree
def calculate_coord_trefoil(p: Integer, q: Integer, R: Float, r: Float, ɸ: Float):

    x = sin(ɸ) * r - sin(ɸ * p) * R
    y = cos(ɸ) * r + cos(ɸ * p) * R
    z = sin(-ɸ * q) * r

    return CombineXYZ(x, y, z)


@tree
def torus_knot(
    res_1: Integer = 128,
    res_2: Integer = 12,
    p: Integer = 4,
    q: Integer = 3,
    r1: Float = 1,
    r2: Float = 0.5,
    r0: Float = 0.2,
    trefoil: Boolean = True
):

    with frame("Initial Circle"):

        circle = CurveCircle(resolution=res_1)

    with frame("Coord"):

        ɸ = circle.parameter.factor * tau

        circle.set_position(position=calculate_coord(p, q, r1, r2, ɸ).switch(trefoil, calculate_coord_trefoil(p, q, r1, r2, ɸ)))

    with frame("Mesh"):

        profile_circle = CurveCircle(resolution=res_2, radius=r0)

        mesh = circle.to_mesh(profile_circle).set_shade_smooth(False).set_material("#5f97eb")

    return mesh
