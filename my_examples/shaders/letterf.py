from pynodes import *

bpy.context.scene.view_settings.view_transform = "Standard"
bpy.context.scene.render.engine = "CYCLES"
bpy.context.scene.cycles.preview_samples = 8
bpy.context.scene.cycles.shading_system = True

osl_code = """
shader F(
    point Pos = P, // should be connected to uv-coordinates

    output float Fac = 1)
{
    float w = 0.02;
    point a = point(0.1, 0.1, 0);
    point b = point(0.1, 0.25, 0);
    point c = point(0.1, 0.4, 0);
    point d = point(0.25, 0.25, 0);
    point e = point(0.28, 0.4, 0);

    if ((distance(a, c, Pos) < w) || (distance(b, d, Pos) < w) || (distance(c, e, Pos) < w))
    {
        Fac = 0;
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

    node = ShaderScript(script=text, pos=TextureCoord().uv)

    shader = BSDF.Diffuse(color=node.fac, roughness=0.5)

    return shader


@tree
def world():
    return Shader.Background(1)


from pynodes.scene import *

scene = Tree({
    O.plane: {
        Mat.slots: ["Material Test"],
    },
}).load()
