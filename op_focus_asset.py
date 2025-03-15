import bpy
from bpy.props import BoolProperty
from .utils.collections import find_layer_collection_by_collection

# TODO: support objects!

class ASSETBROWSER_OT_focus_asset(bpy.types.Operator):
    """Bring this asset into focus. Supports these asset types:\nCollections (local only)\nActions (local & external)"""

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

        action = None
        if type(context.id) == bpy.types.Action:
            action = context.id
        elif context.asset and hasattr(context.asset, 'id_type') and context.asset.id_type == 'ACTION':
            import_method = context.area.spaces.active.params.import_method
            if import_method == 'FOLLOW_PREFS':
                import_method = context.preferences.filepaths.asset_library_import_method
            link = import_method == 'LINK'
            action = get_or_import_action(context.asset.name, context.asset.full_library_path, link=link)

        if action:
            focus_action(context, action, self.focus_view)
            self.report({'INFO'}, f"Focus Action: {context.asset.name}")

        if collections or action:
            return {'FINISHED'}
        else:
            self.report({'ERROR'}, "Nothing to focus.")
            return {'CANCELLED'}

def guess_asset_type(context):
    if not hasattr(context, 'id'):
        return ''
    active_asset = context.id or context.asset
    if type(active_asset) == bpy.types.Action or (hasattr(active_asset, 'id_type') and active_asset.id_type == 'ACTION'):
        active_armature = context.active_object and context.active_object.type == 'ARMATURE'
        if active_armature:
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
        focus_view_on_objects(context, rig.children_recursive)

    return {'FINISHED'}

def get_or_import_action(action_name, library_path, link=False):
    if action_name in bpy.data.actions:
        return bpy.data.actions[action_name]

    with bpy.data.libraries.load(library_path, relative=True, link=link) as (data_from, data_to):
        if action_name in data_from.actions:
            data_to.actions.append(action_name)

    return bpy.data.actions.get(action_name)

def focus_collections(context, collections, focus_view=True, operator=None):
    if not collections:
        if operator:
            operator.report({'ERROR'}, "No collection asset selected.")
        return {'FINISHED'}

    child_colls = []
    parent_colls = []
    for coll in bpy.data.collections:
        if coll in collections:
            # Children of selected collections
            child_colls += coll.children_recursive
            continue
        # Parents of selected collections
        if any([child in collections for child in coll.children_recursive]):
            parent_colls.append(coll)

    all_colls = collections + child_colls + parent_colls

    for coll in all_colls:
        coll.hide_viewport = False

    for coll in context.scene.collection.children_recursive:
        layer_collection = find_layer_collection_by_collection(
            context.view_layer.layer_collection, coll
        )
        if layer_collection:
            if coll not in all_colls:
                layer_collection.hide_viewport = True
            else:
                layer_collection.hide_viewport = False

    if focus_view:
        objs = []
        for coll in collections:
            objs += coll.all_objects
        focus_view_on_objects(context, objs)

    return {'FINISHED'}

def focus_view_on_objects(context, objects):
    org_selected = context.selected_objects[:]
    for obj in org_selected:
        obj.select_set(False)
    for obj in objects:
        try:
            obj.select_set(True)
        except RuntimeError:
            # If the object cannot be selected for any reason, whatever, it's not that important.
            pass
    focus_view_on_objects_without_ops(context, objects)
    # focus_selected_objects(context)
    # Restore selection
    for obj in objects:
        obj.select_set(False)
    for obj in org_selected:
        obj.select_set(True)

def focus_selected_objects(context):
    org_mode = context.active_object.mode if context.active_object else 'OBJECT'
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

def focus_view_on_objects_without_ops(context, objects=[]):
    """This tries to replicate bpy.ops.view3d.view_selected()
    and it's necessary because that operator refuses to work with context.temp_override(),
    which means executing it from any editor other than the 3D View doesn't work.
    And we need it to work from the asset browser.
    An alternative was to switch the asset browser to a 3D View temporarily,
    but this resulted in losing the scrollbar position (it resets to the top).
    """
    # Get the current 3D View region and space data
    area = next(a for a in context.screen.areas if a.type == 'VIEW_3D')
    region_3d = area.spaces.active.region_3d

    # Get the selected object(s)
    if not objects:
        objects = context.selected_objects

    if not objects:
        return

    # Calculate the bounding box of all selected objects
    min_bound = [float('inf'), float('inf'), float('inf')]
    max_bound = [-float('inf'), -float('inf'), -float('inf')]
    
    for obj in objects:
        for co in obj.bound_box:
            for i in range(3):  # X, Y, Z
                min_bound[i] = min(min_bound[i], co[i])
                max_bound[i] = max(max_bound[i], co[i])

    # Calculate the center of the bounding box
    center = [(min_bound[i] + max_bound[i]) / 2 for i in range(3)]

    # Adjust the view to center on the bounding box center
    region_3d.view_location = center  # Move the view's center to the selected object center

    # Optionally, adjust the view distance for zooming out/in based on the bounding box size
    size = max(max_bound[i] - min_bound[i] for i in range(3))  # Largest dimension of the bounding box
    region_3d.view_distance = size * 1.65  # Zoom out a little to fit the selected object(s) in view

registry = [ASSETBROWSER_OT_focus_asset]

def draw_focus_asset(self, context):
    self.layout.operator(ASSETBROWSER_OT_focus_asset.bl_idname, icon='HIDE_OFF')

def register():
    bpy.types.ASSETBROWSER_MT_context_menu.append(draw_focus_asset)

def unregister():
    bpy.types.ASSETBROWSER_MT_context_menu.remove(draw_focus_asset)
