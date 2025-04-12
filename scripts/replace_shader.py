import bpy

def replace_poll_skin(shader_node):
    if len(shader_node.inputs['Skin Red Albedo'].links) > 0:
        return True
    if len(shader_node.inputs['Skin Damage Albedo'].links) > 0:
        return True
    return False

def replace_poll_hair(shader_node):
    return shader_node.inputs['Hair'].default_value

def replace_shader(from_shader, to_shader, poll_func):
    from_shader = bpy.data.node_groups[from_shader]
    to_shader = bpy.data.node_groups[to_shader]

    for mat in bpy.data.materials:
        if not mat.use_nodes:
            continue
        nodes = [node for node in mat.node_tree.nodes if node.type=='GROUP' and node.node_tree == from_shader]
        for node in nodes:
            if poll_func(node):
                print(f"Replacing shader in {mat.name} to {to_shader.name}")
                input_links = {socket.name: socket.links[0].from_socket for socket in node.inputs if len(socket.links)>0}
                output_links = {socket.name: socket.links[0].to_socket for socket in node.outputs if len(socket.links)>0}

                node.node_tree = to_shader
                for name, socket in input_links.items():
                    this_socket = node.inputs[name]
                    mat.node_tree.links.new(this_socket, socket)
                for name, socket in output_links.items():
                    this_socket = node.outputs[name]
                    mat.node_tree.links.new(this_socket, socket)

replace_shader("BotW: Cel Shade", "BotW: Cel Shade - Skin", replace_poll_skin)
replace_shader("BotW: Cel Shade", "BotW: Cel Shade - Hair", replace_poll_hair)
