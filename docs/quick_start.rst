###############
Quick Start
###############

Install Addon
==============

- Download the latest released zip file from `Github <https://github.com/iplai/pynodes/releases>`_

    .. thumbnail:: https://cdn.statically.io/gh/iplai/picx-images-hosting@master/20230713/image.2l9jgrgq4o00.webp

- Install the addon in Blender

    :menuselection:`Preferences --> Add-ons --> Install`

    .. thumbnail:: https://cdn.statically.io/gh/iplai/picx-images-hosting@master/20230713/image.8ak53qej92c.webp

    Select the file and install.

    .. thumbnail:: https://cdn.statically.io/gh/iplai/picx-images-hosting@master/20230713/image.1jzh5bvmpm2o.webp

When the addon installed, enable it. (check the box of ``Node: PyNodes``).
Then the module ``pynodes`` is in your python path of blender,
and the UI will appear in the Sidebar of Node Editor of Blender.
The nodes in node editor can be arranged in real time with the parameters in UI.

.. thumbnail:: https://cdn.statically.io/gh/iplai/picx-images-hosting@master/20230713/image.4jeuhqxio5g0.gif

Setup VSCode
==============

.. tip::

    It is recommanded to use vscode to write python scripts for blender. Here are tutorials to setup vscode for blender python.

5 Steps to setup VSCode for Blender Python by CG Python (on `Windows <https://www.youtube.com/watch?v=YUytEtaVrrc>`_ `Mac <https://www.youtube.com/watch?v=_0srGXAzBZE>`_ `Linux <https://www.youtube.com/watch?v=zP0s1i9EXeM>`_)

.. raw:: html

    <embed>
        <iframe width="809" height="500" src="https://www.youtube.com/embed/YUytEtaVrrc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
    </embed>


A Quick Example
================

.. admonition:: Target
    :class: important

    Make a parametric Torus Knot

.. thumbnail:: https://cdn.statically.io/gh/iplai/picx-images-hosting@master/20230713/image.78ajgij2yts0.webp
   :align: right
   :height: 220
   :width: 220

   A (3,7)-3D torus knot.

The (p,q)-torus knot winds q times around a circle in the interior of the torus, and p times around its axis of rotational symmetry. If p and q are not relatively prime, then we have a torus link with more than one component.

Parametric Equation
---------------------

The (p,q)-torus knot can be given by the parametrization:

.. math::

    \begin{array}{l}
    r=\cos (q \phi)+2,\ \ 0<\phi<2 \pi\\
    x=r \cos (p \phi) \\
    y=r \sin (p \phi) \\
    z=-\sin (q \phi)
    \end{array}

The First Node Tree
--------------------

Define a node tree corresponding the parametric equation above:

.. admonition:: Torus Knot Coord
    :class: pynodes

    .. thumbnail:: https://cdn.statically.io/gh/iplai/picx-images-hosting@master/20230713/image.m94b81dbki8.webp
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

.. note::

    The tree name will be converted from underscore to camel case.
    Which means ``torus_knot_coord`` is converted to ``Torus Knot Coord``.
    If the decorated function has ``__docstring__``, then use it instead.
    More details see: :class:`pynodes.core.tree`

.. important::

    Type hinting in function signatures cannot be omitted. For normal python programs, type hints are dispensable, just like comments, and do not affect program execution. But in ``pynodes``, the program relies on type hinting to work.

    All valid types are subclasses of :class:`pynodes.core.Socket`.

    :doc:`Available Socket Types <../socket_types>`

The Second Node Tree
---------------------

Make a curve circle, set the position of the curve by calling the function above.

.. admonition:: Torus Knot Curve
    :class: pynodes

    .. thumbnail:: https://cdn.statically.io/gh/iplai/picx-images-hosting@master/20230713/image.6vgg5u5rvn00.webp
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


.. admonition:: Default value of parameter
    :class: note

    After being decorated by the decorator, the parameters of the function represent the group input. You can set a default value for the group input. By default, the name of the group input is the parameter name, or you can set it to a tuple, in which the elements represent: name, default, minimum, and maximum

.. admonition:: About implementation logic
    :class: seealso

    The function decorated by the decorator :class:`pynodes.core.tree`, whether it is defined, or called, the parameters passed to it will not really be executed inside the function body, this point for python beginners, may be very confusing, but you only need to know that in the specific implementation of the decorator, with a set of methods(steal the beams and pillars and replace them rotten timber-perpetrate a fraud).

The Third Node Tree
---------------------

Then sweep the curve to mesh with a profile curve.

.. admonition:: Torus Knot Mesh
    :class: pynodes

    .. thumbnail:: https://cdn.statically.io/gh/iplai/picx-images-hosting@master/20230713/image.1kzbf4sl958g.webp
        :group: Torus Knot Mesh
        
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

            # Sweep the curve to mesh with a profile curve
            mesh = curve.to_mesh(CurveCircle(radius=r))

            return mesh

.. note::

    As you can see from the above example, the creation of a node can be achieved by a set of chain calls, which methods can be called depending on the data type of the port, and the advantage of strict type checking is that you can let the IDE automatically indicate which methods the current object has.

At this point, the Geometry node tree is created, and then you just need to add the geometry node modifier to an object in Blender, set the node tree to ``Torus Knot Mesh``, and you will get the result effect!

Version with material
----------------------

Not only geometry nodes, material nodes are also supported.
Modify the third function, and add a material function. 

.. admonition:: Version with material
    :class: pynodes

    .. thumbnail:: https://cdn.statically.io/gh/iplai/picx-images-hosting@master/20230713/image.17iodwy40hz4.webp
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

            shader = BsdfPrincipled()

            factor = Shader.attribute(name="factor").fac

            color = GradientTexture(vector=factor).color

            color = color.mix("#117f0f")

            shader['Base Color'] = color

            return shader

.. note::

    When the ``__docstring__`` starts with ``@Material`` (case insensitive),
    then the tree represents a material node tree. More details see: :class:`pynodes.core.tree`

Scene Management
-----------------

Besides, Scene management is also possible with ``pynodes``

.. code:: python

    from pynodes.scene import *

    scene = Scene({
        O.cube: {
            "location": (0, 0, 0),
            Mod.geometry_nodes: {
                "node_group": "Torus Knot Mesh",
                "End": [(1, 0.0), (230, 1.0)], # Set keyframe for frame 1 and frame 230
            },
        },
    }).load()

.. caution::

    The submodule :class:`pynodes.scene` is still under construction, very limited features are available at the moment.