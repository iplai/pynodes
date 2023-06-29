Small Demos
=============

Flying Dust
------------

.. admonition:: Dust
    :class: pynodes

    .. thumbnail:: /_static/images/Snipaste_2023-06-28_06-26-03.gif

    .. thumbnail:: /_static/images/Snipaste_2023-06-28_06-27-50.png
        
    .. code:: python

        @tree
        def dust(mesh: Mesh, factor: Float = 1, radius: Float = 0.03):

            with frame("Get Points from the volume of the input mesh"):

                volume = mesh.to_volume()

                points = volume.distribute_points_grid()

            with frame("Clone spheres to the points"):

                spheres = MeshIcoSphere(radius).mesh.Instances.on_points(points)

            with frame("Set the position of the spheres"):

                w = SceneTime().seconds * 0.1 # Animating by scene time

                spheres.set_position(offset=(NoiseTexture("4D", w=w).color - 0.5) * factor)

            with frame("Set the scale of the spheres"):

                spheres = spheres.scale_instances(RandomFloat(min=0.5, max=1))

            return spheres