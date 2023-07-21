from pynodes import *

n = 5


@tree
def sample_points_position(points: Points):

    return tuple(points.sample_vector_at_index(points.position, i)(f"p{i}") for i in range(n))


@tree
def lerp_1(p0: Vector, p1: Vector, t: Float = (0.33, 0, 1)):

    p = p0.mix(p1, t)

    return p


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
def geometry_nodes(points_count: Integer = n, fac: Float = (0.33, 0, 1)):

    # with frame("Regular N-gon"):

    curve_regular = CurveCircle(1, points_count).reverse().set_cyclic(False)

    curve_iterate = curve_regular.Curve

    curve_joined = curve_regular.Curve

    with repeat(curve_iterate("Curve"), curve_joined("Curve Joined"), points_count, iterations=points_count - 1) as zone:

        new_curve = curve_iterate.resample(points_count - 1)

        pos = curve_iterate.sample_vector_at_index(curve_iterate.position, curve_iterate.index)
        pos_next = curve_iterate.sample_vector_at_index(curve_iterate.position, curve_iterate.index + 1)

        new_curve.set_position(pos.mix(pos_next, fac))
        curve_joined.join(new_curve)

        zone.to_ouputs(new_curve, curve_joined, points_count - 1)

    with frame("The Result Bézier Curve"):

        points_positions = sample_points_position(curve_regular.points_evaluated)
        bezier_curve = CurveLine().resample(32).set_position(globals()[f"lerp_{n-1}"](*points_positions, curve_regular.parameter.factor))

    return join(curve_joined, curve_joined.points_evaluated, bezier_curve)
