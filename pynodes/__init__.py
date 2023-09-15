# -*- coding: utf-8 -*-

bl_info = {
    "name": "PyNodes",
    "author": "iplai",
    "description": "",
    "blender": (3, 5, 1),
    "version": (0, 1, 0),
    "location": "Node Editor > SideBar > Pynodes",
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


from .core import Tree, tree, frame, simulate, reload, repeat
from .datasocks import *
from .geosocks import *

import mathutils, math

from .colors import rgb, color_tuple
from math import pi, tau
