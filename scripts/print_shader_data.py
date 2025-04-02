import json
print(json.dumps(json.loads(bpy.context.active_object.data.materials[0]['shader_data']), indent=2))