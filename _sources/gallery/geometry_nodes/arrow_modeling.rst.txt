Arrow modeling
===============

.. note::

    This example is derived from the `example <https://github.com/al1brn/geonodes/blob/main/docs/arrow.md>`_ from ``geonodes``, you can compare ``pynodes`` with ``geonodes`` in this example. 

.. admonition:: arrow_coord
    :class: pynodes

    .. thumbnail:: https://i.ibb.co/BcTyWQz/Arrow-comp.png

    .. thumbnail:: https://i.ibb.co/q10sgLs/image.png
        
    .. code:: python

        from pynodes import *
        from pynodes.math import *

        @tree
        def arrow_coord(
            l: Float = ("Length", 1, 0),
            r: Float = ("Radius", 0.1, 0.001),
            s: Float = ("Head size", 2, 1.001),
            α: Angle = ("Angle", radians(20), radians(10), radians(89.999)),
            k: Float = ("Recess", 0.5, 0, 0.99),
        ):
            rh = r * s

            tg = tan(α)

            hh = rh / tg
            z0 = l - hh

            h = r / tg
            d = k * h * (s - 1)

            z1 = z0 + d
            z2 = z0 + k * h * s

            return z1, z2

.. admonition:: coord_correction
    :class: pynodes

    .. thumbnail:: https://i.ibb.co/gv4793z/image.png
        
    .. code:: python

        @tree
        def coord_correction(vertices: Integer = (12, 3)):

            f = 1 / cos(pi / vertices)**2

            position = InputPosition()

            corrected_pos = position * (f, f, 1)

            return corrected_pos


.. admonition:: arrow_modeling
    :class: pynodes

    .. thumbnail:: https://i.ibb.co/Q9k7jC0/image.png
        
    .. code:: python

        @tree
        def arrow_modeling( # name(Optional), default, min(Optional), max(Optional)
            l: Float = ("Length", 1, 0),
            r: Float = ("Radius", 0.1, 0.001),
            s: Float = ("Head size", 2, 1.001),
            α: Angle = ("Angle", radians(20), radians(10), radians(89.999)),
            k: Float = ("Recess", 0.5, 0, 0.99),
            vertices: Integer = (12, 3),
            target: Object = None
        ):
            with frame("The start circle from bottom"):

                arrow = MeshCircle(vertices=vertices, radius=r, fill_type='NGON')

            with frame("Calculate z1 and z2"):

                z1, z2 = arrow_coord(l, r, s, α, k)

            with frame("Extrude the arrow shaft"):

                arrow, top, sides = arrow.extrude_edges(offset_scale=z1)

            with frame("Set the material of the arrow shaft"):

                arrow.set_material("Arrow Shaft")

            with frame("Correct the position of the arrow head"):

                corrected_pos = coord_correction(vertices)

            with frame("Extrude the arrow inner part of the arrow head"):

                arrow, top, sides = arrow[top].extrude_edges(offset=corrected_pos - (0, 0, z2), offset_scale=s - 1)

            with frame("Set the material of the arrow head"):

                arrow[sides].set_material("Arrow Head")

            with frame("Extrude the outer part of the arrow head"):

                arrow, top, sides = arrow[top].extrude_edges(offset=(0, 0, l) - corrected_pos)

            with frame("The location the arrow should point to"):

                loc = target.object_info("RELATIVE").location

            with frame("Rotate the arrow to the location of the target object"):

                rot_track = loc.align_euler_to_vector("Z")

                arrow.transform(rotation=rot_track)

            return arrow

.. admonition:: Arrow materials
    :class: pynodes

    .. thumbnail:: https://i.ibb.co/GdndKM6/image.png
        
    .. code:: python

        @tree
        def arrow_head():
            """@material"""

            shader = BSDF.Principled(base_color="#3ac463")

            return shader


        @tree
        def arrow_shaft():
            """@material"""

            shader = BSDF.Principled(base_color="#2c6397")

            return shader