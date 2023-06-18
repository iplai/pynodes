from pynodes import *


@tree
def mesh_to_contour_lines(mesh: Mesh):

    selection = WaveTextureRings("SPHERICAL", scale=0.2, distortion=50, detail=0).fac < 0.6

    mesh = mesh.subdivide_mesh(2)[selection].delete_faces()

    return mesh


@tree
def geometry_nodes(object: Object = "dragon2"):

    mesh = object.geometry.Mesh.to_curve().to_mesh(profile=CurveCircle(0.2))

    return mesh


from pynodes.scene import *

Tree({
    O.mesh @ "dragon2": {
        Mod.geometry_nodes: {
            "node_group": "mesh_to_contour_lines",
        },
        Mod.decimate: {
            "decimate_type": "DISSOLVE",
            "angle_limit": radians(40),
        },
        Mod.smooth: {
            "iterations": 20,
        },
    }
}).load()
