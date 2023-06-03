from pynodes import *


@tree
def trim_curve_ends(curve: Curve, length: Float = 10):
    return curve.trim_length(length, 100).reverse().trim_length(length, 100)


@tree
def sweep_mesh_edges(mesh: Mesh, profile: Curve, trim_radius: Float):
    curve = mesh.to_curve()
    curve = trim_curve_ends(curve, trim_radius)
    mesh = curve.to_mesh(profile, True)
    return mesh.set_shade_smooth(False)


@tree
def atom_links(radius: Float = (0.2, 0, 1.2)):
    mesh = MeshIcoSphere(2).mesh
    points = mesh.to_points()
    mesh = sweep_mesh_edges(mesh, Rectangle(0.2, 0.2), radius)
    clones = MeshIcoSphere(radius, subdivisions=3).mesh.on_points(points)
    return mesh.join(clones)


@tree
def face_clones(mesh: Mesh, subdivision_level: Integer = (1, 0, 4)):
    cone = MeshCone().mesh
    mesh = mesh.subdivision_surface(level=subdivision_level)
    norm = mesh.capture_vector_on_faces(mesh.nornal)
    rotation = norm.align_euler_to_vector(axis="Z")
    face_area = mesh.capture_float_on_faces(mesh.face_area)
    scale = Float.sqrt(face_area) * 0.4
    cones = cone.on_points(mesh.to_points("FACES"), rotation=rotation, scale=scale)
    return mesh.join(cones)


@tree
def maze(mesh: Mesh, start: Float = (0, 0, 1)):
    with frame("样例"):
        mesh = MeshGrid(1, 1, 20, 20).mesh
        mesh = MeshIcoSphere(subdivisions=3).mesh
        mesh = MeshCube(1, 20, 20, 20).mesh

    index = mesh.index
    end_vertex = (index == 1) | (index == 2)
    next_vertex_index = mesh.shortest_edge_paths(end_vertex, RandomFloat()).next_vertex_index
    curve = mesh.edge_paths_to_curves(next_vertex_index=next_vertex_index).trim_factor(start)

    curve = curve.to_mesh().merge_by_distance().to_curve().fillet_bezier(0.01)
    mesh = curve.to_mesh(Rectangle(0.02, 0.02), True).set_shade_smooth(shade_smooth=False)

    return mesh


@tree
def cubes_on_faces(mesh: Mesh, x: Float = (0, -2, 2)):

    cube = MeshCube(size=0.1).mesh

    points = mesh.distribute_points_on_faces(density=50).points

    factor = cube.position + x

    instances = cube.Instances.on_points(points, scale=factor * 0.6)

    instances = instances.scale_instances(scale=Float.curve(factor=factor, points=[(0.2, 0.3), (0.5, 0.8), (0.8, 0.3)]))

    return instances


@tree
def dust(mesh: Mesh, factor: Float = 1):

    volume = mesh.to_volume()

    points = volume.distribute_points_grid()

    instances = MeshIcoSphere(0.01).mesh.Instances.on_points(points)

    w = SceneTime().seconds * 0.1

    instances.set_position(offset=(NoiseTexture("4D", w=w).color - 0.5) * factor)

    return instances.scale_instances(RandomFloat(0.5))
