Water Flow
=========================

Use Musgrave Texture to simulate water flowing.

.. note::

    This example is from bilibili by @峰峰居士.

.. raw:: html

    <embed>
        <iframe width="810" height="500" src="//player.bilibili.com/player.html?aid=743420681&bvid=BV18k4y1N7pg&cid=1196747039&page=1" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"> </iframe>
    </embed>

Geometry Nodes
------------------

.. admonition:: Geometry Nodes
    :class: pynodes

    .. thumbnail:: https://cdn.staticaly.com/gh/iplai/picx-images-hosting@master/20230715/image.1vu0t1840ge8.webp

    .. thumbnail:: https://cdn.staticaly.com/gh/iplai/picx-images-hosting@master/20230715/image.1pm0lri7mu0w.webp
        
    .. code:: python

        from pynodes import *

        # Disable viewport denoising
        bpy.context.scene.eevee.use_taa_reprojection = False

        @tree
        def water_flow():
            grid = MeshGrid(20, 20, 100, 100).mesh
            with frame("Vector"):
                time = SceneTime().seconds
                pos = grid.position + (time * 1.5, 0, time * 0.5)
            height = MusgraveTexture("3D", "FBM", pos, 0, 0.2, 5, 1, 2).fac
            grid.set_position(offset=(0, 0, height * 0.5))
            grid.set_position(offset=grid.normal * -0.5)
            return grid.set_shade_smooth().set_material("Water")


Water Material
------------------

.. admonition:: Water Material
    :class: pynodes

    .. thumbnail:: https://cdn.staticaly.com/gh/iplai/picx-images-hosting@master/20230715/image.2fempje3nw00.webp

    .. thumbnail:: https://cdn.staticaly.com/gh/iplai/picx-images-hosting@master/20230715/image.2okz6wm8d2g0.webp
        
    .. code:: python

        @tree
        def water():
            """@material"""
            shader = BsdfPrincipled()
            shader.base_color = "#85BDC1"
            shader.transmission = 1
            shader.roughness = 0.07
            time = InputFloat("#frame/30")
            pos = TextureCoord().object + (time, 0, time * 0.5)
            height = MusgraveTexture("3D", "FBM", pos, 0, 0.6, 5, 1, 2).fac
            shader.normal = height.to_normal(strength=0.1)
            return shader