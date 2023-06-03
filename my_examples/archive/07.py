from pynodes import *

bpy.context.scene.view_settings.view_transform = "Standard"
bpy.data.scenes["Scene"].render.engine = "CYCLES"
bpy.data.scenes["Scene"].cycles.feature_set = "EXPERIMENTAL"


@tree
def mat():
    """@material:Brick"""

    bpy.data.images.load("C:/Users/Administrator/Desktop/brick/brick_color.jpg", check_existing=True)
    bpy.data.images.load("C:/Users/Administrator/Desktop/brick/brick_gloss.jpg", check_existing=True)
    bpy.data.images.load("C:/Users/Administrator/Desktop/brick/brick_normal.jpg", check_existing=True)
    bpy.data.images.load("C:/Users/Administrator/Desktop/brick/brick_depth.png", check_existing=True)

    bpy.data.images["brick_gloss.jpg"].colorspace_settings.name = "Non-Color"
    bpy.data.images["brick_normal.jpg"].colorspace_settings.name = "Non-Color"

    shader = BSDF.Principled()

    shader['Base Color'] = ImageTexture("brick_color.jpg").color

    shader['Roughness'] = ImageTexture("brick_gloss.jpg",).color.invert()

    shader['Normal'] = ImageTexture("brick_normal.jpg").color.normal_map()

    depth = ImageTexture("brick_depth.png").color

    depth = ShaderNodeDisplacement(height=depth, scale=0.01)

    return shader, depth


bpy.data.materials["Brick"].cycles.displacement_method = "DISPLACEMENT"


@tree
def material():
    """@material:Noise Volume"""

    shader = BSDF.VolumePrincipled()

    density = NoiseTexture("4D", w="frame/100").fac.float_curve(points=[(0.5, 0), (1, 1)])

    shader['Density'] = density

    return shader


@tree
def mat():
    """@material:Water Circles"""

    shader = BSDF.Principled()

    a = VoronoiTexture('4D', w="frame / 1000", vector=TextureCoord().generated.mapping()).distance

    b = MusgraveTexture(scale=a).fac

    c = WaveTexture(vector=b).fac

    d = c.to_color(color_end=(*rgb("#c463c9"), 1))

    shader['Base Color'] = d

    return shader


@tree
def geometry_nodes(mesh: Mesh):

    MusgraveTexture("4D", w="frame / 100").fac

    return mesh


from pynodes.scene import *

scene = Tree({
    O.plane: {
        Mod.subdivision: {
            "subdivision_type": "SIMPLE",
        }
    },
}).load()

scene[O.plane].cycles.use_adaptive_subdivision = True
scene[O.plane].select_set(False)
