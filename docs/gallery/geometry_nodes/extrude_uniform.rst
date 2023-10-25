Extrude Uniform
======================

The is an util node group for modeling.

.. admonition:: Extrude Uniform
    :class: pynodes

    .. thumbnail:: https://cdn.statically.io/gh/iplai/picx-images-hosting@master/20230713/image.54su2uzjjy40.gif

    .. thumbnail:: https://cdn.statically.io/gh/iplai/picx-images-hosting@master/20230713/image.4yodhizg8fk0.webp
        
    .. code:: python

        from pynodes import *


        @tree
        def line_to_wall(curve: Curve):

            offset = NoiseTexture(scale=0.5).color.map_range(to_min=(-0.5, -0.5, 0), to_max=(0.5, 0.5, 0))

            mesh = curve.subdivide(30).set_position(offset=offset).to_mesh()

            mesh = mesh.extrude_edges(offset=(0, 0, 1)).mesh

            return mesh


        @tree
        def extrude_uniform(mesh: Mesh, thickness: Float = 0.2):

            # The normal here is the average of the normal vector of the
            # surface connected to the current point
            with frame("Evaluate normal on faces"):
                normal = mesh.evaluate_vector_on_faces(mesh.normal)

            # The following tree fomula is equivalent
            with frame("Scale normal"):

                normal1 = normal.normalized * (1 / normal.length)
                normal1.node.label = "Method 1"

                normal2 = normal * (1 / normal.length**2)
                normal2.node.label = "Method 2"

                normal3 = normal * (1 / normal.dot(normal))
                normal3.node.label = "Method 3"

            # Capture the normal on the point field
            with frame("Capture normal"):

                normal = mesh.capture_vector_on_points(normal1)

            mesh, top, side = mesh.extrude_faces(offset_scale=0)

            mesh[top].set_position(offset=normal.scale(thickness))

            return mesh


        from pynodes.scene import *

        Scene({
            O.bezier_curve: {
                Mod.geometry_nodes @ "1": {
                    "node_group": "line_to_wall"
                },
                Mod.geometry_nodes @ "2": {
                    "node_group": "extrude_uniform"
                }
            }
        }).load()
