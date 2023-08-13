Balls Push Apart
===================

.. admonition:: balls_push_apart
    :class: pynodes

    .. thumbnail:: https://cdn.staticaly.com/gh/iplai/picx-images-hosting@master/20230713/image.1idry91l91kw.gif

    .. thumbnail:: https://cdn.staticaly.com/gh/iplai/picx-images-hosting@master/20230713/image.6n8yi6hgeww0.webp
        
    .. code:: python
        
        from pynodes import *


        @tree
        def target_sphere():

            return MeshIcoSphere(subdivisions=4)


        @tree
        def balls_push_apart(obj: Object):

            with frame("Generate Points"):

                mesh = MeshCircle(fill_type="NGON", radius=3)

                points = mesh.distribute_points_on_faces(density=100).points

            with frame("Calculate Positions"):

                diff = points.position - obj.location

                pos = diff.normalize.scale(obj.scale) + points.position

            points.set_position(position=pos)

            return MeshIcoSphere(subdivisions=2, radius=0.06).mesh.on_points(points)


        from pynodes.scene import *

        Scene({
            O.cube @ "Sphere": {
                Mod.geometry_nodes: {
                    "node_group": "Target Sphere",
                }
            },
            O.cube: {
                Mod.geometry_nodes: {
                    "node_group": "Balls Push Apart",
                    "Obj": "Sphere"
                }
            },
        }).load()
