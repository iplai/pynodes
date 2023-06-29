Atom Links
==============

.. admonition:: sweep_mesh_edges
    :class: pynodes

    .. thumbnail:: /_static/images/Snipaste_2023-06-28_04-06-45.png
        
    .. code:: python

        @tree
        def sweep_mesh_edges(mesh: Mesh, profile: Curve, trim_radius: Float):

            with frame("Mesh to Curve"):

                curve = mesh.to_curve().trim_length(trim_radius, 100).reverse().trim_length(trim_radius, 100)

            with frame("Curve to Mesh"):

                mesh = curve.to_mesh(profile, True)

            return mesh.set_shade_smooth(False)

.. admonition:: link_mesh_atoms
    :class: pynodes

    .. thumbnail:: /_static/images/Snipaste_2023-06-28_03-41-02.png
        
    .. code:: python

        @tree                                     # default, min, max
        def link_mesh_atoms(mesh: Mesh, radius: Float = (0.2, 0, 1.2)):

            with frame("Input Mesh"):
                # comment this line to get the mesh from Group Input
                mesh = MeshIcoSphere(2).mesh

            with frame("Get sweeped mesh edges"):
                # call the function defined above
                edges = sweep_mesh_edges(mesh, CurveCircle(radius / 2), radius)

            with frame("Atom spheres"):

                spheres = MeshIcoSphere(radius, subdivisions=3).mesh.on_points(mesh.to_points())

            return edges + spheres
