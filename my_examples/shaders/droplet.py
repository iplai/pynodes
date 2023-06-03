from pynodes import *

bpy.context.scene.view_settings.view_transform = "Standard"
bpy.context.scene.render.engine = "CYCLES"
bpy.context.scene.cycles.preview_samples = 8
bpy.context.scene.cycles.shading_system = True

osl_code = """
shader droplet(
    point pos = P,
    float Time = 1,
    float start_time = 0,
    float end_time = 1,
    float Amplitude = 0.1,
    float wave_length = 0.01,
    float Spread = 1, // dispersion in wave packet I.e lower amplitude
    float Damping = 0.99, // dissipation of energy in Time

    output float Height = 0
) {
    vector center = 0;
    float start = (end_time - start_time) * noise("cell", 0, 2);
    float peak = Time - start;
    // ignore z-component
    float dc = hypot(pos[0] - center[0], pos[1] - center[1]);
    float t = dc / wave_length;
    float a = Amplitude * cos(t);
    a *= pow(Damping, start);
    a *= exp(-(dc - peak) * (dc - peak) / Spread);
    Height += a;
}
"""

if bpy.data.texts.get("droplet.osl") is None:
    bpy.data.texts.new("droplet.osl")
text = bpy.data.texts["droplet.osl"]
text.from_string(osl_code)


@tree
def water_droplet():
    """@material"""

    node = ShaderScript(script=text, pos=TextureCoord().object, time="#(frame - 1) / 50")

    shader = BSDF.Glossy(normal=node.height.to_normal(strength=0.1, distance=0.1), roughness=0.5)

    return shader


@tree
def world():
    """@world"""
    return SkyTexture("HOSEK_WILKIE").color.to_background(2.2)


from pynodes.scene import *

scene = Tree({
    O.plane @ "Water Droplet": {
        Mat.slots: ["Water Droplet"],
    },
}).load()
