from pynodes import *
from pynodes.math import *

font = bpy.data.fonts.load("C:\\Windows\\Fonts\\" + "seguiemj.ttf", check_existing=True)


@tree
def stretchable_bracket(d: Distance = (0, 0, 10), fixed: Boolean = True, reverse: Boolean = False):

    d = d / 2

    curve = StringToCurves("{", "CENTER", "MIDDLE", font=font).curve_instances

    curve = curve.transform((0, -0.01, 0)).realize_instances().Curve

    curve = curve.resample_evaluated()

    a = InputFloat(0.12)

    curve[curve.position.y > 0.15].set_position(offset=(0, d - a, 0))

    curve[curve.position.y < -0.15].set_position(offset=(0, -d + a, 0))

    d = d.switch(reverse, -d)

    curve.transform((0, InputFloat(0).switch(fixed, d), 0))

    return curve
