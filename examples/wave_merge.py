from pynodes import *
from pynodes.math import *


@tree
def func(X: Float, height: Distance = 0.7, width: Distance = 20, tail: Factor = 0.3, frequency: Float = 0.5):

    tail_len = width * tail

    with frame("Middle"):

        y1 = height * sin(2 * pi * frequency * X)

    with frame("Start"):

        y0 = y1 * X / tail_len

    with frame("End"):

        y2 = y1 * (width - X) / tail_len

    return y0.switch(X > tail_len, y1.switch(X > width - tail_len, y2))


@tree
def wave_merge(resolution: Integer = 1024, height: Distance = 0.7, width: Distance = 20, tail: Percentage = (30, 0, 50), f1: Float = 0.5, f2: Float = 0.8, factor: Float = (1, 0, 1)):

    curve = CurveLine(end=(width, 0, 0)).resample(resolution).set_spline_type_catmull_rom()

    x, y, z = curve.position.separate_xyz()

    curve.set_position(offset=(0, func(x, height, width, tail / 100, f1) + func(x, height, width, tail / 100, f2) * factor, 0))

    return curve
