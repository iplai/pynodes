from pynodes import *
from pynodes.math import *


@tree
def func(x: Float, h: Distance = 0.7, w: Distance = 20, tail: Factor = 0.3, f: Float = 0.5):

    tail_len = w * tail

    with frame("Middle"):

        y1 = h * sin(2 * pi * f * x)

    with frame("Start"):

        y0 = y1 * x / tail_len

    with frame("End"):

        y2 = y1 * (w - x) / tail_len

    return y0.switch(x > tail_len, y1.switch(x > w - tail_len, y2))


@tree
def wave_merge(resolution: Integer = 1024, h: Distance = 0.7, w: Distance = 20, tail: Percentage = (30, 0, 50), f1: Float = 0.5, f2: Float = 0.8, factor: Float = (1, 0, 1)):

    curve = CurveLine(end=(w, 0, 0)).resample(resolution).set_spline_type_catmull_rom()

    x, y, z = curve.position.separate_xyz()

    with frame("Curve 1"):

        y1 = func(x, h, w, tail / 100, f1)

    with frame("Curve 2"):

        y2 = func(x, h, w, tail / 100, f2) * factor

    curve.set_position(offset=(0, y1 + y2, 0))

    return curve
