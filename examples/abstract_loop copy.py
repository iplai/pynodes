from pynodes import *

sin, cos = Float.sin, Float.cos


@tree
def möbius_band(resolution: Integer = 64, tilt: Float = (tau, 0)):

    # curve = CurveCircle(3, resolution)

    with frame("Curve Tilt"):

        curve = CurveCircle(3, resolution)
        curve = curve.set_tilt(curve.parameter.factor.map_range(0, 1, 0, tilt))
    # with frame("Curve to Mesh"):

    #     with frame("Profile"):

    #         line = Rectangle(3, 0.05)

    #         circle = CurveCircle(1.5, 3).subdivide(3)

    #     profile = circle

    #     mesh = curve.to_mesh(profile).merge_by_distance(0.15).set_shade_smooth(False).set_material("#51be51")

    return curve


# @tree
def abstract_loop(radius: Float = 0.35):

    points = möbius_band(resolution=32).to_points("FACES")

    mesh = MeshUVSphere(radius=radius).mesh.Instances.on_points(points).set_material("#e7539d")

    return mesh
