import bpy
from mathutils import Matrix, Vector, Euler, Quaternion
from math import radians as rad

def get_fcurve_set(bone_name, action):
    loc_x = action.fcurves.find(f'pose.bones["{bone_name}"].location', index=0)
    loc_y = action.fcurves.find(f'pose.bones["{bone_name}"].location', index=1)
    loc_z = action.fcurves.find(f'pose.bones["{bone_name}"].location', index=2)

    rot_w = action.fcurves.find(f'pose.bones["{bone_name}"].rotation_quaternion', index=0)
    rot_x = action.fcurves.find(f'pose.bones["{bone_name}"].rotation_quaternion', index=1)
    rot_y = action.fcurves.find(f'pose.bones["{bone_name}"].rotation_quaternion', index=2)
    rot_z = action.fcurves.find(f'pose.bones["{bone_name}"].rotation_quaternion', index=3)

    scale_x = action.fcurves.find(f'pose.bones["{bone_name}"].scale', index=0)
    scale_y = action.fcurves.find(f'pose.bones["{bone_name}"].scale', index=1)
    scale_z = action.fcurves.find(f'pose.bones["{bone_name}"].scale', index=2)

    loc = (loc_x, loc_y, loc_z)
    rot = (rot_w, rot_x, rot_y, rot_z)
    scale = (scale_x, scale_y, scale_z)
    return (loc, rot, scale)

def eval_fcurves_to_matrix(fc_loc, fc_rot, fc_scale, frame):
    loc_x, loc_y, loc_z = fc_loc
    rot_w, rot_x, rot_y, rot_z = fc_rot
    scale_x, scale_y, scale_z = fc_scale
    
    loc = Vector((loc.evaluate(frame) for loc in fc_loc))
    rot = Quaternion((rot.evaluate(frame) for rot in fc_rot))
    scale = Vector((scale.evaluate(frame) for scale in fc_scale))

    return Matrix.LocRotScale(loc, rot, scale)

def eval_bone_at_frame(action, bone_name, frame):
    return eval_fcurves_to_matrix(*get_fcurve_set(bone_name, action), frame)

def apply_matrices_to_action(frames, matrices, action, bone_name):
    fcurve_tuples = get_fcurve_set(bone_name, action)

    for frame, mat in zip(frames, matrices):
        loc = mat.to_translation()
        rot = mat.to_quaternion()
        scale = mat.to_scale()

        for fcurve_tuple, transform in zip(fcurve_tuples, (loc, rot, scale)):
            for fcurve, value in zip(fcurve_tuple, transform):
                fcurve.keyframe_points.insert(frame, value)

def transform_bone_in_actions(bone_name, actions, transformation):
    for action in actions:
        start, end = action.curve_frame_range
        end += 1

        frame_numbers = list(range(int(start), int(end)))

        matrices = [eval_bone_at_frame(action, bone_name, frame) @ transformation for frame in frame_numbers]

        assert len(frame_numbers) == len(matrices)

        apply_matrices_to_action(frame_numbers, matrices, action, bone_name)

transform_bone_in_actions(
    bone_name = "Root", 
    actions = [bpy.data.actions['Wolf: Move_Trot_Curve_L']],
    transformation = Matrix.LocRotScale(
        Vector((0, 0, 0)),
        Euler((-rad(90), 0, 0)),
        Vector((1, 1, 1))
    )
)