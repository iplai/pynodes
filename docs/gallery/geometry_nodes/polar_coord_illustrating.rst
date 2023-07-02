Polar Coordinate Illustrating
================================

Concentric Circles
-----------------------

.. admonition:: concentric_circles
    :class: pynodes

    .. thumbnail:: https://i.ibb.co/0GjYSGP/image.png

    .. thumbnail:: https://i.ibb.co/5h6xgJw/image.png
        
    .. code:: python

        from pynodes import *
        from pynodes.math import *

        @tree
        def concentric_circles(band_width: Float = 0.02, count: Integer = (20, 0, 100)):

            points = InputPoints(count=count)

            circle = CurveCircle().set_spline_type("CATMULL_ROM")

            with frame("Clone circles and set scale"):

                circles = circle.on_points(points, scale=(points.index + 1, points.index + 1, 1)).realize_instances()

            with frame("Curve to Mesh and Set material"):

                mesh = circles.to_mesh(CurveLine((-band_width, 0, 0), (band_width, 0, 0))).set_material("Cerulean")

            return mesh

Axis Slices            
----------------
Slice the plane radially, except the x,y-axis.

.. admonition:: axis_slices
    :class: pynodes

    .. thumbnail:: https://i.ibb.co/C2wDGMm/image.png

    .. thumbnail:: https://i.ibb.co/y57NHxT/image.png
        
    .. code:: python

        @tree
        def axis_slices(width: Float = 0.05, length: Float = 50):

            line = Rectangle(length, width).filled_ngons

            lines = [line.Mesh.transform(rotation=(0, 0, pi / 8 * i)) for i in range(8) if i % 4 != 0]

            return join(lines).Mesh.set_material("Cerulean")

Angle Spiral
----------------
The Spiral to illustrate the rotation of coordinate.

.. admonition:: angle_spiral
    :class: pynodes

    .. thumbnail:: https://i.ibb.co/N2wFn4z/image.gif

    .. thumbnail:: https://i.ibb.co/x1YYHny/image.png
        
    .. code:: python

        @tree
        def angle_spiral(end: Float = (1, 0, 1)):

            with frame("Spiral"):

                curve = CurveSpiral(64, 1, 1, 1.08, -0.01, True).set_spline_type("CATMULL_ROM")

            with frame("Trim Spiral"):

                curve = curve.trim_factor(end=end.float_curve(points=[(0, 0.001), (0.53, 0.52), (1, 1)]))

            with frame("Curve to Mesh"):

                mesh = curve.to_mesh(CurveLine((-0.03, 0, 0), (0.03, 0, 0)))

            return mesh.set_material("Cerise")

Text of Polar Coord
--------------------

.. admonition:: radial_coord_text
    :class: pynodes

    .. thumbnail:: https://i.ibb.co/xJhrpFq/image.gif

    .. thumbnail:: https://i.ibb.co/rxFvsdL/image.png
        
    .. code:: python

        # Times New Roman Bold
        font = bpy.data.fonts.load("C:\\Windows\\Fonts\\" + "timesbd.ttf", check_existing=True)

        @tree
        def get_position(r: Float = 2.2, θ: Float = 0):

            return CombineXYZ(r * cos(θ), r * sin(θ), 0)

        @tree
        def radial_coord_text(r: Float = 2.2, θ: Float = 0, decimals: Integer = 2, scale: Float = 1):

            with frame("Get Position"):

                pos = get_position(r, θ)

            with frame("Radius String"):

                string_r = r.to_string(decimals)

            with frame("Angle String"):

                string_θ = θ.to_string(decimals)

            with frame("String Length"):

                length_r = string_r.length

                length_θ = string_θ.length

            with frame("Join String"):

                string = InputString("(").join(string_r, InputString(", "), string_θ, InputString(")"))

            with frame("String to Curve Instances"):

                instances = string.to_curves(align_x="CENTER", size=0.5 * scale, font=font).curve_instances

                instances.transform(pos).transform((0, 0.2, 0.01))

            with frame("Seperate String Curves"):

                text1, text2 = instances[0, length_r + 1, length_r + length_θ + 3].separate()

            text1 = text1.Curve.filled_mesh.set_material("Black")

            with frame("Seperate Float String Curves"):

                text2, text3 = text2[:length_r].separate()

            text2 = text2.Curve.filled_ngons.set_material("Green")

            text3 = text3.Curve.filled_ngons.set_material("Cerise")

            return text1.join(text2, text3)

Line from origin to dot
------------------------

.. admonition:: line_from_origin_to_dot
    :class: pynodes

    .. thumbnail:: https://i.ibb.co/1s0zjWx/image.png
        
    .. code:: python

        @tree
        def line_from_origin_to_dot(r: Float = 2.2, θ: Float = 0):

            pos = (r * cos(θ), r * sin(θ), 0)

            with frame("Line and Dots"):

                line = CurveLine(end=pos).to_mesh(CurveLine((-0.02, 0, 0), (0.02, 0, 0)))

                dot1 = CurveCircle(0.05)

                dot2 = dot1.Curve.transform(pos)

                dot = dot1.join(dot2).filled_ngons

                line = line.join(dot).set_material("Green")

            text = radial_coord_text(r, θ)

            return line.join(text)

Dot with Coord Text
---------------------

.. admonition:: dot_with_coord_text
    :class: pynodes

    .. thumbnail:: https://i.ibb.co/WWqj0FL/image.png
        
    .. code:: python

        @tree
        def dot_with_coord_text(r: Float = 2.2, θ: Float = 0, decimals: Integer = 2, scale: Float = 1, material: Material = None):

            pos = (r * cos(θ), r * sin(θ), 0)

            with frame("Dot"):

                dot = CurveCircle(0.05 * scale).transform(pos).filled_ngons.set_material(material)

            text = radial_coord_text(r, θ, decimals, scale)

            return dot.join(text)

Materials
--------------------------

.. admonition:: Materials
    :class: pynodes
        
    .. code:: python

        @tree
        def cerulean():
            """@material"""
            return BSDF.Principled(base_color="#0070A8", alpha=0.5)

        bpy.data.materials["Cerulean"].blend_method = "BLEND"

        @tree
        def cerise():
            """@material"""
            return BSDF.Principled(base_color="#CE009E")

        @tree
        def green():
            """@material"""
            return BSDF.Principled(base_color="#158C00")

        @tree
        def black():
            """@material"""
            return BSDF.Principled(base_color="#000000")

The Result Illustration
--------------------------

.. admonition:: polar_coordinates
    :class: pynodes

    .. thumbnail:: https://i.ibb.co/y5WxZXF/image.gif

    .. thumbnail:: https://i.ibb.co/nnxpwHK/image.png
        
    .. code:: python

        @tree
        def polar_coordinates(radius: Float = 1.33, factor: Float = (0.3, 0, 1), r: Float = 1.5, θ: Float = pi / 4):

            meshes = [concentric_circles(), axis_slices()]

            meshes.append(line_from_origin_to_dot(r=radius, θ=factor * tau))

            meshes.append(angle_spiral(factor))

            meshes.append(dot_with_coord_text(r, θ, material="Black"))

            return join(meshes)
