Torus Knot
=============

.. admonition:: Torus Knot Coord
    :class: pynodes

    .. thumbnail:: /_static/images/Snipaste_2023-06-29_01-48-13.png
        :group: Torus Knot Coord
        
    .. code:: python

        from pynodes import *
        from pynodes.math import *

        @tree
        def torus_knot_coord(Φ: Float, p: Integer, q: Integer):
            # The name of the function decorated by the decorator is treated as the name of the node tree

            r = cos(q * Φ) + 2

            x = r * cos(p * Φ)

            y = r * sin(p * Φ)

            z = -sin(q * Φ)

            return CombineXYZ(x, y, z)

.. admonition:: Torus Knot Curve
    :class: pynodes

    .. thumbnail:: /_static/images/Snipaste_2023-06-29_02-35-23.png
        :group: Torus Knot Curve
        
    .. code:: python

        @tree
        def torus_knot_curve(
            p: Integer = 2,
            q: Integer = 3,
            # End factor for trim curve (name, default, min, max)
            e: Float = ("End", 1, 0, 1),
            # The larger the value, the smoother the curve (name, default))
            n: Integer = ("Sample", 128)
        ):
            # Create a primitive curve circle node and assign the geometry of the output socket to `curve`
            curve = CurveCircle(resolution=n)

            # Call the node tree defined above as a function
            pos = torus_knot_coord(curve.parameter.factor * 2 * pi, p, q)

            # Use the obtained coordinates to set the position of the curve,
            # and then create a trim curve node to trim the curve by the end factor.
            curve = curve.set_position(position=pos).trim_factor(end=e)

            # Create a frame, pass in the label of the frame.
            with frame("Deal with the connection of endpoints problem"):
                # All nodes created in the scope of the with statement will embeded in this frame
                curve = curve.to_mesh().merge_by_distance().to_curve()
                # The above operation is actually to align the normal lines
                # at the beginning and end of the curve, so that when the mesh
                # surface is generated later, it will not break

            return curve

.. admonition:: Version with material
    :class: pynodes

    .. thumbnail:: /_static/images/Snipaste_2023-06-29_03-20-59.png
        :group: Version with material
        
    .. code:: python

        @tree
        def torus_knot_mesh(
            p: Integer = 3,
            q: Integer = 7,
            e: Float = ("End", 1, 0, 1),
            n: Integer = ("Sample", 256),
            # The radius of the profile curve circle
            r: Float = ("Profile Radius", 0.3)
        ):
            # Call the node tree defined above
            curve = torus_knot_curve(p, q, e, n)

            # Store the parameter factor of the curve for shading
            curve.store_named_attribute("factor", curve.parameter.factor)

            # Sweep the curve to mesh with a profile curve
            mesh = curve.to_mesh(CurveCircle(radius=r))
            # return mesh

            # Optional: set the shade smooth and set the material
            return mesh.set_shade_smooth().set_material("Torus Knot")


        @tree
        def torus_knot():
            """@Material"""

            shader = BSDF.Principled()

            factor = Shader.attribute(name="factor").fac

            color = GradientTexture(vector=factor).color

            color = color.mix("#117f0f")

            shader['Base Color'] = color

            return shader
