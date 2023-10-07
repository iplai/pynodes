Arrow modeling
===============

About
-----------

.. note::

    This example is derived from the `example <https://github.com/al1brn/geonodes/blob/main/docs/arrow.md>`_ from ``geonodes``, you can compare ``pynodes`` with ``geonodes`` in this example. 

Calculate coordinate of arrow
--------------------------------

.. admonition:: arrow_coord
    :class: pynodes

    .. thumbnail:: https://cdn.statically.io/gh/iplai/picx-images-hosting@master/20230713/image.7cj27eak8kg0.webp

    .. thumbnail:: https://cdn.statically.io/gh/iplai/picx-images-hosting@master/20230713/image.66avinfny5k0.webp
        
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

coordinate Correction
--------------------------

.. admonition:: coord_correction
    :class: pynodes

    .. thumbnail:: https://cdn.statically.io/gh/iplai/picx-images-hosting@master/20230713/image.3uy6nq5rsm20.webp
        
    .. code:: python

        @tree
        def coord_correction(vertices: Integer = (12, 3)):

            f = 1 / cos(pi / vertices)**2

            position = InputPosition()

            corrected_pos = position * (f, f, 1)

            return corrected_pos

Arrow Modeling
------------------

.. admonition:: arrow_modeling
    :class: pynodes

    .. thumbnail:: https://cdn.statically.io/gh/iplai/picx-images-hosting@master/20230713/image.lggswhskqrk.webp
        
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

Arrow Materials
-------------------

.. admonition:: Arrow materials
    :class: pynodes

    .. thumbnail:: https://cdn.statically.io/gh/iplai/picx-images-hosting@master/20230713/image.1427vp408cdc.webp
        
    .. code:: python

        @tree
        def arrow_head():
            """@material"""

            shader = BsdfPrincipled(base_color="#3ac463")

            return shader


        @tree
        def arrow_shaft():
            """@material"""

            shader = BsdfPrincipled(base_color="#2c6397")

            return shader