from pynodes import *
from pynodes.math import *


@tree
def sierpinski_triangle(iterations: Integer = (1, 0, 12), scale: Float = 0.5):
    with frame("Original Shape"):
        geo = CurveCircle(1, 3).transform(rotation=(0, 0, -pi / 6)).filled_ngons
    geos = [geo.Geometry, geo.Geometry, geo.Geometry]

    with repeat(geo, *geos, iterations=iterations) as zone:
        with frame("Top"):
            ul = geo.Geometry.transform((0.0, 0.5, 0), scale=scale)
        with frame("Down Left"):
            dl = geo.Geometry.transform((-math.sqrt(3) / 4, -1 / 4, 0), scale=scale)
        with frame("Down Right"):
            dr = geo.Geometry.transform((math.sqrt(3) / 4, -1 / 4, 0), scale=scale)
        zone.to_ouputs(join(ul, dl, dr), ul, dl, dr)

    return join(
        geos[0].set_material("#ff0000"),
        geos[1].set_material("#0000ff"),
        geos[2].set_material("#00ff00")
    )


@tree
def sierpinski_relatives(iterations: Integer = (1, 0, 12)):
    with frame("Original Shape"):
        geo = Rectangle(1, 1).transform((0.5, 0.5, 0)).filled_ngons
    geos = [geo.Geometry, geo.Geometry, geo.Geometry]
    with repeat(geo, *geos, iterations=iterations) as zone:
        # ul = geo.Geometry.transform((0, 0.5, 0), scale=0.5)
        ul = geo.Geometry.transform((0, 1, 0), (0, 0, -pi / 2), scale=0.5)
        dl = geo.Geometry.transform((0.0, 0.0, 0), scale=0.5)
        dr = geo.Geometry.transform((0.5, 0.0, 0), scale=0.5)
        zone.to_ouputs(join(ul, dl, dr), ul, dl, dr)

    return join(
        geos[0].set_material("#ff0000"),
        geos[1].set_material("#0000ff"),
        geos[2].set_material("#00ff00")
    )


@tree
def transform_relatives(geo: Geometry, t: Integer = (1, 1, 8)):
    geo.switch(t == 2, geo.Geometry.transform(rotation=(0, 0, pi / 2)))
    geo.switch(t == 3, geo.Geometry.transform(rotation=(0, 0, pi)))
    geo.switch(t == 4, geo.Geometry.transform(rotation=(0, 0, -pi / 2)))
    geo.switch(t == 5, geo.Geometry.transform(rotation=(pi, 0, 0)))
    geo.switch(t == 6, geo.Geometry.transform(rotation=(0, pi, 0)))
    geo.switch(t == 7, geo.Geometry.transform(rotation=(pi, 0, pi / 2)))
    geo.switch(t == 8, geo.Geometry.transform(rotation=(0, pi, pi / 2)))
    return geo


@tree
def sierpinski_relatives_all(iterations: Integer = (6, 0, 12), t1: Integer = (1, 1, 8), t2: Integer = (1, 1, 8), t3: Integer = (1, 1, 8), seed: Integer = (0, 0)):
    with frame("Original Shape"):
        geo = Rectangle(2, 2).filled_ngons
    geos = [geo.Geometry, geo.Geometry, geo.Geometry]
    with repeat(geo, *geos, iterations=iterations) as zone:
        use_seed = seed != 0
        t1 = t1.switch(use_seed, RandomInteger(1, 8, id=InputFloat(1), seed=seed))
        t2 = t2.switch(use_seed, RandomInteger(1, 8, id=InputFloat(2), seed=seed))
        t3 = t3.switch(use_seed, RandomInteger(1, 8, id=InputFloat(3), seed=seed))
        ul = transform_relatives(geo, t1).transform((-0.5, 0.5, 0), scale=0.5)
        dl = transform_relatives(geo, t2).transform((-0.5, -0.5, 0), scale=0.5)
        dr = transform_relatives(geo, t3).transform((0.5, -0.5, 0), scale=0.5)
        zone.to_ouputs(join(ul, dl, dr), ul, dl, dr)

    return join(
        geos[0].set_material("#ff0000"),
        geos[1].set_material("#0000ff"),
        geos[2].set_material("#00ff00"),
        join_strings(t1.to_string(), t2.to_string(), t3.to_string(), delimiter=", ").to_curve(size=0.5).transform((0, 0.2, 0))
    )


@tree
def sierpinski_triangle_animation(iterations: Float = (1, 0), scale: Float = 0.5, current_loop: Integer = 0, color1: Color = (1, 0, 0, 0.88), color2: Color = (0, 1, 0, 0.66), color3: Color = (0, 0, 1, 0.88), alpha: Float = (0.9, 0, 1)):
    with frame("Original Shape"):
        geo = CurveCircle(1, 3).transform(rotation=(0, 0, -pi / 6)).filled_ngons
    geos = [geo.Geometry, geo.Geometry, geo.Geometry]

    with frame("Total Loop"):
        total_loop = iterations.floor

    with repeat(geo, *geos, current_loop, iterations=total_loop) as zone:
        with frame("Factor"):
            factor = iterations.fract
        with frame("Is Last Loop"):
            is_last_loop = current_loop == total_loop - 1
        with frame("Scale"):
            scale = scale.switch(is_last_loop, factor.map_range(0, 1, 1, scale))
        with frame("Top"):
            ul = geo.Geometry.transform((0.0, 0.5, 0) * InputFloat(1).switch(is_last_loop, factor), scale=scale)
        with frame("Down Left"):
            dl = geo.Geometry.transform((-math.sqrt(3) / 4, -1 / 4, 0) * InputFloat(1).switch(is_last_loop, factor), scale=scale)
        with frame("Down Right"):
            dr = geo.Geometry.transform((math.sqrt(3) / 4, -1 / 4, 0) * InputFloat(1).switch(is_last_loop, factor), scale=scale)
        zone.to_ouputs(join(ul, dl, dr), ul, dl, dr, current_loop + 1)

    with frame("Join"):
        geo_joined = join(
            geos[0].store_named_attribute("color", color1).store_named_attribute("alpha", color1.alpha),
            geos[1].store_named_attribute("color", color2).store_named_attribute("alpha", color2.alpha),
            geos[2].store_named_attribute("color", color3).store_named_attribute("alpha", color3.alpha)
        )

    return geo_joined.set_material("sierpinski_triangle")


@tree
def sierpinski_triangle():
    """@material"""
    shader = BsdfPrincipled()
    shader.base_color = shader.attribute("color").color
    shader.alpha = shader.attribute("alpha").fac
    return shader


bpy.data.materials["Sierpinski Triangle"].blend_method = "BLEND"
