from pynodes import *


@tree
def material():
    """@material"""

    a = VoronoiTexture("2D")

    b = VoronoiTexture("2D", "DISTANCE_TO_EDGE")

    with frame("Surface"):

        with frame("Gray distance with edges"):

            surface = a.distance + b.distance.less_than(0.01)

        with frame("Cell color with edges"):

            surface = a.color + b.distance.less_than(0.01)

    return surface
