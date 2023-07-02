Möbius Band
========================

.. note::

    At first, import namespace

    .. code:: python

        from pynodes import *
        from pynodes.math import *

.. admonition:: extrude_faces
    :class: pynodes

    .. thumbnail:: https://i.ibb.co/rMq2GmK/image.png

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

    .. thumbnail:: https://i.ibb.co/253SHkh/image.png

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

    .. thumbnail:: https://i.ibb.co/W09mpf3/image.gif

    .. thumbnail:: https://i.ibb.co/YPs66Zz/image.png

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
