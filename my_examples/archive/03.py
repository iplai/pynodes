from pynodes import *

sin = Float.sin
tau = math.tau


@tree
def compute_coord(mesh: Mesh, h: Float = 2, Ω: Float = 2, θ: Float = 0):
    """Compute XYZ"""
    d = mesh.position.length
    z = h * sin(d * Ω - θ) / d
    return mesh.position.x, mesh.position.y, z("Z")


@tree
def water_wave(
    l: Integer = ("Grid Size", 20),
    n: Integer = ("Grid Subdivision", 200),
    h: Float = ("Height", 2, -10, 10),
    Ω: Float = 2,
    # θ: Float = ("Offset", 0),
    slice: Boolean = False
):

    grid = MeshGrid(l, l, n, n).mesh

    t = SceneTime().seconds
    θ = sin(t) * tau
    x, y, z = compute_coord(grid, h, Ω, θ)

    # grid = grid[20000:][Boolean.true.switch(slice, (grid.index % 2) == 0)].set_position((x, y, z))
    grid = grid[Boolean.true.switch(slice, (grid.index % 2) == 0)].set_position((x, y, z))

    return grid.set_shade_smooth(slice)


@tree
def mesh_transition(mesh1: Mesh, mesh2: Mesh, factor: Float = (0, 0, 1), smooth: Boolean = False):

    old_pos = mesh1.capture_vector_on_points(mesh1.position)

    new_pos = mesh2.sample_vector_index(mesh1.position, mesh2.sample_nearest())

    mesh1.set_position(old_pos.mix(new_pos, factor))

    return mesh1.set_shade_smooth(shade_smooth=smooth & (factor < 1))


@tree
def geometry_nodes(mesh: Mesh, factor: Float = (0, 0, 1)):

    mesh1 = mesh.subdivision_surface(level=3, edge_crease=0.2)

    mesh2 = MeshIcoSphere(subdivisions=2).mesh

    return mesh_transition(mesh1, mesh2, factor)
