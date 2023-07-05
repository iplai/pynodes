Interactive Sphere Field
============================

Scene Build
------------------

.. admonition:: Scene Build
    :class: pynodes

    .. thumbnail:: https://i.ibb.co/QHgmNyy/image.png

    .. thumbnail:: https://i.ibb.co/sm5ncwx/image.png
        
    .. code:: python

        from pynodes import *

        from pynodes.scene import *

        Tree({
            O.empty_sphere: {},
        }).load()


        @tree
        def sphere_matrix(mesh: Mesh, controller: Object = "Empty Sphere"):

            cube = MeshCube((1.618, 1, 1), 13, 8, 8).mesh

            target = InputPoints(position=controller.location)

            with frame("Control Scale"):

                spheres = MeshIcoSphere(0.2, 4).mesh.on_points(cube, scale=target.proximity("POINTS").distance.color_ramp_with_position((0.2, 0.8), (0.35, 0.2)))

            spheres.set_material("Gradient")
            
            return spheres


Gradient Material
------------------

.. admonition:: Gradient Material
    :class: pynodes

    .. thumbnail:: https://i.ibb.co/KLqJzyR/image.gif

    .. thumbnail:: https://i.ibb.co/VTDdFhr/image.png
        
    .. code:: python

        @tree
        def principled(base_color: Color = (0.8, 0.8, 0.8, 1), roughness: Float = (0.5, 0, 1)):
            """@shader"""
            return BSDF.Principled(base_color=base_color, roughness=roughness)("Shader")


        @tree
        def gradient():
            """@material"""
            with frame("Factor"):
                factor = GradientTexture("SPHERICAL", TextureCoord("Empty Sphere").object.mapping()).fac.color_ramp_with_position((0.3, 0), (0.7, 1))
            with frame("Mix Shader"):
                shader1 = principled()
                shader2 = principled(base_color="#18a161", roughness=0.1)
                shader = MixShader(shader1, shader2, factor)
            return shader
