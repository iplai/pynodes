from pynodes import *


@tree
def möbius_band(resolution: Integer = 64, trim_end: Float = (1, 0, 1), tilt: Float = (pi, 0, pi)):

    n = resolution

    curve = CurveCircle(resolution=n).trim_factor(end=trim_end)

    with frame("curve tilt"):

        t = SceneTime().seconds

        curve = curve.set_tilt(curve.parameter.factor.map_range(0, 1, 0, tilt) + t)

    with frame("curve to mesh"):

        with frame("Profile"):

            line = Rectangle(0.3, 0.05)

            circle = CurveCircle(0.15, 3)

        profile = line

        mesh = curve.to_mesh(profile).merge_by_distance(0.015)

    with frame("curve extrude normal"):

        offset = curve.capture_vector_on_points(curve.tangent.cross(curve.normal))

        norm_mesh = curve.to_mesh().extrude_vertices(0.3, offset).mesh

    # mesh, top, side = mesh.vertices.extrude(0.25)
    # mesh = mesh[top].scale_elements(sin(t * 2).range(-1, 1, 0, 1))
    return curve + norm_mesh + mesh.set_shade_smooth(False)
