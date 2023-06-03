from pynodes import *


@tree
def cal_z1_z2(
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


@tree
def coord_correction(vertices: Integer = (12, 3)):

    f = 1 / cos(pi / vertices)**2

    position = InputPosition()

    corrected_pos = position * (f, f, 1)

    return corrected_pos


@tree
def arrow_modling(
    l: Float = ("Length", 1, 0),
    r: Float = ("Radius", 0.1, 0.001),
    s: Float = ("Head size", 2, 1.001),
    α: Angle = ("Angle", radians(20), radians(10), radians(89.999)),
    k: Float = ("Recess", 0.5, 0, 0.99),
    vertices: Integer = (12, 3),
    target: Object = None
):

    corrected_pos = coord_correction(vertices)

    z1, z2 = cal_z1_z2(l, r, s, α, k)

    arrow = MeshCircle(vertices=vertices, radius=r, fill_type='NGON')

    arrow.set_material("a")

    arrow, top, sides = arrow.extrude_edges(offset_scale=z1)

    arrow, top, sides = arrow[top].extrude_edges(offset=corrected_pos - (0, 0, z2), offset_scale=s - 1)

    arrow[sides].set_material("b")

    arrow, top, sides = arrow[top].extrude_edges(offset=(0, 0, l) - corrected_pos)

    loc = target.object_info("RELATIVE").location

    rot_track = loc.align_euler_to_vector("Z")

    arrow.transform(rotation=rot_track)

    return arrow
