Sparkles
=========================

Geometry Pieces
------------------

.. admonition:: Geometry Pieces
    :class: pynodes

    .. thumbnail:: https://cdn.staticaly.com/gh/iplai/picx-images-hosting@master/20230713/image.6bzabnryexc0.gif

    .. thumbnail:: https://cdn.staticaly.com/gh/iplai/picx-images-hosting@master/20230713/image.261oqcc2lyow.webp
        
    .. code:: python

        @tree
        def sparkles():

            with frame("The value to store"):

                a = (SceneTime().seconds * 0.5 + RandomFloat(0, 10)).fract

            with frame("Position of the points"):

                pos = RandomVector((-1, -1, 0), (1, 1, 0)).normalize * a * 5

            with frame("Points"):

                points = InputPoints(100, position=pos).store_named_attribute("a", a)

            with frame("Scale of the sparkles"):

                scale = (sin(a * 16 + RandomFloat(0, 10)) * 0.5 + 0.5) * a.map_range(0, 0.9, 4, 0, interpolation_type="SMOOTHSTEP")

            with frame("Sparkles Mat"):

                grid = MeshGrid(1, 1, 2, 2)

                mesh = grid.mesh.store_named_attribute("uv_map", grid.uv_map).on_points(points, scale=scale).set_material("Sparkles Mat")

            return mesh


Sparkles Material
------------------

URL of the ImageTexture: `sparkle.png <https://github.com/iplai/pynodes/blob/main/examples/images/sparkle.png>`_

.. admonition:: Sparkles Material
    :class: pynodes

    .. thumbnail:: https://cdn.staticaly.com/gh/iplai/picx-images-hosting@master/20230713/image.5t3sbjfruh40.webp

    .. thumbnail:: https://cdn.staticaly.com/gh/iplai/picx-images-hosting@master/20230713/image.6e4vjtsuvt00.webp
        
    .. code:: python

        @tree
        def sparkles_mat():
            """@Material"""

            shader = BSDF.Emission()

            noise_texture = WhiteNoiseTexture("1D", w=shader.object_info.random)

            image_texture = ImageTexture(vector=shader.attribute("uv_map").vector)

            shader['Color'] = noise_texture.color * 2

            shader['Strength'] = image_texture.color.Float * shader.attribute("a", "INSTANCER").fac.map_range(0.7, 1, 1, 0, "SMOOTHERSTEP")

            return shader.add_shader(BSDF.Transparent())
