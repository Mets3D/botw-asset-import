import bpy
from bpy.props import BoolProperty
from bpy.types import Collection, LayerCollection

# TODO: support objects!

class ASSETBROWSER_OT_focus_asset(bpy.types.Operator):
    """Bring this asset into focus (Supports Collections, Actions)."""

    bl_idname = "asset.focus_asset"
    bl_label = "Focus Asset"
    bl_options = {'REGISTER', 'UNDO'}

    focus_view: BoolProperty(name="Focus View")

    @staticmethod
    def guess_user_intent(context):
        if not hasattr(context, 'id'):
            return ''
        active_action = context.id and type(context.id) == bpy.types.Action
        active_armature = context.active_object and context.active_object.type == 'ARMATURE'
        if active_action and active_armature:
            return 'ACTION'
        any_colls =  any([type(id) == bpy.types.Collection for id in context.selected_ids])
        if any_colls:
            return 'COLLECTION'

    @classmethod
    def poll(cls, context):
        user_intent = cls.guess_user_intent(context)
        if not user_intent:
            cls.poll_message_set("No focusable asset.")
            return False
        return True

    def execute(self, context):
        user_intent = self.guess_user_intent(context)
        if user_intent == 'COLLECTION':
            self.report({'INFO'}, f"Focus {len([c for c in context.selected_ids if type(c) == bpy.types.Collection])} collection(s)")
            return self.focus_collection(context)
        elif user_intent == 'ACTION':
            self.report({'INFO'}, f"Focus Action: {context.id.name}")
            return self.focus_action(context)

        self.report({'ERROR'}, "Nothing to focus.")
        return {'CANCELLED'}

    def focus_action(self, context):
        rig = context.active_object
        action = context.id
        if not rig.animation_data:
            rig.animation_data_create()

        rig.animation_data.action = action
        context.scene.frame_start = int(action.curve_frame_range.x)
        context.scene.frame_end = int(action.curve_frame_range.y)

        if self.focus_view:
            org_selected = context.selected_objects[:]
            for obj in org_selected:
                obj.select_set(False)
            for obj in rig.children_recursive:
                obj.select_set(True)
            focus_selected_objects(context)
            # Restore selection
            for obj in rig.children_recursive:
                obj.select_set(False)
            for obj in org_selected:
                obj.select_set(True)

        return {'FINISHED'}

    def focus_collection(self, context):
        colls_to_isolate = []
        for id in context.selected_ids:
            # NOTE: There seem to be rare cases where an 
            # ID appears as selected here when it shouldn't.
            # If I knew how to reproduce it, I would report it.
            if type(id) == bpy.types.Collection:
                colls_to_isolate.append(id)

        if not colls_to_isolate:
            self.report({'ERROR'}, "No collection asset selected.")
            return {'FINISHED'}

        for coll in bpy.data.collections:
            if coll in colls_to_isolate:
                # Children of selected collections
                colls_to_isolate += coll.children_recursive
                continue
            # Parents of selected collections
            if any([child in colls_to_isolate for child in coll.children_recursive]):
                colls_to_isolate.append(coll)

        for coll in context.scene.collection.children_recursive:
            layer_collection = find_layer_collection_by_collection(
                context.view_layer.layer_collection, coll
            )
            if layer_collection:
                layer_collection.hide_viewport = coll not in colls_to_isolate

        if self.focus_view:
            bpy.ops.object.select_all(action='DESELECT')
            for coll in colls_to_isolate:
                for obj in coll.all_objects:
                    obj.select_set(True)
                focus_selected_objects(context)
            

        return {'FINISHED'}

def focus_selected_objects(context):
    org_mode = context.active_object.mode
    if org_mode != 'OBJECT':
        bpy.ops.object.mode_set(mode='OBJECT')
    for area in context.screen.areas:
        if area.type == 'VIEW_3D':
            region = next(r for r in area.regions if r.type=='WINDOW')
            with context.temp_override(area=area, region=region):
                bpy.ops.view3d.view_selected()
            break
    if org_mode != 'OBJECT':
        bpy.ops.object.mode_set(mode=org_mode)

def find_layer_collection_by_collection(
    layer_collection: LayerCollection, collection: Collection
) -> LayerCollection | None:
    if collection == layer_collection.collection:
        return layer_collection

    # go recursive
    for child in layer_collection.children:
        layer_collection = find_layer_collection_by_collection(child, collection)
        if layer_collection:
            return layer_collection

registry = [ASSETBROWSER_OT_focus_asset]

def draw_isolate_coll(self, context):
    self.layout.operator(ASSETBROWSER_OT_focus_asset.bl_idname, icon='HIDE_OFF')

def register():
    bpy.types.ASSETBROWSER_MT_context_menu.append(draw_isolate_coll)

def unregister():
    bpy.types.ASSETBROWSER_MT_context_menu.remove(draw_isolate_coll)
