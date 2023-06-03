from pynodes import *


@tree
def iterate_sier(instances: Instances, cone: Mesh):
    """Iterate Sierp."""
    instances = cone.Instances.on_points(instances, scale=0.5)
    return instances, cone


@tree
def sierpinski_fractal(scale: Float = (2, 0.1, 10)):
    cone = MeshCone(vertices=3, depth=1.5).mesh
    instances, cone = iterate_sier(cone, cone)
    instances.node.label = f"Iterate 1"

    for i in range(5):
        instances, cone = iterate_sier(instances, cone)
        instances.node.label = f"Iterate {i+2}"

    return instances.scale_elements(scale=scale)


@tree
def iterate_menger(instances: Instances, points: Points, scale: Float = (1 / 3, 0, 1 / 3)):
    return instances.on_points(points, scale=scale)


@tree
def menger_init_points():
    points = MeshCube(1, 3, 3, 3).mesh.to_points()
    return points[points.position.length > 0.5].select()


@tree
def menger_fractal():
    cube = MeshCube(1.5).mesh
    points = menger_init_points()
    instances = iterate_menger(cube, points)

    for i in range(2):
        instances = iterate_menger(points=points, instances=instances)

    return instances


# 计算直角三角形内切圆圆心和半径, v3为直角点
@tree
def inscribed_circle(v1: Vector, v2: Vector, v3: Vector):
    """Inscribed Circle of Right Triangle"""

    with frame("边长"):
        c = v1.distance(v2)
        a = v2.distance(v3)
        b = v3.distance(v1)

    with frame("周长"):
        l = c + a + b

    with frame("半径: a + b = c + 2r"):
        r = (a + b - c) / 2

    with frame("圆心"):
        x = (a * v1.x + b * v2.x + c * v3.x) / l
        y = (a * v1.y + b * v2.y + c * v3.y) / l

    return CombineXYZ(x, y)("圆心"), r("半径")


@tree
def iterate_pythagoras(v1: Vector, v2: Vector, angle: Float = (pi / 6, 0, pi / 2), sphere: Mesh = None):

    with frame("边长"):
        length = v1.distance(v2)

    with frame("正方形"):
        v3 = v2.rotate("Z_AXIS", center=v1, angle=pi / 2)
        v4 = v1.rotate("Z_AXIS", center=v2, angle=-pi / 2)

    with frame("直角点"):
        v5 = v4.rotate("Z_AXIS", center=v3, angle=angle)
        v5 = v3.mix(v5, cos(angle))

    with frame("立方体"):
        rect = Quadrangle(v1, v2, v4, v3)
        cube = rect.fill_curve_with_ngons().extrude(length).mesh

    with frame("圆柱"):
        line = v1.mix(v2).line_to(v3.mix(v4))
        cylinder = line.to_mesh(CurveCircle(length / 2), True)

    with frame("球体"):
        center, radius = inscribed_circle(v3, v4, v5)
        # sphere = MeshIcoSphere(radius, 1).mesh.transform(center)
        sphere_transformed = sphere.Mesh.transform(center, scale=radius)

    mesh = cube.switch(True, cylinder.join(sphere_transformed))

    # with frame("三角形"):
    #     c1 = CurveLine(v2, v4).join(CurveLine(v4, v3))

    return mesh("Mesh"), v3('v1'), v5('v2'), v4('v3'), angle("Angle"), sphere


def iterate_n(v1, v2, angle, sphere, curves: list, n=3):
    if n == 0:
        return
    mesh, v1, v2, v3, angle, sphere = iterate_pythagoras(v1, v2, angle, sphere)
    curves.append(mesh)
    iterate_n(v1, v2, angle, sphere, curves, n - 1)
    iterate_n(v2, v3, angle, sphere, curves, n - 1)


@tree
def pythagoras_tree(
    v1: Vector = (-1, 0, 0),
    v2: Vector = (1, 0, 0),
    angle: Float = (pi / 6, 0, pi / 2),
    animate: Boolean = True,
):
    curves = []

    sphere = MeshIcoSphere(subdivisions=3).mesh

    iterate_n(v1, v2, angle.switch(animate, sin(SceneTime().seconds).map_range(-1, 1, 0, pi / 4)), sphere, curves, 6)

    return join(*curves)
