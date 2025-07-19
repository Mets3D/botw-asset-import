import bpy
from ...utils.resources import ensure_lib_datablock

def ensure_botw_scene_settings(context):
    # Zelda shaders absolutely depend on EEVEE.
    context.scene.render.engine = 'BLENDER_EEVEE_NEXT'

    # Set sRGB view transform, as that's what the game probably uses.
    context.scene.view_settings.view_transform = 'Standard'

    # Set some settings that make things prettier. (and more expensive of course)
    context.scene.eevee.use_shadow_jitter_viewport = True
    context.scene.eevee.use_raytracing = True
    context.scene.eevee.ray_tracing_options.resolution_scale = '16'

    if context.scene.world:
        context.scene.world.use_fake_user = True
    context.scene.world = ensure_world_and_lights(context)

    if not context.scene.use_nodes:
        # Enable compositing nodes.
        context.scene.use_nodes = True
        nodetree = context.scene.node_tree
        nodes = nodetree.nodes
        links = nodetree.links
        # Add a Bloom node at the end of the compositing node tree.
        output_node = nodes['Composite']
        previous_socket = output_node.inputs[0].links[0].from_socket
        bloom_node = nodes.new("CompositorNodeGlare")
        bloom_node.glare_type = 'BLOOM'
        bloom_node.quality = 'HIGH'
        bloom_node.inputs['Size'].default_value = 0.15
        bloom_node.inputs['Strength'].default_value = 2.0
        links.new(previous_socket, bloom_node.inputs['Image'])
        links.new(bloom_node.outputs['Image'], output_node.inputs['Image'])
        if bpy.app.version >= (4, 5, 0):
            viewer = nodes['Viewer']
            links.new(bloom_node.outputs['Image'], viewer.inputs['Image'])

    # Set viewport shading to the BotW MatCap.
    for area in context.screen.areas:
        if area.type == 'VIEW_3D':
            area.spaces.active.shading.type = 'SOLID'
            area.spaces.active.shading.light = 'MATCAP'
            try:
                area.spaces.active.shading.studio_light = 'botw.exr'
            except TypeError:
                # Blender has to be restarted after enabling the add-on for this to work, sigh...
                pass
            area.spaces.active.shading.color_type = 'TEXTURE'
            # Enable viewport compositing for bloom.
            area.spaces.active.shading.use_compositor = 'ALWAYS'

def ensure_world_and_lights(context) -> bpy.types.World:
    """Append BotW world from resources.blend, important for its custom properties
    and drivers. This also brings special lights, hooked up to said properties.
    These properties are then referenced by the shaders via Attribute nodes.
    This way of referencing world properties is 100x faster than using drivers.

    Also de-duplicate resulting light objects and nested node trees.
    """
    world = ensure_lib_datablock('worlds', "BotW Lights", link=False)

    # Ensure the lighting objects are linked to the scene and de-duplicated.
    for obj in bpy.data.objects[:]:
        if 'LGT-botw' in obj.name:
            if obj.name.endswith(".001"):
                existing = bpy.data.objects.get(obj.name[:-4])
                obj.user_remap(existing)
                bpy.data.objects.remove(obj)
                obj = existing
            if obj not in set(context.scene.collection.all_objects):
                context.scene.collection.objects.link(obj)

    return world
