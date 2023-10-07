Mesh Transition
========================

.. admonition:: Mesh Transition
    :class: pynodes

    .. thumbnail:: https://jsd.cdn.zzko.cn/gh/iplai/picx-images-hosting@master/20230713/image.31dov1slsd20.webp

    .. code:: python

        from pynodes import *
        from pynodes.math import *

        @tree
        def mesh_transition(mesh1: Mesh, mesh2: Mesh, factor: Float = (0, 0, 1), smooth: Boolean = False):

            with frame("Old Position"):

                old_pos = mesh1.capture_vector_on_points(mesh1.position)

            with frame("New Position"):

                new_pos = mesh2.sample_vector_at_index(mesh2.position, mesh2.sample_nearest())

            mesh1.set_position(old_pos.mix(new_pos, factor))

            return mesh1.set_shade_smooth(shade_smooth=smooth & (factor < 1))

.. admonition:: Mesh Transition Test
    :class: pynodes

    .. thumbnail:: https://jsd.cdn.zzko.cn/gh/iplai/picx-images-hosting@master/20230713/image.5wymcq0jdao0.webp

    .. thumbnail:: https://jsd.cdn.zzko.cn/gh/iplai/picx-images-hosting@master/20230713/image.573cjhuam5k0.gif

    .. code:: python
                
        @tree
        def mesh_transition_test(factor: Float = (0, 0, 1)):

            mesh1 = MeshCube(2).mesh.subdivision_surface(level=3)

            mesh2 = MeshIcoSphere(subdivisions=2).mesh

            return mesh_transition(mesh1, mesh2, factor)
