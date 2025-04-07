import bpy
import sys
import importlib

def main():
    argv = sys.argv

    blend_path = argv[-1]
    dae_path = argv[-2]

    # Since this is now running in a whole separate Blender and Python instance, we need to import things as if we were inside of Blender.
    botw_import_addon = import_addon_module("botw_asset_import")

    context = bpy.context

    try:
        botw_import_addon.operators.botw_batch_asset_import.ensure_caches(shared_mem_name="BOTW_ASSET_CACHE")
        botw_import_addon.operators.botw_batch_asset_import.import_and_process_dae(context, dae_path)
        bpy.ops.outliner.orphans_purge()
        # NOTE: This could be more optimized if we moved the images and changed their paths, we wouldn't have to save twice,
        # but we would have to write more code which would be more opportunity for error so this feels safer.
        bpy.ops.file.pack_all()
        bpy.ops.wm.save_as_mainfile(filepath=blend_path)
        bpy.ops.file.unpack_all(method='USE_LOCAL')
        bpy.ops.wm.save_as_mainfile(filepath=blend_path, compress=True)
        # Change the library path to point at the resources.blend copy 
        # that's in the asset folder, rather than the add-on's folder.
        for lib in bpy.data.libraries:
            if "resources.blend" in lib.filepath:
                lib.filepath = "//resources.blend"
    except Exception as exc:
        print(f"Failed to import: {dae_path}")
        raise exc


def import_addon_module(module_name):
    import bl_ext
    for repo_name in dir(bl_ext):
        if repo_name.startswith("__"):
            continue
        try:
            # Try to import the module within this repository
            full_module_name = f"bl_ext.{repo_name}.{module_name}"
            module = importlib.import_module(full_module_name)
            return module
        except ModuleNotFoundError:
            # Module wasn't found in this repository, continue checking
            continue
    return None

if __name__ == "__main__":
    main()
