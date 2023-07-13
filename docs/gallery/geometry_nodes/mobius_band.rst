Möbius Band
========================

Möbius Band with Extruded Face
---------------------------------

.. note::

    At first, import namespace

    .. code:: python

        from pynodes import *
        from pynodes.math import *

.. admonition:: extrude_faces
    :class: pynodes

    .. thumbnail:: https://cdn.staticaly.com/gh/iplai/picx-images-hosting@master/20230713/image.11l7gufyn67k.webp

    .. code:: python

        @tree
        def extrude_faces(mesh: Mesh, distance: Distance):

            mesh, top, side = mesh[mesh.index % 4 == 0].extrude_faces(distance)

            with frame("Scale Extruded Top Faces"):

                t = SceneTime().seconds

                scale = sin(t * 2).map_range(-1, 1, 0, 0.8)

                mesh = mesh[top].scale_elements(scale)

            return mesh

.. admonition:: curve_to_mesh
    :class: pynodes

    .. thumbnail:: https://cdn.staticaly.com/gh/iplai/picx-images-hosting@master/20230713/image.39vf62vin6w0.webp

    .. code:: python

        @tree
        def curve_to_mesh(curve: Curve):

            with frame("Profile"):

                profile = CurveCircle(0.15, 3)

                profile = Rectangle(0.3, 0.05)

            mesh = curve.to_mesh(profile).merge_by_distance(0.03).set_shade_smooth(False)

            return mesh

.. admonition:: möbius_band
    :class: pynodes

    .. thumbnail:: https://cdn.staticaly.com/gh/iplai/picx-images-hosting@master/20230713/image.4mscnoo6p2i0.gif

    .. thumbnail:: https://cdn.staticaly.com/gh/iplai/picx-images-hosting@master/20230713/image.64gbaqb2n380.webp

    .. code:: python

        @tree
        def möbius_band(resolution: Integer = 64, factor: Factor = (1, 0, 1), extrude_amount: Distance = (0.3, 0)):

            curve = CurveCircle(resolution=resolution).trim_factor(end=factor)

            t = SceneTime().seconds

            with frame("Set Curve Tilt"):

                curve.set_tilt(curve.parameter.factor * factor * tau + t)

            sweeped_mesh = curve_to_mesh(curve)

            with frame("Extrude faces of one side"):

                extruded_mesh = extrude_faces(sweeped_mesh, extrude_amount)

            return join(sweeped_mesh.switch(extrude_amount > 0, sweeped_mesh + extruded_mesh), curve)

Möbius Band with Vertex Balls
---------------------------------

.. admonition:: Möbius Band with Vertex Balls
    :class: pynodes

    .. thumbnail:: https://cdn.staticaly.com/gh/iplai/picx-images-hosting@master/20230713/image.5px6a99am700.gif

    .. thumbnail:: https://cdn.staticaly.com/gh/iplai/picx-images-hosting@master/20230713/image.638atcnmoi80.webp

    .. code:: python

        @tree
        def möbius_band(resolution: Integer = 64, tilt: Float = (tau, 0)):

            curve = CurveCircle(3, resolution)

            with frame("Curve Tilt"):

                t = SceneTime().seconds

                curve = curve.set_tilt(curve.parameter.factor.map_range(0, 1, 0, tilt) + t).trim_factor()

            with frame("Curve to Mesh"):

                with frame("Profile"):

                    line = Rectangle(3, 0.05)

                    circle = CurveCircle(1.5, 3).subdivide(3)

                profile = circle

                mesh = curve.to_mesh(profile).merge_by_distance(0.15).set_shade_smooth(False).set_material("#51be51")

            return mesh


        @tree
        def abstract_loop(radius: Float = 0.35):

            points = möbius_band(resolution=32).to_points("FACES")

            mesh = MeshUVSphere(radius=radius).mesh.Instances.on_points(points).set_material("#e7539d")

            return mesh
