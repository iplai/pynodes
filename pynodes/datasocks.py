import bpy, typing, math

from bpy.types import NodeSocket
from .core import Socket, new_node, new_link
from . import nodes


class Float(Socket):
    """Floating-point number socket of a node, float in [-inf, inf], default 0.0"""
    bl_idname = "NodeSocketFloat"

    def switch(self, switch=False, true_float=True):
        """The Switch node outputs one of two inputs depending on a condition. Only the input that is passed through the node is computed.
        #### Path
        - Utilities > Switch Node
        #### Outputs:
        - `#0 output: Float = 0.0`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeSwitch.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/switch.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeSwitch.html)
        """
        node = new_node(*nodes.GeometryNodeSwitch("FLOAT", switch, false=self, true=true_float))
        return node.outputs[0].Float

    def mix(self, factor_float=0.5, b_float=0.0, clamp_factor=True):
        """The Mix Node mixes values, colors and vectors inputs using a factor to control the amount of interpolation. The Color mode has additional blending modes.
        #### Path
        - Utilities > Math > Mix Node
        #### Outputs:
        - `#0 result_float: Float = 0.0`

        ![](https://docs.blender.org/manual/en/latest/_images/render_shader-nodes_shader_mix_node.jpg)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/color/mix_rgb.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html)
        """
        node = new_node(*nodes.ShaderNodeMix(data_type='FLOAT', clamp_factor=clamp_factor, factor_float=factor_float, a_float=self, b_float=b_float))
        return node.outputs[0].Float

    def color_ramp(self, start_color=(0.0, 0.0, 0.0, 1.0), end_color=(1.0, 1.0, 1.0, 1.0), interpolation=None):
        """The Color Ramp Node is used for mapping values to colors with the use of a gradient.

        item of colors: hex string or float or tuple
        #### Path
        - Utilities > Color > Color Ramp Node
        #### Outputs:
        - `#0 color: Color = (0.0, 0.0, 0.0, 0.0)`
        - `#1 alpha: Float = 0.0`

        ![](https://docs.blender.org/manual/en/latest/_images/compositing_node-types_CompositorNodeValToRGB.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/color/color_ramp.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeValToRGB.html)
        """
        from .colors import color_tuple
        node = new_node(*nodes.ShaderNodeValToRGB(None, self))
        bnode: bpy.types.ShaderNodeValToRGB = node.bnode
        color_ramp = bnode.color_ramp
        if interpolation is not None:
            color_ramp.interpolation = interpolation
        element = color_ramp.elements[0]
        element.color = color_tuple(start_color)
        element = color_ramp.elements[1]
        element.color = color_tuple(end_color)
        return node.outputs[0].Color

    def color_ramp_uniform(self, *colors, interpolation=None):
        """The Color Ramp Node is used for mapping values to colors with the use of a gradient.

        item of colors: hex string or float or tuple
        #### Path
        - Utilities > Color > Color Ramp Node
        #### Outputs:
        - `#0 color: Color = (0.0, 0.0, 0.0, 0.0)`
        - `#1 alpha: Float = 0.0`

        ![](https://docs.blender.org/manual/en/latest/_images/compositing_node-types_CompositorNodeValToRGB.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/color/color_ramp.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeValToRGB.html)
        """
        from .colors import color_tuple
        node = new_node(*nodes.ShaderNodeValToRGB(None, self))
        bnode: bpy.types.ShaderNodeValToRGB = node.bnode
        color_ramp = bnode.color_ramp
        if interpolation is not None:
            color_ramp.interpolation = interpolation
        if len(colors) > 0 and isinstance(colors[0], list):
            colors = colors[0]
        count = len(colors)
        for _ in range(count - 2):
            color_ramp.elements.new(0)
        for i, color in enumerate(colors):
            element = color_ramp.elements[i]
            element.position = i / (count - 1)
            element.color = color_tuple(color)
        return node.outputs[0].Color

    def color_ramp_with_position(self, *colors: tuple, interpolation=None):
        """The Color Ramp Node is used for mapping values to colors with the use of a gradient.

        colors: `[(position, color), ...]` position from 0 to 1, color: hex string or float or tuple
        #### Path
        - Utilities > Color > Color Ramp Node
        #### Outputs:
        - `#0 color: Color = (0.0, 0.0, 0.0, 0.0)`
        - `#1 alpha: Float = 0.0`

        ![](https://docs.blender.org/manual/en/latest/_images/compositing_node-types_CompositorNodeValToRGB.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/color/color_ramp.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeValToRGB.html)
        """
        from .colors import color_tuple
        node = new_node(*nodes.ShaderNodeValToRGB(None, self))
        bnode: bpy.types.ShaderNodeValToRGB = node.bnode
        color_ramp = bnode.color_ramp
        if interpolation is not None:
            color_ramp.interpolation = interpolation
        if len(colors) > 0 and isinstance(colors[0], list):
            colors = colors[0]
        count = len(colors)
        for _ in range(count - 2):
            color_ramp.elements.new(0)
        for i, (position, color) in enumerate(colors):
            element = color_ramp.elements[i]
            element.position = position
            element.color = color_tuple(color)
        return node.outputs[0].Color

    def to_normal(self, invert=False, strength=1.0, distance=1.0, normal=(0.0, 0.0, 0.0)):
        """The Bump node generates a perturbed normal from a height texture, for bump mapping. The height value will be sampled at the shading point and two nearby points on the surface to determine the local direction of the normal.
        #### Path
        - Vector > Bump Node
        #### Outputs:
        - `#0 normal: Vector = (0.0, 0.0, 0.0)`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeBump.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/render/shader_nodes/vector/bump.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeBump.html)
        """
        node = new_node(*nodes.ShaderNodeBump(invert, strength, distance, self, normal))
        return node.outputs[0].Vector

    def to_string(self, decimals=0):
        """The Value to String node generates string representation of the input value.
        #### Path
        - Utilities > Text > Value to String Node
        #### Outputs:
        - `#0 string: String = ""`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_FunctionNodeValueToString.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/text/value_to_string.html) [[API]](https://docs.blender.org/api/current/bpy.types.FunctionNodeValueToString.html)
        """
        node = new_node(*nodes.FunctionNodeValueToString(self, decimals))
        return node.outputs[0].String

    def clamp(self, clamp_type='MINMAX', min=0.0, max=1.0):
        """The Clamp node clamps a value between a minimum and a maximum.
        #### Path
        - Utilities > Math > Clamp Node
        #### Properties:
        - `clamp_type`: `MINMAX`, `RANGE`
        #### Outputs:
        - `#0 result: Float = 0.0`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeClamp.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/clamp.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeClamp.html)
        """
        node = new_node(*nodes.ShaderNodeClamp(clamp_type, self, min, max))
        return node.outputs[0].Float

    def float_curve(self, factor=1.0, points: list[tuple[float, float, str]] = None):
        """The Float Curve node maps an input float to a curve and outputs a float value.
        - `points`: `[(posx, posy, 'handle_type'), ...]`
        - `handle_type`[Optional]: `AUTO`, `AUTO_CLAMPED`, `VECTOR`
        - Example:

        ```
        value.float_curve(points=[(0, 0), (0.05, 0.03), (0.5, 0.5, "AUTO_CLAMPED"), (1, 0.5)]
        ```
        #### Path
        - Utilities > Math > Float Curve
        #### Outputs:
        - `#0 value: Float = 0.0`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeFloatCurve.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/float_curve.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeFloatCurve.html)
        """
        node = new_node(*nodes.ShaderNodeFloatCurve(None, factor, self))
        bnode: bpy.types.ShaderNodeFloatCurve = node.bnode
        curve = bnode.mapping.curves[0]
        if points is not None:
            if len(points) > 2:
                for _ in range(len(points) - 2):
                    curve.points.new(0, 0)
            for i, point in enumerate(points):
                curve.points[i].location = point[:2]
                if len(point) > 2:
                    curve.points[i].handle_type = point[2].upper()
        return node.outputs[0].Float

    @classmethod
    def curve(cls, value=1.0, factor=1.0, points: list[tuple[float, float]] = None):
        """The Float Curve node maps an input float to a curve and outputs a float value.
        #### Path
        - Utilities > Math > Float Curve
        #### Outputs:
        - `#0 value: Float = 0.0`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeFloatCurve.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/float_curve.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeFloatCurve.html)
        """
        return cls.float_curve(value, factor, points)

    def to_integer(self, rounding_mode='ROUND'):
        """The Float To Integer node takes a single floating point number input and converts it to an integer with a choice of methods.
        #### Path
        - Utilities > Math > Float To Integer Node
        #### Properties:
        - `rounding_mode`: `ROUND`, `FLOOR`, `CEILING`, `TRUNCATE`
        #### Outputs:
        - `#0 integer: Integer = 0`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_FunctionNodeFloatToInt.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/float_to_integer.html) [[API]](https://docs.blender.org/api/current/bpy.types.FunctionNodeFloatToInt.html)
        """
        node = new_node(*nodes.FunctionNodeFloatToInt(rounding_mode, self))
        return node.outputs[0].Integer

    def map_range(self, from_min=0.0, from_max=1.0, to_min=0.0, to_max=1.0, interpolation_type="LINEAR", steps=4.0, clamp=True):
        """The Map Range node remaps a value from a range to a target range.
        #### Path
        - Utilities > Math > Map Range Node
        #### Properties:
        - `interpolation_type`: `LINEAR`, `STEPPED`, `SMOOTHSTEP`, `SMOOTHERSTEP`
        #### Outputs:
        - `#0 result: Float = 0.0`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeMapRange.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/map_range.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeMapRange.html)
        """
        node = new_node(*nodes.ShaderNodeMapRange("FLOAT", interpolation_type, clamp, self, from_min, from_max, to_min, to_max, steps))
        return node.outputs[0].Float

    def math(self, operation='ADD', value_001=0.5, value_002=0.5, use_clamp=False):
        """The Math Node performs math operations.
        #### Path
        - Utilities > Math > Math Node
        #### Properties:
        - `operation`: `ADD`, `SUBTRACT`, `MULTIPLY`, `DIVIDE`, `MULTIPLY_ADD`, `POWER`, `LOGARITHM`, `SQRT`, `INVERSE_SQRT`, `ABSOLUTE`, `EXPONENT`, `MINIMUM`, `MAXIMUM`, `LESS_THAN`, `GREATER_THAN`, `SIGN`, `COMPARE`, `SMOOTH_MIN`, `SMOOTH_MAX`, `ROUND`, `FLOOR`, `CEIL`, `TRUNC`, `FRACT`, `MODULO`, `WRAP`, `SNAP`, `PINGPONG`, `SINE`, `COSINE`, `TANGENT`, `ARCSINE`, `ARCCOSINE`, `ARCTANGENT`, `ARCTAN2`, `SINH`, `COSH`, `TANH`, `RADIANS`, `DEGREES`
        #### Outputs:
        - `#0 value: Float = 0.0`

        ![](https://docs.blender.org/manual/en/latest/_images/compositing_node-types_CompositorNodeMath.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/math.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
        """
        node = new_node(*nodes.ShaderNodeMath(operation, use_clamp, self, value_001, value_002))
        return node.outputs[0].Float

    def __neg__(self):
        return FloatMath("MULTIPLY", False, self, -1)

    def __add__(self, other):
        return FloatMath("ADD", False, self, other)

    def __radd__(self, other):
        return FloatMath("ADD", False, other, self)

    def __sub__(self, other):
        return FloatMath("SUBTRACT", False, self, other)

    def __rsub__(self, other):
        return FloatMath("SUBTRACT", False, other, self)

    def __mul__(self, other):
        return FloatMath("MULTIPLY", False, self, other)

    def __rmul__(self, other):
        return FloatMath("MULTIPLY", False, other, self)

    def __truediv__(self, other):
        return FloatMath("DIVIDE", False, self, other)

    def __rtruediv__(self, other):
        return FloatMath("DIVIDE", False, other, self)

    def __floordiv__(self, other):
        return math.floor(self / other)

    def __eq__(self, other):
        return Compare("FLOAT", operation="EQUAL", a=self, b=other)

    def __ne__(self, other):
        return Compare("FLOAT", operation="NOT_EQUAL", a=self, b=other)

    def __ge__(self, other):
        return Compare("FLOAT", operation="GREATER_EQUAL", a=self, b=other)

    def __gt__(self, other):
        return Compare("FLOAT", operation="GREATER_THAN", a=self, b=other)

    def __le__(self, other):
        return Compare("FLOAT", operation="LESS_EQUAL", a=self, b=other)

    def __lt__(self, other):
        return Compare("FLOAT", operation="LESS_THAN", a=self, b=other)

    def multiply_add(self, multiplier=0.5, addend=0.5, clamp=False):
        """The sum of the product of the two values with Addend.
        #### Path
        - Utilities > Math > Math Node
        """
        return self.math("MULTIPLY_ADD", multiplier, addend, clamp)

    def power(self, exponent=0.5, clamp=False):
        """The Base raised to the power of Exponent.
        #### Path
        - Utilities > Math > Math Node
        """
        return self.math("POWER", exponent, use_clamp=clamp)

    def __pow__(self, exponent):
        return self.power(exponent)

    def log(self, base=0.5, clamp=False):
        """The log of the value with a Base as its base.
        #### Path
        - Utilities > Math > Math Node
        """
        return self.math("LOGARITHM", base, use_clamp=clamp)

    @property
    def log2(self):
        """The log of the value with a Base on 2.
        #### Path
        - Utilities > Math > Math Node
        """
        return self.log(2)

    @property
    def ln(self):
        """The Natural logarithm.
        #### Path
        - Utilities > Math > Math Node
        """
        return self.log(math.e)

    @property
    def square_root(self):
        """The square root of the value.
        #### Path
        - Utilities > Math > Math Node
        """
        return self.math("SQRT")

    @property
    def inverse_sqrt(self):
        """One divided by the square root of the value.
        #### Path
        - Utilities > Math > Math Node
        """
        return self.math("INVERSE_SQRT")

    @classmethod
    def sqrt(cls, value=0.5, clamp=False):
        """The square root of the value.
        #### Path
        - Utilities > Math > Math Node
        """
        return cls.math(value, "SQRT", use_clamp=clamp)

    @property
    def absolute(self):
        """Equivalent to built-in function `abs(self)`. The input value is read without regard to its sign. This turns negative values into positive values.
        #### Path
        - Utilities > Math > Math Node
        """
        return self.math("ABSOLUTE")

    def __abs__(self):
        return self.absolute

    @property
    def exponent(self):
        """Raises [Euler's number](https://en.wikipedia.org/wiki/E_(mathematical_constant)) to the power of the value.
        #### Path
        - Utilities > Math > Math Node
        """
        return self.math("EXPONENT")

    def minimum(self, other=0.5, clamp=False):
        """Outputs the smallest of the input values.
        #### Path
        - Utilities > Math > Math Node
        """
        return self.math("MINIMUM", other, use_clamp=clamp)

    def maximum(self, other=0.5, clamp=False):
        """Outputs the largest of two input values.
        #### Path
        - Utilities > Math > Math Node
        """
        return self.math("MAXIMUM", other, use_clamp=clamp)

    def less_than(self, threshold=0.5, clamp=False):
        """Outputs 1.0 if the first value is smaller than the second value. Otherwise the output is 0.0.
        #### Path
        - Utilities > Math > Math Node
        """
        return self.math("LESS_THAN", threshold, use_clamp=clamp)

    def greater_than(self, threshold=0.5, clamp=False):
        """Outputs 1.0 if the first value is larger than the second value. Otherwise the output is 0.0.
        #### Path
        - Utilities > Math > Math Node
        """
        return self.math("GREATER_THAN", threshold, use_clamp=clamp)

    @property
    def sign(self):
        """Extracts the sign of the input value. All positive numbers will output 1.0. All negative numbers will output -1.0. And 0.0 will output 0.0.
        #### Path
        - Utilities > Math > Math Node
        """
        return self.math("SIGN")

    def compare(self, other=0.5, epsilon=0.5, clamp=False):
        """Outputs 1.0 if the difference between the two input values is less than or equal to Epsilon.
        #### Path
        - Utilities > Math > Math Node
        """
        return self.math("COMPARE", other, epsilon, use_clamp=clamp)

    def smooth_minimum(self, other=0.5, distance=0.5, clamp=False):
        """[Smooth Minimum](https://en.wikipedia.org/wiki/Smooth_maximum).
        #### Path
        - Utilities > Math > Math Node
        """
        return self.math("SMOOTH_MIN", other, distance, use_clamp=clamp)

    def smooth_maximum(self, other=0.5, distance=0.5, clamp=False):
        """[Smooth Maximum](https://en.wikipedia.org/wiki/Smooth_maximum).
        #### Path
        - Utilities > Math > Math Node
        """
        return self.math("SMOOTH_MAX", other, distance, use_clamp=clamp)

    @property
    def round(self):
        """Rounds the input value to the nearest integer.
        #### Path
        - Utilities > Math > Math Node
        """
        return self.math("ROUND")

    def __round__(self):
        """To get called by built-in round() function."""
        return self.round

    @property
    def floor(self):
        """Rounds the input value down to the nearest integer.
        #### Path
        - Utilities > Math > Math Node
        """
        return self.math("FLOOR")

    def __floor__(self):
        """To get called by built-in math.floor() function."""
        return self.floor

    @property
    def ceil(self):
        """Rounds the input value up to the nearest integer.
        #### Path
        - Utilities > Math > Math Node
        """
        return self.math("CEIL")

    def __ceil__(self):
        """To get called by built-in math.ceil() function."""
        return self.ceil

    @property
    def trunc(self):
        """Outputs the integer part of the value.
        #### Path
        - Utilities > Math > Math Node
        """
        return self.math("TRUNC")

    def __trunc__(self):
        """To get called by built-in math.trunc() function."""
        return self.trunc

    @property
    def fract(self):
        """Returns the fractional part of the value.
        #### Path
        - Utilities > Math > Math Node
        """
        return self.math("FRACT")

    def modulo(self, other=0.5, clamp=False):
        """Outputs the remainder once the first value is divided by the second value.
        #### Path
        - Utilities > Math > Math Node
        """
        return self.math("MODULO", other, use_clamp=clamp)

    def __mod__(self, other):
        """To get called on modulo operation using % operator."""
        return self.modulo(other)

    def wrap(self, max=0.5, min=0.5, clamp=False):
        """Outputs a value between Min and Max based on the absolute difference between the input value and the nearest integer multiple of Max less than the value.
        #### Path
        - Utilities > Math > Math Node
        """
        return self.math("WRAP", max, min, use_clamp=clamp)

    def snap(self, increment=0.5, clamp=False):
        """Rounds the input value down to the nearest integer multiple of Increment.
        #### Path
        - Utilities > Math > Math Node
        """
        return self.math("SNAP", increment, use_clamp=clamp)

    def pingpong(self, scale=0.5, clamp=False):
        """The output value is moved between 0.0 and the Scale based on the input value.
        #### Path
        - Utilities > Math > Math Node
        """
        return self.math("PINGPONG", scale, use_clamp=clamp)

    @property
    def sine(self):
        """The [Sine](https://en.wikipedia.org/wiki/Sine) of the input value.
        #### Path
        - Utilities > Math > Math Node
        """
        return self.math("SINE")

    @classmethod
    def sin(cls, value=0.5, clamp=False):
        """The [Sine](https://en.wikipedia.org/wiki/Sine) of the input value.
        #### Path
        - Utilities > Math > Math Node
        """
        return cls.math(value, "SINE", use_clamp=clamp)

    @property
    def cosine(self):
        """The [Sine](https://en.wikipedia.org/wiki/Sine) of the input value.
        #### Path
        - Utilities > Math > Math Node
        """
        return self.math("SINE")

    @classmethod
    def cos(cls, value=0.5, clamp=False):
        """The [Cosine](https://en.wikipedia.org/wiki/Cosine) of the input value.
        #### Path
        - Utilities > Math > Math Node
        """
        return cls.math(value, "COSINE", use_clamp=clamp)

    @property
    def tangent(self):
        """The [Tangent](https://en.wikipedia.org/wiki/Tangent) of the input value.
        #### Path
        - Utilities > Math > Math Node
        """
        return self.math("TANGENT")

    @classmethod
    def tan(cls, value=0.5, clamp=False):
        """The [Tangent](https://en.wikipedia.org/wiki/Tangent) of the input value.
        #### Path
        - Utilities > Math > Math Node
        """
        return cls.math(value, "TANGENT", use_clamp=clamp)

    @property
    def arcsine(self):
        """The [ArcSine](https://en.wikipedia.org/wiki/Inverse_trigonometric_functions) of the input value.
        #### Path
        - Utilities > Math > Math Node
        """
        return self.math("SINE")

    @classmethod
    def arcsin(cls, value=0.5, clamp=False):
        """The [ArcSine](https://en.wikipedia.org/wiki/Inverse_trigonometric_functions) of the input value.
        #### Path
        - Utilities > Math > Math Node
        """
        return cls.math(value, "ARCSINE", use_clamp=clamp)

    @property
    def arccosine(self):
        """The [ArcCosine](https://en.wikipedia.org/wiki/Inverse_trigonometric_functions) of the input value.
        #### Path
        - Utilities > Math > Math Node
        """
        return self.math("ARCCOSINE")

    @classmethod
    def arccos(cls, value=0.5, clamp=False):
        """The [ArcCosine](https://en.wikipedia.org/wiki/Inverse_trigonometric_functions) of the input value.
        #### Path
        - Utilities > Math > Math Node
        """
        return cls.math(value, "ARCCOSINE", use_clamp=clamp)

    @property
    def arctangent(self):
        """The [ArcTangent](https://en.wikipedia.org/wiki/Inverse_trigonometric_functions) of the input value.
        #### Path
        - Utilities > Math > Math Node
        """
        return self.math("ARCTANGENT")

    @classmethod
    def arctan(cls, value=0.5, clamp=False):
        """The [ArcTangent](https://en.wikipedia.org/wiki/Inverse_trigonometric_functions) of the input value.
        #### Path
        - Utilities > Math > Math Node
        """
        return cls.math(value, "ARCTANGENT", use_clamp=clamp)

    def arctan2(self, other=0.5, clamp=False):
        """Outputs the Inverse Tangent of the first value divided by the second value measured in radians.
        #### Path
        - Utilities > Math > Math Node
        """
        return self.math("ARCTAN2", other, use_clamp=clamp)

    @property
    def hyperbolic_sine(self):
        """The [Hyperbolic Sine](https://en.wikipedia.org/wiki/Hyperbolic_functions) of the input value.
        #### Path
        - Utilities > Math > Math Node
        """
        return self.math("SINH")

    @classmethod
    def sinh(cls, value=0.5, clamp=False):
        """The [Hyperbolic Sine](https://en.wikipedia.org/wiki/Inverse_trigonometric_functions) of the input value.
        #### Path
        - Utilities > Math > Math Node
        """
        return cls.math(value, "SINH", use_clamp=clamp)

    @property
    def hyperbolic_cosine(self):
        """The [Hyperbolic Cosine](https://en.wikipedia.org/wiki/Hyperbolic_functions) of the input value.
        #### Path
        - Utilities > Math > Math Node
        """
        return self.math("COSH")

    @classmethod
    def cosh(cls, value=0.5, clamp=False):
        """The [Hyperbolic Cosine](https://en.wikipedia.org/wiki/Inverse_trigonometric_functions) of the input value.
        #### Path
        - Utilities > Math > Math Node
        """
        return cls.math(value, "COSH", use_clamp=clamp)

    @property
    def hyperbolic_tangent(self):
        """The [Hyperbolic Tangent](https://en.wikipedia.org/wiki/Hyperbolic_functions) of the input value.
        #### Path
        - Utilities > Math > Math Node
        """
        return self.math("TANH")

    @classmethod
    def tanh(cls, value=0.5, clamp=False):
        """The [Hyperbolic Tangent](https://en.wikipedia.org/wiki/Inverse_trigonometric_functions) of the input value.
        #### Path
        - Utilities > Math > Math Node
        """
        return cls.math(value, "TANH", use_clamp=clamp)

    @property
    def radians(self):
        """Converts the input from degrees to radians.
        #### Path
        - Utilities > Math > Math Node
        """
        return self.math("RADIANS")

    @property
    def degrees(self):
        """Converts the input from radians to degrees.
        #### Path
        - Utilities > Math > Math Node
        """
        return self.math("DEGREES")

    def to_euler(self, axis=(0.0, 0.0, 1.0), space='OBJECT'):
        """Use separate axis and angle inputs to control the rotation.
        - `space`: `OBJECT`, `LOCAL`
        #### Path
        - Utilities > Rotation > Rotate Euler Node
        #### Outputs:
        - `#0 rotation: Vector = (0.0, 0.0, 0.0)`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_FunctionNodeRotateEuler.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/rotation/rotate_euler.html) [[API]](https://docs.blender.org/api/current/bpy.types.FunctionNodeRotateEuler.html)
        """
        node = new_node(*nodes.FunctionNodeRotateEuler(space, "AXIS_ANGLE", axis=axis, angle=self))
        return node.outputs[0].Vector


class Angle(Float):
    """Floating-point number socket of a node, float in [-inf, inf], default 0.0"""
    bl_idname = "NodeSocketFloatAngle"


class Distance(Float):
    """Floating-point number socket of a node, float in [-inf, inf], default 0.0"""
    bl_idname = "NodeSocketFloatDistance"


class Factor(Float):
    """Floating-point number socket of a node, float in [0, 1], default 0.0"""
    bl_idname = "NodeSocketFloatFactor"


class Percentage(Float):
    """Floating-point number socket of a node, float in [-inf, inf], default 0.0"""
    bl_idname = "NodeSocketFloatPercentage"


class FloatTime(Float):
    """Floating-point number socket of a node, float in [-inf, inf], default 0.0"""
    bl_idname = "NodeSocketFloatTime"


class FloatTimeAbsolute(Float):
    """Floating-point number socket of a node, float in [-inf, inf], default 0.0"""
    bl_idname = "NodeSocketFloatTimeAbsolute"


class Unsigned(Float):
    """Floating-point number socket of a node, float in [0, inf], default 0.0"""
    bl_idname = "NodeSocketFloatUnsigned"


class Vector(Socket):
    """3D vector socket of a node, float array of 3 items in [-inf, inf], default (0.0, 0.0, 0.0)"""
    bl_idname = "NodeSocketVector"

    def __init__(self, bsocket: bpy.types.NodeSocket) -> None:
        super().__init__(bsocket)
        self._seperated = None
        self._length = None

    @property
    def x(self):
        if self._seperated is None:
            self._seperated = self.separate_xyz()
        return self._seperated.x

    @x.setter
    def x(self, value):
        socket = CombineXYZ(value, self.y, self.z)
        self.bsocket = socket.bsocket

    @property
    def y(self):
        if self._seperated is None:
            self._seperated = self.separate_xyz()
        return self._seperated.y

    @y.setter
    def y(self, value):
        socket = CombineXYZ(self.x, value, self.z)
        self.bsocket = socket.bsocket

    @property
    def z(self):
        if self._seperated is None:
            self._seperated = self.separate_xyz()
        return self._seperated.z

    @z.setter
    def z(self, value):
        socket = CombineXYZ(self.x, self.y, value)
        self.bsocket = socket.bsocket

    def line_to(self, end=(0.0, 0.0, 1.0)):
        """The Curve Line node generates poly spline line.
        #### Path
        - Curve > Primitives > Curve Line Node
        #### Outputs:
        - `#0 curve: Geometry = None`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeCurvePrimitiveLine.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/primitives/curve_line.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurvePrimitiveLine.html)
        """
        node = new_node(*nodes.GeometryNodeCurvePrimitiveLine("POINTS", self, end))
        return node.outputs[0].Curve

    def line_towards(self, direction=(0.0, 0.0, 1.0), length=1.0):
        """The Curve Line node generates poly spline line.
        #### Path
        - Curve > Primitives > Curve Line Node
        #### Outputs:
        - `#0 curve: Geometry = None`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeCurvePrimitiveLine.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/curve/primitives/curve_line.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeCurvePrimitiveLine.html)
        """
        node = new_node(*nodes.GeometryNodeCurvePrimitiveLine("DIRECTION", self, direction=direction, length=length))
        return node.outputs[0].Curve

    def switch(self, switch=False, true_vector=(0.0, 0.0, 0.0)):
        """The Switch node outputs one of two inputs depending on a condition. Only the input that is passed through the node is computed.
        #### Path
        - Utilities > Switch Node
        #### Outputs:
        - `#3 output: Vector = (0.0, 0.0, 0.0)`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeSwitch.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/switch.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeSwitch.html)
        """
        node = new_node(*nodes.GeometryNodeSwitch("VECTOR", switch, false_003=self, true_003=true_vector))
        return node.outputs[3].Vector

    def mix(self, b_vector=(0.0, 0.0, 0.0), factor_float=0.5, factor_vector=(0.5, 0.5, 0.5), factor_mode="UNIFORM", clamp_factor=True):
        """The Mix Node mixes values, colors and vectors inputs using a factor to control the amount of interpolation. The Color mode has additional blending modes.
        #### Path
        - Utilities > Vector > Mix Node
        #### Outputs:
        - `#1 result_vector: Vector = (0.0, 0.0, 0.0)`

        ![](https://docs.blender.org/manual/en/latest/_images/render_shader-nodes_shader_mix_node.jpg)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/color/mix_rgb.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html)
        """
        node = new_node(*nodes.ShaderNodeMix(data_type="VECTOR", factor_mode=factor_mode, clamp_factor=clamp_factor, factor_float=factor_float, factor_vector=factor_vector, a_vector=self, b_vector=b_vector))
        return node.outputs[1].Vector

    def separate_xyz(self):
        """The Separate XYZ Node splits a vector into its individual components.
        #### Path
        - Utilities > Vector > Separate XYZ Node
        #### Outputs:
        - `#0 x: Float = 0.0`
        - `#1 y: Float = 0.0`
        - `#2 z: Float = 0.0`

        ![](https://docs.blender.org/manual/en/latest/_images/compositing_node-types_CompositorNodeSeparateXYZ.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/separate_xyz.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeSeparateXYZ.html)
        """
        node = new_node(*nodes.ShaderNodeSeparateXYZ(self))
        ret = typing.NamedTuple("ShaderNodeSeparateXYZ", [("x", Float), ("y", Float), ("z", Float)])
        return ret(node.outputs[0].Float, node.outputs[1].Float, node.outputs[2].Float)

    def vector_curve(self, mapping: bpy.types.CurveMapping = None, fac=1.0):
        """The Vector Curves node maps an input vector components to a curve.
        #### Path
        - Utilities > Vector > Vector Curves Node
        #### Outputs:
        - `#0 vector: Vector = (0.0, 0.0, 0.0)`

        ![](https://docs.blender.org/manual/en/latest/_images/compositing_node-types_CompositorNodeCurveVec.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_curves.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorCurve.html)
        """
        node = new_node(*nodes.ShaderNodeVectorCurve(mapping, fac, self))
        return node.outputs[0].Vector

    def rotate(self, rotation_type='AXIS_ANGLE', invert=False, center=(0.0, 0.0, 0.0), axis=(0.0, 0.0, 1.0), angle=math.radians(0.0), rotation=(0.0, 0.0, 0.0)):
        """The Vector Rotate Node provides the ability to rotate a vector around a pivot point (Center).
        #### Path
        - Utilities > Vector > Vector Rotate Node
        #### Properties:
        - `rotation_type`: `AXIS_ANGLE`, `X_AXIS`, `Y_AXIS`, `Z_AXIS`, `EULER_XYZ`
        #### Outputs:
        - `#0 vector: Vector = (0.0, 0.0, 0.0)`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeVectorRotate.png)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_rotate.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorRotate.html)
        """
        node = new_node(*nodes.ShaderNodeVectorRotate(rotation_type, invert, self, center, axis, angle, rotation))
        return node.outputs[0].Vector

    def rotate_around_axis(self, center=(0.0, 0.0, 0.0), axis=(0.0, 0.0, 1.0), angle=math.radians(0.0), invert=False):
        """The Vector Rotate Node provides the ability to rotate a vector around a pivot point (Center).
        #### Path
        - Utilities > Vector > Vector Rotate Node
        #### Outputs:
        - `#0 vector: Vector = (0.0, 0.0, 0.0)`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeVectorRotate.png)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_rotate.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorRotate.html)
        """
        node = new_node(*nodes.ShaderNodeVectorRotate("AXIS_ANGLE", invert, self, center, axis, angle))
        return node.outputs[0].Vector

    def rotate_around_x_axis(self, center=(0.0, 0.0, 0.0), angle=math.radians(0.0), invert=False):
        """The Vector Rotate Node provides the ability to rotate a vector around a pivot point (Center).
        #### Path
        - Utilities > Vector > Vector Rotate Node
        #### Outputs:
        - `#0 vector: Vector = (0.0, 0.0, 0.0)`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeVectorRotate.png)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_rotate.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorRotate.html)
        """
        node = new_node(*nodes.ShaderNodeVectorRotate("X_AXIS", invert, self, center, angle=angle))
        return node.outputs[0].Vector

    def rotate_around_y_axis(self, center=(0.0, 0.0, 0.0), angle=math.radians(0.0), invert=False):
        """The Vector Rotate Node provides the ability to rotate a vector around a pivot point (Center).
        #### Path
        - Utilities > Vector > Vector Rotate Node
        #### Outputs:
        - `#0 vector: Vector = (0.0, 0.0, 0.0)`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeVectorRotate.png)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_rotate.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorRotate.html)
        """
        node = new_node(*nodes.ShaderNodeVectorRotate("Y_AXIS", invert, self, center, angle=angle))
        return node.outputs[0].Vector

    def rotate_around_z_axis(self, center=(0.0, 0.0, 0.0), angle=math.radians(0.0), invert=False):
        """The Vector Rotate Node provides the ability to rotate a vector around a pivot point (Center).
        #### Path
        - Utilities > Vector > Vector Rotate Node
        #### Outputs:
        - `#0 vector: Vector = (0.0, 0.0, 0.0)`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeVectorRotate.png)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_rotate.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorRotate.html)
        """
        node = new_node(*nodes.ShaderNodeVectorRotate("Z_AXIS", invert, self, center, angle=angle))
        return node.outputs[0].Vector

    def rotate_around_euler_xyz(self, center=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), invert=False):
        """The Vector Rotate Node provides the ability to rotate a vector around a pivot point (Center).
        #### Path
        - Utilities > Vector > Vector Rotate Node
        #### Outputs:
        - `#0 vector: Vector = (0.0, 0.0, 0.0)`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeVectorRotate.png)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_rotate.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorRotate.html)
        """
        node = new_node(*nodes.ShaderNodeVectorRotate("EULER_XYZ", invert, self, center, rotation=rotation))
        return node.outputs[0].Vector

    def rotate_object_euler(self, rotate_by=(0.0, 0.0, 0.0)):
        """The Rotate Euler node rotates an Euler rotation.
        #### Path
        - Utilities > Rotation > Rotate Euler Node
        #### Outputs:
        - `#0 rotation: Vector = (0.0, 0.0, 0.0)`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_FunctionNodeRotateEuler.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/rotation/rotate_euler.html) [[API]](https://docs.blender.org/api/current/bpy.types.FunctionNodeRotateEuler.html)
        """
        node = new_node(*nodes.FunctionNodeRotateEuler("OBJECT", "EULER", self, rotate_by))
        return node.outputs[0].Vector

    def rotate_local_euler(self, rotate_by=(0.0, 0.0, 0.0)):
        """The Rotate Euler node rotates an Euler rotation.
        #### Path
        - Utilities > Rotation > Rotate Euler Node
        #### Outputs:
        - `#0 rotation: Vector = (0.0, 0.0, 0.0)`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_FunctionNodeRotateEuler.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/rotation/rotate_euler.html) [[API]](https://docs.blender.org/api/current/bpy.types.FunctionNodeRotateEuler.html)
        """
        node = new_node(*nodes.FunctionNodeRotateEuler("LOCAL", "EULER", self, rotate_by))
        return node.outputs[0].Vector

    def rotate_object_around_axis_by_angle(self, axis=(0.0, 0.0, 1.0), angle=math.radians(0.0)):
        """Use separate axis and angle inputs to control the rotation.
        #### Path
        - Utilities > Rotation > Rotate Euler Node
        #### Outputs:
        - `#0 rotation: Vector = (0.0, 0.0, 0.0)`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_FunctionNodeRotateEuler.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/rotation/rotate_euler.html) [[API]](https://docs.blender.org/api/current/bpy.types.FunctionNodeRotateEuler.html)
        """
        node = new_node(*nodes.FunctionNodeRotateEuler("OBJECT", "AXIS_ANGLE", self, axis=axis, angle=angle))
        return node.outputs[0].Vector

    def rotate_local_around_axis_by_angle(self, axis=(0.0, 0.0, 1.0), angle=math.radians(0.0)):
        """Use separate axis and angle inputs to control the rotation.
        #### Path
        - Utilities > Rotation > Rotate Euler Node
        #### Outputs:
        - `#0 rotation: Vector = (0.0, 0.0, 0.0)`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_FunctionNodeRotateEuler.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/rotation/rotate_euler.html) [[API]](https://docs.blender.org/api/current/bpy.types.FunctionNodeRotateEuler.html)
        """
        node = new_node(*nodes.FunctionNodeRotateEuler("LOCAL", "AXIS_ANGLE", self, axis=axis, angle=angle))
        return node.outputs[0].Vector

    def math(self, operation='ADD', vector_001=(0.0, 0.0, 0.0), vector_002=(0.0, 0.0, 0.0), scale=1.0):
        """The Vector Math node performs the selected math operation on the input vectors.
        #### Path
        - Utilities > Vector > Vector Math Node
        #### Properties:
        - `operation`: `ADD`, `SUBTRACT`, `MULTIPLY`, `DIVIDE`, `MULTIPLY_ADD`, `CROSS_PRODUCT`, `PROJECT`, `REFLECT`, `REFRACT`, `FACEFORWARD`, `DOT_PRODUCT`, `DISTANCE`, `LENGTH`, `SCALE`, `NORMALIZE`, `ABSOLUTE`, `MINIMUM`, `MAXIMUM`, `FLOOR`, `CEIL`, `FRACTION`, `MODULO`, `WRAP`, `SNAP`, `SINE`, `COSINE`, `TANGENT`
        #### Outputs:
        - `#0 vector: Vector = (0.0, 0.0, 0.0)`
        - `#1 value: Float = 0.0`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeVectorMath.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_math.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)
        """
        node = new_node(*nodes.ShaderNodeVectorMath(operation, self, vector_001, vector_002, scale))
        ret = typing.NamedTuple("ShaderNodeVectorMath", [("vector", Vector), ("value", Float)])
        return ret(node.outputs[0].Vector, node.outputs[1].Float)

    def __add__(self, other):
        """The sum of A and B."""
        return VectorMath("ADD", self, other).vector

    def __radd__(self, other):
        return VectorMath("ADD", other, self).vector

    def __sub__(self, other):
        """The difference between A and B."""
        return VectorMath("SUBTRACT", self, other).vector

    def __rsub__(self, other):
        return VectorMath("SUBTRACT", other, self).vector

    def __neg__(self):
        return VectorMath("SCALE", self, scale=-1).vector

    def __mul__(self, other):
        """1.The result of multiplying A by the scalar input Scale; 2.The entrywise product of A and B."""
        if isinstance(other, (float, int, Float, Integer)):
            return VectorMath("SCALE", self, scale=other).vector
        else:
            return VectorMath("MULTIPLY", self, other).vector

    def __truediv__(self, other):
        """1.The result of multiplying A by the 1/scalar input Scale; 2.The entrywise division of A by B. Division by zero results in zero."""
        if isinstance(other, (float, int, Float, Integer)):
            return VectorMath("SCALE", self, scale=1 / other).vector
        else:
            return VectorMath("DIVIDE", self, other).vector

    def multiply_add(self, multiplier=(0.0, 0.0, 0.0), addend=(0.0, 0.0, 0.0)):
        """The entrywise combination of the multiply and addition operations.
        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_math.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)
        #### Path
        - Utilities > Vector > Vector Math Node
        #### Outputs:
        - `#0 vector: Vector = (0.0, 0.0, 0.0)`
        """
        return self.math("MULTIPLY_ADD", multiplier, addend).vector

    def cross(self, other=(0.0, 0.0, 0.0)):
        """The cross product of A and B.
        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_math.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)
        #### Path
        - Utilities > Vector > Vector Math Node
        #### Outputs:
        - `#0 vector: Vector = (0.0, 0.0, 0.0)`
        """
        return self.math("CROSS_PRODUCT", other).vector

    def project(self, other=(0.0, 0.0, 0.0)):
        """The projection of A onto B.
        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_math.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)
        #### Path
        - Utilities > Vector > Vector Math Node
        #### Outputs:
        - `#0 vector: Vector = (0.0, 0.0, 0.0)`
        """
        return self.math("PROJECT", other).vector

    def reflect(self, other=(0.0, 0.0, 0.0)):
        """The reflection of A around the normal B. B need not be normalized.
        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_math.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)
        #### Path
        - Utilities > Vector > Vector Math Node
        #### Outputs:
        - `#0 vector: Vector = (0.0, 0.0, 0.0)`
        """
        return self.math("REFLECT", other).vector

    def refract(self, normal=(0.0, 0.0, 0.0), IOR=1.0):
        """For a given incident vector A, surface normal B and ratio of indices of refraction (IOR), refract outputs the refraction vector R.
        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_math.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)
        #### Path
        - Utilities > Vector > Vector Math Node
        #### Outputs:
        - `#0 vector: Vector = (0.0, 0.0, 0.0)`
        """
        return self.math("REFRACT", normal, scale=IOR).vector

    def faceforward(self, b=(0.0, 0.0, 0.0), c=(0.0, 0.0, 0.0)):
        """Orients a vector A to point away from a surface B as defined by its normal C. `(dot(B, C) < 0) ? A : -A`
        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_math.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)
        #### Path
        - Utilities > Vector > Vector Math Node
        #### Outputs:
        - `#0 vector: Vector = (0.0, 0.0, 0.0)`
        """
        return self.math("FACEFORWARD", b, c).vector

    def dot(self, other=(0.0, 0.0, 0.0)):
        """The dot product of A and B. `A_x · B_x + A_y · B_y + A_z · B_z`
        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_math.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)
        #### Path
        - Utilities > Vector > Vector Math Node
        #### Outputs:
        - `#1 value: Float = 0.0`
        """
        return self.math("DOT_PRODUCT", other).value

    def distance(self, other=(0.0, 0.0, 0.0)):
        """The distance between A and B.
        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_math.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)
        #### Path
        - Utilities > Vector > Vector Math Node
        #### Outputs:
        - `#1 value: Float = 0.0`
        """
        return self.math("DISTANCE", other).value

    @property
    def length(self):
        """The length of A. 
        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_math.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)
        #### Path
        - Utilities > Vector > Vector Math Node
        #### Outputs:
        - `#1 value: Float = 0.0`
        """
        if self._length is None:
            self._length = self.math("LENGTH").value
        return self._length

    def scale(self, scale=1.0):
        """The result of multiplying A by the scalar input Scale.
        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_math.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)
        #### Path
        - Utilities > Vector > Vector Math Node
        #### Outputs:
        - `#0 vector: Vector = (0.0, 0.0, 0.0)`
        """
        return self.math("SCALE", scale=scale).vector

    @property
    def normalize(self):
        """The result of normalizing A. The result vector points to the same direction as A and has a length of 1. If A is (0, 0, 0), the result is (0, 0, 0) as well.
        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_math.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)
        #### Path
        - Utilities > Vector > Vector Math Node
        #### Outputs:
        - `#0 vector: Vector = (0.0, 0.0, 0.0)`
        """
        return self.math("NORMALIZE").vector

    def absolute(self):
        """The entrywise absolute value of A.
        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_math.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)
        #### Path
        - Utilities > Vector > Vector Math Node
        #### Outputs:
        - `#0 vector: Vector = (0.0, 0.0, 0.0)`
        """
        return self.math("ABSOLUTE").vector

    def __abs__(self):
        return self.absolute()

    def minimum(self, other=(0.0, 0.0, 0.0)):
        """The entrywise minimum value from A and B.
        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_math.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)
        #### Path
        - Utilities > Vector > Vector Math Node
        #### Outputs:
        - `#0 vector: Vector = (0.0, 0.0, 0.0)`
        """
        return self.math("MINIMUM", other).vector

    def maximum(self, other=(0.0, 0.0, 0.0)):
        """The entrywise maximum value from A and B.
        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_math.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)
        #### Path
        - Utilities > Vector > Vector Math Node
        #### Outputs:
        - `#0 vector: Vector = (0.0, 0.0, 0.0)`
        """
        return self.math("MAXIMUM", other).vector

    def floor(self):
        """Rounds the input value entrywise down to the nearest integer.
        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_math.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)
        #### Path
        - Utilities > Vector > Vector Math Node
        #### Outputs:
        - `#0 vector: Vector = (0.0, 0.0, 0.0)`
        """
        return self.math("FLOOR").vector

    def __floor__(self):
        return self.floor()

    def ceil(self):
        """Rounds the input value entrywise up to the nearest integer.
        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_math.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)
        #### Path
        - Utilities > Vector > Vector Math Node
        #### Outputs:
        - `#0 vector: Vector = (0.0, 0.0, 0.0)`
        """
        return self.math("CEIL").vector

    def __ceil__(self):
        return self.ceil()

    def fraction(self):
        """Returns the fractional part of the value entrywise.
        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_math.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)
        #### Path
        - Utilities > Vector > Vector Math Node
        #### Outputs:
        - `#0 vector: Vector = (0.0, 0.0, 0.0)`
        """
        return self.math("FRACTION").vector

    def modulo(self, other=(0.0, 0.0, 0.0)):
        """The entrywise modulo of A by B.
        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_math.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)
        #### Path
        - Utilities > Vector > Vector Math Node
        #### Outputs:
        - `#0 vector: Vector = (0.0, 0.0, 0.0)`
        """
        return self.math("MODULO", other).vector

    def __mod__(self, other):
        return self.modulo(other)

    def wrap(self, max=(0.0, 0.0, 0.0), min=(0.0, 0.0, 0.0)):
        """The entrywise output of a value between Min and Max based on the absolute difference between the input value and the nearest integer multiple of Max less than the value.
        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_math.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)
        #### Path
        - Utilities > Vector > Vector Math Node
        #### Outputs:
        - `#0 vector: Vector = (0.0, 0.0, 0.0)`
        """
        return self.math("WRAP", max, min).vector

    def snap(self, increment=(0.0, 0.0, 0.0)):
        """The result of rounding A to the largest integer multiple of B less than or equal A.
        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_math.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)
        #### Path
        - Utilities > Vector > Vector Math Node
        #### Outputs:
        - `#0 vector: Vector = (0.0, 0.0, 0.0)`
        """
        return self.math("SNAP", increment).vector

    def sin(self):
        """The entrywise Sine of A.
        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_math.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)
        #### Path
        - Utilities > Vector > Vector Math Node
        #### Outputs:
        - `#0 vector: Vector = (0.0, 0.0, 0.0)`
        """
        return self.math("SINE").vector

    def cos(self):
        """The entrywise Cosine of A.
        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_math.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)
        #### Path
        - Utilities > Vector > Vector Math Node
        #### Outputs:
        - `#0 vector: Vector = (0.0, 0.0, 0.0)`
        """
        return self.math("COSINE").vector

    def tangent(self):
        """The entrywise Tangent of A.
        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_math.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)
        #### Path
        - Utilities > Vector > Vector Math Node
        #### Outputs:
        - `#0 vector: Vector = (0.0, 0.0, 0.0)`
        """
        return self.math("TANGENT").vector

    def map_range(self, from_min=(0.0, 0.0, 0.0), from_max=(1.0, 1.0, 1.0), to_min=(0.0, 0.0, 0.0), to_max=(1.0, 1.0, 1.0), interpolation_type="LINEAR", clamp=True, steps=(4.0, 4.0, 4.0)):
        """The Map Range node remaps a value from a range to a target range.
        #### Path
        - Utilities > Math > Map Range Node
        #### Properties:
        - `interpolation_type`: `LINEAR`, `STEPPED`, `SMOOTHSTEP`, `SMOOTHERSTEP`
        #### Outputs:
        - `#1 vector: Vector = (0.0, 0.0, 0.0)`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeMapRange.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/map_range.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeMapRange.html)
        """
        node = new_node(*nodes.ShaderNodeMapRange("FLOAT_VECTOR", interpolation_type, clamp, vector=self, from_min_float3=from_min, from_max_float3=from_max, to_min_float3=to_min, to_max_float3=to_max, steps_float3=steps))
        return node.outputs[1].Vector

    def align_euler_to_vector(self, axis='X', pivot_axis='AUTO', rotation=(0.0, 0.0, 0.0), factor=1.0):
        """The Align Euler to Vector node rotates an Euler rotation into the given direction.
        #### Path
        - Utilities > Rotation > Align Euler to Vector Node
        #### Properties:
        - `axis`: `X`, `Y`, `Z`
        - `pivot_axis`: `AUTO`, `X`, `Y`, `Z`
        #### Outputs:
        - `#0 rotation: Vector = (0.0, 0.0, 0.0)`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_FunctionNodeAlignEulerToVector.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/rotation/align_euler_to_vector.html) [[API]](https://docs.blender.org/api/current/bpy.types.FunctionNodeAlignEulerToVector.html)
        """
        node = new_node(*nodes.FunctionNodeAlignEulerToVector(axis, pivot_axis, rotation, factor, self))
        return node.outputs[0].Vector

    def mapping(self, vector_type='POINT', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(1.0, 1.0, 1.0)):
        """The Mapping node transforms the input vector by applying translation, rotation, and scaling.
        #### Path
        - Vector > Mapping Node
        #### Properties:
        - `vector_type`: `POINT`, `TEXTURE`, `VECTOR`, `NORMAL`
        #### Outputs:
        - `#0 vector: Vector = (0.0, 0.0, 0.0)`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeMapping.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/render/shader_nodes/vector/mapping.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeMapping.html)
        """
        node = new_node(*nodes.ShaderNodeMapping(vector_type, self, location, rotation, scale))
        return node.outputs[0].Vector


class VectorAcceleration(Vector):
    """3D vector socket of a node, mathutils.Vector of 3 items in [-inf, inf], default (0.0, 0.0, 0.0)"""
    bl_idname = "NodeSocketVectorAcceleration"


class VectorDirection(Vector):
    """3D vector socket of a node, mathutils.Vector of 3 items in [-inf, inf], default (0.0, 0.0, 1.0)"""
    bl_idname = "NodeSocketVectorDirection"


class VectorEuler(Vector):
    """3D vector socket of a node, mathutils.Euler rotation of 3 items in [-inf, inf], default (0.0, 0.0, 0.0)"""
    bl_idname = "NodeSocketVectorEuler"


class VectorTranslation(Vector):
    """3D vector socket of a node, mathutils.Vector of 3 items in [-inf, inf], default (0.0, 0.0, 0.0)"""
    bl_idname = "NodeSocketVectorTranslation"


class VectorVelocity(Vector):
    """3D vector socket of a node, mathutils.Vector of 3 items in [-inf, inf], default (0.0, 0.0, 0.0)"""
    bl_idname = "NodeSocketVectorVelocity"


class VectorXYZ(Vector):
    """3D vector socket of a node, mathutils.Vector of 3 items in [-inf, inf], default (0.0, 0.0, 0.0)"""
    bl_idname = "NodeSocketVectorXYZ"


class Integer(Float):
    """Integer number socket of a node, int in [-inf, inf], default 0"""
    bl_idname = "NodeSocketInt"

    def __eq__(self, other):
        return Compare("INT", operation="EQUAL", a_int=self, b_int=other)

    def __ne__(self, other):
        return Compare("INT", operation="NOT_EQUAL", a_int=self, b_int=other)

    def __ge__(self, other):
        return Compare("INT", operation="GREATER_EQUAL", a_int=self, b_int=other)

    def __gt__(self, other):
        return Compare("INT", operation="GREATER_THAN", a_int=self, b_int=other)

    def __le__(self, other):
        return Compare("INT", operation="LESS_EQUAL", a_int=self, b_int=other)

    def __lt__(self, other):
        return Compare("INT", operation="LESS_THAN", a_int=self, b_int=other)

    def switch(self, switch=False, true=0):
        """The Switch node outputs one of two inputs depending on a condition. Only the input that is passed through the node is computed.
        #### Path
        - Utilities > Switch Node
        #### Outputs:
        - `#1 output: Integer = 0`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeSwitch.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/switch.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeSwitch.html)
        """
        node = new_node(*nodes.GeometryNodeSwitch("INT", switch=switch, false_001=self, true_001=true))
        return node.outputs[1].Integer


class IntFactor(Integer):
    """Integer factor socket of a node, int in [0, inf], default 1"""
    bl_idname = "NodeSocketIntFactor"


class IntPercentage(Integer):
    """Integer number socket of a node, int in [0, inf], default 100"""
    bl_idname = "NodeSocketIntPercentage"


class IntUnsigned(Integer):
    """Integer number socket of a node, int in [0, inf], default 0"""
    bl_idname = "NodeSocketIntUnsigned"


class Boolean(Socket):
    """Boolean value socket of a node, default False"""
    bl_idname = "NodeSocketBool"

    @classmethod
    @property
    def true(cls):
        return InputBool(True)

    @classmethod
    @property
    def false(cls):
        return InputBool()

    def switch(self, switch=False, true_bool=True):
        """The Switch node outputs one of two inputs depending on a condition. Only the input that is passed through the node is computed.
        #### Path
        - Utilities > Switch Node
        #### Outputs:
        - `#2 output_002: Boolean = False`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeSwitch.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/switch.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeSwitch.html)
        """
        node = new_node(*nodes.GeometryNodeSwitch("BOOLEAN", switch, false_002=self, true_002=true_bool))
        return node.outputs[2].Boolean

    def math(self, operation='AND', boolean_001=False):
        """The Boolean Math node performs a basic logical operation on its inputs.
        #### Path
        - Utilities > Math > Boolean Math Node
        #### Properties:
        - `operation`: `AND`, `OR`, `NOT`, `NAND`, `NOR`, `XNOR`, `XOR`, `IMPLY`, `NIMPLY`
        #### Outputs:
        - `#0 boolean: Boolean = False`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_FunctionNodeBooleanMath.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/boolean_math.html) [[API]](https://docs.blender.org/api/current/bpy.types.FunctionNodeBooleanMath.html)
        """
        node = new_node(*nodes.FunctionNodeBooleanMath(operation, self, boolean_001))
        return node.outputs[0].Boolean

    def math_and(self, other=False):
        """True when both inputs are true. ([AND](https://en.wikipedia.org/wiki/AND_gate))
        #### Path
        - Utilities > Math > Boolean Math Node
        #### Outputs:
        - `#0 boolean: Boolean = False`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_FunctionNodeBooleanMath.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/boolean_math.html) [[API]](https://docs.blender.org/api/current/bpy.types.FunctionNodeBooleanMath.html)
        """
        return self.math("AND", other)

    def __and__(self, other):
        return self.math_and(other)

    def __mul__(self, other):
        return self.math_and(other)

    def math_or(self, other=False):
        """True when at least one input is true. ([OR](https://en.wikipedia.org/wiki/OR_gate))
        #### Path
        - Utilities > Math > Boolean Math Node
        #### Outputs:
        - `#0 boolean: Boolean = False`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_FunctionNodeBooleanMath.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/boolean_math.html) [[API]](https://docs.blender.org/api/current/bpy.types.FunctionNodeBooleanMath.html)
        """
        return self.math("OR", other)

    def __or__(self, other):
        return self.math_or(other)

    def __add__(self, other):
        return self.math_or(other)

    @property
    def invert(self):
        """Opposite of the input. ([NOT](https://en.wikipedia.org/wiki/NOT_gate))
        #### Path
        - Utilities > Math > Boolean Math Node
        #### Outputs:
        - `#0 boolean: Boolean = False`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_FunctionNodeBooleanMath.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/boolean_math.html) [[API]](https://docs.blender.org/api/current/bpy.types.FunctionNodeBooleanMath.html)
        """
        return self.math("NOT")

    def __neg__(self,):
        """To get called for unary negative e.g. -someobject."""
        return self.invert

    def __invert__(self,):
        """To get called for inversion using the ~ operator."""
        return self.invert

    def not_and(self, other=False):
        """True when at least one input is false. ([NAND](https://en.wikipedia.org/wiki/NAND_gate))
        #### Path
        - Utilities > Math > Boolean Math Node
        #### Outputs:
        - `#0 boolean: Boolean = False`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_FunctionNodeBooleanMath.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/boolean_math.html) [[API]](https://docs.blender.org/api/current/bpy.types.FunctionNodeBooleanMath.html)
        """
        return self.math("NAND", other)

    def nor(self, other=False):
        """True when both inputs are false. ([NOR](https://en.wikipedia.org/wiki/NOR_gate))
        #### Path
        - Utilities > Math > Boolean Math Node
        #### Outputs:
        - `#0 boolean: Boolean = False`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_FunctionNodeBooleanMath.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/boolean_math.html) [[API]](https://docs.blender.org/api/current/bpy.types.FunctionNodeBooleanMath.html)
        """
        return self.math("NOR", other)

    def xnor(self, other=False):
        """True when both inputs are equal. Also known as "exclusive nor". ([XNOR](https://en.wikipedia.org/wiki/XNOR_gate))
        #### Path
        - Utilities > Math > Boolean Math Node
        #### Outputs:
        - `#0 boolean: Boolean = False`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_FunctionNodeBooleanMath.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/boolean_math.html) [[API]](https://docs.blender.org/api/current/bpy.types.FunctionNodeBooleanMath.html)
        """
        return self.math("XNOR", other)

    def xor(self, other=False):
        """True when both inputs are different. Also known as "exclusive or". ([XOR](https://en.wikipedia.org/wiki/XOR_gate))
        #### Path
        - Utilities > Math > Boolean Math Node
        #### Outputs:
        - `#0 boolean: Boolean = False`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_FunctionNodeBooleanMath.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/boolean_math.html) [[API]](https://docs.blender.org/api/current/bpy.types.FunctionNodeBooleanMath.html)
        """
        return self.math("XOR", other)

    def imply(self, other=False):
        """True unless the first input is true and the second is false. ([IMPLY](https://en.wikipedia.org/wiki/IMPLY_gate))
        #### Path
        - Utilities > Math > Boolean Math Node
        #### Outputs:
        - `#0 boolean: Boolean = False`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_FunctionNodeBooleanMath.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/boolean_math.html) [[API]](https://docs.blender.org/api/current/bpy.types.FunctionNodeBooleanMath.html)
        """
        return self.math("IMPLY", other)

    def not_imply(self, other=False):
        """True when the first input is true and the second is false. Also known as ""not imply". ([NIMPLY](https://en.wikipedia.org/wiki/NIMPLY_gate))
        #### Path
        - Utilities > Math > Boolean Math Node
        #### Outputs:
        - `#0 boolean: Boolean = False`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_FunctionNodeBooleanMath.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/boolean_math.html) [[API]](https://docs.blender.org/api/current/bpy.types.FunctionNodeBooleanMath.html)
        """
        return self.math("NIMPLY", other)

    def substract(self, other=False):
        """True when the first input is true and the second is false. Also known as ""not imply". ([NIMPLY](https://en.wikipedia.org/wiki/NIMPLY_gate))
        #### Path
        - Utilities > Math > Boolean Math Node
        #### Outputs:
        - `#0 boolean: Boolean = False`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_FunctionNodeBooleanMath.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/boolean_math.html) [[API]](https://docs.blender.org/api/current/bpy.types.FunctionNodeBooleanMath.html)
        """
        return self.math("NIMPLY", other)


class String(Socket):
    """String socket of a node"""
    bl_idname = "NodeSocketString"

    def join(self, *strings: str, delimiter=""):
        """The Join Strings node combines any number of input strings into the output string. The order of the result depends on the vertical ordering of the inputs in the multi-input socket.
        #### Path
        - Utilities > Text > Join Strings Node
        #### Outputs:
        - `#0 string: String = ""`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeStringJoin.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/text/join_strings.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeStringJoin.html)
        """
        items = list(reversed(strings)) + [self]
        node = new_node(*nodes.GeometryNodeStringJoin(delimiter))
        for item in items:
            if type(item) == str:
                item = InputString(item)
            new_link(item.bsocket, node.bnode.inputs[1])
        return node.outputs[0].String

    def replace(self, find='', replace=''):
        """The Replace String node replaces a string segment with another.
        #### Path
        - Utilities > Text > Replace String Node
        #### Outputs:
        - `#0 string: String = ""`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_FunctionNodeReplaceString.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/text/replace_string.html) [[API]](https://docs.blender.org/api/current/bpy.types.FunctionNodeReplaceString.html)
        """
        node = new_node(*nodes.FunctionNodeReplaceString(self, find, replace))
        return node.outputs[0].String

    def slice(self, position=0, length=10):
        """The Slice String node extracts a string segment from a larger string.
        #### Path
        - Utilities > Text > Slice String Node
        #### Outputs:
        - `#0 string: String = ""`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_FunctionNodeSliceString.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/text/slice_string.html) [[API]](https://docs.blender.org/api/current/bpy.types.FunctionNodeSliceString.html)
        """
        node = new_node(*nodes.FunctionNodeSliceString(self, position, length))
        return node.outputs[0].String

    @property
    def special_characters(self):
        """The Special Characters node is used to output string characters that can’t be typed directly with the keyboard.
        #### Path
        - Utilities > Text > Special Characters Node
        #### Outputs:
        - `#0 line_break: String = ""`
        - `#1 tab: String = ""`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_FunctionNodeInputSpecialCharacters.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/text/special_characters.html) [[API]](https://docs.blender.org/api/current/bpy.types.FunctionNodeInputSpecialCharacters.html)
        """
        node = new_node(*nodes.FunctionNodeInputSpecialCharacters())
        ret = typing.NamedTuple("FunctionNodeInputSpecialCharacters", [("line_break", String), ("tab", String)])
        return ret(node.outputs[0].String, node.outputs[1].String)

    @property
    def length(self):
        """The String Length node outputs the number of characters in the input string.
        #### Path
        - Utilities > Text > String Length Node
        #### Outputs:
        - `#0 length: Integer = 0`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_FunctionNodeStringLength.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/text/string_length.html) [[API]](https://docs.blender.org/api/current/bpy.types.FunctionNodeStringLength.html)
        """
        node = new_node(*nodes.FunctionNodeStringLength(self))
        return node.outputs[0].Integer

    def to_curves(self, align_x='LEFT', align_y='TOP_BASELINE', overflow='OVERFLOW', pivot_mode='BOTTOM_LEFT', font=None, size=1.0, character_spacing=1.0, word_spacing=1.0, line_spacing=1.0, text_box_width=0.0, text_box_height=0.0):
        """The String to Curves converts a string to curve instances. Each unique character used in the string is converted to a curve once, and further uses of that character are more instances of the same geometry.
        #### Path
        - Utilities > Text > String to Curves Node
        #### Properties:
        - `align_x`: `LEFT`, `CENTER`, `RIGHT`, `JUSTIFY`, `FLUSH`
        - `align_y`: `TOP_BASELINE`, `TOP`, `MIDDLE`, `BOTTOM_BASELINE`, `BOTTOM`
        - `overflow`: `OVERFLOW`, `SCALE_TO_FIT`, `TRUNCATE`
        - `pivot_mode`: `BOTTOM_LEFT`, `MIDPOINT`, `TOP_LEFT`, `TOP_CENTER`, `TOP_RIGHT`, `BOTTOM_CENTER`, `BOTTOM_RIGHT`
        #### Outputs:
        - `#0 curve_instances: Geometry = None`
        - `#1 remainder: String = ""`
        - `#2 line: Integer = 0`
        - `#3 pivot_point: Vector = (0.0, 0.0, 0.0)`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeStringToCurves.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/text/string_to_curves.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeStringToCurves.html)
        """
        if type(font) == str:
            font = bpy.data.fonts.get(font)
        node = new_node(*nodes.GeometryNodeStringToCurves(align_x, align_y, overflow, pivot_mode, font, self, size, character_spacing, word_spacing, line_spacing, text_box_width, text_box_height))
        ret = typing.NamedTuple("GeometryNodeStringToCurves", [("curve_instances", Instances), ("remainder", String), ("line", Integer), ("pivot_point", Vector)])
        return ret(node.outputs[0].Instances, node.outputs[1].String, node.outputs[2].Integer, node.outputs[3].Vector)

    def to_curve(self, align_x='LEFT', align_y='TOP_BASELINE', overflow='OVERFLOW', pivot_mode='BOTTOM_LEFT', font=None, size=1.0, character_spacing=1.0, word_spacing=1.0, line_spacing=1.0, text_box_width=0.0, text_box_height=0.0):
        """The String to Curves converts a string to curve instances. Each unique character used in the string is converted to a curve once, and further uses of that character are more instances of the same geometry.
        #### Path
        - Utilities > Text > String to Curves Node
        #### Properties:
        - `align_x`: `LEFT`, `CENTER`, `RIGHT`, `JUSTIFY`, `FLUSH`
        - `align_y`: `TOP_BASELINE`, `TOP`, `MIDDLE`, `BOTTOM_BASELINE`, `BOTTOM`
        - `overflow`: `OVERFLOW`, `SCALE_TO_FIT`, `TRUNCATE`
        - `pivot_mode`: `BOTTOM_LEFT`, `MIDPOINT`, `TOP_LEFT`, `TOP_CENTER`, `TOP_RIGHT`, `BOTTOM_CENTER`, `BOTTOM_RIGHT`
        #### Outputs:
        - `#0 curve_instances: Geometry = None`
        - `#1 remainder: String = ""`
        - `#2 line: Integer = 0`
        - `#3 pivot_point: Vector = (0.0, 0.0, 0.0)`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeStringToCurves.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/text/string_to_curves.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeStringToCurves.html)
        """
        if type(font) == str:
            font = bpy.data.fonts.get(font)
        node = new_node(*nodes.GeometryNodeStringToCurves(align_x, align_y, overflow, pivot_mode, font, self, size, character_spacing, word_spacing, line_spacing, text_box_width, text_box_height))
        ret = typing.NamedTuple("GeometryNodeStringToCurves", [("curve_instances", Instances), ("remainder", String), ("line", Integer), ("pivot_point", Vector)])
        return ret(node.outputs[0].Instances, node.outputs[1].String, node.outputs[2].Integer, node.outputs[3].Vector)


class Color(Vector):
    """RGBA color socket of a node, float array of 4 items in [0, inf], default (0.0, 0.0, 0.0, 0.0)"""
    bl_idname = "NodeSocketColor"

    def mix(self, b_color=(0.5, 0.5, 0.5, 1.0), blend_type="MIX", clamp_factor=True, clamp_result=False, factor_float=0.5):
        """The Mix Node mixes values, colors and vectors inputs using a factor to control the amount of interpolation. The Color mode has additional blending modes.
        - `blend_type`: `MIX`, `DARKEN`, `MULTIPLY`, `BURN`, `LIGHTEN`, `SCREEN`, `DODGE`, `ADD`, `OVERLAY`, `SOFT_LIGHT`, `LINEAR_LIGHT`, `DIFFERENCE`, `EXCLUSION`, `SUBTRACT`, `DIVIDE`, `HUE`, `SATURATION`, `COLOR`, `VALUE`
        #### Path
        - Utilities > Color > Mix Node
        #### Outputs:
        - `#2 result_color: Color = (0.0, 0.0, 0.0, 0.0)`

        ![](https://docs.blender.org/manual/en/latest/_images/render_shader-nodes_shader_mix_node.jpg)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/color/mix_rgb.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html)
        """
        node = new_node(*nodes.ShaderNodeMix(blend_type, "RGBA", clamp_factor=clamp_factor, clamp_result=clamp_result, factor_float=factor_float, a_color=self, b_color=b_color))
        return node.outputs[2].Color

    def rgb_curve(self, mapping=None, fac=1.0):
        """The RGB Curves Node allows color corrections for each color channel and levels adjustments in the compositing context.
        #### Path
        - Utilities > Color > RGB Curves Node
        #### Outputs:
        - `#0 color: Color = (0.0, 0.0, 0.0, 0.0)`

        ![](https://docs.blender.org/manual/en/latest/_images/compositing_node-types_CompositorNodeCurveRGB.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/color/rgb_curves.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeRGBCurve.html)
        """
        node = new_node(*nodes.ShaderNodeRGBCurve(mapping, fac, self))
        return node.outputs[0].Color

    def seperate(self, mode='RGB'):
        """The Separate Color Node splits an image into its composite color channels. The node can output multiple Color Models depending on the Mode property.
        #### Path
        - Utilities > Color > Separate Color Node
        #### Properties:
        - `mode`: `RGB`, `HSV`, `HSL`
        #### Outputs:
        - `#0 red: Float = 0.0`
        - `#1 green: Float = 0.0`
        - `#2 blue: Float = 0.0`
        - `#3 alpha: Float = 0.0`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_FunctionNodeSeparateColor.png)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/color/separate_color.html) [[API]](https://docs.blender.org/api/current/bpy.types.FunctionNodeSeparateColor.html)
        """
        node = new_node(*nodes.FunctionNodeSeparateColor(mode, self))
        ret = typing.NamedTuple("FunctionNodeSeparateColor", [("red", Float), ("green", Float), ("blue", Float), ("alpha", Float)])
        return ret(node.outputs[0].Float, node.outputs[1].Float, node.outputs[2].Float, node.outputs[3].Float)

    def bright_contrast(self, bright=0.0, contrast=0.0):
        """
        #### Path
        - Color > Bright/Contrast Node
        #### Outputs:
        - `#0 color: Color = (0.0, 0.0, 0.0, 0.0)`

        ![](https://docs.blender.org/manual/en/latest/_images/compositing_node-types_CompositorNodeBrightContrast.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/render/shader_nodes/color/bright_contrast.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeBrightContrast.html)
        """
        node = new_node(*nodes.ShaderNodeBrightContrast(self, bright, contrast))
        return node.outputs[0].Color

    def gamma(self, gamma=1.0):
        """Use this node to apply a gamma correction.
        #### Path
        - Color > Gamma Node
        #### Outputs:
        - `#0 color: Color = (0.0, 0.0, 0.0, 0.0)`

        ![](https://docs.blender.org/manual/en/latest/_images/compositing_node-types_CompositorNodeGamma.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/render/shader_nodes/color/gamma.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeGamma.html)
        """
        node = new_node(*nodes.ShaderNodeGamma(self, gamma))
        return node.outputs[0].Color

    def hue_saturation(self, hue=0.5, saturation=1.0, value=1.0, fac=1.0):
        """The Hue Saturation Value Node applies a color transformation in the HSV Color Model.
        #### Path
        - Color > Hue Saturation Value Node
        #### Outputs:
        - `#0 color: Color = (0.0, 0.0, 0.0, 0.0)`

        ![](https://docs.blender.org/manual/en/latest/_images/compositing_node-types_CompositorNodeHueSat.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/render/shader_nodes/color/hue_saturation.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeHueSaturation.html)
        """
        node = new_node(*nodes.ShaderNodeHueSaturation(hue, saturation, value, fac, self))
        return node.outputs[0].Color

    def invert(self, fac=1.0):
        """The Invert Node inverts the colors in the input image, producing a negative.
        #### Path
        - Color > Invert Node
        #### Outputs:
        - `#0 color: Color = (0.0, 0.0, 0.0, 0.0)`

        ![](https://docs.blender.org/manual/en/latest/_images/compositing_node-types_CompositorNodeInvert.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/render/shader_nodes/color/invert.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeInvert.html)
        """
        node = new_node(*nodes.ShaderNodeInvert(fac, self))
        return node.outputs[0].Color

    def normal_map(self, space='TANGENT', uv_map='', strength=1.0):
        """The Normal Map node generates a perturbed normal from an RGB normal map image. This is usually chained with an Image Texture node in the color input, to specify the normal map image. For tangent space normal maps, the UV coordinates for the image must match, and the image texture should be set to Non-Color mode to give correct results.
        #### Path
        - Vector > Normal Map Node
        #### Properties:
        - `space`: `TANGENT`, `OBJECT`, `WORLD`, `BLENDER_OBJECT`, `BLENDER_WORLD`
        #### Outputs:
        - `#0 normal: Vector = (0.0, 0.0, 0.0)`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeNormalMap.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/render/shader_nodes/vector/normal_map.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeNormalMap.html)
        """
        node = new_node(*nodes.ShaderNodeNormalMap(space, uv_map, strength, self))
        return node.outputs[0].Vector

    def to_background(self, strength=1.0):
        """The Background shader node is used to add background light emission. This node should only be used for the world surface output.
        #### Path
        - Shader > Background
        #### Outputs:
        - `#0 background: Shader = None`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeBackground.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/render/shader_nodes/shader/background.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeBackground.html)
        """
        node = new_node(*nodes.ShaderNodeBackground(self, strength))
        return node.outputs[0].Shader


class Shader(Socket):
    """Shader socket of a node"""
    bl_idname = "NodeSocketShader"

    def __init__(self, bsocket: NodeSocket) -> None:
        super().__init__(bsocket)
        self._hair_info = None
        self._geometry = None
        self._object_info = None
        self._particle_info = None
        self._point_info = None
        self._volume_info = None

    @staticmethod
    def attribute(name='', attribute_type='GEOMETRY'):
        """The Attribute node allows you to retrieve attributes attached to an object or mesh.
        #### Path
        - Input > Attribute Node
        #### Properties:
        - `attribute_type`: `GEOMETRY`, `OBJECT`, `INSTANCER`, `VIEW_LAYER`
        #### Outputs:
        - `#0 color: Color = (0.0, 0.0, 0.0, 0.0)`
        - `#1 vector: Vector = (0.0, 0.0, 0.0)`
        - `#2 fac: Float = 0.0`
        - `#3 alpha: Float = 0.0`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeAttribute.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/render/shader_nodes/input/attribute.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeAttribute.html)
        """
        node = new_node(*nodes.ShaderNodeAttribute(attribute_type, name))
        ret = typing.NamedTuple("ShaderNodeAttribute", [("color", Color), ("vector", Vector), ("fac", Float), ("alpha", Float)])
        return ret(node.outputs[0].Color, node.outputs[1].Vector, node.outputs[2].Float, node.outputs[3].Float)

    @staticmethod
    def bevel(samples=4, radius=0.05, normal=(0.0, 0.0, 0.0)):
        """Cycles Only
        #### Path
        - Input > Bevel Node
        #### Outputs:
        - `#0 normal: Vector = (0.0, 0.0, 0.0)`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeBevel.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/render/shader_nodes/input/bevel.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeBevel.html)
        """
        node = new_node(*nodes.ShaderNodeBevel(samples, radius, normal))
        return node.outputs[0].Vector

    @staticmethod
    @property
    def camera_data():
        """The Camera Data node returns information about the shading point relative to the camera. This could be used for example to change the shading of objects further away from the camera, or make custom fog effects.
        #### Path
        - Input > Camera Data Node
        #### Outputs:
        - `#0 view_vector: Vector = (0.0, 0.0, 0.0)`
        - `#1 view_z_depth: Float = 0.0`
        - `#2 view_distance: Float = 0.0`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeCameraData.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/render/shader_nodes/input/camera_data.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeCameraData.html)
        """
        node = new_node(*nodes.ShaderNodeCameraData())
        ret = typing.NamedTuple("ShaderNodeCameraData", [("view_vector", Vector), ("view_z_depth", Float), ("view_distance", Float)])
        return ret(node.outputs[0].Vector, node.outputs[1].Float, node.outputs[2].Float)

    @staticmethod
    def fresnel(ior=1.45, normal=(0.0, 0.0, 0.0)):
        """The Fresnel or Dielectric Fresnel node computes how much light is reflected off a layer, where the rest will be refracted through the layer. The resulting weight can be used for layering shaders with the Mix Shader node. It is dependent on the angle between the surface normal and the viewing direction.
        #### Path
        - Input > Fresnel Node
        #### Outputs:
        - `#0 fac: Float = 0.0`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeFresnel.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/render/shader_nodes/input/fresnel.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeFresnel.html)
        """
        node = new_node(*nodes.ShaderNodeFresnel(ior, normal))
        return node.outputs[0].Float

    @property
    def geometry(self):
        """The Geometry node gives geometric information about the current shading point. All vector coordinates are in World Space. For volume shaders, only the position and incoming vector are available.
        #### Path
        - Input > Geometry Node
        #### Outputs:
        - `#0 position: Vector = (0.0, 0.0, 0.0)`
        - `#1 normal: Vector = (0.0, 0.0, 0.0)`
        - `#2 tangent: Vector = (0.0, 0.0, 0.0)`
        - `#3 true_normal: Vector = (0.0, 0.0, 0.0)`
        - `#4 incoming: Vector = (0.0, 0.0, 0.0)`
        - `#5 parametric: Vector = (0.0, 0.0, 0.0)`
        - `#6 backfacing: Float = 0.0`
        - `#7 pointiness: Float = 0.0`
        - `#8 random_per_island: Float = 0.0`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeNewGeometry.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/render/shader_nodes/input/geometry.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeNewGeometry.html)
        """
        if self._geometry is None:
            node = new_node(*nodes.ShaderNodeNewGeometry())
            ret = typing.NamedTuple("ShaderNodeNewGeometry", [("position", Vector), ("normal", Vector), ("tangent", Vector), ("true_normal", Vector), ("incoming", Vector), ("parametric", Vector), ("backfacing", Float), ("pointiness", Float), ("random_per_island", Float)])
            self._geometry = ret(node.outputs[0].Vector, node.outputs[1].Vector, node.outputs[2].Vector, node.outputs[3].Vector, node.outputs[4].Vector, node.outputs[5].Vector, node.outputs[6].Float, node.outputs[7].Float, node.outputs[8].Float)
        return self._geometry

    @property
    def hair_info(self):
        """The Curves Info node gives access to Hair information.
        #### Path
        - Input > Curves Info Node
        #### Outputs:
        - `#0 is_strand: Float = 0.0`
        - `#1 intercept: Float = 0.0`
        - `#2 length: Float = 0.0`
        - `#3 thickness: Float = 0.0`
        - `#4 tangent_normal: Vector = (0.0, 0.0, 0.0)`
        - `#5 random: Float = 0.0`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeHairInfo.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/render/shader_nodes/input/hair_info.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeHairInfo.html)
        """
        if self._hair_info is None:
            node = new_node(*nodes.ShaderNodeHairInfo())
            ret = typing.NamedTuple("ShaderNodeHairInfo", [("is_strand", Float), ("intercept", Float), ("length", Float), ("thickness", Float), ("tangent_normal", Vector), ("random", Float)])
            self._hair_info = ret(node.outputs[0].Float, node.outputs[1].Float, node.outputs[2].Float, node.outputs[3].Float, node.outputs[4].Vector, node.outputs[5].Float)
        return self._hair_info

    @staticmethod
    def layer_weight(blend=0.5, normal=(0.0, 0.0, 0.0)):
        """The Layer Weight node outputs a weight typically used for layering shaders with the Mix Shader node.
        #### Path
        - Input > Layer Weight Node
        #### Outputs:
        - `#0 fresnel: Float = 0.0`
        - `#1 facing: Float = 0.0`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeLayerWeight.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/render/shader_nodes/input/layer_weight.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeLayerWeight.html)
        """
        node = new_node(*nodes.ShaderNodeLayerWeight(blend, normal))
        ret = typing.NamedTuple("ShaderNodeLayerWeight", [("fresnel", Float), ("facing", Float)])
        return ret(node.outputs[0].Float, node.outputs[1].Float)

    @staticmethod
    @property
    def light_path():
        """The Light Path node is used to find out for which kind of incoming ray the shader is being executed; particularly useful for non-physically-based tricks. More information about the meaning of each type is in the Light Paths documentation.
        #### Path
        - Input > Light Path Node
        #### Outputs:
        - `#0 is_camera_ray: Float = 0.0`
        - `#1 is_shadow_ray: Float = 0.0`
        - `#2 is_diffuse_ray: Float = 0.0`
        - `#3 is_glossy_ray: Float = 0.0`
        - `#4 is_singular_ray: Float = 0.0`
        - `#5 is_reflection_ray: Float = 0.0`
        - `#6 is_transmission_ray: Float = 0.0`
        - `#7 ray_length: Float = 0.0`
        - `#8 ray_depth: Float = 0.0`
        - `#9 diffuse_depth: Float = 0.0`
        - `#10 glossy_depth: Float = 0.0`
        - `#11 transparent_depth: Float = 0.0`
        - `#12 transmission_depth: Float = 0.0`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeLightPath.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/render/shader_nodes/input/light_path.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeLightPath.html)
        """
        node = new_node(*nodes.ShaderNodeLightPath())
        ret = typing.NamedTuple("ShaderNodeLightPath", [("is_camera_ray", Float), ("is_shadow_ray", Float), ("is_diffuse_ray", Float), ("is_glossy_ray", Float), ("is_singular_ray", Float), ("is_reflection_ray", Float), ("is_transmission_ray", Float), ("ray_length", Float), ("ray_depth", Float), ("diffuse_depth", Float), ("glossy_depth", Float), ("transparent_depth", Float), ("transmission_depth", Float)])
        return ret(node.outputs[0].Float, node.outputs[1].Float, node.outputs[2].Float, node.outputs[3].Float, node.outputs[4].Float, node.outputs[5].Float, node.outputs[6].Float, node.outputs[7].Float, node.outputs[8].Float, node.outputs[9].Float, node.outputs[10].Float, node.outputs[11].Float, node.outputs[12].Float)

    @property
    def object_info(self):
        """The Object Info node gives information about the object instance. This can be useful to give some variation to a single material assigned to multiple instances, either manually controlled through the object index, based on the object location, or randomized for each instance. For example a Noise texture can give random colors or a Color Ramp can give a range of colors to be randomly picked from.
        #### Path
        - Input > Object Info Node
        #### Outputs:
        - `#0 location: Vector = (0.0, 0.0, 0.0)`
        - `#1 color: Color = (0.0, 0.0, 0.0, 0.0)`
        - `#2 alpha: Float = 0.0`
        - `#3 object_index: Float = 0.0`
        - `#4 material_index: Float = 0.0`
        - `#5 random: Float = 0.0`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeObjectInfo.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/render/shader_nodes/input/object_info.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeObjectInfo.html)
        """
        if self._object_info is None:
            node = new_node(*nodes.ShaderNodeObjectInfo())
            ret = typing.NamedTuple("ShaderNodeObjectInfo", [("location", Vector), ("color", Color), ("alpha", Float), ("object_index", Float), ("material_index", Float), ("random", Float)])
            self._object_info = ret(node.outputs[0].Vector, node.outputs[1].Color, node.outputs[2].Float, node.outputs[3].Float, node.outputs[4].Float, node.outputs[5].Float)
        return self._object_info

    @property
    def particle_info(self):
        """Cycles Only
        #### Path
        - Input > Particle Info Node
        #### Outputs:
        - `#0 index: Float = 0.0`
        - `#1 random: Float = 0.0`
        - `#2 age: Float = 0.0`
        - `#3 lifetime: Float = 0.0`
        - `#4 location: Vector = (0.0, 0.0, 0.0)`
        - `#5 size: Float = 0.0`
        - `#6 velocity: Vector = (0.0, 0.0, 0.0)`
        - `#7 angular_velocity: Vector = (0.0, 0.0, 0.0)`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeParticleInfo.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/render/shader_nodes/input/particle_info.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeParticleInfo.html)
        """
        if self._particle_info is None:
            node = new_node(*nodes.ShaderNodeParticleInfo())
            ret = typing.NamedTuple("ShaderNodeParticleInfo", [("index", Float), ("random", Float), ("age", Float), ("lifetime", Float), ("location", Vector), ("size", Float), ("velocity", Vector), ("angular_velocity", Vector)])
            self._particle_info = ret(node.outputs[0].Float, node.outputs[1].Float, node.outputs[2].Float, node.outputs[3].Float, node.outputs[4].Vector, node.outputs[5].Float, node.outputs[6].Vector, node.outputs[7].Vector)
        return self._particle_info

    @property
    def point_info(self):
        """Cycles Only
        #### Path
        - Input > Point Info
        #### Outputs:
        - `#0 position: Vector = (0.0, 0.0, 0.0)`
        - `#1 radius: Float = 0.0`
        - `#2 random: Float = 0.0`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodePointInfo.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/render/shader_nodes/input/point_info.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodePointInfo.html)
        """
        if self._point_info is None:
            node = new_node(*nodes.ShaderNodePointInfo())
            ret = typing.NamedTuple("ShaderNodePointInfo", [("position", Vector), ("radius", Float), ("random", Float)])
            self._point_info = ret(node.outputs[0].Vector, node.outputs[1].Float, node.outputs[2].Float)
        return self._point_info

    @staticmethod
    def tangent_radial(axis='Z'):
        """The Tangent node generates a tangent direction for the Anisotropic BSDF.
        #### Path
        - Input > Tangent Node
        #### Properties:
        - `axis`: `Z`, `X`, `Y`
        #### Outputs:
        - `#0 tangent: Vector = (0.0, 0.0, 0.0)`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeTangent.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/render/shader_nodes/input/tangent.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeTangent.html)
        """
        node = new_node(*nodes.ShaderNodeTangent(axis, "RADIAL"))
        return node.outputs[0].Vector

    @staticmethod
    def tangent_uv_map(uv_map=""):
        """The Tangent node generates a tangent direction for the Anisotropic BSDF.
        #### Path
        - Input > Tangent Node
        #### Outputs:
        - `#0 tangent: Vector = (0.0, 0.0, 0.0)`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeTangent.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/render/shader_nodes/input/tangent.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeTangent.html)
        """
        node = new_node(*nodes.ShaderNodeTangent(direction_type="UV_MAP", uv_map=uv_map))
        return node.outputs[0].Vector

    @staticmethod
    def uv_map(from_instancer=False, uv_map=''):
        """The UV Map node is used to retrieve specific UV maps. Unlike the Texture Coordinate Node which only provides the active UV map, this node can retrieve any UV map belonging to the object using the material.
        #### Path
        - Input > UV Map Node
        #### Outputs:
        - `#0 uv: Vector = (0.0, 0.0, 0.0)`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeUVMap.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/render/shader_nodes/input/uv_map.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeUVMap.html)
        """
        node = new_node(*nodes.ShaderNodeUVMap(from_instancer, uv_map))
        return node.outputs[0].Vector

    @staticmethod
    def color_attribute(layer_name=''):
        """The Color Attribute node provides access to Color Attributes as well as their alpha value.
        #### Path
        - Input > Color Attribute Node
        #### Outputs:
        - `#0 color: Color = (0.0, 0.0, 0.0, 0.0)`
        - `#1 alpha: Float = 0.0`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeVertexColor.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/render/shader_nodes/input/vertex_color.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeVertexColor.html)
        """
        node = new_node(*nodes.ShaderNodeVertexColor(layer_name))
        ret = typing.NamedTuple("ShaderNodeVertexColor", [("color", Color), ("alpha", Float)])
        return ret(node.outputs[0].Color, node.outputs[1].Float)

    @property
    def volume_info(self):
        """The Volume Info node provides information about Smoke Domains.
        #### Path
        - Input > Volume Info Node
        #### Outputs:
        - `#0 color: Color = (0.0, 0.0, 0.0, 0.0)`
        - `#1 density: Float = 0.0`
        - `#2 flame: Float = 0.0`
        - `#3 temperature: Float = 0.0`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeVolumeInfo.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/render/shader_nodes/input/volume_info.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeVolumeInfo.html)
        """
        if self._volume_info is None:
            node = new_node(*nodes.ShaderNodeVolumeInfo())
            ret = typing.NamedTuple("ShaderNodeVolumeInfo", [("color", Color), ("density", Float), ("flame", Float), ("temperature", Float)])
            self._volume_info = ret(node.outputs[0].Color, node.outputs[1].Float, node.outputs[2].Float, node.outputs[3].Float)
        return self._volume_info

    @staticmethod
    def wire_frame(use_pixel_size=False, size=0.01):
        """The Wireframe node is used to retrieve the edges of an object as it appears to Cycles. As meshes are triangulated before being processed by Cycles, topology will always appear triangulated when viewed with the Wireframe node.
        #### Path
        - Input > Wireframe Node
        #### Outputs:
        - `#0 fac: Float = 0.0`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeWireframe.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/render/shader_nodes/input/wireframe.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeWireframe.html)
        """
        node = new_node(*nodes.ShaderNodeWireframe(use_pixel_size, size))
        ret = typing.NamedTuple("ShaderNodeWireframe", [("fac", Float)])
        return ret(node.outputs[0].Float)

    def add_shader(self, shader_001=None):
        """The Add node is used to add two Shaders together.
        #### Path
        - Shader > Add Shader
        #### Outputs:
        - `#0 shader: Shader = None`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeAddShader.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/render/shader_nodes/shader/add.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeAddShader.html)
        """
        node = new_node(*nodes.ShaderNodeAddShader(self, shader_001))
        return node.outputs[0].Shader

    def __add__(self, shader_001=None):
        """The Add node is used to add two Shaders together.
        #### Path
        - Shader > Add Shader
        #### Outputs:
        - `#0 shader: Shader = None`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeAddShader.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/render/shader_nodes/shader/add.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeAddShader.html)
        """
        node = new_node(*nodes.ShaderNodeAddShader(self, shader_001))
        return node.outputs[0].Shader

    @staticmethod
    def Background(color=(0.8, 0.8, 0.8, 1.0), strength=1.0, weight=0.0):
        """The Background shader node is used to add background light emission. This node should only be used for the world surface output.
        #### Path
        - Shader > Background
        #### Outputs:
        - `#0 background: Shader = None`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeBackground.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/render/shader_nodes/shader/background.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeBackground.html)
        """
        node = new_node(*nodes.ShaderNodeBackground(color, strength, weight))
        return node.outputs[0].Shader

    @staticmethod
    def Emission(color=(1.0, 1.0, 1.0, 1.0), strength=1.0, weight=0.0):
        """The Emission node is used to add Lambertian emission shader. This can for example, be used for material and light surface outputs.
        #### Path
        - Shader > Emission
        #### Outputs:
        - `#0 emission: Shader = None`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeEmission.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/render/shader_nodes/shader/emission.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeEmission.html)
        """
        node = new_node(*nodes.ShaderNodeEmission(color, strength, weight))
        return node.outputs[0].Shader

    @staticmethod
    def Holdout():
        """The Holdout shader node is used to create a “hole” in the image with zero alpha transparency, which is useful for compositing (see Alpha Channel).
        #### Path
        - Shader > Holdout
        #### Outputs:
        - `#0 holdout: Shader = None`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeHoldout.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/render/shader_nodes/shader/holdout.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeHoldout.html)
        """
        node = new_node(*nodes.ShaderNodeHoldout())
        return node.outputs[0].Shader

    def mix(self, shader=None, fac=0.5):
        """The Mix node is used to mix two shaders together. Mixing can be used for material layering, where the Factor input may, for example, be connected to a Blend Weight node.
        #### Path
        - Shader > Mix Shader
        #### Outputs:
        - `#0 shader: Shader = None`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeMixShader.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/render/shader_nodes/shader/mix.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeMixShader.html)
        """
        node = new_node(*nodes.ShaderNodeMixShader(fac, self, shader))
        return node.outputs[0].Shader

    @staticmethod
    def VolumePrincipled(color=(0.5, 0.5, 0.5, 1.0), color_attribute='', density=1.0, density_attribute='density', anisotropy=0.0, absorption_color=(0.0, 0.0, 0.0, 1.0), emission_strength=0.0, emission_color=(1.0, 1.0, 1.0, 1.0), blackbody_intensity=0.0, blackbody_tint=(1.0, 1.0, 1.0, 1.0), temperature=1000.0, temperature_attribute='temperature', weight=0.0):
        """The Principled Volume shader combines all volume shading components into a single easy to use node. Volumes like smoke and fire can be rendered with a single shader node, which includes scattering, absorption and blackbody emission.
        #### Path
        - Shader > Principled Volume
        #### Outputs:
        - `#0 volume: Shader = None`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeVolumePrincipled.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/render/shader_nodes/shader/volume_principled.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeVolumePrincipled.html)
        """
        node = new_node(*nodes.ShaderNodeVolumePrincipled(color, color_attribute, density, density_attribute, anisotropy, absorption_color, emission_strength, emission_color, blackbody_intensity, blackbody_tint, temperature, temperature_attribute, weight))
        return node.outputs[0].Shader

    @staticmethod
    def SubsurfaceScattering(falloff='RANDOM_WALK', color=(0.8, 0.8, 0.8, 1.0), scale=1.0, radius=(1.0, 0.2, 0.1), ior=1.4, anisotropy=0.0, normal=(0.0, 0.0, 0.0), weight=0.0):
        """The Subsurface Scattering node is used to add simple subsurface multiple scattering, for materials such as skin, wax, marble, milk and others. For these materials, rather than light being reflect directly off the surface, it will penetrate the surface and bounce around internally before getting absorbed or leaving the surface at a nearby point.
        #### Path
        - Shader > Subsurface Scattering
        #### Properties:
        - `falloff`: `RANDOM_WALK`, `BURLEY`, `RANDOM_WALK_FIXED_RADIUS`
        #### Outputs:
        - `#0 bssrdf: Shader = None`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeSubsurfaceScattering.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/render/shader_nodes/shader/sss.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeSubsurfaceScattering.html)
        """
        node = new_node(*nodes.ShaderNodeSubsurfaceScattering(falloff, color, scale, radius, ior, anisotropy, normal, weight))
        return node.outputs[0].Shader

    @staticmethod
    def VolumeAbsorption(color=(0.8, 0.8, 0.8, 1.0), density=1.0, weight=0.0):
        """The Volume Absorption node allows light to be absorbed as it passes through the volume. Typical usage for this node would be water and colored glass.
        #### Path
        - Shader > Volume Absorption
        #### Outputs:
        - `#0 volume: Shader = None`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeVolumeAbsorption.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/render/shader_nodes/shader/volume_absorption.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeVolumeAbsorption.html)
        """
        node = new_node(*nodes.ShaderNodeVolumeAbsorption(color, density, weight))
        return node.outputs[0].Shader

    @staticmethod
    def VolumeScatter(color=(0.8, 0.8, 0.8, 1.0), density=1.0, anisotropy=0.0, weight=0.0):
        """The Volume Scatter node allows light to be scattered as it passes through the volume. Typical usage would be to add fog to a scene. It can also be used with the Volume Absorption node to create smoke.
        #### Path
        - Shader > Volume Scatter
        #### Outputs:
        - `#0 volume: Shader = None`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeVolumeScatter.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/render/shader_nodes/shader/volume_scatter.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeVolumeScatter.html)
        """
        node = new_node(*nodes.ShaderNodeVolumeScatter(color, density, anisotropy, weight))
        return node.outputs[0].Shader

    def to_rgb(self):
        """Eevee Only
        #### Path
        - Converter > Shader To RGB
        #### Outputs:
        - `#0 color: Color = (0.0, 0.0, 0.0, 0.0)`
        - `#1 alpha: Float = 0.0`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeShaderToRGB.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/render/shader_nodes/converter/shader_to_rgb.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeShaderToRGB.html)
        """
        node = new_node(*nodes.ShaderNodeShaderToRGB(self))
        ret = typing.NamedTuple("ShaderNodeShaderToRGB", [("color", Color), ("alpha", Float)])
        return ret(node.outputs[0].Color, node.outputs[1].Float)


class BSDF(Shader):

    @property
    def base_color(self):
        raise RuntimeError("Input Sockets cannot be accessed in this context")

    @base_color.setter
    def base_color(self, value):
        self["base_color"] = value

    @staticmethod
    def Principled(distribution='GGX', subsurface_method='RANDOM_WALK', base_color=(0.8, 0.8, 0.8, 1.0), subsurface=0.0, subsurface_radius=(1.0, 0.2, 0.1), subsurface_color=(0.8, 0.8, 0.8, 1.0), subsurface_ior=1.4, subsurface_anisotropy=0.0, metallic=0.0, specular=0.5, specular_tint=0.0, roughness=0.5, anisotropic=0.0, anisotropic_rotation=0.0, sheen=0.0, sheen_tint=0.5, clearcoat=0.0, clearcoat_roughness=0.03, ior=1.45, transmission=0.0, transmission_roughness=0.0, emission=(0.0, 0.0, 0.0, 1.0), emission_strength=1.0, alpha=1.0, normal=(0.0, 0.0, 0.0), clearcoat_normal=(0.0, 0.0, 0.0), tangent=(0.0, 0.0, 0.0), weight=0.0):
        """The Principled BSDF that combines multiple layers into a single easy to use node. It is based on the Disney principled model also known as the “PBR” shader, making it compatible with other software such as Pixar’s Renderman® and Unreal Engine®. Image textures painted or baked from software like Substance Painter® may be directly linked to the corresponding parameters in this shader.
        #### Path
        - Shader > Principled BSDF
        #### Properties:
        - `distribution`: `GGX`, `MULTI_GGX`
        - `subsurface_method`: `RANDOM_WALK`, `BURLEY`, `RANDOM_WALK_FIXED_RADIUS`
        #### Outputs:
        - `#0 bsdf: Shader = None`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeBsdfPrincipled.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/render/shader_nodes/shader/principled.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeBsdfPrincipled.html)
        """
        node = new_node(*nodes.ShaderNodeBsdfPrincipled(distribution, subsurface_method, base_color, subsurface, subsurface_radius, subsurface_color, subsurface_ior, subsurface_anisotropy, metallic, specular, specular_tint, roughness, anisotropic, anisotropic_rotation, sheen, sheen_tint, clearcoat, clearcoat_roughness, ior, transmission, transmission_roughness, emission, emission_strength, alpha, normal, clearcoat_normal, tangent, weight))
        return BSDF(node.outputs[0].bsocket)

    @staticmethod
    def HairPrincipled(parametrization='COLOR', color=(0.018, 0.006, 0.002, 1.0), melanin=0.8, melanin_redness=1.0, tint=(1.0, 1.0, 1.0, 1.0), absorption_coefficient=(0.246, 0.52, 1.365), roughness=0.3, radial_roughness=0.3, coat=0.0, ior=1.55, offset=math.radians(2.0), random_color=0.0, random_roughness=0.0, random=0.0, weight=0.0):
        """Cycles Only
        #### Path
        - Shader > Principled Hair BSDF
        #### Properties:
        - `parametrization`: `COLOR`, `ABSORPTION`, `MELANIN`
        #### Outputs:
        - `#0 bsdf: Shader = None`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeBsdfHairPrincipled.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/render/shader_nodes/shader/hair_principled.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeBsdfHairPrincipled.html)
        """
        node = new_node(*nodes.ShaderNodeBsdfHairPrincipled(parametrization, color, melanin, melanin_redness, tint, absorption_coefficient, roughness, radial_roughness, coat, ior, offset, random_color, random_roughness, random, weight))
        return node.outputs[0].Shader

    @staticmethod
    def Anisotropic(distribution='GGX', color=(0.8, 0.8, 0.8, 1.0), roughness=0.5, anisotropy=0.5, rotation=0.0, normal=(0.0, 0.0, 0.0), tangent=(0.0, 0.0, 0.0), weight=0.0):
        """Cycles Only
        #### Path
        - Shader > Anisotropic BSDF
        #### Properties:
        - `distribution`: `GGX`, `BECKMANN`, `MULTI_GGX`, `ASHIKHMIN_SHIRLEY`
        #### Outputs:
        - `#0 bsdf: Shader = None`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeBsdfAnisotropic.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/render/shader_nodes/shader/anisotropic.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeBsdfAnisotropic.html)
        """
        node = new_node(*nodes.ShaderNodeBsdfAnisotropic(distribution, color, roughness, anisotropy, rotation, normal, tangent, weight))
        return node.outputs[0].Shader

    @staticmethod
    def Diffuse(color=(0.8, 0.8, 0.8, 1.0), roughness=0.0, normal=(0.0, 0.0, 0.0), weight=0.0):
        """The Diffuse BSDF node is used to add Lambertian and Oren-Nayar diffuse reflection.
        #### Path
        - Shader > Diffuse BSDF
        #### Outputs:
        - `#0 bsdf: Shader = None`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeBsdfDiffuse.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/render/shader_nodes/shader/diffuse.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeBsdfDiffuse.html)
        """
        node = new_node(*nodes.ShaderNodeBsdfDiffuse(color, roughness, normal, weight))
        return node.outputs[0].Shader

    @staticmethod
    def Glass(distribution='BECKMANN', color=(1.0, 1.0, 1.0, 1.0), roughness=0.0, ior=1.45, normal=(0.0, 0.0, 0.0), weight=0.0):
        """The Glass BSDF is used to add a Glass-like shader mixing refraction and reflection at grazing angles. Like the transparent shader, only pure white will make it transparent. The glass shader tends to cause noise due to caustics. Since the Cycles path tracing integrator is not very good at rendering caustics, it helps to combine this with a transparent shader for shadows; for more details see here.
        #### Path
        - Shader > Glass BSDF
        #### Properties:
        - `distribution`: `BECKMANN`, `SHARP`, `GGX`, `MULTI_GGX`
        #### Outputs:
        - `#0 bsdf: Shader = None`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeBsdfGlass.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/render/shader_nodes/shader/glass.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeBsdfGlass.html)
        """
        node = new_node(*nodes.ShaderNodeBsdfGlass(distribution, color, roughness, ior, normal, weight))
        return node.outputs[0].Shader

    @staticmethod
    def Glossy(distribution='GGX', color=(0.8, 0.8, 0.8, 1.0), roughness=0.5, normal=(0.0, 0.0, 0.0), weight=0.0):
        """The Glossy BSDF node is used to add reflection with microfacet distribution, used for materials such as metal or mirrors.
        #### Path
        - Shader > Glossy BSDF
        #### Properties:
        - `distribution`: `GGX`, `SHARP`, `BECKMANN`, `ASHIKHMIN_SHIRLEY`, `MULTI_GGX`
        #### Outputs:
        - `#0 bsdf: Shader = None`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeBsdfGlossy.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/render/shader_nodes/shader/glossy.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeBsdfGlossy.html)
        """
        node = new_node(*nodes.ShaderNodeBsdfGlossy(distribution, color, roughness, normal, weight))
        return node.outputs[0].Shader

    @staticmethod
    def Hair(component='Reflection', color=(0.8, 0.8, 0.8, 1.0), offset=math.radians(0.0), roughnessu=0.1, roughnessv=1.0, tangent=(0.0, 0.0, 0.0), weight=0.0):
        """Cycles Only
        #### Path
        - Shader > Hair BSDF
        #### Properties:
        - `component`: `Reflection`, `Transmission`
        #### Outputs:
        - `#0 bsdf: Shader = None`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeBsdfHair.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/render/shader_nodes/shader/hair.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeBsdfHair.html)
        """
        node = new_node(*nodes.ShaderNodeBsdfHair(component, color, offset, roughnessu, roughnessv, tangent, weight))
        return node.outputs[0].Shader

    @staticmethod
    def Refraction(distribution='BECKMANN', color=(1.0, 1.0, 1.0, 1.0), roughness=0.0, ior=1.45, normal=(0.0, 0.0, 0.0), weight=0.0):
        """The Refraction BSDF is used to add glossy refraction with sharp or microfacet distribution, used for materials that transmit light. For best results this node should be considered as a building block and not be used on its own, but rather mixed with a glossy node using a Fresnel factor. Otherwise it will give quite dark results at the edges for glossy refraction.
        #### Path
        - Shader > Refraction BSDF
        #### Properties:
        - `distribution`: `BECKMANN`, `SHARP`, `GGX`
        #### Outputs:
        - `#0 bsdf: Shader = None`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeBsdfRefraction.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/render/shader_nodes/shader/refraction.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeBsdfRefraction.html)
        """
        node = new_node(*nodes.ShaderNodeBsdfRefraction(distribution, color, roughness, ior, normal, weight))
        return node.outputs[0].Shader

    @staticmethod
    def Specular(base_color=(0.8, 0.8, 0.8, 1.0), specular=(0.03, 0.03, 0.03, 1.0), roughness=0.2, emissive_color=(0.0, 0.0, 0.0, 1.0), transparency=0.0, normal=(0.0, 0.0, 0.0), clear_coat=0.0, clear_coat_roughness=0.0, clear_coat_normal=(0.0, 0.0, 0.0), ambient_occlusion=0.0, weight=0.0):
        """Eevee Only
        #### Path
        - Shader > Specular BSDF
        #### Outputs:
        - `#0 bsdf: Shader = None`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeEeveeSpecular.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/render/shader_nodes/shader/specular_bsdf.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeEeveeSpecular.html)
        """
        node = new_node(*nodes.ShaderNodeEeveeSpecular(base_color, specular, roughness, emissive_color, transparency, normal, clear_coat, clear_coat_roughness, clear_coat_normal, ambient_occlusion, weight))
        return node.outputs[0].Shader

    @staticmethod
    def Toon(component='DIFFUSE', color=(0.8, 0.8, 0.8, 1.0), size=0.5, smooth=0.0, normal=(0.0, 0.0, 0.0), weight=0.0):
        """Cycles Only
        #### Path
        - Shader > Toon BSDF
        #### Properties:
        - `component`: `DIFFUSE`, `GLOSSY`
        #### Outputs:
        - `#0 bsdf: Shader = None`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeBsdfToon.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/render/shader_nodes/shader/toon.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeBsdfToon.html)
        """
        node = new_node(*nodes.ShaderNodeBsdfToon(component, color, size, smooth, normal, weight))
        return node.outputs[0].Shader

    @staticmethod
    def Translucent(color=(0.8, 0.8, 0.8, 1.0), normal=(0.0, 0.0, 0.0)):
        """The Translucent BSDF is used to add Lambertian diffuse transmission.
        #### Path
        - Shader > Translucent BSDF
        #### Outputs:
        - `#0 bsdf: Shader = None`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeBsdfTranslucent.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/render/shader_nodes/shader/translucent.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeBsdfTranslucent.html)
        """
        node = new_node(*nodes.ShaderNodeBsdfTranslucent(color, normal))
        return node.outputs[0].Shader

    @staticmethod
    def Transparent(color=(1.0, 1.0, 1.0, 1.0)):
        """The Transparent BSDF is used to add transparency without refraction, passing straight through the surface, as if there were no geometry there. Useful with alpha maps, for example. This shader affects light paths somewhat differently than other BSDFs. Note that only pure white transparent shaders are completely transparent.
        #### Path
        - Shader > Transparent BSDF
        #### Outputs:
        - `#0 bsdf: Shader = None`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeBsdfTransparent.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/render/shader_nodes/shader/transparent.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeBsdfTransparent.html)
        """
        node = new_node(*nodes.ShaderNodeBsdfTransparent(color))
        return node.outputs[0].Shader

    @staticmethod
    def Velvet(color=(0.8, 0.8, 0.8, 1.0), sigma=1.0, normal=(0.0, 0.0, 0.0)):
        """Cycles Only
        #### Path
        - Shader > Velvet BSDF
        #### Outputs:
        - `#0 bsdf: Shader = None`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeBsdfVelvet.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/render/shader_nodes/shader/velvet.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeBsdfVelvet.html)
        """
        node = new_node(*nodes.ShaderNodeBsdfVelvet(color, sigma, normal))
        return node.outputs[0].Shader


class Object(Socket):
    """Object socket of a node"""
    bl_idname = "NodeSocketObject"

    def __init__(self, bsocket: bpy.types.NodeSocket):
        super().__init__(bsocket)
        self._object = None

    @property
    def geometry(self):
        if self._object is None:
            self._object = self.object_info()
        return self._object.geometry

    @property
    def location(self):
        if self._object is None:
            self._object = self.object_info()
        return self._object.location

    @property
    def rotation(self):
        if self._object is None:
            self._object = self.object_info()
        return self._object.rotation

    @property
    def scale(self):
        if self._object is None:
            self._object = self.object_info()
        return self._object.scale

    def object_info(self, transform_space='ORIGINAL', as_instance=False):
        """The Object Info node gets information from objects. This can be useful to control parameters in the geometry node tree with an external object, either directly by using its geometry, or via its transformation properties.
        #### Path
        - Input > Scene > Object Info Node
        #### Properties
        - `transform_space`: `ORIGINAL`, `RELATIVE`
        #### Outputs:
        - `#0 location: Vector = (0.0, 0.0, 0.0)`
        - `#1 rotation: Vector = (0.0, 0.0, 0.0)`
        - `#2 scale: Vector = (0.0, 0.0, 0.0)`
        - `#3 geometry: Geometry = None`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeObjectInfo.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/scene/object_info.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeObjectInfo.html)
        """
        node = new_node(*nodes.GeometryNodeObjectInfo(transform_space, self, as_instance))
        ret = typing.NamedTuple("GeometryNodeObjectInfo", [("location", Vector), ("rotation", Vector), ("scale", Vector), ("geometry", Geometry)])
        return ret(node.outputs[0].Vector, node.outputs[1].Vector, node.outputs[2].Vector, node.outputs[3].Geometry)


class Collection(Socket):
    """Collection socket of a node"""
    bl_idname = "NodeSocketCollection"


class Texture(Socket):
    """Texture socket of a node"""
    bl_idname = "NodeSocketTexture"


class Material(Socket):
    """Material socket of a node"""
    bl_idname = "NodeSocketMaterial"

    def __init__(self, bsocket: bpy.types.NodeSocket) -> None:
        super().__init__(bsocket)
        self._index = None

    @property
    def index(self):
        """The Material Index node outputs which material in the list of materials of the geometry each element corresponds to. Currently the node supports mesh data, where material_index is a built-in attribute on faces.
        #### Path
        - Material > Material Index Node
        #### Outputs:
        - `#0 material_index: Integer = 0`

        ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeInputMaterialIndex.webp)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/material_index.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMaterialIndex.html)
        """
        if self._index is None:
            node = new_node(*nodes.GeometryNodeInputMaterialIndex())
            self._index = node.outputs[0].Integer
        return self._index

    def material_selection(self):
        """The Material Selection node provides a selection for meshes that use this material. Since the material_index is stored on each face, the output will be implicitly interpolated to a different domain when necessary. For example, every vertex connected to a selected face will be selected.
        #### Path
        - Material > Material Selection Node
        #### Outputs:
        - `#0 selection: Boolean = False`

        ![](https://docs.blender.org/manual/en/latest/_images/modeling_geometry-nodes_material_material-selection_node.png)

        [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/material/material_selection.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeMaterialSelection.html)
        """
        node = new_node(*nodes.GeometryNodeMaterialSelection(self))
        return node.outputs[0].Boolean


class Image(Socket):
    """Image socket of a node"""
    bl_idname = "NodeSocketImage"


def InputBool(boolean=False):
    """The Boolean node provides a Boolean value.
    #### Path
    - Input > Constant > Boolean Node

    #### Outputs:
    - `#0 boolean: Boolean = False`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_FunctionNodeInputBool.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/constant/boolean.html) [[API]](https://docs.blender.org/api/current/bpy.types.FunctionNodeInputBool.html)
    """
    node = new_node(*nodes.FunctionNodeInputBool(boolean))
    return node.outputs[0].Boolean


def InputColor(color=(0.0, 0.0, 0.0, 0.0)):
    """Geometry Nodes Tree: The Color node outputs the color value chosen with the color picker widget.
    #### Path
    - Input > Constant > Color Node

    #### Outputs:
    - `#0 color: Color = (0.0, 0.0, 0.0, 0.0)`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_FunctionNodeInputColor.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/constant/color.html) [[API]](https://docs.blender.org/api/current/bpy.types.FunctionNodeInputColor.html)
    """
    node = new_node(*nodes.FunctionNodeInputColor())
    node.outputs[0].default_value = color
    return node.outputs[0].Color


def InputRGB(color=(0.5, 0.5, 0.5, 1.0)):
    """Shader Tree: The RGB node outputs the color value chosen with the color picker widget.
    #### Path
    - Input > RGB Node
    #### Outputs:
    - `#0 color: Color = (0.5, 0.5, 0.5, 1.0)`

    ![](https://docs.blender.org/manual/en/latest/_images/compositing_node-types_CompositorNodeRGB.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/render/shader_nodes/input/rgb.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeRGB.html)
    """
    node = new_node(*nodes.ShaderNodeRGB())
    node.outputs[0].default_value = color
    return node.outputs[0].Color


def InputImage(image=None):
    """The Image node provides access to a image file which allows you to conveniently enter and switch images for multiple nodes in the tree.
    #### Path
    - Input > Constant > Image Node

    #### Outputs:
    - `#0 image: Image = None`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeImage.jpg)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/constant/image.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputImage.html)
    """
    node = new_node(*nodes.GeometryNodeInputImage(image))
    return node.outputs[0].Image


def InputInteger(integer=0):
    """The Integer node provides an integer value.
    #### Path
    - Input > Constant > Integer Node

    #### Outputs:
    - `#0 integer: Integer = 0`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_FunctionNodeInputInt.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/constant/integer.html) [[API]](https://docs.blender.org/api/current/bpy.types.FunctionNodeInputInt.html)
    """
    node = new_node(*nodes.FunctionNodeInputInt(integer))
    return node.outputs[0].Integer


def InputMaterial(material=None):
    """The Material input node outputs a single material. It can be connected to other material sockets to make using the same material name in multiple places more convenient.
    #### Path
    - Input > Constant > Material Node

    #### Outputs:
    - `#0 material: Material = None`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeInputMaterial.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/constant/material.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputMaterial.html)
    """
    node = new_node(*nodes.GeometryNodeInputMaterial(material))
    return node.outputs[0].Material


def InputString(string=''):
    """The String input node creates a single string. It can be connected to attribute name sockets to make using the same attribute name in multiple places more convenient.
    #### Path
    - Input > Constant > String Node

    #### Outputs:
    - `#0 string: String = ""`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_FunctionNodeInputString.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/constant/string.html) [[API]](https://docs.blender.org/api/current/bpy.types.FunctionNodeInputString.html)
    """
    node = new_node(*nodes.FunctionNodeInputString(string))
    return node.outputs[0].String


def StringToCurves(string='', align_x='LEFT', align_y='TOP_BASELINE', overflow='OVERFLOW', pivot_mode='BOTTOM_LEFT', font=None, size=1.0, character_spacing=1.0, word_spacing=1.0, line_spacing=1.0, text_box_width=0.0, text_box_height=0.0):
    """The String to Curves converts a string to curve instances. Each unique character used in the string is converted to a curve once, and further uses of that character are more instances of the same geometry.
    #### Path
    - Utilities > Text > String to Curves Node
    #### Properties:
    - `align_x`: `LEFT`, `CENTER`, `RIGHT`, `JUSTIFY`, `FLUSH`
    - `align_y`: `TOP_BASELINE`, `TOP`, `MIDDLE`, `BOTTOM_BASELINE`, `BOTTOM`
    - `overflow`: `OVERFLOW`, `SCALE_TO_FIT`, `TRUNCATE`
    - `pivot_mode`: `BOTTOM_LEFT`, `MIDPOINT`, `TOP_LEFT`, `TOP_CENTER`, `TOP_RIGHT`, `BOTTOM_CENTER`, `BOTTOM_RIGHT`
    #### Outputs:
    - `#0 curve_instances: Geometry = None`
    - `#1 remainder: String = ""`
    - `#2 line: Integer = 0`
    - `#3 pivot_point: Vector = (0.0, 0.0, 0.0)`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeStringToCurves.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/text/string_to_curves.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeStringToCurves.html)
    """
    if type(font) == str:
        font = bpy.data.fonts.get(font)
    node = new_node(*nodes.GeometryNodeStringToCurves(align_x, align_y, overflow, pivot_mode, font, string, size, character_spacing, word_spacing, line_spacing, text_box_width, text_box_height))
    ret = typing.NamedTuple("GeometryNodeStringToCurves", [("curve_instances", Instances), ("remainder", String), ("line", Integer), ("pivot_point", Vector)])
    return ret(node.outputs[0].Instances, node.outputs[1].String, node.outputs[2].Integer, node.outputs[3].Vector)


def InputValue(value=0.0):
    """The Value Node is a simple node to input numerical values to other nodes in the tree.
    #### Path
    - Input > Constant > Value Node

    #### Outputs:
    - `#0 value: Float = 0.0`

    ![](https://docs.blender.org/manual/en/latest/_images/compositing_node-types_CompositorNodeValue.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/constant/value.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeValue.html)
    """
    node = new_node(*nodes.ShaderNodeValue())
    node.outputs[0].default_value = value
    return node.outputs[0].Float


def InputFloat(value=0.0):
    """The Value Node is a simple node to input numerical values to other nodes in the tree.
    #### Path
    - Input > Constant > Value Node

    #### Outputs:
    - `#0 value: Float = 0.0`

    ![](https://docs.blender.org/manual/en/latest/_images/compositing_node-types_CompositorNodeValue.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/constant/value.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeValue.html)
    """
    node = new_node(*nodes.ShaderNodeValue())
    node.outputs[0].default_value = value
    return node.outputs[0].Float


def InputVector(vector=(0.0, 0.0, 0.0)):
    """The Vector input node creates a single vector.
    #### Path
    - Input > Constant > Vector Node

    #### Outputs:
    - `#0 vector: Vector = (0.0, 0.0, 0.0)`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_FunctionNodeInputVector.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/constant/vector.html) [[API]](https://docs.blender.org/api/current/bpy.types.FunctionNodeInputVector.html)
    """
    node = new_node(*nodes.FunctionNodeInputVector(vector))
    return node.outputs[0].Vector


def CollectionInfo(transform_space='ORIGINAL', collection=None, separate_children=False, reset_children=False):
    """The Collection Info node gets information from collections. This can be useful to control parameters in the geometry node tree with an external collection.
    #### Path
    - Input > Scene > Collection Info Node
    #### Properties
    - `transform_space`: `ORIGINAL`, `RELATIVE`
    #### Outputs:
    - `#0 instances: Geometry = None`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeCollectionInfo.jpeg)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/scene/collection_info.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeCollectionInfo.html)
    """
    node = new_node(*nodes.GeometryNodeCollectionInfo(transform_space, collection, separate_children, reset_children))
    return node.outputs[0].Instances


def ImageInfo(image=None, frame=0):
    """The Image Info node gets information from image and animation. This can be useful to generate parameters in the geometry node for arbitrary images. Image information can be either general or frame-specific.
    #### Path
    - Input > Scene > Image Info Node

    #### Outputs:
    - `#0 width: Integer = 0`
    - `#1 height: Integer = 0`
    - `#2 has_alpha: Boolean = False`
    - `#3 frame_count: Integer = 0`
    - `#4 fps: Float = 0.0`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeImageInfo.jpg)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/scene/image_info.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeImageInfo.html)
    """
    node = new_node(*nodes.GeometryNodeImageInfo(image, frame))
    ret = typing.NamedTuple("GeometryNodeImageInfo", [("width", Integer), ("height", Integer), ("has_alpha", Boolean), ("frame_count", Integer), ("fps", Float)])
    return ret(node.outputs[0].Integer, node.outputs[1].Integer, node.outputs[2].Boolean, node.outputs[3].Integer, node.outputs[4].Float)


def IsViewport():
    """The Is Viewport node outputs true when geometry nodes are evaluated for the viewport. For the final render the node outputs false.
    #### Path
    - Input > Scene > Is Viewport Node

    #### Outputs:
    - `#0 is_viewport: Boolean = False`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeIsViewport.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/scene/is_viewport.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeIsViewport.html)
    """
    node = new_node(*nodes.GeometryNodeIsViewport())
    return node.outputs[0].Boolean


def ObjectInfo(transform_space='ORIGINAL', object=None, as_instance=False):
    """The Object Info node gets information from objects. This can be useful to control parameters in the geometry node tree with an external object, either directly by using its geometry, or via its transformation properties.
    #### Path
    - Input > Scene > Object Info Node
    #### Properties
    - `transform_space`: `ORIGINAL`, `RELATIVE`
    #### Outputs:
    - `#0 location: Vector = (0.0, 0.0, 0.0)`
    - `#1 rotation: Vector = (0.0, 0.0, 0.0)`
    - `#2 scale: Vector = (0.0, 0.0, 0.0)`
    - `#3 geometry: Geometry = None`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeObjectInfo.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/scene/object_info.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeObjectInfo.html)
    """
    node = new_node(*nodes.GeometryNodeObjectInfo(transform_space, object, as_instance))
    ret = typing.NamedTuple("GeometryNodeObjectInfo", [("location", Vector), ("rotation", Vector), ("scale", Vector), ("geometry", Geometry)])
    return ret(node.outputs[0].Vector, node.outputs[1].Vector, node.outputs[2].Vector, node.outputs[3].Geometry)


def SelfObject():
    """The Self Object node outputs the object that contains the geometry nodes modifier currently being executed. This can be used to retrieve the original transforms.
    #### Path
    - Input > Scene > Self Object Node

    #### Outputs:
    - `#0 self_object: Object = None`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeSelfObject.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/input/scene/self_object.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeSelfObject.html)
    """
    node = new_node(*nodes.GeometryNodeSelfObject())
    return node.outputs[0].Object


def GeometryNodeViewer(data_type='FLOAT', domain='AUTO', geometry=None, value=0.0, value_001=(0.0, 0.0, 0.0), value_002=(0.0, 0.0, 0.0, 0.0), value_003=0, value_004=False):
    """The Viewer node allows viewing data from inside a geometry node group in the Spreadsheet Editor and the 3D Viewport.
    #### Path
    - Output > Viewer Node
    #### Properties
    - `data_type`: `FLOAT`, `INT`, `FLOAT_VECTOR`, `FLOAT_COLOR`, `BOOLEAN`
    - `domain`: `AUTO`, `POINT`, `EDGE`, `FACE`, `CORNER`, `CURVE`, `INSTANCE`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeViewer.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/output/viewer.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeViewer.html)
    """
    node = new_node(*nodes.GeometryNodeViewer(data_type, domain, geometry, value, value_001, value_002, value_003, value_004))
    return node


def ViewFloat(domain="AUTO", geometry=None, value=0.0):
    """The Viewer node allows viewing data from inside a geometry node group in the Spreadsheet Editor and the 3D Viewport.
    #### Path
    - Output > Viewer Node
    #### Properties
    - `domain`: `AUTO`, `POINT`, `EDGE`, `FACE`, `CORNER`, `CURVE`, `INSTANCE`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeViewer.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/output/viewer.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeViewer.html)
    """
    node = new_node(*nodes.GeometryNodeViewer("FLOAT", domain, geometry, value))
    return node


def ViewVector(domain="AUTO", geometry=None, value=(0.0, 0.0, 0.0)):
    """The Viewer node allows viewing data from inside a geometry node group in the Spreadsheet Editor and the 3D Viewport.
    #### Path
    - Output > Viewer Node
    #### Properties
    - `domain`: `AUTO`, `POINT`, `EDGE`, `FACE`, `CORNER`, `CURVE`, `INSTANCE`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeViewer.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/output/viewer.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeViewer.html)
    """
    node = new_node(*nodes.GeometryNodeViewer("FLOAT_VECTOR", domain, geometry, value_001=value))
    return node


def ViewInteger(domain="AUTO", geometry=None, value=0):
    """The Viewer node allows viewing data from inside a geometry node group in the Spreadsheet Editor and the 3D Viewport.
    #### Path
    - Output > Viewer Node
    #### Properties
    - `domain`: `AUTO`, `POINT`, `EDGE`, `FACE`, `CORNER`, `CURVE`, `INSTANCE`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeViewer.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/output/viewer.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeViewer.html)
    """
    node = new_node(*nodes.GeometryNodeViewer("INT", domain, geometry, value_003=value))
    return node


def ViewColor(domain="AUTO", geometry=None, value=(0.0, 0.0, 0.0, 0.0)):
    """The Viewer node allows viewing data from inside a geometry node group in the Spreadsheet Editor and the 3D Viewport.
    #### Path
    - Output > Viewer Node
    #### Properties
    - `domain`: `AUTO`, `POINT`, `EDGE`, `FACE`, `CORNER`, `CURVE`, `INSTANCE`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeViewer.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/output/viewer.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeViewer.html)
    """
    node = new_node(*nodes.GeometryNodeViewer("FLOAT_COLOR", domain, geometry, value_002=value))
    return node


def ViewBoolean(domain="AUTO", geometry=None, value=False):
    """The Viewer node allows viewing data from inside a geometry node group in the Spreadsheet Editor and the 3D Viewport.
    #### Path
    - Output > Viewer Node
    #### Properties
    - `domain`: `AUTO`, `POINT`, `EDGE`, `FACE`, `CORNER`, `CURVE`, `INSTANCE`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeViewer.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/output/viewer.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeViewer.html)
    """
    node = new_node(*nodes.GeometryNodeViewer("BOOLEAN", domain, geometry, value_004=value))
    return node


def BrickTexture(offset=0.5, offset_frequency=2, squash=1.0, squash_frequency=2, texture_mapping=None, vector: Vector = None, color1=(0.8, 0.8, 0.8, 1.0), color2=(0.2, 0.2, 0.2, 1.0), mortar=(0.0, 0.0, 0.0, 1.0), scale=5.0, mortar_size=0.02, mortar_smooth=0.1, bias=0.0, brick_width=0.5, row_height=0.25):
    """The Brick Texture is used to add a procedural texture producing bricks.
    #### Path
    - Texture > Brick Texture Node
    #### Outputs:
    - `#0 color: Color = (0.0, 0.0, 0.0, 0.0)`
    - `#1 fac: Float = 0.0`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeTexBrick.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/brick.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexBrick.html)
    """
    node = new_node(*nodes.ShaderNodeTexBrick(None, offset, offset_frequency, squash, squash_frequency, texture_mapping, vector, color1, color2, mortar, scale, mortar_size, mortar_smooth, bias, brick_width, row_height))
    ret = typing.NamedTuple("ShaderNodeTexBrick", [("color", Color), ("fac", Float)])
    return ret(node.outputs[0].Color, node.outputs[1].Float)


def CheckerTexture(vector: Vector = None, color1=(0.8, 0.8, 0.8, 1.0), color2=(0.2, 0.2, 0.2, 1.0), scale=5.0):
    """The Checker Texture is used to add a checkerboard texture.
    #### Path
    - Texture > Checker Texture Node
    #### Outputs:
    - `#0 color: Color = (0.0, 0.0, 0.0, 0.0)`
    - `#1 fac: Float = 0.0`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeTexChecker.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/checker.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexChecker.html)
    """
    node = new_node(*nodes.ShaderNodeTexChecker(None, None, vector, color1, color2, scale))
    ret = typing.NamedTuple("ShaderNodeTexChecker", [("color", Color), ("fac", Float)])
    return ret(node.outputs[0].Color, node.outputs[1].Float)


def GradientTexture(gradient_type='LINEAR', vector: Vector = None):
    """The Gradient Texture node generates interpolated color and intensity values based on the input vector.
    #### Path
    - Texture > Gradient Texture Node
    #### Properties:
    - `gradient_type`: `LINEAR`, `QUADRATIC`, `EASING`, `DIAGONAL`, `SPHERICAL`, `QUADRATIC_SPHERE`, `RADIAL`
    #### Outputs:
    - `#0 color: Color = (0.0, 0.0, 0.0, 0.0)`
    - `#1 fac: Float = 0.0`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeTexGradient.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/gradient.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexGradient.html)
    """
    node = new_node(*nodes.ShaderNodeTexGradient(gradient_type, None, None, vector))
    ret = typing.NamedTuple("ShaderNodeTexGradient", [("color", Color), ("fac", Float)])
    return ret(node.outputs[0].Color, node.outputs[1].Float)


def ImageTextureGeo(extension='REPEAT', interpolation='Linear', image=None, vector: Vector = None, frame=0):
    """The Image Texture node is used to add an image file as a texture. The image data is sampled with the input Vector and outputs a Color and Alpha value.
    #### Path
    - Texture > Image Texture Node
    #### Properties:
    - `extension`: `REPEAT`, `EXTEND`, `CLIP`, `MIRROR`
    - `interpolation`: `Linear`, `Closest`, `Cubic`
    #### Outputs:
    - `#0 color: Color = (0.0, 0.0, 0.0, 0.0)`
    - `#1 alpha: Float = 0.0`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeImageTexture.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/image.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeImageTexture.html)
    """
    node = new_node(*nodes.GeometryNodeImageTexture(extension, interpolation, image, vector, frame))
    ret = typing.NamedTuple("GeometryNodeImageTexture", [("color", Color), ("alpha", Float)])
    return ret(node.outputs[0].Color, node.outputs[1].Float)


def MagicTexture(color_mapping=None, texture_mapping=None, turbulence_depth=2, vector: Vector = None, scale=5.0, distortion=1.0):
    """The Magic Texture node is used to add a psychedelic color texture.
    #### Path
    - Texture > Magic Texture Node
    #### Outputs:
    - `#0 color: Color = (0.0, 0.0, 0.0, 0.0)`
    - `#1 fac: Float = 0.0`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeTexMagic.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/magic.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexMagic.html)
    """
    node = new_node(*nodes.ShaderNodeTexMagic(color_mapping, texture_mapping, turbulence_depth, vector, scale, distortion))
    ret = typing.NamedTuple("ShaderNodeTexMagic", [("color", Color), ("fac", Float)])
    return ret(node.outputs[0].Color, node.outputs[1].Float)


def MusgraveTexture(musgrave_dimensions='3D', musgrave_type='FBM', color_mapping=None, texture_mapping=None, vector: Vector = None, w=0.0, scale=5.0, detail=2.0, dimension=2.0, lacunarity=2.0, offset=0.0, gain=1.0):
    """The Musgrave Texture node evaluates a fractal Perlin noise at the input texture coordinates. Unlike the Noise Texture, which is also a fractal Perlin noise, the Musgrave Texture allows greater control over how octaves are combined.
    #### Path
    - Texture > Musgrave Texture Node
    #### Properties:
    - `musgrave_dimensions`: `3D`, `1D`, `2D`, `4D`
    - `musgrave_type`: `FBM`, `MULTIFRACTAL`, `RIDGED_MULTIFRACTAL`, `HYBRID_MULTIFRACTAL`, `HETERO_TERRAIN`
    #### Outputs:
    - `#0 fac: Float = 0.0`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeTexMusgrave.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/musgrave.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexMusgrave.html)
    """
    node = new_node(*nodes.ShaderNodeTexMusgrave(musgrave_dimensions, musgrave_type, color_mapping, texture_mapping, vector, w, scale, detail, dimension, lacunarity, offset, gain))
    ret = typing.NamedTuple("ShaderNodeTexMusgrave", [("fac", Float)])
    return ret(node.outputs[0].Float)


def NoiseTexture(noise_dimensions='3D', vector: Vector = None, w=0.0, scale=5.0, detail=2.0, roughness=0.5, distortion=0.0):
    """The Noise Texture node evaluates a fractal Perlin noise at the input texture coordinates.
    #### Path
    - Texture > Noise Texture Node
    #### Properties:
    - `noise_dimensions`: `3D`, `1D`, `2D`, `4D`
    #### Outputs:
    - `#0 fac: Float = 0.0`
    - `#1 color: Color = (0.0, 0.0, 0.0, 0.0)`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeTexNoise.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/noise.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexNoise.html)
    """
    node = new_node(*nodes.ShaderNodeTexNoise(noise_dimensions, None, None, vector, w, scale, detail, roughness, distortion))
    ret = typing.NamedTuple("ShaderNodeTexNoise", [("fac", Float), ("color", Color)])
    return ret(node.outputs[0].Float, node.outputs[1].Color)


def VoronoiTexture(voronoi_dimensions='3D', feature='F1', distance='EUCLIDEAN', color_mapping=None, texture_mapping=None, vector: Vector = None, w=0.0, scale=5.0, smoothness=1.0, exponent=0.5, randomness=1.0):
    """The Voronoi Texture node evaluates a Worley Noise at the input texture coordinates.
    #### Path
    - Texture > Voronoi Texture Node
    #### Properties:
    - `voronoi_dimensions`: `3D`, `1D`, `2D`, `4D`
    - `feature`: `F1`, `F2`, `SMOOTH_F1`, `DISTANCE_TO_EDGE`, `N_SPHERE_RADIUS`
    - `distance`: `EUCLIDEAN`, `MANHATTAN`, `CHEBYCHEV`, `MINKOWSKI`
    #### Outputs:
    - `#0 distance: Float = 0.0`
    - `#1 color: Color = (0.0, 0.0, 0.0, 0.0)`
    - `#2 position: Vector = (0.0, 0.0, 0.0)`
    - `#3 w: Float = 0.0`
    - `#4 radius: Float = 0.0`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeTexVoronoi.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/voronoi.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexVoronoi.html)
    """
    node = new_node(*nodes.ShaderNodeTexVoronoi(distance, feature, voronoi_dimensions, color_mapping, texture_mapping, vector, w, scale, smoothness, exponent, randomness))
    ret = typing.NamedTuple("ShaderNodeTexVoronoi", [("distance", Float), ("color", Color), ("position", Vector), ("w", Float), ("radius", Float)])
    return ret(node.outputs[0].Float, node.outputs[1].Color, node.outputs[2].Vector, node.outputs[3].Float, node.outputs[4].Float)


def WaveTexture(wave_type='BANDS', bands_direction='X', rings_direction='X', wave_profile='SIN', vector: Vector = None, scale=5.0, distortion=0.0, detail=2.0, detail_scale=1.0, detail_roughness=0.5, phase_offset=0.0):
    """The Wave Texture node adds procedural bands or rings with noise distortion.
    #### Path
    - Texture > Wave Texture Node
    #### Properties:
    - `bands_direction`: `X`, `Y`, `Z`, `DIAGONAL`
    - `rings_direction`: `X`, `Y`, `Z`, `SPHERICAL`
    - `wave_profile`: `SIN`, `SAW`, `TRI`
    - `wave_type`: `BANDS`, `RINGS`
    #### Outputs:
    - `#0 color: Color = (0.0, 0.0, 0.0, 0.0)`
    - `#1 fac: Float = 0.0`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeTexWave.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/wave.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexWave.html)
    """
    node = new_node(*nodes.ShaderNodeTexWave(bands_direction, rings_direction, wave_profile, wave_type, None, None, vector, scale, distortion, detail, detail_scale, detail_roughness, phase_offset))
    ret = typing.NamedTuple("ShaderNodeTexWave", [("color", Color), ("fac", Float)])
    return ret(node.outputs[0].Color, node.outputs[1].Float)


def WaveTextureBands(bands_direction='X', wave_profile='SIN', vector: Vector = None, scale=5.0, distortion=0.0, detail=2.0, detail_scale=1.0, detail_roughness=0.5, phase_offset=0.0):
    """The Wave Texture node adds procedural bands or rings with noise distortion.
    #### Path
    - Texture > Wave Texture Node
    #### Properties:
    - `bands_direction`: `X`, `Y`, `Z`, `DIAGONAL`
    - `wave_profile`: `SIN`, `SAW`, `TRI`
    #### Outputs:
    - `#0 color: Color = (0.0, 0.0, 0.0, 0.0)`
    - `#1 fac: Float = 0.0`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeTexWave.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/wave.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexWave.html)
    """
    node = new_node(*nodes.ShaderNodeTexWave(bands_direction, "X", wave_profile, "BANDS", None, None, vector, scale, distortion, detail, detail_scale, detail_roughness, phase_offset))
    ret = typing.NamedTuple("ShaderNodeTexWave", [("color", Color), ("fac", Float)])
    return ret(node.outputs[0].Color, node.outputs[1].Float)


def WaveTextureRings(rings_direction='X', wave_profile='SIN', vector: Vector = None, scale=5.0, distortion=0.0, detail=2.0, detail_scale=1.0, detail_roughness=0.5, phase_offset=0.0):
    """The Wave Texture node adds procedural bands or rings with noise distortion.
    #### Path
    - Texture > Wave Texture Node
    #### Properties:
    - `rings_direction`: `X`, `Y`, `Z`, `SPHERICAL`
    - `wave_profile`: `SIN`, `SAW`, `TRI`
    #### Outputs:
    - `#0 color: Color = (0.0, 0.0, 0.0, 0.0)`
    - `#1 fac: Float = 0.0`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeTexWave.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/wave.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexWave.html)
    """
    node = new_node(*nodes.ShaderNodeTexWave("X", rings_direction, wave_profile, "RINGS", None, None, vector, scale, distortion, detail, detail_scale, detail_roughness, phase_offset))
    ret = typing.NamedTuple("ShaderNodeTexWave", [("color", Color), ("fac", Float)])
    return ret(node.outputs[0].Color, node.outputs[1].Float)


def WhiteNoiseTexture(noise_dimensions='3D', vector: Vector = None, w=0.0):
    """The White Noise Texture node returns a random number based on an input Seed. The seed can be a number, a 2D vector, a 3D vector, or a 4D vector; depending on the Dimensions property. The output number ranges between zero and one.
    #### Path
    - Texture > White Noise Texture Node
    #### Properties:
    - `noise_dimensions`: `3D`, `1D`, `2D`, `4D`
    #### Outputs:
    - `#0 value: Float = 0.0`
    - `#1 color: Color = (0.0, 0.0, 0.0, 0.0)`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeTexWhiteNoise.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/texture/white_noise.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexWhiteNoise.html)
    """
    node = new_node(*nodes.ShaderNodeTexWhiteNoise(noise_dimensions, vector, w))
    ret = typing.NamedTuple("ShaderNodeTexWhiteNoise", [("value", Float), ("color", Color)])
    return ret(node.outputs[0].Float, node.outputs[1].Color)


def ColorRamp(fac=0.5):
    """The Color Ramp Node is used for mapping values to colors with the use of a gradient.
    #### Path
    - Utilities > Color > Color Ramp Node
    #### Outputs:
    - `#0 color: Color = (0.0, 0.0, 0.0, 0.0)`
    - `#1 alpha: Float = 0.0`

    ![](https://docs.blender.org/manual/en/latest/_images/compositing_node-types_CompositorNodeValToRGB.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/color/color_ramp.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeValToRGB.html)
    """
    node = new_node(*nodes.ShaderNodeValToRGB(None, fac))
    ret = typing.NamedTuple("ShaderNodeValToRGB", [("color", Color), ("alpha", Float)])
    return ret(node.outputs[0].Color, node.outputs[1].Float)


def CombineColor(red=0.0, green=0.0, blue=0.0, alpha=1.0, mode='RGB'):
    """The Combine Color Node combines an image from its composite color channels. The node can combine multiple Color Models depending on the Mode property.
    #### Path
    - Utilities > Color > Combine Color Node
    #### Properties:
    - `mode`: `RGB`, `HSV`, `HSL`
    #### Outputs:
    - `#0 color: Color = (0.0, 0.0, 0.0, 0.0)`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_FunctionNodeCombineColor.png)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/color/combine_color.html) [[API]](https://docs.blender.org/api/current/bpy.types.FunctionNodeCombineColor.html)
    """
    node = new_node(*nodes.FunctionNodeCombineColor(mode, red, green, blue, alpha))
    return node.outputs[0].Color


def MixFloat(factor_float=0.5, a_float=0.0, b_float=0.0, clamp_factor=True):
    """The Mix Node mixes values, colors and vectors inputs using a factor to control the amount of interpolation. The Color mode has additional blending modes.
    #### Path
    - Utilities > Math > Mix Node
    #### Outputs:
    - `#0 result_float: Float = 0.0`

    ![](https://docs.blender.org/manual/en/latest/_images/render_shader-nodes_shader_mix_node.jpg)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/color/mix_rgb.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html)
    """
    node = new_node(*nodes.ShaderNodeMix(data_type='FLOAT', clamp_factor=clamp_factor, factor_float=factor_float, a_float=a_float, b_float=b_float))
    return node.outputs[0].Float


def MixVector(a_vector=(0.0, 0.0, 0.0), b_vector=(0.0, 0.0, 0.0), factor_float=0.5, factor_vector=(0.5, 0.5, 0.5), factor_mode="UNIFORM", clamp_factor=True):
    """The Mix Node mixes images by working on the individual and corresponding pixels of the two input images. Called “Mix Color” in the shader, geometry, and texture context.
    #### Path
    - Utilities > Vector > Mix Node
    #### Outputs:
    - `#1 result_vector: Vector = (0.0, 0.0, 0.0)`

    ![](https://docs.blender.org/manual/en/latest/_images/render_shader-nodes_shader_mix_node.jpg)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/color/mix_rgb.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html)
    """
    node = new_node(*nodes.ShaderNodeMix(data_type="VECTOR", factor_mode=factor_mode, clamp_factor=clamp_factor, factor_float=factor_float, factor_vector=factor_vector, a_vector=a_vector, b_vector=b_vector))
    return node.outputs[1].Vector


def MixColor(a_color=(0.5, 0.5, 0.5, 1.0), b_color=(0.5, 0.5, 0.5, 1.0), blend_type="MIX", clamp_factor=True, clamp_result=False, factor_float=0.5):
    """The Mix Node mixes images by working on the individual and corresponding pixels of the two input images. Called “Mix Color” in the shader, geometry, and texture context.
    #### Path
    - Utilities > Color > Mix Node
    #### Outputs:
    - `#2 result_color: Color = (0.0, 0.0, 0.0, 0.0)`

    ![](https://docs.blender.org/manual/en/latest/_images/render_shader-nodes_shader_mix_node.jpg)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/color/mix_rgb.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeMix.html)
    """
    node = new_node(*nodes.ShaderNodeMix(blend_type, "RGBA", clamp_factor=clamp_factor, clamp_result=clamp_result, factor_float=factor_float, a_color=a_color, b_color=b_color))
    return node.outputs[1].Vector


def ShaderNodeRGBCurve(mapping=None, fac=1.0, color=(1.0, 1.0, 1.0, 1.0)):
    """The RGB Curves Node allows color corrections for each color channel and levels adjustments in the compositing context.
    #### Path
    - Utilities > Color > RGB Curves Node
    #### Outputs:
    - `#0 color: Color = (0.0, 0.0, 0.0, 0.0)`

    ![](https://docs.blender.org/manual/en/latest/_images/compositing_node-types_CompositorNodeCurveRGB.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/color/rgb_curves.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeRGBCurve.html)
    """
    node = new_node(*nodes.ShaderNodeRGBCurve(mapping, fac, color))
    return node.outputs[0].Color


def SeparateColor(color=(1.0, 1.0, 1.0, 1.0), mode='RGB'):
    """The Separate Color Node splits an image into its composite color channels. The node can output multiple Color Models depending on the Mode property.
    #### Path
    - Utilities > Color > Separate Color Node
    #### Properties:
    - `mode`: `RGB`, `HSV`, `HSL`
    #### Outputs:
    - `#0 red: Float = 0.0`
    - `#1 green: Float = 0.0`
    - `#2 blue: Float = 0.0`
    - `#3 alpha: Float = 0.0`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_FunctionNodeSeparateColor.png)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/color/separate_color.html) [[API]](https://docs.blender.org/api/current/bpy.types.FunctionNodeSeparateColor.html)
    """
    node = new_node(*nodes.FunctionNodeSeparateColor(mode, color))
    ret = typing.NamedTuple("FunctionNodeSeparateColor", [("red", Float), ("green", Float), ("blue", Float), ("alpha", Float)])
    return ret(node.outputs[0].Float, node.outputs[1].Float, node.outputs[2].Float, node.outputs[3].Float)


def CombineXYZ(x=0.0, y=0.0, z=0.0):
    """The Combine XYZ Node combines a vector from its individual components.
    #### Path
    - Utilities > Vector > Combine XYZ Node
    #### Outputs:
    - `#0 vector: Vector = (0.0, 0.0, 0.0)`

    ![](https://docs.blender.org/manual/en/latest/_images/compositing_node-types_CompositorNodeCombineXYZ.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/combine_xyz.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeCombineXYZ.html)
    """
    node = new_node(*nodes.ShaderNodeCombineXYZ(x, y, z))
    return node.outputs[0].Vector


def FloatMath(operation='ADD', use_clamp=False, value=0.5, value_001=0.5, value_002=0.5):
    """The Math Node performs math operations.
    #### Path
    - Utilities > Math > Math Node
    #### Properties:
    - `operation`: `ADD`, `SUBTRACT`, `MULTIPLY`, `DIVIDE`, `MULTIPLY_ADD`, `POWER`, `LOGARITHM`, `SQRT`, `INVERSE_SQRT`, `ABSOLUTE`, `EXPONENT`, `MINIMUM`, `MAXIMUM`, `LESS_THAN`, `GREATER_THAN`, `SIGN`, `COMPARE`, `SMOOTH_MIN`, `SMOOTH_MAX`, `ROUND`, `FLOOR`, `CEIL`, `TRUNC`, `FRACT`, `MODULO`, `WRAP`, `SNAP`, `PINGPONG`, `SINE`, `COSINE`, `TANGENT`, `ARCSINE`, `ARCCOSINE`, `ARCTANGENT`, `ARCTAN2`, `SINH`, `COSH`, `TANH`, `RADIANS`, `DEGREES`
    #### Outputs:
    - `#0 value: Float = 0.0`

    ![](https://docs.blender.org/manual/en/latest/_images/compositing_node-types_CompositorNodeMath.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/math.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeMath.html)
    """
    node = new_node(*nodes.ShaderNodeMath(operation, use_clamp, value, value_001, value_002))
    return node.outputs[0].Float


def VectorMath(operation='ADD', vector=(0.0, 0.0, 0.0), vector_001=(0.0, 0.0, 0.0), vector_002=(0.0, 0.0, 0.0), scale=1.0):
    """The Vector Math node performs the selected math operation on the input vectors.
    #### Path
    - Utilities > Vector > Vector Math Node
    #### Properties:
    - `operation`: `ADD`, `SUBTRACT`, `MULTIPLY`, `DIVIDE`, `MULTIPLY_ADD`, `CROSS_PRODUCT`, `PROJECT`, `REFLECT`, `REFRACT`, `FACEFORWARD`, `DOT_PRODUCT`, `DISTANCE`, `LENGTH`, `SCALE`, `NORMALIZE`, `ABSOLUTE`, `MINIMUM`, `MAXIMUM`, `FLOOR`, `CEIL`, `FRACTION`, `MODULO`, `WRAP`, `SNAP`, `SINE`, `COSINE`, `TANGENT`
    #### Outputs:
    - `#0 vector: Vector = (0.0, 0.0, 0.0)`
    - `#1 value: Float = 0.0`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeVectorMath.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/vector/vector_math.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorMath.html)
    """
    node = new_node(*nodes.ShaderNodeVectorMath(operation, vector, vector_001, vector_002, scale))
    ret = typing.NamedTuple("ShaderNodeVectorMath", [("vector", Vector), ("value", Float)])
    return ret(node.outputs[0].Vector, node.outputs[1].Float)


def BooleanMath(operation='AND', boolean=False, boolean_001=False):
    """The Boolean Math node performs a basic logical operation on its inputs.
    #### Path
    - Utilities > Math > Boolean Math Node
    #### Properties:
    - `operation`: `AND`, `OR`, `NOT`, `NAND`, `NOR`, `XNOR`, `XOR`, `IMPLY`, `NIMPLY`
    #### Outputs:
    - `#0 boolean: Boolean = False`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_FunctionNodeBooleanMath.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/boolean_math.html) [[API]](https://docs.blender.org/api/current/bpy.types.FunctionNodeBooleanMath.html)
    """
    node = new_node(*nodes.FunctionNodeBooleanMath(operation, boolean, boolean_001))
    return node.outputs[0].Boolean


def Compare(data_type='FLOAT', mode='ELEMENT', operation='GREATER_THAN', a=0.0, b=0.0, a_int=0, b_int=0, a_vec3=(0.0, 0.0, 0.0), b_vec3=(0.0, 0.0, 0.0), a_col=(0.0, 0.0, 0.0, 0.0), b_col=(0.0, 0.0, 0.0, 0.0), a_str='', b_str='', c=0.9, angle=math.radians(5.0), epsilon=0.001):
    # TODO
    """The Compare node takes two inputs and does an operation to determine whether they are similar. The node can work on all generic data types, and has modes for vectors that contain more complex comparisons, which can help to reduce the number of necessary nodes, and make a node tree more readable.
    #### Path
    - Utilities > Math > Compare Node
    #### Properties:
    - `data_type`: `FLOAT`, `INT`, `VECTOR`, `STRING`, `RGBA`
    - `mode`: `ELEMENT`, `LENGTH`, `AVERAGE`, `DOT_PRODUCT`, `DIRECTION`
    - `operation`: `GREATER_THAN`, `LESS_THAN`, `LESS_EQUAL`, `GREATER_EQUAL`, `EQUAL`, `NOT_EQUAL`
    #### Outputs:
    - `#0 result: Boolean = False`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_FunctionNodeCompare.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/math/compare.html) [[API]](https://docs.blender.org/api/current/bpy.types.FunctionNodeCompare.html)
    """
    node = new_node(*nodes.FunctionNodeCompare(data_type, mode, operation, a, b, a_int, b_int, a_vec3, b_vec3, a_col, b_col, a_str, b_str, c, angle, epsilon))
    return node.outputs[0].Boolean


def Switch(input_type='GEOMETRY', switch=False, switch_001=False, false=0.0, true=0.0, false_001=0, true_001=0, false_002=False, true_002=True, false_003=(0.0, 0.0, 0.0), true_003=(0.0, 0.0, 0.0), false_004=(0.8, 0.8, 0.8, 1.0), true_004=(0.8, 0.8, 0.8, 1.0), false_005='', true_005='', false_006=None, true_006=None, false_007=None, true_007=None, false_008=None, true_008=None, false_009=None, true_009=None, false_010=None, true_010=None, false_011=None, true_011=None):
    # TODO
    """The Switch node outputs one of two inputs depending on a condition. Only the input that is passed through the node is computed.
    #### Path
    - Utilities > Switch Node
    #### Properties:
    - `input_type`: `GEOMETRY`, `FLOAT`, `INT`, `BOOLEAN`, `VECTOR`, `STRING`, `RGBA`, `OBJECT`, `IMAGE`, `COLLECTION`, `TEXTURE`, `MATERIAL`
    #### Outputs:
    - `#0 output: Float = 0.0`
    - `#1 output_001: Integer = 0`
    - `#2 output_002: Boolean = False`
    - `#3 output_003: Vector = (0.0, 0.0, 0.0)`
    - `#4 output_004: Color = (0.0, 0.0, 0.0, 0.0)`
    - `#5 output_005: String = ""`
    - `#6 output_006: Geometry = None`
    - `#7 output_007: Object = None`
    - `#8 output_008: Collection = None`
    - `#9 output_009: Texture = None`
    - `#10 output_010: Material = None`
    - `#11 output_011: Image = None`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeSwitch.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/switch.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeSwitch.html)
    """
    node = new_node(*nodes.GeometryNodeSwitch(input_type, switch, switch_001, false, true, false_001, true_001, false_002, true_002, false_003, true_003, false_004, true_004, false_005, true_005, false_006, true_006, false_007, true_007, false_008, true_008, false_009, true_009, false_010, true_010, false_011, true_011))
    return node.outputs[0].Float, node.outputs[1].Integer, node.outputs[2].Boolean, node.outputs[3].Vector, node.outputs[4].Color, node.outputs[5].String, node.outputs[6].Geometry, node.outputs[7].Object, node.outputs[8].Collection, node.outputs[9].Texture, node.outputs[10].Material, node.outputs[11].Image


def RandomFloat(min=0.0, max=1.0, id=0, seed=0):
    """The Random Value node outputs a white noise like value as a Float, Integer, Vector, or Boolean field.
    #### Path
    - Utilities > Random Value Node
    #### Outputs:
    - `#1 value_001: Float = 0.0`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_FunctionNodeRandomValue.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/random_value.html) [[API]](https://docs.blender.org/api/current/bpy.types.FunctionNodeRandomValue.html)
    """
    node = new_node(*nodes.FunctionNodeRandomValue("FLOAT", min_001=min, max_001=max, id=id, seed=seed))
    return node.outputs[1].Float


def RandomInteger(min=0, max=100, id=0, seed=0):
    """The Random Value node outputs a white noise like value as a Float, Integer, Vector, or Boolean field.
    #### Path
    - Utilities > Random Value Node
    #### Outputs:
    - `#2 value_002: Integer = 0`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_FunctionNodeRandomValue.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/random_value.html) [[API]](https://docs.blender.org/api/current/bpy.types.FunctionNodeRandomValue.html)
    """
    node = new_node(*nodes.FunctionNodeRandomValue("INT", min_002=min, max_002=max, id=id, seed=seed))
    return node.outputs[2].Integer


def RandomVector(min=(0.0, 0.0, 0.0), max=(1.0, 1.0, 1.0), id=0, seed=0):
    """The Random Value node outputs a white noise like value as a Float, Integer, Vector, or Boolean field.
    #### Path
    - Utilities > Random Value Node
    #### Outputs:
    - `#0 value: Vector = (0.0, 0.0, 0.0)`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_FunctionNodeRandomValue.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/random_value.html) [[API]](https://docs.blender.org/api/current/bpy.types.FunctionNodeRandomValue.html)
    """
    node = new_node(*nodes.FunctionNodeRandomValue("FLOAT_VECTOR", min=min, max=max, id=id, seed=seed))
    return node.outputs[0].Vector


def RandomBoolean(probability=0.5, id=0, seed=0):
    """The Random Value node outputs a white noise like value as a Float, Integer, Vector, or Boolean field.
    #### Path
    - Utilities > Random Value Node
    #### Outputs:
    - `#3 value_003: Boolean = False`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_FunctionNodeRandomValue.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/utilities/random_value.html) [[API]](https://docs.blender.org/api/current/bpy.types.FunctionNodeRandomValue.html)
    """
    node = new_node(*nodes.FunctionNodeRandomValue("BOOLEAN", probability=probability, id=id, seed=seed))
    return node.outputs[3].Boolean


def InputPosition():
    """The Position node outputs a vector of each point of the geometry the node is connected to.
    #### Path
    - Geometry > Read > Position Node
    #### Outputs:
    - `#0 position: Vector = (0.0, 0.0, 0.0)`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeInputPosition.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/read/position.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputPosition.html)
    """
    node = new_node(*nodes.GeometryNodeInputPosition())
    return node.outputs[0].Vector


def InputIndex():
    """The Index node gives an integer value indicating the position of each element in the list, starting at zero. This depends on the internal order of the data in the geometry, which is not necessarily visible in the 3D Viewport. However, the index value is visible in the left-most column in the Spreadsheet Editor.
    #### Path
    - Geometry > Read > Index Node
    #### Outputs:
    - `#0 index: Integer = 0`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_GeometryNodeInputIndex.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/geometry/read/input_index.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputIndex.html)
    """
    node = new_node(*nodes.GeometryNodeInputIndex())
    return node.outputs[0].Integer


def SceneTime():
    """The Scene Time node outputs the current time in the scene's animation in units of seconds or frames.
    #### Path
    - Input > Scene > Scene Time Node
    #### Outputs:
    - `#0 seconds: Float = 0.0`
    - `#1 frame: Float = 0.0`

    ![](https://docs.blender.org/manual/en/3.5/_images/node-types_GeometryNodeInputSceneTime.webp)

    [[Manual]](https://docs.blender.org/manual/en/3.5/modeling/geometry_nodes/input/scene/scene_time.html) [[API]](https://docs.blender.org/api/current/bpy.types.GeometryNodeInputSceneTime.html)
    """
    node = new_node(*nodes.GeometryNodeInputSceneTime())
    ret = typing.NamedTuple("SceneTime", [("seconds", Float), ("frame", Float)])
    return ret(node.outputs[0].Float, node.outputs[1].Float)


def AmbientOcclusion(inside=False, only_local=False, samples=16, color=(1.0, 1.0, 1.0, 1.0), distance=1.0, normal=(0.0, 0.0, 0.0)):
    """The Ambient Occlusion shader computes how much the hemisphere above the shading point is occluded. This can be used for procedural texturing, for example to add weathering effects to corners only.
    #### Path
    - Input > Ambient Occlusion
    #### Outputs:
    - `#0 color: Color = (0.0, 0.0, 0.0, 0.0)`
    - `#1 ao: Float = 0.0`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeAmbientOcclusion.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/render/shader_nodes/input/ao.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeAmbientOcclusion.html)
    """
    node = new_node(*nodes.ShaderNodeAmbientOcclusion(inside, only_local, samples, color, distance, normal))
    ret = typing.NamedTuple("ShaderNodeAmbientOcclusion", [("color", Color), ("ao", Float)])
    return ret(node.outputs[0].Color, node.outputs[1].Float)


def EnvironmentTexture(image=None, interpolation='Linear', projection='EQUIRECTANGULAR', vector=(0.0, 0.0, 0.0)):
    """The Node Environmental Texture is used to light your scene using an environment map image file as a texture.
    #### Path
    - Texture > Environment Texture Node
    #### Properties:
    - `interpolation`: `Linear`, `Closest`, `Cubic`, `Smart`
    - `projection`: `EQUIRECTANGULAR`, `MIRROR_BALL`
    #### Outputs:
    - `#0 color: Color = (0.0, 0.0, 0.0, 0.0)`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeTexEnvironment.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/render/shader_nodes/textures/environment.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexEnvironment.html)
    """
    if isinstance(image, str):
        image = bpy.data.images[image]
    node = new_node(*nodes.ShaderNodeTexEnvironment(interpolation, projection, None, image, None, None, vector))
    ret = typing.NamedTuple("ShaderNodeTexEnvironment", [("color", Color)])
    return ret(node.outputs[0].Color)


def IES_Texture(mode='INTERNAL', filepath='', ies=None, vector=(0.0, 0.0, 0.0), strength=1.0):
    """The IES Texture is used to match real world lights based on IES files (IES). IES files store the directional intensity distribution of light sources.
    #### Path
    - Texture > IES Texture Node
    #### Properties:
    - `mode`: `INTERNAL`, `EXTERNAL`
    #### Outputs:
    - `#0 fac: Float = 0.0`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeTexIES.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/render/shader_nodes/textures/ies.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexIES.html)
    """
    node = new_node(*nodes.ShaderNodeTexIES(mode, filepath, ies, vector, strength))
    ret = typing.NamedTuple("ShaderNodeTexIES", [("fac", Float)])
    return ret(node.outputs[0].Float)


def ImageTexture(image=None, interpolation='Linear', projection='FLAT', extension='REPEAT', color_mapping=None, image_user=None, projection_blend=0.0, texture_mapping=None, vector=(0.0, 0.0, 0.0)):
    """The Image Texture is used to add an image file as a texture.
    #### Path
    - Texture > Image Texture Node
    #### Properties:
    - `extension`: `REPEAT`, `EXTEND`, `CLIP`, `MIRROR`
    - `interpolation`: `Linear`, `Closest`, `Cubic`, `Smart`
    - `projection`: `FLAT`, `BOX`, `SPHERE`, `TUBE`
    #### Outputs:
    - `#0 color: Color = (0.0, 0.0, 0.0, 0.0)`
    - `#1 alpha: Float = 0.0`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeTexImage.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/render/shader_nodes/textures/image.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexImage.html)
    """
    if isinstance(image, str):
        image = bpy.data.images[image]
    node = new_node(*nodes.ShaderNodeTexImage(extension, interpolation, projection, color_mapping, image, image_user, projection_blend, texture_mapping, vector))
    ret = typing.NamedTuple("ShaderNodeTexImage", [("color", Color), ("alpha", Float)])
    return ret(node.outputs[0].Color, node.outputs[1].Float)


def PointDensity(interpolation='Linear', particle_color_source='PARTICLE_AGE', point_source='PARTICLE_SYSTEM', space='OBJECT', vertex_color_source='VERTEX_COLOR', object=None, particle_system=None, radius=0.3, resolution=100, vertex_attribute_name='', vector=(0.0, 0.0, 0.0)):
    """The Point Density node is used to add volumetric points for each particle or vertex of another object.
    #### Path
    - Texture > Point Density Node
    #### Properties:
    - `interpolation`: `Linear`, `Closest`, `Cubic`
    - `particle_color_source`: `PARTICLE_AGE`, `PARTICLE_SPEED`, `PARTICLE_VELOCITY`
    - `point_source`: `PARTICLE_SYSTEM`, `OBJECT`
    - `space`: `OBJECT`, `WORLD`
    - `vertex_color_source`: `VERTEX_COLOR`, `VERTEX_WEIGHT`, `VERTEX_NORMAL`
    #### Outputs:
    - `#0 color: Color = (0.0, 0.0, 0.0, 0.0)`
    - `#1 density: Float = 0.0`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeTexPointDensity.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/render/shader_nodes/textures/point_density.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexPointDensity.html)
    """
    node = new_node(*nodes.ShaderNodeTexPointDensity(interpolation, particle_color_source, point_source, space, vertex_color_source, object, particle_system, radius, resolution, vertex_attribute_name, vector))
    ret = typing.NamedTuple("ShaderNodeTexPointDensity", [("color", Color), ("density", Float)])
    return ret(node.outputs[0].Color, node.outputs[1].Float)


def SkyTexture(sky_type='NISHITA', air_density=1.0, altitude=0.0, color_mapping=None, dust_density=1.0, ground_albedo=0.3, ozone_density=1.0, sun_direction=(0.0, 0.0, 1.0), sun_disc=True, sun_elevation=math.radians(15.0), sun_intensity=1.0, sun_rotation=0.0, sun_size=math.radians(0.545), texture_mapping=None, turbidity=2.2, vector=(0.0, 0.0, 0.0)):
    """The Sky Texture node adds a procedural Sky texture.
    #### Path
    - Texture > Sky Texture Node
    #### Properties:
    - `sky_type`: `NISHITA`, `PREETHAM`, `HOSEK_WILKIE`
    #### Outputs:
    - `#0 color: Color = (0.0, 0.0, 0.0, 0.0)`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeTexSky.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/render/shader_nodes/textures/sky.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexSky.html)
    """
    node = new_node(*nodes.ShaderNodeTexSky(sky_type, air_density, altitude, color_mapping, dust_density, ground_albedo, ozone_density, sun_direction, sun_disc, sun_elevation, sun_intensity, sun_rotation, sun_size, texture_mapping, turbidity, vector))
    ret = typing.NamedTuple("ShaderNodeTexSky", [("color", Color)])
    return ret(node.outputs[0].Color)


def BrightContrast(color=(1.0, 1.0, 1.0, 1.0), bright=0.0, contrast=0.0):
    """ShaderNodeBrightContrast
    #### Path
    - Color > Bright/Contrast Node
    #### Outputs:
    - `#0 color: Color = (0.0, 0.0, 0.0, 0.0)`

    ![](https://docs.blender.org/manual/en/latest/_images/compositing_node-types_CompositorNodeBrightContrast.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/render/shader_nodes/color/bright_contrast.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeBrightContrast.html)
    """
    node = new_node(*nodes.ShaderNodeBrightContrast(color, bright, contrast))
    return node.outputs[0].Color


def ColorGamma(color=(1.0, 1.0, 1.0, 1.0), gamma=1.0):
    """Use this node to apply a gamma correction.
    #### Path
    - Color > Gamma Node
    #### Outputs:
    - `#0 color: Color = (0.0, 0.0, 0.0, 0.0)`

    ![](https://docs.blender.org/manual/en/latest/_images/compositing_node-types_CompositorNodeGamma.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/render/shader_nodes/color/gamma.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeGamma.html)
    """
    node = new_node(*nodes.ShaderNodeGamma(color, gamma))
    return node.outputs[0].Color


def HueSaturation(hue=0.5, saturation=1.0, value=1.0, fac=1.0, color=(0.8, 0.8, 0.8, 1.0)):
    """The Hue Saturation Value Node applies a color transformation in the HSV Color Model.
    #### Path
    - Color > Hue Saturation Value Node
    #### Outputs:
    - `#0 color: Color = (0.0, 0.0, 0.0, 0.0)`

    ![](https://docs.blender.org/manual/en/latest/_images/compositing_node-types_CompositorNodeHueSat.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/render/shader_nodes/color/hue_saturation.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeHueSaturation.html)
    """
    node = new_node(*nodes.ShaderNodeHueSaturation(hue, saturation, value, fac, color))
    return node.outputs[0].Color


def LightFalloff(strength=100.0, smooth=0.0):
    """Cycles Only
    #### Path
    - Color > Light Falloff Node
    #### Outputs:
    - `#0 quadratic: Float = 0.0`
    - `#1 linear: Float = 0.0`
    - `#2 constant: Float = 0.0`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeLightFalloff.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/render/shader_nodes/color/light_falloff.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeLightFalloff.html)
    """
    node = new_node(*nodes.ShaderNodeLightFalloff(strength, smooth))
    ret = typing.NamedTuple("ShaderNodeLightFalloff", [("quadratic", Float), ("linear", Float), ("constant", Float)])
    return ret(node.outputs[0].Float, node.outputs[1].Float, node.outputs[2].Float)


def ShaderNodeBump(invert=False, strength=1.0, distance=1.0, height=1.0, normal=(0.0, 0.0, 0.0)):
    """The Bump node generates a perturbed normal from a height texture, for bump mapping. The height value will be sampled at the shading point and two nearby points on the surface to determine the local direction of the normal.
    #### Path
    - Vector > Bump Node
    #### Outputs:
    - `#0 normal: Vector = (0.0, 0.0, 0.0)`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeBump.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/render/shader_nodes/vector/bump.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeBump.html)
    """
    node = new_node(*nodes.ShaderNodeBump(invert, strength, distance, height, normal))
    return node.outputs[0].Vector


def ShaderNodeDisplacement(space='OBJECT', height=0.0, midlevel=0.5, scale=1.0, normal=(0.0, 0.0, 0.0)):
    """The Displacement node is used to displace the surface along the surface normal, to add more detail to the geometry. Both procedural textures and baked displacement maps can be used.
    #### Path
    - Vector > Displacement Node
    #### Properties:
    - `space`: `OBJECT`, `WORLD`
    #### Outputs:
    - `#0 displacement: Vector = (0.0, 0.0, 0.0)`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeDisplacement.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/render/shader_nodes/vector/displacement.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeDisplacement.html)
    """
    node = new_node(*nodes.ShaderNodeDisplacement(space, height, midlevel, scale, normal))
    return node.outputs[0].Vector


def ShaderNodeNormal(normal=(0.0, 0.0, 1.0)):
    """The Normal node generates a normal vector and a dot product.
    #### Path
    - Vector > Normal Node
    #### Outputs:
    - `#0 normal: Vector = (0.0, 0.0, 1.0)`
    - `#1 dot: Float = 0.0`

    ![](https://docs.blender.org/manual/en/latest/_images/compositing_node-types_CompositorNodeNormal.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/render/shader_nodes/vector/normal.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeNormal.html)
    """
    node = new_node(*nodes.ShaderNodeNormal(normal))
    ret = typing.NamedTuple("ShaderNodeNormal", [("normal", Vector), ("dot", Float)])
    return ret(node.outputs[0].Vector, node.outputs[1].Float)


def ShaderNodeNormalMap(space='TANGENT', uv_map='', strength=1.0, color=(0.5, 0.5, 1.0, 1.0)):
    """The Normal Map node generates a perturbed normal from an RGB normal map image. This is usually chained with an Image Texture node in the color input, to specify the normal map image. For tangent space normal maps, the UV coordinates for the image must match, and the image texture should be set to Non-Color mode to give correct results.
    #### Path
    - Vector > Normal Map Node
    #### Properties:
    - `space`: `TANGENT`, `OBJECT`, `WORLD`, `BLENDER_OBJECT`, `BLENDER_WORLD`
    #### Outputs:
    - `#0 normal: Vector = (0.0, 0.0, 0.0)`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeNormalMap.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/render/shader_nodes/vector/normal_map.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeNormalMap.html)
    """
    node = new_node(*nodes.ShaderNodeNormalMap(space, uv_map, strength, color))
    return node.outputs[0].Vector


def ShaderNodeVectorDisplacement(space='TANGENT', vector=(0.0, 0.0, 0.0, 0.0), midlevel=0.0, scale=1.0):
    """The Vector Displacement node is used to displace the surface along arbitrary directions, unlike the regular Displacement node which only displaces along the surface normal.
    #### Path
    - Vector > Vector Displacement Node
    #### Properties:
    - `space`: `TANGENT`, `OBJECT`, `WORLD`
    #### Outputs:
    - `#0 displacement: Vector = (0.0, 0.0, 0.0)`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeVectorDisplacement.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/render/shader_nodes/vector/vector_displacement.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorDisplacement.html)
    """
    node = new_node(*nodes.ShaderNodeVectorDisplacement(space, vector, midlevel, scale))
    return node.outputs[0].Vector


def ShaderNodeVectorTransform(convert_from='WORLD', convert_to='OBJECT', vector_type='VECTOR', vector=(0.5, 0.5, 0.5)):
    """The Vector Transform node allows converting a vector, point, or normal between world and camera and object coordinate space.
    #### Path
    - Vector > Vector Transform Node
    #### Properties:
    - `convert_from`: `WORLD`, `OBJECT`, `CAMERA`
    - `convert_to`: `OBJECT`, `WORLD`, `CAMERA`
    - `vector_type`: `VECTOR`, `POINT`, `NORMAL`
    #### Outputs:
    - `#0 vector: Vector = (0.0, 0.0, 0.0)`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeVectorTransform.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/render/shader_nodes/vector/transform.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeVectorTransform.html)
    """
    node = new_node(*nodes.ShaderNodeVectorTransform(convert_from, convert_to, vector_type, vector))
    return node.outputs[0].Vector


def ShaderNodeBlackbody(temperature=1500.0):
    """The Blackbody node converts a blackbody temperature to RGB value. This can be useful for materials that emit light at natural occurring frequencies.
    #### Path
    - Converter > Blackbody Node
    #### Outputs:
    - `#0 color: Color = (0.0, 0.0, 0.0, 0.0)`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeBlackbody.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/render/shader_nodes/converter/blackbody.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeBlackbody.html)
    """
    node = new_node(*nodes.ShaderNodeBlackbody(temperature))
    return node.outputs[0].Color


def ShaderNodeCombineColor(mode='RGB', red=0.0, green=0.0, blue=0.0):
    """The Combine Color Node combines an image from its composite color channels. The node can combine multiple Color Models depending on the Mode property.
    #### Path
    - Converter > Combine Color Node
    #### Properties:
    - `mode`: `RGB`, `HSV`, `HSL`
    #### Outputs:
    - `#0 color: Color = (0.0, 0.0, 0.0, 0.0)`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_FunctionNodeCombineColor.png)

    [[Manual]](https://docs.blender.org/manual/en/latest/render/shader_nodes/converter/combine_color.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeCombineColor.html)
    """
    node = new_node(*nodes.ShaderNodeCombineColor(mode, red, green, blue))
    return node.outputs[0].Color


def ShaderNodeRGBToBW(color=(0.5, 0.5, 0.5, 1.0)):
    """The RGB to BW Node maps an RGB color image to a gray-scale by the luminance.
    #### Path
    - Converter > RGB to BW Node
    #### Outputs:
    - `#0 val: Float = 0.0`

    ![](https://docs.blender.org/manual/en/latest/_images/compositing_node-types_CompositorNodeRGBToBW.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/render/shader_nodes/converter/rgb_to_bw.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeRGBToBW.html)
    """
    node = new_node(*nodes.ShaderNodeRGBToBW(color))
    return node.outputs[0].Float


def ShaderNodeSeparateColor(color=(0.8, 0.8, 0.8, 1.0), mode='RGB'):
    """The Separate Color Node splits an image into its composite color channels. The node can output multiple Color Models depending on the Mode property.
    #### Path
    - Converter > Separate Color Node
    #### Properties:
    - `mode`: `RGB`, `HSV`, `HSL`
    #### Outputs:
    - `#0 red: Float = 0.0`
    - `#1 green: Float = 0.0`
    - `#2 blue: Float = 0.0`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_FunctionNodeSeparateColor.png)

    [[Manual]](https://docs.blender.org/manual/en/latest/render/shader_nodes/converter/separate_color.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeSeparateColor.html)
    """
    node = new_node(*nodes.ShaderNodeSeparateColor(mode, color))
    ret = typing.NamedTuple("ShaderNodeSeparateColor", [("red", Float), ("green", Float), ("blue", Float)])
    return ret(node.outputs[0].Float, node.outputs[1].Float, node.outputs[2].Float)


def ShaderNodeWavelength(wavelength=500.0):
    """The Wavelength node converts a wavelength value to an RGB value. This can be used to achieve a specific color on the light spectrum.
    #### Path
    - Converter > Wavelength Node
    #### Outputs:
    - `#0 color: Color = (0.0, 0.0, 0.0, 0.0)`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeWavelength.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/render/shader_nodes/converter/wavelength.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeWavelength.html)
    """
    node = new_node(*nodes.ShaderNodeWavelength(wavelength))
    return node.outputs[0].Color


def TextureCoord(object=None, from_instancer=False):
    """The Texture Coordinate node is commonly used for the coordinates of textures, typically used as inputs for the Vector input for texture nodes.
    #### Path
    - Input > Texture Coordinate Node
    #### Outputs:
    - `#0 generated: Vector = (0.0, 0.0, 0.0)`
    - `#1 normal: Vector = (0.0, 0.0, 0.0)`
    - `#2 uv: Vector = (0.0, 0.0, 0.0)`
    - `#3 object: Vector = (0.0, 0.0, 0.0)`
    - `#4 camera: Vector = (0.0, 0.0, 0.0)`
    - `#5 window: Vector = (0.0, 0.0, 0.0)`
    - `#6 reflection: Vector = (0.0, 0.0, 0.0)`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeTexCoord.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/render/shader_nodes/input/texture_coordinate.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeTexCoord.html)
    """
    node = new_node(*nodes.ShaderNodeTexCoord(from_instancer, object))
    ret = typing.NamedTuple("ShaderNodeTexCoord", [("generated", Vector), ("normal", Vector), ("uv", Vector), ("object", Vector), ("camera", Vector), ("window", Vector), ("reflection", Vector)])
    return ret(node.outputs[0].Vector, node.outputs[1].Vector, node.outputs[2].Vector, node.outputs[3].Vector, node.outputs[4].Vector, node.outputs[5].Vector, node.outputs[6].Vector)


def ShaderNodeMapping(vector_type='POINT', vector=(0.0, 0.0, 0.0), location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(1.0, 1.0, 1.0)):
    """The Mapping node transforms the input vector by applying translation, rotation, and scaling.
    #### Path
    - Vector > Mapping Node
    #### Properties:
    - `vector_type`: `POINT`, `TEXTURE`, `VECTOR`, `NORMAL`
    #### Outputs:
    - `#0 vector: Vector = (0.0, 0.0, 0.0)`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeMapping.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/render/shader_nodes/vector/mapping.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeMapping.html)
    """
    node = new_node(*nodes.ShaderNodeMapping(vector_type, vector, location, rotation, scale))
    return node.outputs[0].Vector


def ShaderGeometry():
    """The Geometry node gives geometric information about the current shading point. All vector coordinates are in World Space. For volume shaders, only the position and incoming vector are available.
    #### Path
    - Input > Geometry Node
    #### Outputs:
    - `#0 position: Vector = (0.0, 0.0, 0.0)`
    - `#1 normal: Vector = (0.0, 0.0, 0.0)`
    - `#2 tangent: Vector = (0.0, 0.0, 0.0)`
    - `#3 true_normal: Vector = (0.0, 0.0, 0.0)`
    - `#4 incoming: Vector = (0.0, 0.0, 0.0)`
    - `#5 parametric: Vector = (0.0, 0.0, 0.0)`
    - `#6 backfacing: Float = 0.0`
    - `#7 pointiness: Float = 0.0`
    - `#8 random_per_island: Float = 0.0`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeNewGeometry.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/render/shader_nodes/input/geometry.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeNewGeometry.html)
    """
    node = new_node(*nodes.ShaderNodeNewGeometry())
    ret = typing.NamedTuple("ShaderNodeNewGeometry", [("position", Vector), ("normal", Vector), ("tangent", Vector), ("true_normal", Vector), ("incoming", Vector), ("parametric", Vector), ("backfacing", Float), ("pointiness", Float), ("random_per_island", Float)])
    return ret(node.outputs[0].Vector, node.outputs[1].Vector, node.outputs[2].Vector, node.outputs[3].Vector, node.outputs[4].Vector, node.outputs[5].Vector, node.outputs[6].Float, node.outputs[7].Float, node.outputs[8].Float)


def MixShader(shader1=None, shader2=None, fac=0.5):
    """The Mix node is used to mix two shaders together. Mixing can be used for material layering, where the Factor input may, for example, be connected to a Blend Weight node.
    #### Path
    - Shader > Mix Shader
    #### Outputs:
    - `#0 shader: Shader = None`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeMixShader.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/render/shader_nodes/shader/mix.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeMixShader.html)
    """
    node = new_node(*nodes.ShaderNodeMixShader(fac, shader1, shader2))
    return node.outputs[0].Shader


def ShaderScript(mode="INTERNAL", script: bpy.types.Text = None, **kwargs):
    """It is also possible to create your own nodes using [Open Shading Language](https://github.com/AcademySoftwareFoundation/OpenShadingLanguage) (OSL). These nodes will only work with the CPU and OptiX rendering backend. OSL was designed for node-based shading, and each OSL shader corresponds to one node in a node setup. To add an OSL shader, add a script node and link it to a text data-block or an external file. Input and output sockets will be created from the shader parameters on clicking the update button in the Node or the Text editor. OSL shaders can be linked to the node in a few different ways. With the Internal mode, a text data-block is used to store the OSL shader, and the OSO bytecode is stored in the node itself. This is useful for distributing a blend-file with everything packed into it. The *External* mode can be used to specify a `.osl` file from a drive, and this will then be automatically compiled into a `.oso` file in the same directory. It is also possible to specify a path to a `.oso` file, which will then be used directly, with compilation done manually by the user. The third option is to specify just the module name, which will be looked up in the shader search path.
    ```
    bpy.data.scenes["Scene"].render.engine = "CYCLES"
    bpy.data.scenes["Scene"].cycles.shading_system = True
    ```
    #### Path
    - Input > Geometry Node
    #### Outputs:
    - `#0 position: Vector = (0.0, 0.0, 0.0)`
    - `#1 normal: Vector = (0.0, 0.0, 0.0)`
    - `#2 tangent: Vector = (0.0, 0.0, 0.0)`
    - `#3 true_normal: Vector = (0.0, 0.0, 0.0)`
    - `#4 incoming: Vector = (0.0, 0.0, 0.0)`
    - `#5 parametric: Vector = (0.0, 0.0, 0.0)`
    - `#6 backfacing: Float = 0.0`
    - `#7 pointiness: Float = 0.0`
    - `#8 random_per_island: Float = 0.0`

    ![](https://docs.blender.org/manual/en/latest/_images/node-types_ShaderNodeScript.webp)

    [[Manual]](https://docs.blender.org/manual/en/latest/render/shader_nodes/osl.html) [[API]](https://docs.blender.org/api/current/bpy.types.ShaderNodeScript.html)
    """
    if isinstance(script, str):
        if bpy.data.texts.get(script) is not None:
            script = bpy.data.texts[script]
    node = new_node(*nodes.ShaderNodeScript(mode, script))
    node.bnode.width = 160
    from .core import Script
    node = Script(node.bnode)
    for input in node.inputs:
        input.bsocket.name = input.bsocket.name.replace("_", " ").title()
    for key, val in kwargs.items():
        node[key] = val
    return node


from .geosocks import Geometry, Instances
