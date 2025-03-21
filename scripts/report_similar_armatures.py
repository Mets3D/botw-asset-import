import bpy

active_rig = bpy.context.active_object

other_rigs = [obj for obj in bpy.data.objects if obj.type == 'ARMATURE' and obj != active_rig]

differences = []
threshold = 0.001

for other_rig in other_rigs:
    diffs = []
    for bone in active_rig.data.bones:
        other_bone = other_rig.data.bones.get(bone.name)
        if not other_bone:
            # diffs.append("Extra bone: " + bone.name)
            continue
        transf_diff = max((bone.head - other_bone.head).length, (bone.tail - other_bone.tail).length)
        if transf_diff > threshold:
            diffs.append("Mismatch transform: " + bone.name + " " + str(transf_diff))
    for other_bone in other_rig.data.bones:
        if other_bone.name not in active_rig.data.bones:
            diffs.append("Missing bone: " + other_bone.name)
    differences.append((diffs, other_rig))

differences.sort(key=lambda tup: tup[0])
for diffs, obj in differences:
    if len(diffs) > 5:
        continue
    print()
    print(len(diffs), obj.name)
    for diff in diffs:
        print(diff)