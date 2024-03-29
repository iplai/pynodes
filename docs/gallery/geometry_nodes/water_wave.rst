Water Wave
========================

.. admonition:: wave_coord
    :class: pynodes

    .. thumbnail:: https://cdn.statically.io/gh/iplai/picx-images-hosting@master/20230713/Snipaste_2023-06-29_00-37-541.2hllk8g5r760.webp
    .. code:: python

        from pynodes import *
        from pynodes.math import *

        @tree
        def wave_coord(mesh: Mesh, h: Float = 2, Ω: Float = 2, θ: Float = 0):

            d = mesh.position.length

            with frame("z = h * sin(d * Ω - θ) / d"):

                z = h * sin(d * Ω - θ) / d

            return CombineXYZ(mesh.position.x, mesh.position.y, z)

.. admonition:: grid_vertex_select
    :class: pynodes

    .. thumbnail:: https://cdn.statically.io/gh/iplai/picx-images-hosting@master/20230713/Snipaste_2023-06-29_00-40-141.3q0r3ofzu320.webp

    .. code:: python

        @tree
        def grid_vertex_select(grid: Mesh, slice: Boolean):

            with frame("Selection"):

                index = grid.index

                with frame("Index >= 2000"):

                    selection1 = grid[20000:].selection

                with frame("Index % 2 == 0 if slice"):

                    selection2 = grid[Boolean.true.switch(slice, (index % 2) == 0)].selection

            return selection1, selection2

.. admonition:: water_wave
    :class: pynodes

    .. thumbnail:: https://cdn.statically.io/gh/iplai/picx-images-hosting@master/20230713/Snipaste_2023-06-29_00-40-231.3iavy3eynjk0.webp

    .. thumbnail:: https://cdn.statically.io/gh/iplai/picx-images-hosting@master/20230713/Snipaste_2023-06-29_00-45-451.1t2h3z9gz98g.webp

    .. code:: python

        @tree
        def water_wave(
            l: Integer = ("Grid Size", 20),
            n: Integer = ("Grid Subdivision", 200),
            h: Float = ("Height", 2, -10, 10),
            Ω: Float = 2,
            θ: Float = ("Phase", 0),
            slice: Boolean = False
        ):

            grid = MeshGrid(l, l, n, n).mesh

            θ = sin(SceneTime().seconds) * tau

            pos = wave_coord(grid, h, Ω, θ)

            sel1, sel2 = grid_vertex_select(grid, slice)

            grid[sel1].set_position(pos)

            return grid.set_shade_smooth(slice)