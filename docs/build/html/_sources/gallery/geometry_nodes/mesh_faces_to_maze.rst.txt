Mesh Surface to Maze
=====================
.. raw:: html

    <embed>
        <iframe width="809" height="500" src="https://www.youtube.com/embed/0MTiMby4NaQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
    </embed>

.. admonition:: mesh_to_maze
    :class: pynodes

    .. thumbnail:: https://jsd.cdn.zzko.cn/gh/iplai/picx-images-hosting@master/20230713/image.51vh8uuhmvk0.webp
        
    .. code:: python

        @tree
        def mesh_to_maze(mesh: Mesh, start: Float = (0, 0, 1)):

            with frame("Input Mesh"):
                # Choose one of the following meshes to test effects
                mesh = MeshGrid(1, 1, 20, 20).mesh
                mesh = MeshIcoSphere(subdivisions=3).mesh
                mesh = MeshCube(1, 10, 10, 10).mesh

            index = mesh.index

            with frame("End Vertex"):

                end_vertex = (index == 1) | (index == 2)  # Boolean Math Or

            with frame("Next Vertex Index"):

                next_vertex_index = mesh.shortest_edge_paths(end_vertex, RandomFloat()).next_vertex_index

            with frame("Edge paths to curves"):

                curve = mesh.edge_paths_to_curves(next_vertex_index=next_vertex_index).trim_factor(start)

            with frame("Merge and fillet curve"):

                curve = curve.to_mesh().merge_by_distance().to_curve().fillet_bezier(0.01)

            with frame("Curve to Mesh"):

                mesh = curve.to_mesh(Rectangle(0.02, 0.02), True).set_shade_smooth(shade_smooth=False)

            return mesh
