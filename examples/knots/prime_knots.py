"""https://en.wikipedia.org/wiki/List_of_prime_knots"""
"""

"""


from pynodes import *


@tree
def trefoil_knot_coord(t: Float):

    with frame("X"):
        x = sin(t) + 2 * sin(2 * t)

    with frame("Y"):
        y = cos(t) - 2 * cos(2 * t)

    with frame("Z"):
        z = 2 * sin(3 * t)

    return x("X"), y('Y'), z("Z")


@tree
def trefoil_knot(radius: Float = 0.2):

    with frame("Curve"):

        curve = CurveCircle().set_spline_type("NURBS")

        t = curve.parameter.factor.map_range(0, 1, 0, tau)

        curve.set_position(trefoil_knot_coord(t))

    with frame("Curve to Mesh"):

        mesh = curve.to_mesh(CurveCircle(radius))

    return mesh


@tree
def torus_knot_coord(p: Integer, q: Integer, t: Float):

    with frame("r"):
        r = cos(q * t) + 2

    with frame("X"):
        x = r * cos(p * t)

    with frame("Y"):
        y = r * sin(p * t)

    with frame("Z"):
        z = -sin(q * t)

    return CombineXYZ(x, y, z)


@tree
def torus_knot(p: Integer = 2, q: Integer = 3, radius: Float = 0.2):

    with frame("Curve"):

        curve = CurveCircle().set_spline_type("NURBS")

        t = curve.parameter.factor.map_range(0, 1, 0, tau)

        curve.set_position(torus_knot_coord(p, q, t))

    with frame("Curve to Mesh"):

        mesh = curve.to_mesh(CurveCircle(radius))

    return mesh


@tree
def figure_8_knot_coord(t: Float):

    with frame("2 + cos(2 * t)"):
        k = 2 + cos(2 * t)

    with frame("X"):
        x = k * cos(3 * t)

    with frame("Y"):
        y = k * sin(3 * t)

    with frame("Z"):
        z = sin(4 * t) * 1

    return CombineXYZ(x, y, z)


@tree
def figure_8_knot(radius: Float = 0.2):

    with frame("Curve"):

        curve = CurveCircle().set_spline_type("NURBS")

        t = curve.parameter.factor.map_range(0, 1, 0, tau)

        curve.set_position(figure_8_knot_coord(t))

    with frame("Curve to Mesh"):

        mesh = curve.to_mesh(CurveCircle(radius))

    return mesh


@tree
def pentafoil_knot_coord(t: Float):

    with frame("3 + cos(5 * t)"):
        k = 3 + cos(5 * t)

    with frame("X"):
        x = k * cos(2 * t)

    with frame("Y"):
        y = k * sin(2 * t)

    with frame("Z"):
        z = sin(5 * t)

    return CombineXYZ(x, y, z)


@tree
def pentafoil_knot(radius: Float = 0.2):

    with frame("Curve"):

        curve = CurveCircle().set_spline_type("NURBS")

        t = curve.parameter.factor.map_range(0, 1, 0, tau)

        curve.set_position(pentafoil_knot_coord(t))

    with frame("Curve to Mesh"):

        mesh = curve.to_mesh(CurveCircle(radius))

    return mesh


@tree
def square_knot_coord(t: Float):

    with frame("X"):
        x = 3 * sin(t) + 2 * sin(3 * t)

    with frame("Y"):
        y = cos(t) - 2 * cos(3 * t)

    with frame("Z"):
        z = cos(5 * t)

    return CombineXYZ(x, y, z)


@tree
def square_knot(radius: Float = 0.2):

    with frame("Curve"):

        curve = CurveCircle().set_spline_type("NURBS")

        t = curve.parameter.factor.map_range(0, 1, 0, tau)

        curve.set_position(square_knot_coord(t))

    with frame("Curve to Mesh"):

        mesh = curve.to_mesh(CurveCircle(radius))

    return mesh


@tree
def eight_knot_coord(t: Float):

    with frame("X"):
        x = 3 * cos(t) + 5 * cos(3 * t)

    with frame("Y"):
        y = 3 * sin(t) + 5 * sin(3 * t)

    with frame("Z"):
        z = sin((5 * t) / 2) * sin(3 * t) + sin(4 * t) - sin(6 * t)

    return CombineXYZ(x, y, z)


@tree
def eight_knot(radius: Float = 0.2):

    with frame("Curve"):

        curve = CurveCircle().set_spline_type("NURBS")

        t = curve.parameter.factor.map_range(0, 1, 0, tau)

        curve.set_position(eight_knot_coord(t))

    with frame("Curve to Mesh"):

        mesh = curve.to_mesh(CurveCircle(radius))

    return mesh


@tree
def twisted_unknot_coord(t: Float):

    with frame("X"):
        x = 2 * sin(t + 1)

    with frame("Y"):
        y = 3 * sin(t + 1) * cos(t + 1)

    with frame("Z"):
        z = sin(t) * 1

    return CombineXYZ(x, y, z)


@tree
def twisted_unknot(radius: Float = 0.2):

    with frame("Curve"):

        curve = CurveCircle().set_spline_type("NURBS")

        t = curve.parameter.factor.map_range(0, 1, 0, tau)

        curve.set_position(twisted_unknot_coord(t))

    with frame("Curve to Mesh"):

        mesh = curve.to_mesh(CurveCircle(radius))

    return mesh
