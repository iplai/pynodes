World Shader
================

This is the default world shader of blender

.. code:: python

    from pynodes import *

    @tree
    def world():
        """@World"""

        bpy.data.images.load("C:/Program Files/Blender Foundation/Blender 3.5/3.5/datafiles/studiolights/world/forest.exr", check_existing=True)

        color = EnvironmentTexture("forest.exr").color

        return color


