import bpy
from bpy.types import Context, Collection, LayerCollection


def ensure_collection(
    context: Context, collection_name: str, parent=None, hidden=False,
) -> Collection:
    """Check if a collection with a certain name exists.
    If yes, return it, if not, create it in the active collection.
    """
    collection = bpy.data.collections.get(collection_name)
    if not collection or collection.library:
        # Create the collection
        collection = bpy.data.collections.new(collection_name)
        collection.hide_viewport = hidden
        collection.hide_render = hidden


    # Let the new collection be a child of the active one or the passed parent.
    if not parent:
        parent = context.scene.collection
    if collection not in set(parent.children) and collection != parent:
        parent.children.link(collection)

    return collection


def recursive_search_layer_collection(
    coll_name: str, layer_coll: LayerCollection
) -> LayerCollection:
    # Recursivly transverse layer_collection for a particular name
    # This is the only way to set active collection as of 14-04-2020.
    found = None
    if layer_coll.name == coll_name:
        return layer_coll
    for layer in layer_coll.children:
        found = recursive_search_layer_collection(coll_name, layer)
        if found:
            return found


def set_active_collection(context, collection: Collection):
    layer_coll = context.view_layer.layer_collection

    layer_collection = recursive_search_layer_collection(collection.name, layer_coll)
    context.view_layer.active_layer_collection = layer_collection
