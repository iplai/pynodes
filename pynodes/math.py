from .datasocks import Float


def sin(value=0.5, clamp=False):
    """The [Sine](https://en.wikipedia.org/wiki/Sine) of the input value.
    #### Path
    - Utilities > Math > Math Node
    """
    return Float.math(value, "SINE", use_clamp=clamp)


def cos(value=0.5, clamp=False):
    """The [Cosine](https://en.wikipedia.org/wiki/Cosine) of the input value.
    #### Path
    - Utilities > Math > Math Node
    """
    return Float.math(value, "COSINE", use_clamp=clamp)


def tan(value=0.5, clamp=False):
    """The [Tangent](https://en.wikipedia.org/wiki/Tangent) of the input value.
    #### Path
    - Utilities > Math > Math Node
    """
    return Float.math(value, "TANGENT", use_clamp=clamp)


def cot(value=0.5, clamp=False):
    """
    #### Path
    - Utilities > Math > Math Node
    """
    return 1 / Float.math(value, "TANGENT", use_clamp=clamp)


def sec(value=0.5, clamp=False):
    """
    #### Path
    - Utilities > Math > Math Node
    """
    return 1 / Float.math(value, "COSINE", use_clamp=clamp)


def csc(value=0.5, clamp=False):
    """
    #### Path
    - Utilities > Math > Math Node
    """
    return 1 / Float.math(value, "SINE", use_clamp=clamp)


def sqrt(value=0.5, clamp=False):
    """The square root of the value.
    #### Path
    - Utilities > Math > Math Node
    """
    return Float.math(value, "SQRT", use_clamp=clamp)


def sinh(value=0.5, clamp=False):
    """The [Hyperbolic Sine](https://en.wikipedia.org/wiki/Inverse_trigonometric_functions) of the input value.
    #### Path
    - Utilities > Math > Math Node
    """
    return Float.math(value, "SINH", use_clamp=clamp)


def cosh(value=0.5, clamp=False):
    """The [Hyperbolic Cosine](https://en.wikipedia.org/wiki/Inverse_trigonometric_functions) of the input value.
    #### Path
    - Utilities > Math > Math Node
    """
    return Float.math(value, "COSH", use_clamp=clamp)


def arcsin(value=0.5, clamp=False):
    """The [ArcSine](https://en.wikipedia.org/wiki/Inverse_trigonometric_functions) of the input value.
    #### Path
    - Utilities > Math > Math Node
    """
    return Float.math(value, "ARCSINE", use_clamp=clamp)


def arccos(value=0.5, clamp=False):
    """The [ArcCosine](https://en.wikipedia.org/wiki/Inverse_trigonometric_functions) of the input value.
    #### Path
    - Utilities > Math > Math Node
    """
    return Float.math(value, "ARCCOSINE", use_clamp=clamp)


def arctan(value=0.5, clamp=False):
    """The [ArcTangent](https://en.wikipedia.org/wiki/Inverse_trigonometric_functions) of the input value.
    #### Path
    - Utilities > Math > Math Node
    """
    return Float.math(value, "ARCTANGENT", use_clamp=clamp)


def exp(value):
    """Raises [Euler's number](https://en.wikipedia.org/wiki/E_(mathematical_constant)) to the power of the value.
    #### Path
    - Utilities > Math > Math Node
    """
    return Float.math(value, "EXPONENT")


def log(value, base=0.5, clamp=False):
    """The log of the value with a Base as its base.
    #### Path
    - Utilities > Math > Math Node
    """
    return Float.math(value, "LOGARITHM", base, use_clamp=clamp)


def ln(value, clamp=False):
    """The Natural logarithm.
    #### Path
    - Utilities > Math > Math Node
    """
    import math
    return Float.math(value, "LOGARITHM", math.e, use_clamp=clamp)


from math import pi, tau, e, radians, degrees, floor, ceil
