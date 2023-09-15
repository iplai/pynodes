from pynodes import *
from pynodes.math import *


@tree
def galaxy_simulate():
    grid = MeshGrid(10, 10, 3, 3).mesh
    points = grid.distribute_points_on_faces(density=1000).points[InputPosition().length > 5].delete_points()
    with simulate(points) as zone:
        points.set_position(offset=(-points.position).rotate_around_z_axis(angle=radians(75)) * 0.1 / points.position.length)
        rnd_id = SceneTime().frame + points.index
        theta1 = RandomFloat(0, tau, rnd_id, seed=1)
        theta2 = RandomFloat(0, tau, rnd_id, seed=2)
        points[points.position.length < 1].set_position(position=(sin(theta1) * 5, cos(theta2) * 5, 0))
        # points.Points[(points.position.distance(points.evaluate_vector_at_index_on_points(points.index_of_nearest().index, points.position)) > 0.2) & (points.position.length > 6)].delete()
        zone.to_output(points)
    return points


@tree
def geometry_nodes_repeat(n: Integer = (0, 0)):
    grid = MeshGrid(10, 10, 3, 3).mesh
    points = grid.distribute_points_on_faces(density=600).points[InputPosition().length > 5].delete_points()
    with repeat(points, iterations=n) as zone:
        points.set_position(offset=(points.position * -0.1).rotate_around_z_axis(angle=radians(75)))
        theta = RandomFloat(0, tau, n + points.index)
        points[points.position.length < 1].set_position(position=(sin(theta) * 5, cos(theta) * 5, 0))
        zone.to_output(points)
    return points
