Toon Shader
=============

Color Setting
---------------

:menuselection:`Render Properties --> Color Management --> View Transform`

.. code:: python

    bpy.context.scene.view_settings.view_transform = "Standard"

inner_faces_shader
-----------------------

.. admonition:: Shader: inner_faces_shader
    :class: pynodes

    .. thumbnail:: https://cdn.statically.io/gh/iplai/picx-images-hosting@master/20230713/image.3cll8lna3n60.webp
        
    .. code:: python

        @tree
        def inner_faces_shader(color: Color):
            """@shader"""

            shader1 = BSDF.Transparent()

            shader2 = BSDF.Emission(color)

            shader = shader1.mix(shader2, fac=shader1.geometry.backfacing)

            return shader

inner_faces_shader_with_hole
-----------------------------

.. admonition:: Shader: inner_faces_shader_with_hole
    :class: pynodes

    .. thumbnail:: https://cdn.statically.io/gh/iplai/picx-images-hosting@master/20230713/image.1q2uqykxlu74.webp
        
    .. code:: python

        @tree
        def inner_faces_shader_with_hole(color: Color, hole_y: Float = 0.5):
            """@shader"""

            shader1 = BSDF.Transparent()

            shader2 = BSDF.Emission(color)

            fac = shader1.geometry.backfacing + shader1.geometry.position.y.less_than(hole_y)

            shader = shader1.mix(shader2, fac=fac)

            return shader

ramped_diffuse_color
-----------------------------

.. admonition:: Shader: ramped_diffuse_color
    :class: pynodes

    .. thumbnail:: https://cdn.statically.io/gh/iplai/picx-images-hosting@master/20230713/image.6mff3difqjo0.webp
        
    .. code:: python

        @tree
        def ramped_diffuse_color():
            """@shader"""

            color = BSDF.Diffuse().to_rgb().color

            factor = color.Float.float_curve(points=[(0, 0), (0.25, 0.2), (0.8, 0.85), (1, 1)])

            colors = []

            base_color = mathutils.Color(rgb(245, 120, 193))

            ramp_steps = 8

            for i in range(ramp_steps):

                base_color.v = (0.5 if i == 0 else i) / (ramp_steps - 1)

                colors.append(base_color.copy())

            # The upper for loop is equivalent to the following:
            colors = rgb(76, 32, 58), rgb(106, 48, 82), rgb(146, 69, 114), rgb(175, 84, 137),\
                rgb(199, 96, 156), rgb(220, 107, 173), rgb(238, 117, 188), rgb(255, 125, 201)

            color = factor.color_ramp_uniform(*colors, interpolation="CONSTANT")

            return color

Enable Color Decorator
-----------------------

.. tip::

    To enable color decorator in vscode python editor, add this line to vscode config json:

    .. code-block:: json
        :emphasize-lines: 4

        {
            "[python]": {
                "editor.formatOnSave": true,
                "editor.defaultColorDecorators": true
            },
        }

    Then, there will be a color panel to select colors in vscode.

    .. thumbnail:: https://cdn.statically.io/gh/iplai/picx-images-hosting@master/20230713/image.55lahynrje80.webp

grandient_color
-----------------------------

.. admonition:: Shader: grandient_color
    :class: pynodes

    .. thumbnail:: https://cdn.statically.io/gh/iplai/picx-images-hosting@master/20230713/image.678967xqn0o0.webp
        
    .. code:: python

        @tree
        def grandient_color():
            """@shader"""

            fac = TextureCoord().uv.mapping(location=(0, 0.3, 0)).y

            color = fac.color_ramp_with_position(
                [(0.4, rgb(245, 120, 193)), (0.55, rgb(63, 50, 188))], interpolation="B_SPLINE"
            )

            return color

Material: toon
-----------------------------

.. admonition:: Material: toon
    :class: pynodes

    .. thumbnail:: https://cdn.statically.io/gh/iplai/picx-images-hosting@master/20230713/image.42bjmx8tbqu0.webp

    .. thumbnail:: https://cdn.statically.io/gh/iplai/picx-images-hosting@master/20230713/image.794di5bdugg0.webp
        
    .. code:: python

        @tree
        def toon():
            """@material"""

            color = ramped_diffuse_color()

            shader = BsdfPrincipled(base_color=color)

            return shader
        
        bpy.data.materials["Toon"].blend_method = "CLIP"

Material: toon_gradient
-----------------------------

.. admonition:: Material: toon_gradient
    :class: pynodes

    .. thumbnail:: https://cdn.statically.io/gh/iplai/picx-images-hosting@master/20230713/image.5o2ez49aa3s0.webp

    .. thumbnail:: https://cdn.statically.io/gh/iplai/picx-images-hosting@master/20230713/image.1fusn7n8orhc.webp
        
    .. code:: python

        @tree
        def toon_gradient():
            """@material"""

            color = grandient_color()

            shader = BsdfPrincipled(base_color=color)

            return shader

Material: toon_inner
-----------------------------

.. admonition:: Material: toon_inner
    :class: pynodes

    .. thumbnail:: https://cdn.statically.io/gh/iplai/picx-images-hosting@master/20230713/image.7h434o03uw00.gif

    .. thumbnail:: https://cdn.statically.io/gh/iplai/picx-images-hosting@master/20230713/image.49cp2k6wucy0.webp
        
    .. code:: python

        @tree
        def toon_inner():
            """@material"""

            color = ramped_diffuse_color()

            # shader = inner_faces_shader(color)

            shader = inner_faces_shader_with_hole(color)

            return shader

        bpy.data.materials["Toon Inner"].blend_method = "CLIP"


