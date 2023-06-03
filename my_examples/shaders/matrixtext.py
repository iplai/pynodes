from pynodes import *

bpy.context.scene.view_settings.view_transform = "Standard"
bpy.context.scene.render.engine = "CYCLES"
bpy.context.scene.cycles.preview_samples = 8
bpy.context.scene.cycles.shading_system = True

osl_code = r"""
shader MatrixDisplay(
    point Pos = P,
    int Offset = 0,
    string Text = "Blender",
    string Font = "C:\Users\Administrator\Documents\osl-shaders\Shaders\\font5x7.xml",
    output float Fac = 0)
{
    float x = Pos[0] - Offset / 5.0;
    int nchar = (int)floor(x);
    if (nchar >= 0 && nchar < strlen(Text))
    {
        string xpath = format("//char[@name='%s']", substr(Text, nchar, 1));
        int nodeid = dict_find(Font, xpath);
        if (nodeid > 0)
        {
            string pattern;
            dict_value(nodeid, "pattern", pattern);
            int row = 6 - (int)floor(Pos[1] * 7);
            int col = (int)floor(mod(x, 1.0) * 5);
            if (row >= 0 && row < 7 && col < 5)
            {
                string bits[5];
                split(pattern, bits);
                if (substr(bits[col], row, 1) == "1")
                {
                    float xcell = mod(mod(x, 1.0) * 5, 1.0);
                    float ycell = mod(mod(Pos[1], 1.0) * 7, 1.0);
                    Fac = max((0.4 - hypot(xcell - 0.5, ycell - 0.5)) / 0.4, 0.0);
                }
            }
        }
    }
}
"""

if bpy.data.texts.get("shader.osl") is None:
    bpy.data.texts.new("shader.osl")
text = bpy.data.texts["shader.osl"]
text.from_string(osl_code)


@tree
def material_test():
    """@material"""

    node = ShaderScript(script=text, pos=TextureCoord().uv.mapping(scale=(8, 1, 1)), offset=3)

    shader = BSDF.Diffuse(color=node.fac, roughness=0.5)

    return shader


@tree
def geometry_nodes(mesh: Mesh):
    return mesh.transform(scale=(8, 1, 1))


@tree
def world():
    return Shader.Background(1)


from pynodes.scene import *

scene = Tree({
    O.plane: {
        Mod.geometry_nodes: {
            "node_group": "Geometry Nodes"
        },
        Mat.slots: ["Material Test"],
    },
}).load()
