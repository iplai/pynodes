import functools, logging, bpy, random, time, mathutils, math


def load_font(name=None, file_name=None, windows=True):
    font = bpy.data.fonts.get(name)
    if font is not None:
        return font
    if windows:
        prefix = "C:\\Windows\\Fonts\\"
    else:
        prefix = "C:\\Users\\Administrator\\AppData\\Local\\Microsoft\\Windows\\Fonts\\"
    font = bpy.data.fonts.load(prefix + file_name, check_existing=True)
    print("Loaded", font.name)
    return font


def clean_scene():
    """
    Removing all of the objects, collection, materials, particles,
    textures, images, curves, meshes, actions, nodes, and worlds from the scene
    """
    if bpy.context.active_object and bpy.context.active_object.mode == "EDIT":
        bpy.ops.object.editmode_toggle()

    for obj in bpy.data.objects:
        obj.hide_set(False)
        obj.hide_select = False
        obj.hide_viewport = False

    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete()

    for collection in bpy.data.collections:
        if collection.name == "Collection":
            continue
        bpy.data.collections.remove(collection)

    bpy.ops.outliner.orphans_purge(do_recursive=True)


def active_object():
    """
    returns the currently active object
    """
    return bpy.context.active_object


def add_ctrl_empty(name="empty.cntrl"):
    bpy.ops.object.empty_add(type="PLAIN_AXES")

    empty_ctrl = active_object()
    empty_ctrl.name = name

    return empty_ctrl


def duplicate_object(obj=None, linked=False):
    if obj is None:
        obj = active_object()

    deselect_all_objects()

    obj.select_set(True)

    bpy.context.view_layer.objects.active = obj

    bpy.ops.object.duplicate(linked=linked)
    dup_obj = active_object()

    return dup_obj


def make_active(obj: bpy.types.Object):
    deselect_all_objects()
    obj.select_set(True)
    bpy.context.view_layer.objects.active = obj


def track_empty(obj: bpy.types.Object):
    """
    create an empty and add a 'Track To' constraint
    """
    empty = add_ctrl_empty(name=f"empty.tracker-target.{obj.name}")

    make_active(obj)
    bpy.ops.object.constraint_add(type="TRACK_TO")
    bpy.context.object.constraints["Track To"].target = empty

    return empty


def join_objects(objects: list[bpy.types.Object]):
    deselect_all_objects()

    for obj in objects:
        obj.select_set(True)

    bpy.ops.object.join()

    new_obj = active_object()

    return new_obj


def set_1080px_square_render_res():
    """
    Set the resolution of the rendered image to 1080 by 1080
    """
    bpy.context.scene.render.resolution_x = 1080
    bpy.context.scene.render.resolution_y = 1080


def set_fcurve_extrapolation_to_linear():
    for fc in bpy.context.active_object.animation_data.action.fcurves:
        fc.extrapolation = "LINEAR"


def rgb_to_hex(rgb: mathutils.Color | list | tuple) -> str:
    red = int(rgb[0] * 255)
    green = int(rgb[1] * 255)
    blue = int(rgb[2] * 255)
    # Format the RGB values as hexadecimal strings
    hex_color = f"#{red:02x}{green:02x}{blue:02x}"
    return hex_color


def hex_color_to_rgb(hex_color: str):
    hex_color = hex_color.lstrip("#")
    r = convert_srgb_to_linear_rgb(int(hex_color[:2], 16) / 255)
    g = convert_srgb_to_linear_rgb(int(hex_color[2:4], 16) / 255)
    b = convert_srgb_to_linear_rgb(int(hex_color[4:6], 16) / 255)
    return r, g, b


def hex_color_to_rgba(hex_color: str, alpha=1.0):
    r, g, b = hex_color_to_rgb(hex_color)
    return r, g, b, alpha


def convert_srgb_to_linear_rgb(srgb_color_component: float):
    """
    Converting from sRGB to Linear RGB
    based on https://en.wikipedia.org/wiki/SRGB#From_sRGB_to_CIE_XYZ
    """
    if srgb_color_component <= 0.04045:
        linear_color_component = srgb_color_component / 12.92
    else:
        linear_color_component = math.pow((srgb_color_component + 0.055) / 1.055, 2.4)
    return linear_color_component


def deselect_all_objects():
    """
    Similar to bpy.ops.object.select_all(action="DESELECT")
    """
    for obj in bpy.data.objects:
        obj.select_set(False)


def create_collection(collection_name):
    deselect_all_objects()

    collection = bpy.data.collections.new(name=collection_name)
    bpy.context.scene.collection.children.link(collection)

    return collection


def add_to_collection(collection_name: str, obj: bpy.types.Object = None, base_collection: bpy.types.Collection = None):
    """
    Adds a given object to a collection with collection_name
    """
    if obj is None:
        obj = bpy.context.active_object

    if base_collection is None:
        base_collection = bpy.context.scene.collection

    if collection_name not in bpy.data.collections:
        logging.error("couldn't find a collection with the name '%s' ", collection_name)
        return

    collection = bpy.data.collections[collection_name]
    collection.objects.link(obj)

    base_collection.objects.unlink(obj)


def make_instance_of_collection(collection_name, location, rotation_euler=None, base_collection=None):
    source_collection = bpy.data.collections.get(collection_name)
    if source_collection is None:
        logging.error("couldn't find a collection with the name '%s' ", collection_name)
        return

    if base_collection is None:
        base_collection = bpy.context.scene.collection

    new_name = f"{collection_name}.instance.{str(location)}"
    collection_instance = bpy.data.objects.new(name=new_name, object_data=None)
    collection_instance.location = location
    collection_instance.instance_type = "COLLECTION"
    collection_instance.instance_collection = source_collection

    base_collection.objects.link(collection_instance)

    if rotation_euler:
        collection_instance.rotation_euler = rotation_euler

    return collection_instance


class Axis:
    X = 0
    Y = 1
    Z = 2


def rotate_object(axis, degrees):
    bpy.context.active_object.rotation_euler[axis] = math.radians(degrees)


def create_reflective_material(color, name=None, roughness=0.1, specular=0.5, return_nodes=False):
    if name is None:
        name = ""

    material = bpy.data.materials.new(name=f"material.reflective.{name}")
    material.use_nodes = True

    material.node_tree.nodes["Principled BSDF"].inputs["Base Color"].default_value = color
    material.node_tree.nodes["Principled BSDF"].inputs["Roughness"].default_value = roughness
    material.node_tree.nodes["Principled BSDF"].inputs["Specular"].default_value = specular

    if return_nodes:
        return material, material.node_tree.nodes
    else:
        return material


def apply_reflective_material(color, name=None, roughness=0.1, specular=0.5):
    material = create_reflective_material(color, name=name, roughness=roughness, specular=specular)

    obj = active_object()
    obj.data.materials.append(material)


def set_up_world_sun_light(sun_config: dict = None, strength=1.0):
    world_node_tree = bpy.context.scene.world.node_tree
    world_node_tree.nodes.clear()

    node_location_x_sep = 200
    node_location_x = 0

    node_sky = world_node_tree.nodes.new(type="ShaderNodeTexSky")
    node_location_x += node_location_x_sep

    world_background_node = world_node_tree.nodes.new(type="ShaderNodeBackground")
    world_background_node.inputs["Strength"].default_value = strength
    world_background_node.location.x = node_location_x
    node_location_x += node_location_x_sep

    world_output_node = world_node_tree.nodes.new(type="ShaderNodeOutputWorld")
    world_output_node.location.x = node_location_x

    if sun_config:
        print("Updating ShaderNodeTexSky params:")
        for attr, value in sun_config.items():
            if hasattr(node_sky, attr):
                print(f"    {attr} set to {value}")
                setattr(node_sky, attr, value)
            else:
                print(f"    {attr} is not an attribute of ShaderNodeTexSky node")

    world_node_tree.links.new(node_sky.outputs["Color"], world_background_node.inputs["Color"])
    world_node_tree.links.new(world_background_node.outputs["Background"], world_output_node.inputs["Surface"])

    return node_sky


# bpybb end


def configure_logging(level=logging.INFO):
    logging.basicConfig(level=level)


@functools.cache
def load_color_palettes():
    return [
        ["#69D2E7", "#A7DBD8", "#E0E4CC", "#F38630", "#FA6900"],
        ["#FE4365", "#FC9D9A", "#F9CDAD", "#C8C8A9", "#83AF9B"],
        ["#ECD078", "#D95B43", "#C02942", "#542437", "#53777A"],
        ["#556270", "#4ECDC4", "#C7F464", "#FF6B6B", "#C44D58"],
        ["#1B325F", "#9CC4E4", "#E9F2F9", "#3A89C9", "#F26C4F"],
        ["#E8DDCB", "#CDB380", "#036564", "#033649", "#031634"],
        ["#490A3D", "#BD1550", "#E97F02", "#F8CA00", "#8A9B0F"],
        ["#594F4F", "#547980", "#45ADA8", "#9DE0AD", "#E5FCC2"],
        ["#00A0B0", "#6A4A3C", "#CC333F", "#EB6841", "#EDC951"],
        ["#413D3D", "#040004", "#C8FF00", "#FA023C", "#4B000F"],
        ["#3FB8AF", "#7FC7AF", "#DAD8A7", "#FF9E9D", "#FF3D7F"],
        ["#CCF390", "#E0E05A", "#F7C41F", "#FC930A", "#FF003D"],
        ["#395A4F", "#432330", "#853C43", "#F25C5E", "#FFA566"],
        ["#343838", "#005F6B", "#008C9E", "#00B4CC", "#00DFFC"],
        ["#AAFF00", "#FFAA00", "#FF00AA", "#AA00FF", "#00AAFF"],
        ["#00A8C6", "#40C0CB", "#F9F2E7", "#AEE239", "#8FBE00"],
    ]


def select_random_color_palette():
    random_palette = random.choice(load_color_palettes())
    print(f"Random palette:\n{random_palette}")
    return random_palette


@functools.cache
def get_color_palette():
    """Note: we will select a random color palette once.
    With the functools.cache decorator we will return the same palette.
    """
    return select_random_color_palette()


def get_random_color():
    color_palette = get_color_palette()
    hex_color = random.choice(color_palette)
    return hex_color_to_rgba(hex_color)


def select_color_pair():
    first_color = get_random_color()
    second_color = get_random_color()
    while second_color == first_color:
        second_color = get_random_color()
    return first_color, second_color


def setup_camera():
    """
    create and setup the camera
    """
    bpy.ops.object.camera_add()
    camera = active_object()

    # set the camera as the "active camera" in the scene
    bpy.context.scene.camera = camera

    # set the Focal Length of the camera
    camera.data.lens = 70

    camera.data.passepartout_alpha = 0.9

    empty = track_empty(camera)
    camera.parent = empty

    return camera, empty


def set_scene_props(fps, loop_seconds):
    """
    Set scene properties
    """
    frame_count = fps * loop_seconds

    scene = bpy.context.scene
    scene.frame_end = frame_count

    # set the world background to black
    world = bpy.data.worlds["World"]
    if "Background" in world.node_tree.nodes:
        world.node_tree.nodes["Background"].inputs[0].default_value = (0, 0, 0, 1)

    scene.render.fps = fps

    scene.frame_current = 1
    scene.frame_start = 1

    scene.render.engine = "CYCLES"

    # Use the GPU to render
    scene.cycles.device = "GPU"

    # Use the CPU to render
    # scene.cycles.device = "CPU"

    scene.cycles.samples = 300

    scene.view_settings.look = "Very High Contrast"

    set_1080px_square_render_res()


def setup_scene(i=0, fps=30, loop_seconds=12, seed=0, project_name="project_test"):
    scene = bpy.context.scene
    frame_count = fps * loop_seconds
    scene.frame_end = frame_count

    scene.render.image_settings.file_format = "FFMPEG"
    scene.render.ffmpeg.format = "MPEG4"
    scene.render.filepath = f"/tmp/project_{project_name}/loop_{i}.mp4"

    if seed != 0:
        random.seed(seed)
    else:
        seed = round(time.time())
        bpy.context.window_manager.clipboard = str(seed)
        random.seed(seed)

    # bpy.data.worlds["World"].node_tree.nodes["Background"].inputs[0].default_value = 0, 0, 0, 1

    scene.render.fps = fps

    scene.frame_current = 1
    scene.frame_start = 1

    scene.render.engine = "CYCLES"

    scene.cycles.device = "GPU"
    scene.cycles.samples = 300

    scene.view_settings.look = "Very High Contrast"

    return {"frame_count": frame_count, "frame_count_loop": frame_count + 1}


################################################################
# helper functions END
################################################################


def animate_truchet_tile(context, truchet_tile):
    frame_step = context["frame_count"] / 4

    frame = 1
    truchet_tile.keyframe_insert("rotation_euler", index=Axis.Z, frame=frame)

    truchet_tile.rotation_euler.z += math.radians(90)
    frame += frame_step
    truchet_tile.keyframe_insert("rotation_euler", index=Axis.Z, frame=frame)

    frame += frame_step
    truchet_tile.keyframe_insert("rotation_euler", index=Axis.Z, frame=frame)

    truchet_tile.rotation_euler.z += math.radians(90)
    frame += frame_step
    truchet_tile.keyframe_insert("rotation_euler", index=Axis.Z, frame=frame)


def create_truchet_tile_pattern(context, truchet_tile_size, collection_name):
    # Note: we need to enable the "Add Curve Extra Objects" addon
    tile_pattern_size = truchet_tile_size / 2
    bpy.ops.curve.simple(
        location=(-tile_pattern_size, -tile_pattern_size, 0),
        Simple_Type="Arc",
        Simple_endangle=90,
        Simple_radius=tile_pattern_size,
        use_cyclic_u=False,
        edit_mode=False,
    )

    tile_part_1 = active_object()

    tile_part_1.data.extrude = 0.15
    bpy.ops.object.modifier_add(type="SOLIDIFY")
    tile_part_1.modifiers["Solidify"].thickness = 0.1
    tile_part_1.modifiers["Solidify"].offset = 0

    bpy.ops.object.convert(target="MESH")

    bpy.ops.object.shade_smooth()
    bpy.ops.object.shade_smooth(use_auto_smooth=True)

    bpy.ops.object.origin_set(type="ORIGIN_CURSOR", center="MEDIAN")

    tile_part_2 = duplicate_object()
    rotate_object(Axis.Z, 180)

    join_objects([tile_part_1, tile_part_2])
    add_to_collection(collection_name)

    apply_reflective_material(context["first_color"], roughness=0.5)

    tile = active_object()
    tile.name = "tile_pattern"

    return tile


def create_truchet_tile(context, truchet_tile_size, collection_name):
    truchet_tile = create_truchet_tile_pattern(context, truchet_tile_size, collection_name)

    animate_truchet_tile(context, truchet_tile)

    return truchet_tile


def create_truchet_tile_platform(context, truchet_tile_size):
    collection_name = "truchet_tile_platform"
    create_collection(collection_name=collection_name)

    ctrl_empty = add_ctrl_empty()
    ctrl_empty.name = "platform_ctrl"
    add_to_collection(collection_name)

    bpy.ops.mesh.primitive_plane_add(size=truchet_tile_size)
    add_to_collection(collection_name)
    plane = active_object()
    plane.parent = ctrl_empty

    apply_reflective_material(context["second_color"], roughness=1.0)

    truchet_tile = create_truchet_tile(context, truchet_tile_size, collection_name)
    truchet_tile.parent = ctrl_empty

    return collection_name


def create_truchet_tile_platform_group(step_x, step_y, x_range, y_range, base_truchet_tile_collection):
    current_x = step_x
    start_y = step_y

    platform_group_collection_name = "truchet_tiles_group"
    create_collection(collection_name=platform_group_collection_name)

    for _ in range(x_range):
        current_y = start_y
        for _ in range(y_range):
            loc = (current_x, current_y, 0)
            new_collection_obj = make_instance_of_collection(base_truchet_tile_collection, loc)
            make_active(new_collection_obj)
            add_to_collection(platform_group_collection_name)

            current_deg_rot = random.choice([0, 90])
            new_collection_obj.rotation_euler.z = math.radians(current_deg_rot)

            current_y += step_y

        current_x += step_x

    return platform_group_collection_name


def animate_camera(context, section_step, camera_ctrl_empty):
    frame = 1
    camera_ctrl_empty.keyframe_insert("location", index=Axis.X, frame=frame)
    camera_ctrl_empty.location.x += section_step * 2
    camera_ctrl_empty.keyframe_insert("location", index=Axis.X, frame=context["frame_count_loop"])
    make_active(camera_ctrl_empty)
    set_fcurve_extrapolation_to_linear()


def create_and_animate_camera(context, section_step):
    camera, camera_ctrl_empty = setup_camera()

    camera_ctrl_empty.location = (section_step, (section_step / 3), 0)

    camera.location.x += section_step / 2
    camera.location.y = -section_step / 2 + section_step / 10
    camera.location.z = section_step / 2

    animate_camera(context, section_step, camera_ctrl_empty)


def create_centerpiece(context):
    truchet_tile_size = 2
    base_truchet_tile_collection = create_truchet_tile_platform(context, truchet_tile_size)

    step_x = truchet_tile_size
    step_y = truchet_tile_size
    x_range = 12
    y_range = 12
    platform_group_collection_name = create_truchet_tile_platform_group(
        step_x, step_y, x_range, y_range, base_truchet_tile_collection
    )

    section_instance_count = 3
    section_step = step_x * x_range
    for i in range(1, section_instance_count + 1):
        loc = (section_step * i, 0, 0)
        make_instance_of_collection(platform_group_collection_name, loc)

    create_and_animate_camera(context, section_step)


def main():
    """
    Python code to generate this animation
    https://www.artstation.com/artwork/g2lDPx
    """
    configure_logging()

    context = setup_scene()
    context["first_color"], context["second_color"] = select_color_pair()

    create_centerpiece(context)

    sun_config = {"sun_rotation": math.radians(random.uniform(0, 360))}
    set_up_world_sun_light(sun_config, strength=0.1)


main()
