Selection Example
===================

.. admonition:: Selection Example
    :class: pynodes

    .. thumbnail:: https://cdn.staticaly.com/gh/iplai/picx-images-hosting@master/20230713/image.tuy4to2ropc.webp

    .. thumbnail:: https://cdn.staticaly.com/gh/iplai/picx-images-hosting@master/20230713/image.fegtswnjoso.webp
        
    .. code:: python

        from pynodes import *


        @tree
        def index_number_to_curve(index: Integer, max_index: Integer, size: Float):

            return index.to_string().to_curve("CENTER", "MIDDLE", size=size).join_to_instances().switch(max_index < index)


        @tree
        def show_index_of_instances(instances: Instances, size: Float = 1, offset: Vector = (0, 0, 0)):

            numbers = []

            max_index = instances.integer_statistic_on_instances(instances.index).max.Integer

            for i in range(10):

                with frame(f"Index {i}"):

                    numbers.append(index_number_to_curve(InputInteger(i), max_index, size))

            numbers = join(numbers)

            with frame("Set position offset"):

                with frame("Sample position"):

                    pos = instances.sample_vector_at_index(instances.position, instances.index)

                numbers.set_position(offset=pos + offset)

            return instances + numbers


        @tree
        def selection_example(start: Integer = (0, -1, 10), span: Integer = (3, 0, 10)):

            line = MeshLine(offset=(0, 0.5, 0))

            with frame("Selection"):

                with frame("Select every two points"):

                    line = line.Mesh[line.index % 2]

                with frame("Select from start to span points"):

                    line = line.Mesh[start:start + span]

            points = line.set_position(offset=(1, 0, 0))

            ins = MeshIcoSphere(0.2, 3).mesh.Instances.on_points(points)

            return show_index_of_instances(ins, size=0.5, offset=(0.5, 0, 0))
