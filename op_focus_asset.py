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

    @classmethod
    def poll(cls, context):
        asset_type = guess_asset_type(context)
        if not asset_type:
            cls.poll_message_set("No focusable asset.")
            return False
        return True

    def execute(self, context):
        collections = [id for id in context.selected_ids if type(id)==bpy.types.Collection]
        if collections:
            focus_collections(context, collections, self.focus_view, self)
            self.report({'INFO'}, f"Focused {len([collections])} collection(s)")
            
        actions = [id for id in context.selected_ids if type(id)==bpy.types.Action]
        if actions:
            for action in actions:
                focus_action(context, action, self.focus_view)
            self.report({'INFO'}, f"Focus Action: {context.id.name}")

        if collections or actions:
            return {'FINISHED'}
        else:
            self.report({'ERROR'}, "Nothing to focus.")
            return {'CANCELLED'}

def guess_asset_type(context):
    if not hasattr(context, 'id'):
        return ''
    active_action = context.id and type(context.id) == bpy.types.Action
    active_armature = context.active_object and context.active_object.type == 'ARMATURE'
    if active_action and active_armature:
        return 'ACTION'
    any_colls =  any([type(id) == bpy.types.Collection for id in context.selected_ids])
    if any_colls:
        return 'COLLECTION'

def focus_action(context, action, focus_view=True):
    rig = context.active_object
    if rig.type != 'ARMATURE' or not rig.visible_get():
        return {'CANCELLED'}

    if not rig.animation_data:
        rig.animation_data_create()

    for pb in rig.pose.bones:
        pb.matrix_basis.identity()
    rig.animation_data.action = action
    context.scene.frame_start = int(action.curve_frame_range.x)
    context.scene.frame_end = int(action.curve_frame_range.y)

    if focus_view:
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

def focus_collections(context, collections, focus_view=True, operator=None):
    if not collections:
        if operator:
            operator.report({'ERROR'}, "No collection asset selected.")
        return {'FINISHED'}

    for coll in bpy.data.collections:
        if coll in collections:
            # Children of selected collections
            collections += coll.children_recursive
            continue
        # Parents of selected collections
        if any([child in collections for child in coll.children_recursive]):
            collections.append(coll)

    for coll in context.scene.collection.children_recursive:
        layer_collection = find_layer_collection_by_collection(
            context.view_layer.layer_collection, coll
        )
        if layer_collection:
            layer_collection.hide_viewport = coll not in collections

    if focus_view:
        bpy.ops.object.select_all(action='DESELECT')
        for coll in collections:
            for obj in coll.all_objects:
                obj.select_set(True)
            focus_selected_objects(context)

    return {'FINISHED'}

def focus_selected_objects(context):
    org_mode = context.active_object.mode
    if org_mode != 'OBJECT':
        bpy.ops.object.mode_set(mode='OBJECT')
    area = next(a for a in context.screen.areas if a.type == 'VIEW_3D')
    region = next(r for r in area.regions if r.type=='WINDOW')
    org_area = context.area.ui_type
    context.area.ui_type = 'VIEW_3D'
    context.area.tag_redraw()
    with context.temp_override(area=area, region=region):
        bpy.ops.view3d.view_selected()
    if org_mode != 'OBJECT':
        bpy.ops.object.mode_set(mode=org_mode)
    context.area.ui_type = org_area

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

def draw_focus_asset(self, context):
    self.layout.operator(ASSETBROWSER_OT_focus_asset.bl_idname, icon='HIDE_OFF')

def register():
    bpy.types.ASSETBROWSER_MT_context_menu.append(draw_focus_asset)

def unregister():
    bpy.types.ASSETBROWSER_MT_context_menu.remove(draw_focus_asset)
