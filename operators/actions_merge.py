import bpy


class ASSET_OT_merge_actions(bpy.types.Operator):
    """Merge two or more selected actions into the active one. In the case of conflicts, the fcurves of the active action are used, and the rest discarded."""

    bl_idname = "asset.merge_actions"
    bl_label = "Merge Actions"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        if (
            not hasattr(context, 'id') or 
            not context.id or
            type(context.id) != bpy.types.Action
        ):
            cls.poll_message_set("No active action.")
            return False
        sel_actions = [a for a in context.selected_ids if type(a) == bpy.types.Action]
        if len(sel_actions) < 2:
            cls.poll_message_set("Select more than one action.")
            return False

        return True

    def execute(self, context):
        active = context.id
        others = [a for a in context.selected_ids if type(a) == bpy.types.Action and a != active]

        try:
            merge_actions(active, others)
        except Exception as exc:
            self.report({'ERROR'}, str(exc))
            return {'CANCELLED'}

        self.report({'INFO'}, f"Merged {len(others)} action(s) into {active.name}.")

        return {'FINISHED'}

def merge_actions(destination: bpy.types.Action, others: list[bpy.types.Action]):
    """
    Merges selected actions into a new action.
    Raises an error if multiple actions attempt to animate the same bone, except for 'Root'.
    """
    merged_fcurves = {}

    for action in others:
        for fcurve in action.fcurves:
            data_path = fcurve.data_path
            array_index = fcurve.array_index
            key = (data_path, array_index)
            
            existing = destination.fcurves.find(data_path, index=array_index)
            if existing:
                if "Root" in data_path:
                    continue
                raise ValueError(f"Conflict detected: {data_path}[{array_index}] is animated in multiple actions.")
            else:
                new_fcurve = destination.fcurves.new(data_path, index=array_index)
                new_fcurve.keyframe_points.add(count=len(fcurve.keyframe_points))
                for i, kf in enumerate(fcurve.keyframe_points):
                    new_fcurve.keyframe_points[i].co = kf.co
                    new_fcurve.keyframe_points[i].interpolation = kf.interpolation
                merged_fcurves[key] = new_fcurve
        action.user_remap(destination)
    
    for action in others:
        bpy.data.actions.remove(action)

    return destination

registry = [ASSET_OT_merge_actions]

def draw_merge_actions(self, context):
    if context.id and type(context.id) == bpy.types.Action:
        self.layout.operator(ASSET_OT_merge_actions.bl_idname)

def register():
    if bpy.app.version < (4, 5, 0):
        bpy.types.ASSETBROWSER_MT_asset.append(draw_merge_actions)
    else:
        bpy.types.ASSETBROWSER_MT_metadata_preview_menu.append(draw_merge_actions)

def unregister():
    try:
        if bpy.app.version < (4, 5, 0):
            bpy.types.ASSETBROWSER_MT_asset.remove(draw_merge_actions)
        else:
            bpy.types.ASSETBROWSER_MT_metadata_preview_menu.remove(draw_merge_actions)
    except Exception:
        # Looks like Blender unregisters this class before the add-on?
        pass
