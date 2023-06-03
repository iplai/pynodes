bl_info = {
    "name": "PyNodes",
    "author": "iplai",
    "description": "",
    "blender": (3, 5, 1),
    "version": (0, 0, 1),
    "location": "Node Editor > Properties > Trees",
    "warning": "",
    "doc_url": "https://github.com/iplai/pynodes",
    "tracker_url": "https://github.com/iplai/pynodes/issues",
    "category": "Node"
}

from . import auto_load
auto_load.init()


def register():
    auto_load.register()


def unregister():
    auto_load.unregister()


from .core import tree, frame, reload
from .datasocks import *
from .geosocks import *

sin = Float.sin
cos = Float.cos
tan = Float.tan

from math import pi, tau, radians, degrees
import mathutils

from .colors import rgb
