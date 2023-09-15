from pynodes import *


@tree
def particles_on_surface(mesh: Mesh, geometry: Points, obj: Object):

    with frame("Points"):

        vol = obj.object_info("RELATIVE").geometry.Mesh.to_volume()

        points = vol.distribute_points_random(density=500, seed=SceneTime().frame)

    with simulate(geometry) as zone:

        geometry.join(points)

        lifetime = geometry.named_attribute_float("lt").attribute

        radius = lifetime.map_range(0, 1, 0.02, 0)

        geometry.set_radius(radius)

        geometry.store_named_attribute("lt", lifetime + 0.1)

        geometry[radius == 0].delete()

        geometry.set_position(offset=NoiseTexture().color - 0.5)

        zone.to_output(geometry)

    return geometry
