OSL Shader
================

It is also possible to create your own nodes using `Open Shading Language <https://github.com/AcademySoftwareFoundation/OpenShadingLanguage>`_ (OSL). These nodes will only work with the CPU and OptiX rendering backend. OSL was designed for node-based shading, and each OSL shader corresponds to one node in a node setup. To add an OSL shader, add a script node and link it to a text data-block or an external file. Input and output sockets will be created from the shader parameters on clicking the update button in the Node or the Text editor. OSL shaders can be linked to the node in a few different ways. With the Internal mode, a text data-block is used to store the OSL shader, and the OSO bytecode is stored in the node itself. This is useful for distributing a blend-file with everything packed into it. The External mode can be used to specify a ``.osl`` file from a drive, and this will then be automatically compiled into a ``.oso`` file in the same directory. It is also possible to specify a path to a ``.oso`` file, which will then be used directly, with compilation done manually by the user. The third option is to specify just the module name, which will be looked up in the shader search path.


Color Setting
---------------

:menuselection:`Render Properties --> Color Management --> View Transform`

.. code:: python

    bpy.context.scene.view_settings.view_transform = "Standard"


Render Engine
---------------

Set render engine to cycle.

:menuselection:`Render Properties --> Render Engine`

.. code:: python

    bpy.context.scene.render.engine = "CYCLES"

OSL Support
---------------

Enable open shading language for cycle.

:menuselection:`Render Properties --> Render Engine`

.. code:: python

    bpy.context.scene.cycles.shading_system = True

Load ols files
---------------
Load all the ``.osl`` file needed in this example to blender data-blocks.
The files can be found in ``examles/ols`` folder of the `repo <https://github.com/iplai/pynodes/tree/main/examples/osl>`_.

.. code:: python

    from pynodes.utils import load_text
    import os
    load_text(f"{os.getcwd()}/examples/osl/castironcover.osl")
    load_text(f"{os.getcwd()}/examples/osl/checker.osl")
    load_text(f"{os.getcwd()}/examples/osl/noise.osl")
    load_text(f"{os.getcwd()}/examples/osl/colorname.osl")
    load_text(f"{os.getcwd()}/examples/osl/colorrange.osl")
    load_text(f"{os.getcwd()}/examples/osl/diamondplate.osl")
    load_text(f"{os.getcwd()}/examples/osl/dots.osl")
    load_text(f"{os.getcwd()}/examples/osl/droplet.osl")
    load_text(f"{os.getcwd()}/examples/osl/droplets.osl")

Define Shaders
------------------

.. admonition:: castiron_cover
    :class: pynodes

    .. thumbnail:: https://i.ibb.co/86TMHMg/image.png

    .. thumbnail:: https://i.ibb.co/SngHqjN/image.png
        
    .. code:: python

        @tree
        def castiron_cover():
            """@material"""

            with frame("Castiron Cover"):
                node = ShaderScript(script="castironcover.osl", vector=TextureCoord().uv, scale=1)
                factor = node['Fac'].Float

            with frame("Normal"):
                normal = (factor + NoiseTexture(scale=100).fac * 0.06).to_normal(distance=0.1)

            with frame("Diffuse and Glossy"):
                shader = MixShader(BSDF.Diffuse(color="#1b7cb4", normal=normal, roughness=0.4), BSDF.Glossy(normal=normal, roughness=0.3), 0.2)

            with frame("Switch Transparent"):
                shader = MixShader(shader, BSDF.Transparent(), factor.less_than(0.005))

            return shader

.. admonition:: checker_board
    :class: pynodes

    .. thumbnail:: https://i.ibb.co/Fzcgwtj/image.png

    .. thumbnail:: https://i.ibb.co/85LXWBr/image.png
        
    .. code:: python

        @tree
        def checker_board():
            """@material"""

            node = ShaderScript(script="checker.osl", vector=TextureCoord().uv.mapping())

            return node["Color"]

.. admonition:: color_range
    :class: pynodes

    .. thumbnail:: https://i.ibb.co/VSPztyQ/image.png

    .. thumbnail:: https://i.ibb.co/gRXMbZx/image.png
        
    .. code:: python

        @tree
        def color_range():
            """@material"""

            node = ShaderScript(script="colorrange.osl", value=NoiseTexture().fac, low=0.4, high=0.5)

            return node["Color"]

.. admonition:: Other examples
    :class: pynodes

    .. thumbnail:: https://i.ibb.co/1sK1xjZ/image.png
        :title: Diamond Plate
        :show_caption: true

    .. thumbnail:: https://i.ibb.co/KhDMkHH/image.png
        :title: Dots
        :show_caption: True

    .. thumbnail:: https://i.ibb.co/L1MFy7D/image.png
        :title: Simple Noise
        :show_caption: True

    .. thumbnail:: https://i.ibb.co/1bTzyMM/image.png
        :title: Water Droplet
        :show_caption: True
        
    .. code:: python

        @tree
        def color_name():
            """@material"""
            with frame("Only CPU"):
                node = ShaderScript(script="colorname.osl", file_path=f"{os.getcwd()}/examples/osl/colors.xml")

            return node["Color"]


        @tree
        def simple_noise():
            """@material"""

            node = ShaderScript(script="noise.osl", vector=TextureCoord().uv.mapping())

            return node["Color"]


        @tree
        def dots():
            """@material"""

            with frame("CPU only"):
                node = ShaderScript(script="dots.osl", pos=TextureCoord().object.mapping(), scale=1)

            factor, color = node['Fac'].Float, node['Color'].Color

            shader = MixShader(factor, color)

            with frame("Black background to Transparent"):
                shader = MixShader(shader, BSDF.Transparent(), factor.compare(0, 0))

            return shader


        @tree
        def diamond_plate():
            """@material"""

            vector = TextureCoord().uv

            node = ShaderScript(script="diamondplate.osl", vector=vector, scale=16)

            factor, disp = node['Fac'].Float, node['Disp'].Float

            with frame("Factor to Color"):

                factor = (factor + NoiseTexture(vector=vector, scale=100).fac * 0.3)

                color = factor.color_ramp_with_position(
                    [(0.063, "#000000"), (0.199, "#613B35"), (0.643, "#ffffff")],
                    interpolation="B_SPLINE"
                )

            with frame("Displacement to Normal"):

                normal = disp.to_normal(strength=0.51, distance=0.1)

            with frame("Mix Shader"):

                shader = MixShader(BSDF.Diffuse(color, 0.1, normal), BSDF.Anisotropic("BECKMANN", roughness=0.316, anisotropy=0.2), 0.4)

            return shader


        @tree
        def droplet_wrapper(pos: Vector, time: Float = (0.3, 0, 2), end_time: Float = 2, spread: Float = 1):
            """@shader"""

            node = ShaderScript(script="droplet.osl", pos=pos, time=time, end_time=end_time, spread=spread)

            return node.height


        @tree
        def water_droplet():
            """@material"""

            height = droplet_wrapper(pos=TextureCoord().uv.mapping())

            shader = BSDF.Glossy(normal=height.to_normal(strength=0.1, distance=0.1), roughness=0.0001)

            return shader


        @tree
        def droplets_wrapper(pos: Vector, drops: Integer = 3, time: Float = (0, 0, 10), end_time: Float = 10, spread: Float = 0.03):
            """@shader"""

            node = ShaderScript(script="droplets.osl", pos=pos, drops=drops, time=time, end_time=end_time, spread=spread)

            return node.height


        @tree
        def water_droplets():
            """@material"""

            height = droplets_wrapper(pos=TextureCoord().uv.mapping())

            shader = BSDF.Glossy(normal=height.to_normal(strength=0.1, distance=0.1), roughness=0.25)

            return shader

