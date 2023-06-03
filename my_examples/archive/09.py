from pynodes import *

"""N次贝塞尔"""

N = 2
n = N + 1


@tree
def sample_points_position(points: Points):

    return tuple(points.sample_vector_index(points.position, i)(f"p{i}") for i in range(n))


@tree
def points_to_curve(points: Points):

    position = points.sample_vector_index(points.position, points.index)

    curve = CurveLine().resample(points.domain_size.point_count).set_position(position)

    return curve


@tree
def lerp_1(p0: Vector, p1: Vector, t: Float = (0.33, 0, 1)):

    p = p0.mix(p1, 1 - t)

    return p("p")


@tree
def lerp_2(p0: Vector, p1: Vector, p2: Vector, t: Float = (0.33, 0, 1)):

    m0 = lerp_1(p0, p1, t)

    m1 = lerp_1(p1, p2, t)

    return lerp_1(m0, m1, t)


@tree
def lerp_3(p0: Vector, p1: Vector, p2: Vector, p3: Vector, t: Float = (0.33, 0, 1)):

    m0 = lerp_2(p0, p1, p2, t)

    m1 = lerp_2(p1, p2, p3, t)

    return lerp_1(m0, m1, t)


@tree
def lerp_4(p0: Vector, p1: Vector, p2: Vector, p3: Vector, p4: Vector, t: Float = (0.33, 0, 1)):

    m0 = lerp_3(p0, p1, p2, p3, t)

    m1 = lerp_3(p1, p2, p3, p4, t)

    return lerp_1(m0, m1, t)


@tree
def iterate(points: Points, t: Float = (0.33, 0, 1)):

    points_lerped = points.Points[0].delete().set_radius()

    p0 = points.sample_vector_index(points.position, points.index)

    p1 = points.sample_vector_index(points.position, points.index + 1)

    points_lerped.set_position(p0.mix(p1, 1 - t))

    return points_lerped, t


@tree
def change_points_position(points: Points, p0: Vector = None, p1: Vector = None, p2: Vector = None):
    """修改点位置"""

    points_positions = [p0, p1, p2]

    for i, position in enumerate(points_positions):

        points[i].set_position(offset=position)

    return points


@tree
def bezier_curve_example(t: Float = (0.33, 0, 1)):

    with frame("正多边形"):

        curve = CurveCircle(1, n).set_cyclic(False)

        points = curve.to_points("EVALUATED").points

    points = change_points_position(points)

    curve = points_to_curve(points)

    with frame("插点"):

        points_lerped, t = iterate(points, t)

        lerps = [points_lerped]

        for _ in range(n - 2):

            points_lerped, t = iterate(points_lerped, t)

            lerps.append(points_lerped)

    with frame("连线"):

        curves = [points_to_curve(points_lerped) for points_lerped in lerps]

    with frame("曲线"):

        points_positions = sample_points_position(points)

        bezier_curve = CurveLine().resample(32).set_position(globals()[f"lerp_{n-1}"](*points_positions, curve.parameter.factor))

    return curve.join(*curves, *lerps) + bezier_curve
