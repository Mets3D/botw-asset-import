import bpy
from bpy.types import Context, Collection


def ensure_collection(
    context: Context, collection_name: str, parent=None, hidden=False,
) -> Collection:
    """Check if a collection with a certain name exists.
    If yes, return it, if not, create it in the active collection.
    """
    view_layer = context.view_layer

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
