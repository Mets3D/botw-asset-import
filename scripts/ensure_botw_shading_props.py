import bpy

# Driving shader node properties directly is a massive hit on performance.
# Instead, we can use Attribute shader nodes, which can then reference World custom properties, which can be driven.
# This script needs to run once per scene that has BotW shading and lights, to create those properties and drivers.

# This script can be ran if you want BotW lighting to function in a given scene, without replacing its World.
# The necessary properties and drivers will be created on the active World.

def create_world_properties():
    scene = bpy.context.scene
    sun = bpy.data.objects.get('LGT-botw-sun')
    sun_z = bpy.data.objects.get('LGT-botw-sun_z_axis')
    sphere_light = bpy.data.objects.get('LGT-botw-sphere_light')
    assert sun, "Sun object missing: LGT-botw-sun"
    assert sun_z, "Sun Z-axis helper missing: LGT-botw-sun_z_axis"
    assert sphere_light, "Sphere light missing: LGT-botw-sphere_light"

    world = scene.world
    if not world:
        world = bpy.data.worlds.new("BotW Lighting")
        scene.world = world

    # Sun Rotation
    world['Sun Rotation'] = (0.0, 0.0, 0.0)
    world.id_properties_ui('Sun Rotation').update(subtype='EULER')
    world.driver_remove('["Sun Rotation"]')
    for i, axis in enumerate("XYZ"):
        drv_rot = world.driver_add('["Sun Rotation"]', i).driver
        drv_rot.type = 'MIN'
        var = drv_rot.variables.new()
        var.type = 'TRANSFORMS'
        var.targets[0].id = sun
        var.targets[0].transform_type = "ROT_"+axis

    # Sun Z Rotation
    world['Sun Z Rotation'] = 0.0
    world.driver_remove('["Sun Z Rotation"]')
    drv_z = world.driver_add('["Sun Z Rotation"]').driver
    drv_z.type = 'MIN'
    var = drv_z.variables.new()
    var.type = 'TRANSFORMS'
    var.targets[0].id = sun_z
    var.targets[0].transform_type = "ROT_Z"

    # Sun/Sphere Color
    for name, obj in (('Sun', sun), ('Sphere', sphere_light)):
        world[f"{name} Color"] = (1.9, 1.0, 1.0)
        world.id_properties_ui(f'{name} Color').update(subtype='COLOR_GAMMA')
        world.driver_remove(f'["{name} Color"]')
        for i, col in enumerate("RGB"):
            drv_sun_color = world.driver_add(f'["{name} Color"]', i).driver
            drv_sun_color.type = 'MIN'
            var = drv_sun_color.variables.new()
            var.targets[0].id = obj
            var.targets[0].data_path = f'data.color[{i}]'

        # Sun/Sphere Brightness
        world[f'{name} Brightness'] = 1.0
        world.driver_remove(f'["{name} Brightness"]')
        drv_sun_bright = world.driver_add(f'["{name} Brightness"]').driver
        drv_sun_bright.type = 'MIN'
        var = drv_sun_bright.variables.new()
        var.targets[0].id = obj
        var.targets[0].data_path = 'data.energy'

    # Sphere Location
    world['Sphere Location'] = (0.0, 0.0, 0.0)
    world.id_properties_ui('Sphere Location').update(subtype='EULER')
    world.driver_remove('["Sphere Location"]')
    for i, axis in enumerate("XYZ"):
        drv_rot = world.driver_add('["Sphere Location"]', i).driver
        drv_rot.type = 'MIN'
        var = drv_rot.variables.new()
        var.type = 'TRANSFORMS'
        var.targets[0].id = sphere_light
        var.targets[0].transform_type = "LOC_"+axis

    # Sphere Radius
    world['Sphere Radius'] = 1.0
    drv_radius = world.driver_add(f'["Sphere Radius"]').driver
    drv_radius.type = 'MIN'
    var = drv_radius.variables.new()
    var.targets[0].id = obj
    var.targets[0].data_path = f'data.shadow_soft_size'

    # Time Seconds
    world['Time Seconds'] = 0.0
    world.id_properties_ui('Sun Rotation').update(min=-1.7976931348623157e+308, max=1.7976931348623157e+308)
    drv_time = world.driver_add(f'["Time Seconds"]').driver
    drv_time.expression = "frame / var"
    var = drv_time.variables.new()
    var.type = 'CONTEXT_PROP'
    var.targets[0].context_property = 'ACTIVE_SCENE'
    var.targets[0].data_path = 'render.fps'

create_world_properties()