from pynodes import *


@tree
def iterate(points: Points, instance: Instances):

    normal = points.capture_vector_on_faces(points.nornal)

    points = points.Mesh.to_points("FACES")

    return instance.on_points(points, rotation=normal.align_euler_to_vector("Z"), scale=1 / 3)


@tree
def fractal():

    mesh = MeshGrid(3, 3, 4, 4).mesh

    base_mesh = mesh[4].extrude_faces().mesh

    iterated_mesh = iterate(base_mesh, base_mesh)

    iterated_mesh = iterate(iterated_mesh, base_mesh)

    iterated_mesh = iterate(iterated_mesh, base_mesh)

    return iterated_mesh
