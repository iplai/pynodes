Text Examples
=============

Text Volume Mesh
-----------------

.. admonition:: Text Volume Mesh
    :class: pynodes

    .. thumbnail:: https://cdn.statically.io/gh/iplai/picx-images-hosting@master/20230713/image.43ih4llcu7e0.gif

    .. thumbnail:: https://cdn.statically.io/gh/iplai/picx-images-hosting@master/20230713/image.42t64zw495a0.webp
        
    .. code:: python

        @tree
        def text_volume_mesh():

            with frame("Text Curve"):

                curve = StringToCurves("Text", align_x="CENTER").curve_instances.realize_instances().Curve.resample_length(0.01)

            with frame("Expand Along Normal"):

                curve = curve.set_position(offset=curve.normal * 0.02)

            with frame("Position Offset by Noise"):

                noise = NoiseTexture("4D", w=SceneTime().seconds * 0.1)

                offset = (noise.color - 0.5) * 0.5

            curve = curve.set_position(offset=offset)

            with frame("Curve to Volume"):

                vol = curve.Points.to_volume("VOXEL_SIZE", voxel_size=0.02, radius=0.04)

            with frame("Volume to Mesh"):

                mesh = vol.to_mesh()

            return mesh