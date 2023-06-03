from pynodes import *

bpy.context.scene.view_settings.view_transform = "Standard"
bpy.context.scene.render.fps = 60


@tree
def prime_dots(prime_curve: Object, count: Integer = (8000, 0)):

    curve = prime_curve.object_info().geometry.separate_components().curve[:count].select()

    return MeshIcoSphere(subdivisions=2).mesh.on_points(curve, scale=curve.position.length.square_root * 1.2)


from pynodes.scene import *

scene = Tree({
    O.cube: {
        Mod.geometry_nodes: {
            "node_group": "Prime Dots",
            "Prime Curve": bpy.data.objects['Prime Curve'],
            # "Count": [(0, 0), (1000, 240)],
        },
    },
}).load()
