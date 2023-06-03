from pynodes import *


@tree
def curve_binormal(curve: Curve, length: Float = (0.3, 0)):
    binormal = curve.capture_vector_on_points(curve.tangent.cross(curve.nornal))
    mesh = curve.to_mesh().extrude_vertices(length, binormal).mesh
    return mesh.to_curve()


@tree
def tilt_curve(curve: Curve, max_angle: Float = tau, offset_angle: Float = 0):
    return curve.set_tilt(curve.parameter.factor.map_range(0, 1, 0, max_angle) + offset_angle)


@tree
def extrude_binomal_faces(mesh: Mesh, length: Float):

    mesh, top, side = mesh[mesh.index % 4 == 0].extrude_faces(length)

    t = SceneTime().seconds

    mesh = mesh[top].scale_elements(sin(t * 2).map_range(-1, 1, 0, 0.8))

    return mesh


@tree
def curve_to_mesh(curve: Curve):
    with frame("Profile"):

        profile = CurveCircle(0.15, 3)

        profile = Rectangle(0.3, 0.05)

    mesh = curve.to_mesh(profile).merge_by_distance(0.02).set_shade_smooth(False)

    return mesh


@tree
def möbius_band(resolution: Integer = 64, trim_end: Float = (1, 0, 1), max_angle: Float = tau, extrude_top: Boolean = True):

    curve = CurveCircle(resolution=resolution)

    curve = curve.trim_factor(end=trim_end)

    t = SceneTime().seconds

    curve = tilt_curve(curve, max_angle, t)

    mesh = curve_to_mesh(curve)

    binormal = curve_binormal(curve)

    with frame("Extrude faces of binormal"):

        extruded_mesh = extrude_binomal_faces(mesh, 0.2)

        mesh = mesh.switch(extrude_top, extruded_mesh)

    return join(mesh, curve, binormal)


@tree
def link_vertices(trim_end: Float):

    points = MeshIcoSphere(subdivisions=2).mesh.distribute_points_on_faces().points

    line = CurveLine().resample(points.float_statistic_on_points(points.index).max + 1)

    line = line.set_position(points.sample_vector_index(points.position, points.index))

    # line = line.select(line.index < last_index)
    line = line.trim_length(end=trim_end)

    return line + points


@tree
def text_test():

    curve = StringToCurves("Text", align_x="CENTER").curve_instances.realize_instances().Curve.resample_length(0.01)

    curve = curve.set_position(offset=curve.tangent.rotate("EULER_XYZ", rotation=(0, 0, pi / 2)) * -0.02)

    noise = NoiseTexture("4D", w=SceneTime().seconds * 0.1)

    curve = curve.set_position(offset=(noise.color - 0.5) * 0.5)

    vol = curve.Points.to_volume("VOXEL_SIZE", voxel_size=0.02, radius=0.04)

    mesh = vol.to_mesh()

    return mesh


@tree
def random_subdivide_iterate(mesh: Mesh, p: Float = ("Probability", 0.5, 0, 1), seed: Integer = 0):

    mesh1, mesh2 = mesh.separate_faces(RandomBoolean(p, 0, seed))

    mesh1 = mesh1.subdivide_mesh()

    new_seed = (seed + 1).to_integer()

    return mesh1.join(mesh2), p, new_seed("Seed")


@tree
def random_subdivide(p: Float = ("Probability", 0.5, 0, 1), seed: Integer = 0):

    mesh = MeshGrid(1, 1, 12, 12).mesh

    mesh, p, seed = random_subdivide_iterate(mesh, p, seed)

    for i in range(3):

        mesh, p, seed = random_subdivide_iterate(mesh, p, seed)

        mesh.node.label = f"Subdivide {i+2}"

    return mesh.split_edges()
