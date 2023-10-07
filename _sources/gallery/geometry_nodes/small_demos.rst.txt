Small Demos
=============

Flying Dust
------------

.. admonition:: Dust
    :class: pynodes

    .. thumbnail:: https://cdn.statically.io/gh/iplai/picx-images-hosting@master/20230713/Snipaste_2023-06-28_06-26-031.2q6a7jmkj6u0.gif

    .. thumbnail:: https://cdn.statically.io/gh/iplai/picx-images-hosting@master/20230713/Snipaste_2023-06-28_06-27-501.3okdbi6lycc0.webp
        
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

Link Vertices
-----------------

.. admonition:: Link Vertices
    :class: pynodes

    .. thumbnail:: https://cdn.statically.io/gh/iplai/picx-images-hosting@master/20230713/image.4bnb2szcq900.gif

    .. thumbnail:: https://cdn.statically.io/gh/iplai/picx-images-hosting@master/20230713/image.7kfiut2ntxo0.webp
        
    .. code:: python

        def link_vertices(trim_end: Factor = (0, 0, 1)):

            points = MeshIcoSphere(subdivisions=2).mesh.distribute_points_on_faces().points

            with frame("Point Count"):

                count = points.float_statistic_on_points(points.index).max + 1

            line = CurveLine().resample(count)

            with frame("Set vertex position of line"):

                line = line.set_position(points.sample_vector_at_index(points.position, points.index))

            line = line.trim_factor(trim_end)

            return line + points


Recursive Subdivide
---------------------

.. admonition:: random_subdivide_iterate
    :class: pynodes

    .. thumbnail:: https://cdn.statically.io/gh/iplai/picx-images-hosting@master/20230713/image.3bqvahfligg0.webp
        
    .. code:: python

        @tree
        def random_subdivide_iterate(mesh: Mesh, p: Float = ("Probability", 0.5, 0, 1), seed: Integer = 0):

            mesh1, mesh2 = mesh.separate_faces(RandomBoolean(p, 0, seed))

            mesh1 = mesh1.subdivide_mesh()

            new_seed = (seed + 1).to_integer()

            return mesh1.join(mesh2), p, new_seed("Seed")


.. admonition:: random_subdivide
    :class: pynodes

    .. thumbnail:: https://cdn.statically.io/gh/iplai/picx-images-hosting@master/20230713/image.19onsipxxuf4.webp

    .. thumbnail:: https://cdn.statically.io/gh/iplai/picx-images-hosting@master/20230713/image.2rh1xzi37t60.webp
        
    .. code:: python

        @tree
        def random_subdivide(p: Float = ("Probability", 0.5, 0, 1), seed: Integer = 0):

            mesh = MeshGrid(1, 1, 12, 12).mesh

            mesh, p, seed = random_subdivide_iterate(mesh, p, seed)

            mesh.node.label = f"Subdivide 1"

            for i in range(3):

                mesh, p, seed = random_subdivide_iterate(mesh, p, seed)

                mesh.node.label = f"Subdivide {i+2}"

            return mesh.split_edges()
