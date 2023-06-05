from pynodes import *

sin, cos = Float.sin, Float.cos


@tree
def möbius_band(resolution: Integer = 64, tilt: Float = (tau, 0)):

    curve = CurveCircle(0.3, resolution)

    with frame("Curve Tilt"):

        t = SceneTime().seconds

        curve = curve.set_tilt(curve.parameter.factor.map_range(0, 1, 0, tilt) + t).trim_factor()

    with frame("Curve to Mesh"):

        with frame("Profile"):

            line = Rectangle(0.3, 0.05)

            circle = CurveCircle(0.15, 3).subdivide(3)

        profile = circle

        mesh = curve.to_mesh(profile).merge_by_distance(0.015).set_shade_smooth(False).set_material("#51be51")

    return mesh


@tree
def abstract_loop():

    mesh = möbius_band()
