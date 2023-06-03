import bpy, math


def l_system(axiom, rules, generations):
    """
    Generate an L-system string.

    :param axiom: The starting string.
    :param rules: A dictionary of replacement rules.
    :param generations: The number of iterations to perform.
    :return: The final L-system string.
    """
    for i in range(generations):
        new_string = ""
        for char in axiom:
            if char in rules:
                new_string += rules[char]
            else:
                new_string += char
        axiom = new_string
    return axiom


def get_points(l_system_string, angle, distance):
    """
    Generate a list of points from an L-system string.

    :param l_system_string: The L-system string.
    :param angle: The angle to turn in degrees.
    :param distance: The distance to move forward.
    :return: A list of (x, y) tuples representing the points.
    """
    x = 0
    y = 0
    direction = 0
    points = [(x, y)]
    for char in l_system_string:
        if char == "F":
            x += distance * math.cos(math.radians(direction))
            y += distance * math.sin(math.radians(direction))
            points.append((round(x), round(y)))
        elif char == "+":
            direction += angle
        elif char == "-":
            direction -= angle
    return points


def get_corners(points):
    """
    Get the corner points from a list of points.

    :param points: A list of (x, y) tuples representing the points.
    :return: A list of (x, y) tuples representing the corner points.
    """
    corners = [points[0]]
    for i in range(1, len(points) - 1):
        x1, y1 = points[i - 1]
        x2, y2 = points[i]
        x3, y3 = points[i + 1]
        if (x2 - x1) * (y3 - y2) != (y2 - y1) * (x3 - x2):
            corners.append((x2, y2))
    corners.append(points[-1])
    return corners


axiom = "+A"
rules = {
    'A': '-BF+AFA+FB-',
    'B': '+AF-BFB-FA+'
}
generations = 4
angle = 90
distance = 1

l_system_string = l_system(axiom, rules, generations)
points = get_points(l_system_string, angle, distance)
corners = get_corners(points)

bpy.ops.outliner.orphans_purge(do_recursive=True)
curve_data = bpy.data.curves.new("Hilbert Curve", "CURVE")
curve_obj = bpy.data.objects.new("Hilbert Curve", curve_data)
curve_spline = curve_data.splines.new('POLY')  # 'POLY' 'BEZIER' 'BSPLINE' 'CARDINAL' 'NURBS'
curve_spline.points.add(len(corners) - 1)
for i, point in enumerate(corners):
    x, y = point
    curve_spline.points[i].co = x, y, 0, 1
bpy.context.collection.objects.link(curve_obj)
