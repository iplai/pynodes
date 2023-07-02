Text Examples
=============

Text Volume Mesh
-----------------

.. admonition:: Text Volume Mesh
    :class: pynodes

    .. thumbnail:: https://i.ibb.co/mDyQTFf/image.gif

    .. thumbnail:: https://i.ibb.co/CBx7w8g/image.png
        
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