from pynodes import *
from pynodes.utils import get_or_create_mat, load_font
"""极坐标"""
bpy.context.scene.view_settings.view_transform = "Standard"
bpy.context.scene.render.fps = 60


font = load_font("Times New Roman Bold", "timesbd.ttf")


cerulean = get_or_create_mat("Cerulean", (*rgb(0, 112, 168), 0.5))

cerise = get_or_create_mat("Cerise", (*rgb(206, 0, 158), 1))

green = get_or_create_mat("Green", (*rgb(21, 140, 0), 1))

black = get_or_create_mat("Black", (*rgb(0, 0, 0), 1))


@tree
def circle_band(radius: Float, band_width: Float):

    circle = CurveCircle(radius).set_spline_type("CATMULL_ROM")

    return circle.to_mesh(CurveLine((-band_width, 0, 0), (band_width, 0, 0)))


@tree
def concentric_circles(band_width: Float = 0.02):

    circles = [circle_band(i, band_width) for i in range(1, 20)]

    return join(*circles).Mesh.set_material(cerulean)


@tree
def axis_slices():

    line = Rectangle(20, 0.02).filled_ngons

    lines = [line.Mesh.transform(rotation=(0, 0, pi / 8 * i)) for i in range(8) if i % 4 != 0]

    return join(lines).Mesh.set_material(cerulean)


@tree
def angle_spiral(end: Float = (1, 0, 1)):

    curve = CurveSpiral(64, 1, 1, 1.08, -0.01, True).set_spline_type("CATMULL_ROM")

    curve = curve.trim_factor(end=end.float_curve(points=[(0, 0.001), (0.53, 0.52), (1, 1)]))

    mesh = curve.to_mesh(CurveLine((-0.03, 0, 0), (0.03, 0, 0)))

    return mesh.set_material(cerise)


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

    text1 = text1.Curve.filled_mesh.set_material(black)

    with frame("Seperate Float String Curves"):

        text2, text3 = text2[:length_r].separate()

    text2 = text2.Curve.filled_ngons.set_material(green)

    text3 = text3.Curve.filled_ngons.set_material(cerise)

    return text1.join(text2, text3)


@tree
def origin_to_dot(r: Float = 2.2, θ: Float = 0):

    pos = (r * cos(θ), r * sin(θ), 0)

    with frame("Line and Dots"):

        line = CurveLine(end=pos).to_mesh(CurveLine((-0.02, 0, 0), (0.02, 0, 0)))

        dot1 = CurveCircle(0.05)

        dot2 = dot1.Curve.transform(pos)

        dot = dot1.join(dot2).filled_ngons

        line = line.join(dot).set_material(green)

    text = radial_coord_text(r, θ)

    return line.join(text)


@tree
def dot_with_coord_text(r: Float = 2.2, θ: Float = 0, decimals: Integer = 2, scale: Float = 1, material: Material = None):

    pos = (r * cos(θ), r * sin(θ), 0)

    with frame("Dot"):

        dot = CurveCircle(0.05 * scale).transform(pos).filled_ngons.set_material(material)

    text = radial_coord_text(r, θ, decimals, scale)

    return dot.join(text)


def prime_fast_generator(n):
    result = [2, 3]
    a = 5
    b = 7
    count = 3
    factor = [5]  # caching factor
    threshold = 25  # instead of calculating square-root on each candidate,
    while a < n:  # ...I change threshold every other time
        if a == threshold:
            factor.append(result[count])
            threshold = factor[-1]**2
            count += 1
        elif all(a % k for k in factor):
            result.append(a)
        if b >= n:
            break
        elif b == threshold:
            factor.append(result[count])
            threshold = factor[-1]**2
            count += 1
        elif all(b % k for k in factor):
            result.append(b)
        a += 6
        b += 6
    return result


@tree
def prime_coords(scale: Float = 2):
    meshes = []

    for i in prime_fast_generator(15):

        meshes.append(dot_with_coord_text(i, i, 0, scale, material=black))

    return join(meshes)


@tree
def polar_coordinates(radius: Float = 1.33, factor: Float = (0.3, 0, 1)):
    """极坐标"""

    meshes = [concentric_circles(), axis_slices()]

    meshes.append(origin_to_dot(r=radius, θ=factor * tau))

    meshes.append(angle_spiral(factor))

    meshes.append(dot_with_coord_text(1.5, pi / 4, material=black))

    # meshes.append(prime_coords())

    return join(meshes)


from pynodes.scene import *

scene = Tree({
    O.cube: {
        Mod.geometry_nodes: {
            "node_group": "极坐标",
            "Factor": [(1, 0), (120, 1)]
        },
    },
}).load()

scene[O.cube].select_set(False)
