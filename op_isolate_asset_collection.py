import bpy
from bpy.props import BoolProperty
from bpy.types import Collection, LayerCollection


class ASSETBROWSER_OT_isolate_collection_asset(bpy.types.Operator):
    """Hide all collections except this one."""

    bl_idname = "ed.isolate_collection_asset"
    bl_label = "Isolate Collection"
    bl_options = {'REGISTER', 'UNDO'}

    focus_view: BoolProperty(name="Focus View")

    def execute(self, context):
        collection = context.id
        if not collection or type(collection) != bpy.types.Collection:
            self.report({'ERROR'}, "No collection asset selected.")
            return {'FINISHED'}
        
        colls = []
        for id in context.selected_ids:
            if type(id) == bpy.types.Collection:
                colls.append(id)

        for coll in bpy.data.collections:
            if coll in colls:
                # Children of selected collections
                colls += coll.children_recursive
                continue
            # Parents of selected collections
            if any([child in colls for child in coll.children_recursive]):
                colls.append(coll)

        for coll in context.scene.collection.children_recursive:
            layer_collection = find_layer_collection_by_collection(
                context.view_layer.layer_collection, coll
            )
            layer_collection.hide_viewport = coll not in colls

        if self.focus_view:
            bpy.ops.object.select_all(action='DESELECT')
            for obj in collection.all_objects:
                obj.select_set(True)
            for area in context.screen.areas:
                if area.type == 'VIEW_3D':
                    region = next(r for r in area.regions if r.type=='WINDOW')
                    with context.temp_override(area=area, region=region):
                        bpy.ops.view3d.view_selected()
                    break

        return {'FINISHED'}

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

registry = [ASSETBROWSER_OT_isolate_collection_asset]

def draw_isolate_coll(self, context):
    self.layout.operator(ASSETBROWSER_OT_isolate_collection_asset.bl_idname, icon='HIDE_OFF')

def register():
    bpy.types.ASSETBROWSER_MT_context_menu.append(draw_isolate_coll)

def unregister():
    bpy.types.ASSETBROWSER_MT_context_menu.remove(draw_isolate_coll)
