import bpy
from bpy.types import Context, Collection, LayerCollection


def ensure_collection(
    context: Context, collection_name: str, hidden=False, exclude=False,
) -> Collection:
    """Check if a collection with a certain name exists.
    If yes, return it, if not, create it in the active collection.
    """
    view_layer = context.view_layer
    active_layer_coll = context.layer_collection
    active_collection = active_layer_coll.collection

    collection = bpy.data.collections.get(collection_name)
    if not collection or collection.library:
        # Create the collection
        collection = bpy.data.collections.new(collection_name)
        collection.hide_viewport = hidden
        collection.hide_render = hidden

        layer_collection = None
    else:
        layer_collection = find_layer_collection_by_collection(
            view_layer.layer_collection, collection
        )

    if not layer_collection:
        # Let the new collection be a child of the active one.
        active_collection.children.link(collection)
        layer_collection = [
            c for c in active_layer_coll.children if c.collection == collection
        ][0]

        layer_collection.exclude = exclude

    return collection


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
