from pynodes import *


@tree
def target_sphere():

    return MeshIcoSphere(subdivisions=4)


@tree
def balls_push_apart(obj: Object):

    with frame("Generate Points"):

        mesh = MeshCircle(fill_type="NGON", radius=3)

        points = mesh.distribute_points_on_faces(density=100).points

    with frame("Calculate Positions"):

        diff = points.position - obj.location

        pos = diff.normalize().scale(obj.scale) + points.position

    points.set_position(position=pos)

    return points


from pynodes.scene import *

Tree({
    O.cube @ "Sphere": {
        Mod.geometry_nodes: {
            "node_group": "Target Sphere",
        }
    },
    O.cube: {
        Mod.geometry_nodes: {
            "node_group": "Balls Push Apart",
            "Obj": "Sphere"
        }
    },
}).load()
