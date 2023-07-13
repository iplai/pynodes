Show Index
===================

This is an util node group.

.. admonition:: show_index
    :class: pynodes

    .. thumbnail:: https://i.ibb.co/KbvbzH3/image.png

    .. thumbnail:: https://i.ibb.co/2Ybff2T/image.png
        
    .. code:: python
        
        from pynodes import *

        @tree
        def index_to_curve(index: Integer, max_index: Integer, size: Float):

            return index.to_string().to_curve("CENTER", "MIDDLE", size=size).curve_instances.join_to_instances().switch(max_index < index)

        @tree
        def show_index(geometry: Geometry, size: Float = 1, offset_along_normal: Float = 0.2):

            numbers = []

            max_index = geometry.float_statistic_on_points(geometry.index).max.Integer

            for i in range(10):

                with frame(f"Index {i}"):

                    numbers.append(index_to_curve(InputInteger(i), max_index, size))

            numbers = join(numbers)

            with frame("Set position offset"):

                with frame("Sample position"):

                    pos = geometry.sample_vector_at_index(geometry.position, geometry.index)

                with frame("Sample normal"):

                    normal = geometry.sample_vector_at_index(geometry.normal, geometry.index)

                    normal = normal * offset_along_normal

                numbers.set_position(offset=pos + normal)

            return geometry + numbers
