import bpy
from bpy.types import Context, Collection, LayerCollection


class ASSETBROWSER_OT_isolate_collection_asset(bpy.types.Operator):
    """Hide all collections except this one."""

    bl_idname = "ed.isolate_collection_asset"
    bl_label = "Isolate Collection"
    bl_options = {'REGISTER', 'UNDO'}

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
                continue
            if any([child in colls for child in coll.children_recursive]):
                colls.append(coll)

        for coll in context.scene.collection.children_recursive:
            layer_collection = find_layer_collection_by_collection(
                context.view_layer.layer_collection, coll
            )
            layer_collection.hide_viewport = coll not in colls

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
