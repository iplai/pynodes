from pynodes import *


@tree
def texture_volume_to_mesh(mesh: Mesh, resolution: Integer = 64):

    with frame("Textures to control density"):

        with frame("Checker Texture"):

            density = CheckerTexture(color1=1, color2=0, scale=2).fac

        with frame("Musgrave Texture"):

            density = MusgraveTexture("4D", scale=1.5, w=SceneTime().seconds).fac.color_ramp_uniform()

        with frame("Voronoi Texture"):

            density = VoronoiTexture(scale=2).distance.map_range("#sin(frame/20)", 1, -1, 1)

    with frame("Volume to Mesh"):

        mesh = VolumeCube(density=density, resolution_x=resolution, resolution_y=resolution, resolution_z=resolution).to_mesh()

    return mesh
