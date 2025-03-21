import bpy, hashlib

DECIMALS = 8

def deduplicate_actions(actions):
    """Crunch relevant data into a hash, then user remap if this hash already existed."""

    act_hashes = {}
    copy_counter = {}
    for action in sorted(actions, key=lambda a: a.name):
        act_hash = hash_action(action)
        if act_hash in act_hashes:
            print(f"Duplicate action: '{action.name}' -> {act_hashes[act_hash].name}")
            other_act = act_hashes[act_hash]
            action['is_duplicate_of'] = other_act
            if 'duplicates' not in other_act:
                other_act['duplicates'] = ""
            other_act['duplicates'] += ", " + action.get('filepath') or action.name
            if act_hash not in copy_counter:
                copy_counter[act_hash] = 0
            copy_counter[act_hash] += 1
        else:
            act_hashes[act_hash] = action

    for act_hash, count in copy_counter.items():
        print(f"{act_hashes[act_hash].name} had {count} duplicates.")

    for act in actions[:]:
        if 'is_duplicate_of' in act and 'is_duplicate_of' not in act['is_duplicate_of']:
            print("Removing ", act.name)
            bpy.data.actions.remove(act)

def hash_action(action) -> str:
    hash_str = ""
    for layer in action.layers:
        hash_str += "Layer"
        for strip in layer.strips:
            hash_str += "Strip"
            for channelbag in strip.channelbags:
                slot = channelbag.slot
                hash_str += "ChannelBag: " + slot.identifier
                for fcurve in channelbag.fcurves:
                    hash_str += f"FCurve: {fcurve.data_path} ({fcurve.array_index})"
                    for kf in fcurve.keyframe_points:
                        hash_str += f"x: {round(kf.co.x, DECIMALS)}, y: {round(kf.co.y, DECIMALS)}"

    return hashlib.md5(hash_str.encode("utf-8")).hexdigest()

deduplicate_actions(bpy.data.actions)