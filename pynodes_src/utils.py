import bpy


def get_or_create_mat(name, rgba):
    if bpy.data.materials.get(name) is None:
        bpy.data.materials.new(name)
    mat = bpy.data.materials[name]
    mat.use_nodes = False
    mat.diffuse_color = rgba
    return mat


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


def load_text(filepath):
    for text in bpy.data.texts:
        if text.filepath == filepath:
            break
    else:
        bpy.data.texts.load(filepath)
    import pathlib
    return bpy.data.texts[pathlib.Path(filepath).name]
