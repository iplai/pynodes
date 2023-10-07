import math, mathutils


def hex_color_to_rgb(hex_color: str):
    hex_color = hex_color.lstrip("#")
    r = srgb_to_linear(int(hex_color[:2], 16) / 255)
    g = srgb_to_linear(int(hex_color[2:4], 16) / 255)
    b = srgb_to_linear(int(hex_color[4:6], 16) / 255)
    return r, g, b


def hex_color_to_rgba(hex_color: str):
    r, g, b = hex_color_to_rgb(hex_color)
    hex_color = hex_color.lstrip("#")
    try:
        a = int(hex_color[6:8], 16) / 255
    except ValueError:
        a = 1.0
    return r, g, b, a


def linear_to_srgb(color_value: float):
    if color_value <= 0.0031308:
        return int(12.92 * color_value * 255.99)
    else:
        return int((1.055 * color_value ** (1 / 2.4) - 0.055) * 255.99)


def srgb_to_hex_string(r, g, b):
    return '#{:02X}{:02X}{:02X}'.format(r, g, b)


def srgb_to_linear(srgb_color_component: float):
    """Converting from sRGB to Linear RGB, based on [wikipedia](https://en.wikipedia.org/wiki/SRGB#From_sRGB_to_CIE_XYZ)"""
    if srgb_color_component <= 0.04045:
        linear_color_component = srgb_color_component / 12.92
    else:
        linear_color_component = math.pow((srgb_color_component + 0.055) / 1.055, 2.4)
    return linear_color_component


white = "#ffffff"
black = "#000000"
light_gray = "#7f5f5f"
gray = "#7f3f3f"
dark_gray = "#7f1f1f"
silver = "#bfbfbf"

light_red = "#ffbfbf"
mid_red = "#ff7f7f"
dark_red = "#ff3f3f"
red = "#ff0000"

light_orange = "#7f6f5f"
mid_orange = "#7f5f3f"
dark_orange = "#7f4f1f"
orange = "#7f3f00"

light_yellow = "#ffffbf"
mid_yellow = "#ffff7f"
dark_yellow = "#ffff3f"
yellow = "#ffff00"

light_olive = "#6f7f5f"
mid_olive = "#5f7f3f"
dark_olive = "#4f7f1f"
olive = "#3f7f00"

light_lime = "#bfffbf"
mid_lime = "#7fff7f"
dark_lime = "#3fff3f"
lime = "#00ff00"

light_green = "#5f7f6f"
mid_green = "#3f7f5f"
dark_green = "#1f7f4f"
green = "#007f3f"

light_cyan = "#bfffff"
mid_cyan = "#7fffff"
dark_cyan = "#3fffff"
cyan = "#00ffff"

light_azure = "#5f6f7f"
mid_azure = "#3f5f7f"
dark_azure = "#1f4f7f"
azure = "#003f7f"

light_blue = "#bfbfff"
mid_blue = "#7f7fff"
dark_blue = "#3f3fff"
blue = "#0000ff"

light_violet = "#6f5f7f"
mid_violet = "#5f3f7f"
dark_violet = "#4f1f7f"
violet = "#3f007f"

light_magenta = "#ffbfff"
mid_magenta = "#ff7fff"
dark_magenta = "#ff3fff"
magenta = "#ff00ff"

light_rose = "#7f5f6f"
mid_rose = "#7f3f5f"
dark_rose = "#7f1f4f"
rose = "#7f003f"

color_palettes = [
    ["#69D2E7", "#A7DBD8", "#E0E4CC", "#F38630", "#FA6900"],
    ["#FE4365", "#FC9D9A", "#F9CDAD", "#C8C8A9", "#83AF9B"],
    ["#ECD078", "#D95B43", "#C02942", "#542437", "#53777A"],
    ["#556270", "#4ECDC4", "#C7F464", "#FF6B6B", "#C44D58"],
    ["#1B325F", "#9CC4E4", "#E9F2F9", "#3A89C9", "#F26C4F"],
    ["#E8DDCB", "#CDB380", "#036564", "#033649", "#031634"],
    ["#490A3D", "#BD1550", "#E97F02", "#F8CA00", "#8A9B0F"],
    ["#594F4F", "#547980", "#45ADA8", "#9DE0AD", "#E5FCC2"],
    ["#00A0B0", "#6A4A3C", "#CC333F", "#EB6841", "#EDC951"],
    ["#413D3D", "#040004", "#C8FF00", "#FA023C", "#4B000F"],
    ["#3FB8AF", "#7FC7AF", "#DAD8A7", "#FF9E9D", "#FF3D7F"],
    ["#CCF390", "#E0E05A", "#F7C41F", "#FC930A", "#FF003D"],
    ["#395A4F", "#432330", "#853C43", "#F25C5E", "#FFA566"],
    ["#343838", "#005F6B", "#008C9E", "#00B4CC", "#00DFFC"],
    ["#AAFF00", "#FFAA00", "#FF00AA", "#AA00FF", "#00AAFF"],
    ["#00A8C6", "#40C0CB", "#F9F2E7", "#AEE239", "#8FBE00"],
]


def rgb(r=0, g=0, b=0):
    if isinstance(r, str):
        return hex_color_to_rgb(r)
    c = srgb_to_linear
    return c(r / 255), c(g / 255), c(b / 255)


def rgba(r=0, g=0, b=0, a=1.0):
    return *mathutils.Color((r, g, b)) / 255, a


def color_tuple(color: float | str | tuple[float, float, float] | tuple[float, float, float, float]):
    """Turns common color representations into a tuple with length 4"""
    a = 1
    if isinstance(color, str):
        return hex_color_to_rgba(color)
    if isinstance(color, (float, int)):
        r = g = b = color
        return r, g, b, a
    if len(color) == 3:
        return *color, a
    return color
