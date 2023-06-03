from pynodes import *


import bpy

image_src = bpy.data.images.new('src', 1024, 102)
print(*image_src.size)
print(type(image_src.pixels))
print(image_src.pixels[0:4])

image_src.scale(1024, 720)
image_src.pixels[0:4] = (0.5, 0.5, 0.5, 0.5)
image_src.update()
print(*image_src.size)
print(image_src.pixels[0:4])

image_dest = image_src.copy()
image_dest.update()
print(*image_dest.size)
print(image_dest.pixels[0:4])
