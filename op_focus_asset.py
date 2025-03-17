import bpy
from bpy.props import BoolProperty
from .utils.collections import find_layer_collection_by_collection
from mathutils import Vector
from .utils.timer import Timer
from .ui_asset_metadata import get_asset_library

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

        asset = context.asset
        action = None
        if type(context.id) == bpy.types.Action:
            action = context.id
        elif asset and hasattr(asset, 'id_type') and asset.id_type == 'ACTION':
            import_method = context.area.spaces.active.params.import_method
            if import_method == 'FOLLOW_PREFS':
                asset_library = get_asset_library(context, asset)
                if asset_library:
                    import_method = asset_library.import_method
                else:
                    # This is only if asset_library is None, which should never happen.
                    import_method = 'APPEND'
            link = import_method == 'LINK'
            action = get_or_import_action(asset.name, asset.full_library_path, link=link)

        if action:
            focus_action(context, action, self.focus_view and action.library)
            self.report({'INFO'}, f"Focus Action: {asset.name}")

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
        with Timer("Focus View"):
            focus_view_on_objects(context, objs)

    return {'FINISHED'}

def focus_view_on_objects(context, objects=[]):
    if not objects:
        objects = context.selected_objects
    fit_view3d_to_coords(context, *get_bbox_3d(objects))

def fit_view3d_to_coords(context, center, coords):
    area = next(a for a in context.screen.areas if a.type == 'VIEW_3D')
    if not area:
        return
    space_data = area.spaces.active
    region_3d = space_data.region_3d
    use_temp_cam = False
    camera = None
    if region_3d.view_perspective == 'CAMERA' and space_data.lock_camera:
        if space_data.use_local_camera:
            camera = space_data.camera
        else:
            camera = context.scene.camera
    if not camera:
        use_temp_cam = True
        org_cam = context.scene.camera
        org_persp = region_3d.view_perspective
        cam_data = bpy.data.cameras.new(name="temp_Camera")
        if region_3d.view_perspective == 'ORTHO':
            cam_data.type = 'ORTHO'
        cam_data.sensor_width = 72
        cam_data.lens = space_data.lens

        camera = bpy.data.objects.new("temp_Camera", object_data=cam_data)
        camera.matrix_world = region_3d.view_matrix.inverted()
        context.scene.collection.objects.link(camera)
        context.scene.camera = camera
        region_3d.view_perspective = 'CAMERA'

    coords = [co for corner in coords for co in corner]
    depsgraph = context.evaluated_depsgraph_get()
    camera.location, ortho_scale = camera.camera_fit_coords(depsgraph, coords)
    if camera.data.type == 'ORTHO':
        camera.data.ortho_scale = ortho_scale

    context.view_layer.update()

    if use_temp_cam:
        region_3d.view_perspective = org_persp
        cam_matrix = camera.matrix_world.inverted()
        distance = (camera.matrix_world.translation - center).length
        if org_persp == 'ORTHO':
            region_3d.view_distance = camera.data.ortho_scale * space_data.lens / 72
        else:
            region_3d.view_distance = distance

        bpy.data.objects.remove(camera)
        bpy.data.cameras.remove(cam_data)
        region_3d.view_matrix = cam_matrix
        context.scene.camera = org_cam

def get_bbox_3d(objects) -> tuple[Vector, list[Vector]]:
    """Return combined transformed bounding box center and 8 corners in world space."""
    min_bound = [float('inf'), float('inf'), float('inf')]
    max_bound = [-float('inf'), -float('inf'), -float('inf')]
    
    for obj in objects:
        for co in get_world_bounding_box(obj):
            for i in range(3):  # X, Y, Z
                min_bound[i] = min(min_bound[i], co[i])
                max_bound[i] = max(max_bound[i], co[i])

    # Calculate the center of the bounding box
    center = Vector([(min_bound[i] + max_bound[i]) / 2 for i in range(3)])

    # Construct the 8 bounding box corners from the min/max X/Y/Z coords.
    corners = [
        Vector((min_bound[0], min_bound[1], min_bound[2])),
        Vector((min_bound[0], min_bound[1], max_bound[2])),
        Vector((min_bound[0], max_bound[1], min_bound[2])),
        Vector((min_bound[0], max_bound[1], max_bound[2])),
        Vector((max_bound[0], min_bound[1], min_bound[2])),
        Vector((max_bound[0], min_bound[1], max_bound[2])),
        Vector((max_bound[0], max_bound[1], min_bound[2])),
        Vector((max_bound[0], max_bound[1], max_bound[2])),
    ]

    return center, corners

def get_world_bounding_box(obj) -> list[Vector]:
    """Returns the world-space coordinates of an object's bounding box."""
    # Get the 8 local-space bounding box corners
    local_bbox_corners = [Vector(corner) for corner in obj.bound_box]
    # Convert to world space using matrix_world
    world_bbox_corners = [obj.matrix_world @ corner for corner in local_bbox_corners]
    
    return world_bbox_corners

registry = [ASSETBROWSER_OT_focus_asset]

def draw_focus_asset(self, context):
    self.layout.operator(ASSETBROWSER_OT_focus_asset.bl_idname, icon='HIDE_OFF')

def register():
    bpy.types.ASSETBROWSER_MT_context_menu.append(draw_focus_asset)

def unregister():
    bpy.types.ASSETBROWSER_MT_context_menu.remove(draw_focus_asset)
