import hashlib

def deduplicate_materials(objects):
    """Crunch relevant data into a hash, then user remap if this hash already existed."""

    mat_hashes = {}
    copy_counter = {}
    for obj in objects:
        if not hasattr(obj.data, 'materials'):
            continue
        for mat in obj.data.materials:
            if 'hash' not in mat:
                mat['hash'] = hash_material(mat)
            mat_hash = mat['hash']
            if mat_hash in mat_hashes:
                print(f"Duplicate material: '{mat.name}' -> {mat_hashes[mat_hash].name}")
                if len(mat.node_tree.nodes) < 3:
                    print("Fewer than 3 nodes. Won't de-duplicate.")
                    continue
                mat.user_remap(mat_hashes[mat_hash])
                if mat_hash not in copy_counter:
                    copy_counter[mat_hash] = 0
                copy_counter[mat_hash] += 1
            else:
                mat_hashes[mat_hash] = mat

    for mat_hash, count in copy_counter.items():
        print(f"{mat_hashes[mat_hash].name} had {count} duplicates.")

def hash_material(material) -> str:
    if not material.use_nodes:
        raise NotImplementedError("Hashing is only implemented for node materials at the moment.")

    out_node = next((n for n in material.node_tree.nodes if n.type == 'OUTPUT_MATERIAL'), None)
    assert out_node, "There must be a material output node for hashing: " + material.name

    return hashlib.md5(node_inputs_to_hashable(out_node).encode("utf-8")).hexdigest()

def node_inputs_to_hashable(node) -> str:
    """Recursively collect some data towards the left of the node-tree, 
    resulting in a string that uniquely represents this node and its dependencies.
    Useful for de-duplicating node set-ups.

    Not meant for fringe cases:
    - Re-routes contribute to uniqueness
    - Node positions don't contribute to uniqueness
    - Only checks what's connected to the passed node on the left side
    - Does not check node properties that are not sockets
    """
    str_data = node.type
    if node.type == 'GROUP' and node.node_tree:
        str_data += node.node_tree.name
    elif node.type == 'TEX_IMAGE' and node.image:
        str_data += node.image.filepath

    for in_socket in node.inputs:
        if hasattr(in_socket, 'default_value'):
            # Shader sockets don't have a default_value.
            str_data += in_socket.name + str(in_socket.default_value)
        for link in in_socket.links:
            str_data += "->" + node_inputs_to_hashable(link.from_node)

    return str_data
