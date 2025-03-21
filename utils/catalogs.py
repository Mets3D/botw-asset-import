import bpy
import os

def get_catalog_map() -> dict[str, str]:
    # Build a dictionary mapping catalog UUID -> full catalog path (slash-separated)
    catalogs = {}

    # Path to the asset catalog file
    blend_dir = os.path.dirname(bpy.data.filepath)
    catalog_file = os.path.join(blend_dir, "blender_assets.cats.txt")

    if os.path.exists(catalog_file):
        with open(catalog_file, "r") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                parts = line.split(":")
                if len(parts) >= 3:
                    uuid = parts[0]
                    catalog_path = parts[1]  # Use the slash-separated path directly
                    catalogs[uuid] = catalog_path

    return catalogs

def get_or_create_collection(collection_name):
    """
    Creates a new collection if it does not already exist.
    """
    collection = bpy.data.collections.get(collection_name)
    if not collection:
        collection = bpy.data.collections.new(name=collection_name)
        collection.hide_viewport = True
        print("New coll: ", collection.name)
    return collection

def get_or_create_nested_collection(path):
    """
    Recursively creates and nests collections based on a slash-separated path.
    Each level is created if it does not exist.
    """
    if "/" in path:
        parent_path = path.rsplit("/", 1)[0]  # Everything before the last "/"
    else:
        parent_path = None

    collection = get_or_create_collection(path)  # Create or get this collection

    # Determine the parent collection
    if parent_path:
        parent_collection = get_or_create_nested_collection(parent_path)
        if "/" not in parent_path and parent_collection not in set(bpy.context.scene.collection.children):
            bpy.context.scene.collection.children.link(parent_collection)
    else:
        parent_collection = bpy.context.scene.collection  # If no parent, link to root

    # Ensure the collection is parented correctly
    if collection not in set(parent_collection.children):
        parent_collection.children.link(collection)

    return collection

def delete_non_asset_collections(only_empty=True):
    for coll in bpy.data.collections[:]:
        if not coll.asset_data:
            if coll.all_objects and only_empty:
                continue
            for obj in coll.objects[:]:
                print("Deleting object: ", obj.name)
                bpy.data.objects.remove(obj)
            print("Deleting collection: ", coll.name)
            bpy.data.collections.remove(coll)

def asset_catalogs_to_scene_collection(context):
    """Organize scene collections by asset catalogs."""
    delete_non_asset_collections(only_empty=True)

    # Get the scene’s root collection and its children as a set
    scene_root = context.scene.collection
    scene_collections = set(scene_root.children)

    catalogs = get_catalog_map()

    # Iterate through all collections that are marked as assets
    for coll in bpy.data.collections:
        if not coll.asset_data:
            continue
        catalog_id = coll.asset_data.catalog_id
        if catalog_id not in catalogs:
            continue
        catalog_name = catalogs[catalog_id]
        catalog_collection = get_or_create_nested_collection(catalog_name)
        
        # Link the asset collection to the catalog collection if not already linked
        if coll not in set(catalog_collection.children):
            catalog_collection.children.link(coll)
        
        # Remove the asset collection from the scene’s root collection if it was there
        if coll in scene_collections:
            scene_root.children.unlink(coll)
