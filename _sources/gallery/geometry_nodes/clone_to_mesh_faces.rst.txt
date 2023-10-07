Clone to Mesh Faces
=====================

.. admonition:: clone_cones_to_mesh_faces
    :class: pynodes

    .. thumbnail:: https://cdn.statically.io/gh/iplai/picx-images-hosting@master/20230713/image.5dqm67qax240.webp
        
    .. code:: python

        @tree
        def clone_cones_to_mesh_faces(mesh: Mesh, subdivision_level: Integer = (1, 0, 4)):

            with frame("Input Mesh"):
                # For this example, the input mesh is a blender cube object
                mesh = mesh.subdivision_surface(level=subdivision_level)

                with frame("Capture normal"):

                    norm = mesh.capture_vector_on_faces(mesh.normal)

                with frame("Get rotation by normal"):

                    rotation = norm.align_euler_to_vector(axis="Z")

                with frame("Capture Face Area"):

                    face_area = mesh.capture_float_on_faces(mesh.face_area)

                with frame("Get scale by face area"):

                    scale = Float.sqrt(face_area) * 0.4

            with frame("Mesh to Clone"):

                cone = MeshCone().mesh

            cones = cone.on_points(mesh.to_points("FACES"), rotation=rotation, scale=scale)

            return mesh + cones