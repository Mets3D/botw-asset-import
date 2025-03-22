import re
from math import isclose

def bonename_from_data_path(data_path):
    match = re.search(r'pose\.bones\["(.*?)"\]', data_path)
    return match.group(1) if match else None

def fix_groups(action) -> int:
    count = 0
    for fcurve in action.fcurves:
        if not fcurve.group:
            bone_name = bonename_from_data_path(fcurve.data_path)
            group = action.groups.get(bone_name)
            if not group:
                group = action.groups.new(bone_name)
            fcurve.group = group
            count += 1
    return count

def remove_negative_frames(action) -> int:
    count = 0
    for fcurve in action.fcurves:
        for kf in fcurve.keyframe_points[:]:
            if kf.co.x < 0:
                fcurve.keyframe_points.remove(kf)
                count += 1
    return count

def remove_redundant_keyframes(action, threshold=1e-6) -> int:
    """
    Removes redundant keyframes from all F-Curves in the active action.
    A keyframe is considered redundant if it has the same value as its neighbors within a given threshold.
    """
    count = 0
    bad_fcurves = []
    for fcurve in action.fcurves:
        if not fcurve.keyframe_points:
            continue
        
        keyframes = fcurve.keyframe_points
        i = 1  # Start from second keyframe
        while i < len(keyframes) - 1:
            prev_kf = keyframes[i - 1]
            curr_kf = keyframes[i]
            next_kf = keyframes[i + 1]
            
            # Check if current keyframe is redundant (same value as before and after within threshold)
            if (
                abs(prev_kf.co.y - curr_kf.co.y) < threshold and
                abs(next_kf.co.y - curr_kf.co.y) < threshold
            ):
                keyframes.remove(curr_kf)
                count += 1
            else:
                i += 1  # Only increment if we didn't delete to avoid skipping elements

        values = []
        for kf in fcurve.keyframe_points:
            values.append(kf.co.y)

        def equalish(a, b, threshold=0.00001):
            return abs(a-b) < threshold

        if all([v==values[0] for v in values]):
            if (
                ("scale" in fcurve.data_path and equalish(values[0], 1)) or
                ("rotation" in fcurve.data_path and (equalish(values[0], 1) or equalish(values[0], 0))) or
                ("location" in fcurve.data_path and equalish(values[0], 0))
            ):
                bad_fcurves.append(fcurve)

    for fc in bad_fcurves:
        count += len(fc.keyframe_points)
        action.fcurves.remove(fc)

    return count
