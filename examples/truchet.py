from pynodes import *
from pynodes.math import *


@tree
def convert_to_snake_order(index: Integer, n: Integer):

    cur_column = index // n

    return index.switch(cur_column % 2 != 0, cur_column * n + (cur_column + 1) * n - index - 1)


@tree
def triangle_tile():
    curve = CurveCircle(resolution=3)
    curve[0].set_position((-0.5, -0.5, 0))
    curve[1].set_position((0.5, -0.5, 0))
    curve[2].set_position((0.5, 0.5, 0))
    return curve.filled_ngons


@tree
def smith_tiles():
    arc = CurveArc(radius=0.5, sweep_angle=pi * 0.50).transform((-0.5, -0.5, 0))
    arc2 = arc.Curve.transform(rotation=(0, 0, pi))
    tile = join_to_instances(arc, arc2)
    return join_to_instances(tile, tile.Instances.transform(rotation=(0, 0, pi / 2))).store_named_attribute("tile_index", InputIndex())


@tree
def standard_tiles():
    tile = triangle_tile()
    return tile.Instances.on_points(InputPoints(4), rotation=(0, 0, InputIndex() * pi / 2))


@tree
def four_arc_square_tiles():
    """4 Arc Tiles"""
    # 6 different tiles
    tiles: list[Curve] = [0] * 6
    with frame("Semi Circle"):
        semicircle = CurveArc(radius=1 / 6, start_angle=pi / 2, sweep_angle=pi).transform((0.5, 0, 0)).join(CurveLine((0.5, 1 / 6, 0), (0.5, -1 / 6, 0)))
    with frame("Corner Arc"):
        corner_arc = CurveArc(radius=1 / 3, start_angle=pi, sweep_angle=pi / 2).transform((0.5, 0.5, 0))
    with frame("Biggest Arc"):
        big_arc = CurveArc(32, radius=2 / 3, start_angle=pi, sweep_angle=pi / 2).transform((0.5, 0.5, 0))
    with frame("Center Line"):
        center_line = CurveLine((0.5, -1 / 6, 0), (0.5, 1 / 6, 0))
    with frame("Tile 0"):
        tiles[0] = corner_arc.Curve.join(center_line).on_points(InputPoints(4), rotation=(0, 0, InputIndex() * pi / 2)).realize_instances().Curve.to_mesh().merge_by_distance().to_curve()
    with frame("Tile 1"):
        tiles[1] = semicircle.Curve.on_points(InputPoints(4), rotation=(0, 0, InputIndex() * pi / 2)).realize_instances().Curve.to_mesh().merge_by_distance().to_curve()
    with frame("Tile 2"):
        curve = center_line.Curve.join(center_line.Curve.transform(rotation=(0, 0, pi / 2)), corner_arc, big_arc)
        tiles[2] = curve.join(curve.Curve.transform(rotation=(0, 0, pi))).to_mesh().merge_by_distance().to_curve()
    with frame("Tile 3"):
        curve = semicircle.Curve.join(semicircle.Curve.transform(rotation=(0, 0, pi / 2)))
        curve.join(big_arc.Curve.transform(rotation=(0, 0, pi)), corner_arc.Curve.transform(rotation=(0, 0, pi)), center_line.Curve.transform(rotation=(0, 0, pi)), center_line.Curve.transform(rotation=(0, 0, -pi / 2)))
        tiles[3] = curve.to_mesh().merge_by_distance().to_curve()
    with frame("Tile 4"):
        curve = semicircle.Curve.join(semicircle.Curve.transform(rotation=(0, 0, pi)))
        curve.join(Rectangle(1 / 3, 1))
        tiles[4] = curve.to_mesh().merge_by_distance().to_curve()
    with frame("Tile 5"):
        curve = CurveLine((-1 / 6, -0.5, 0), (-1 / 6, 0.5, 0)).join(center_line, center_line.Curve.transform(rotation=(0, 0, pi / 2)), center_line.Curve.transform(rotation=(0, 0, -pi / 2)))
        curve.join(corner_arc, corner_arc.Curve.transform(rotation=(0, 0, -pi / 2)))
        curve.join(semicircle.Curve.transform(rotation=(0, 0, pi)))
        tiles[5] = curve.to_mesh().merge_by_distance().to_curve()
    return join_to_instances([tile.filled_ngons for tile in tiles if tile])


@tree
def truchet_tiling(tiles: Instances, n: Integer = 4, pick_random: Boolean = False, seed: Integer = 0):
    grid_size = n - 1
    grid = MeshGrid(grid_size, grid_size, n, n)
    tiles_max_index = tiles.domain_size - 1
    instance_index = tiles.index.switch(pick_random, RandomInteger(0, tiles_max_index, seed=seed))
    return tiles.on_points(grid.mesh, pick_instance=True, instance_index=instance_index)


@tree
def curve_pattern_to_mesh(tiles: Instances):
    return tiles.realize_instances().Curve.to_mesh().merge_by_distance().to_curve().to_mesh(CurveCircle(0.1)).set_material("Curve Pattern")


@tree
def windmill_pattern(n: Integer = 1, reverse: Boolean = False):
    with frame("Tiles"):
        tile = triangle_tile()
        angles = [
            InputFloat(0).switch(reverse, 1) * pi,
            InputFloat(-1).switch(reverse, 1) * pi / 2,
            InputFloat(1).switch(reverse, -1) * pi / 2,
            InputFloat(1).switch(reverse, 0) * pi
        ]
        tiles = [
            tile.Mesh.transform(rotation=(0, 0, angles[i])).join_to_instances()
            for i in range(len(angles))
        ]
    tiles = join_to_instances(tiles)
    with frame("Basic Pattern"):
        pattern1 = tiles.on_points(MeshGrid(1, 1, 2, 2).mesh, pick_instance=True).store_named_attribute("tile_index", InputIndex())
    with frame("Result Pattern"):
        grid_size = (n - 1) * 2
        pattern2 = pattern1.Instances.on_points(MeshGrid(grid_size, grid_size, n, n).mesh)
    return pattern1("Basic Pattern"), pattern2("Result Pattern")


@tree
def index_number_to_curve(index: Integer, max_index: Integer, size: Float):
    return index.to_string().to_curve("CENTER", "MIDDLE", size=size).curve_instances.join_to_instances().switch(max_index < index)


@tree
def convert_to_hilbert(index: Integer):

    nums = [0, 4, 5, 1, 2, 3, 7, 6, 10, 11, 15, 14, 13, 9, 8, 12]

    value = index

    for i, num in enumerate(nums):

        value = value.switch(index == num, i)

    return value


@tree
def show_index_of_instances(instances: Instances, size: Float = 1, offset: Vector = (0, 0, 0)):
    numbers = []
    max_index = instances.domain_size - 1
    for i in range(36):
        with frame(f"Index {i}"):
            numbers.append(index_number_to_curve(i, max_index, size))
    numbers = join(numbers)
    with frame("Set position offset"):
        with frame("Sample position"):
            pos = instances.sample_vector_at_index(instances.position, InputIndex())
        numbers.set_position(offset=pos + offset)
    return instances + numbers


@tree
def truchet_tiling_with_delete(n: Integer = 20, seed: Integer = 0, m: Integer = (20, 0, 40)):

    tiles = truchet_tiling(n, seed, m)

    with frame("Delete"):

        index = tiles.index
        tiles[(index % n >= m) | (index // n >= m)].delete_instances()

    return tiles


@tree
def geometry_nodes(mesh: Mesh):
    # return windmill_pattern(4)[1].set_material("Direction Color")
    # return curve_pattern_to_mesh(general_truchet(smith_tiles()))
    tiles = truchet_tiling(four_arc_square_tiles(), 6, True).set_material("Curve Pattern")
    return show_index_of_instances(tiles)


@tree
def direction_color():
    """@material"""
    shader = BSDF.Principled()
    color = MagicTexture(vector=shader.attribute("tile_index", "INSTANCER").fac).color
    shader.base_color = color
    return shader


@tree
def curve_pattern():
    """@material"""
    shader = BSDF.Principled(roughness=0.2)
    shader.base_color = "#c53bd1"
    return shader
