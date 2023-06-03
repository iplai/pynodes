from pynodes import *


@tree
def hilbert(curve_object: Object, count: Integer = (100, 0, 206)):

    curve = curve_object.geometry.separate_components().curve[:count].select()

    return curve


from pynodes.scene import *
scene = Tree({
    O.cube: {
        Mod.geometry_nodes: {
            "node_group": "Hilbert",
            "Curve Object": "Hilbert Curve",
        },
    },
}).load()
