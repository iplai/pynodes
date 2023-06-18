from pynodes import *


@tree
def line_to_wall(curve: Curve):

    return curve.subdivide(30).set_position(offset=NoiseTexture(scale=0.5).color.map_range(to_min=(-0.5, -0.5, 0), to_max=(0.5, 0.5, 0))).to_mesh().extrude_edges(offset=(0, 0, 1)).mesh


@tree
def extrude_uniform(mesh: Mesh, thickness: Float = 0.2):

    # 这里的法向是与当前点相连的面的法向量的平均值，
    # 这个平均法向量的长度小于等于1
    with frame("Evaluate normal on faces"):
        normal = mesh.evaluate_vector_on_faces(mesh.normal)

    # 将评估的法向量缩放自身长度的倒数的平方
    # 等效于 normal = normal.normalize() * (1 / normal.length)
    with frame("Scale normal"):
        normal1 = normal.normalize() * (1 / normal.length)
        normal1.node.label = "Method 1"
        normal2 = normal * (1 / normal.length**2)
        normal2.node.label = "Method 2"
        normal3 = normal * (1 / normal.dot(normal))
        normal3.node.label = "Method 3"

    # 在点域上捕捉这个法向量
    with frame("Capture normal"):
        normal = mesh.capture_vector_on_points(normal1)

    mesh, top, side = mesh.extrude_faces(offset_scale=0)

    mesh[top].set_position(offset=normal.scale(thickness))

    return mesh


from pynodes.scene import *

Tree({
    O.bezier_curve: {
        Mod.geometry_nodes @ "1": {
            "node_group": "line_to_wall"
        },
        Mod.geometry_nodes @ "2": {
            "node_group": "extrude_uniform"
        }
    }
}).load()
