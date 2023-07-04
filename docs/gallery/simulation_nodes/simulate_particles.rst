Simulate Particles
===================

.. admonition:: simulate_particles
    :class: pynodes

    .. thumbnail:: https://i.ibb.co/Zx7Vj8N/image.gif

    .. thumbnail:: https://i.ibb.co/sVstYSv/image.png
        
    .. code:: python

        from pynodes import *

        @tree
        def simulate_particles(mesh: Mesh, velocity: VectorVelocity, force: VectorAcceleration):

            points = mesh.distribute_points_on_faces().points

            with frame("Velocity"):

                velocity = velocity + RandomVector(-1, 1)

                velocity.name = "Velocity"

            with simulate(points, velocity) as zone:

                points.set_position(offset=velocity * zone.delta_time)

                zone.to_ouputs(points, velocity + force * zone.delta_time)

            return points
