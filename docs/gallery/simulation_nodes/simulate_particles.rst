Simulate Particles
===================

.. admonition:: simulate_particles
    :class: pynodes

    .. thumbnail:: https://cdn.staticaly.com/gh/iplai/picx-images-hosting@master/20230713/image.6z5v8i88a200.gif

    .. thumbnail:: https://cdn.staticaly.com/gh/iplai/picx-images-hosting@master/20230713/image.5eyc0rkn9480.webp
        
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
