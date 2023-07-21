from pynodes import *


@tree
def tree_d_grid(resolution: Integer = (10, 2), target: Object = "Suzanne"):
    points = MeshGrid(1, 1, resolution, resolution).mesh.on_points(CurveLine((0, 0, -0.5), (0, 0, 0.5)).resample(resolution)).realize_instances().to_points(radius=0.01)
    grid_pos = points.capture_vector_on_points(points.position)
    index = target.geometry.Mesh.sample_nearest_on_faces()
    target_pos = target.geometry.Mesh.sample_vector_at_index(points.position, index, "FACE")
    points[(target_pos - grid_pos).dot(grid_pos) < 0].delete()

    return points
