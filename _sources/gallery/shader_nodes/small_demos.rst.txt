Small Demos
================

Voronoi Example
------------------

.. admonition:: Voronoi Example
    :class: pynodes

    .. thumbnail:: https://i.ibb.co/HNXV4Qj/image.png

    .. thumbnail:: https://i.ibb.co/T0YMYmZ/image.png
        
    .. code:: python

        from pynodes import *


        @tree
        def texture_example():
            """@material"""

            a = VoronoiTexture("2D")

            b = VoronoiTexture("2D", "DISTANCE_TO_EDGE")

            with frame("Surface"):

                with frame("Gray distance with edges"):

                    surface = a.distance + b.distance.less_than(0.01)

                with frame("Cell color with edges"):

                    surface = a.color + b.distance.less_than(0.01)

            return surface


Random Color
------------------

.. admonition:: Random Color
    :class: pynodes

    .. thumbnail:: https://i.ibb.co/SXhWy0x/image.png

    .. thumbnail:: https://i.ibb.co/g6jZzhN/image.png
        
    .. code:: python
                
        from pynodes import *


        @tree
        def random_color():
            """@material"""
            shader = BSDF.Principled()
            # a list with ten bright hex color strings
            bright_colors = ["#ff0000", "#ff8000", "#ffff00", "#80ff00", "#00ff00",
                            "#00ff80", "#00ffff", "#0080ff", "#0000ff", "#8000ff"]
            shader['Base Color'] = shader.object_info.random.color_ramp_uniform(*bright_colors)
            shader['roughness'] = 0.1
            return shader


        @tree
        def geometry_nodes(mesh: Mesh):
            return MeshIcoSphere(subdivisions=3).mesh.on_points(MeshIcoSphere(subdivisions=2).mesh)\
                .set_shade_smooth().set_material("random_color")
