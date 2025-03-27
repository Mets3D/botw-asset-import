module_names = (
    "botw_batch_asset_import",
    "botw_batch_seanim_import",
    "botw_file_cleanup",
    "actions_merge",
    "armature_constrain_outfit",
    "armature_merge_outfit",
    "asset_focus",
    "asset_rename",
    "asset_thumbnail_render",
)


modules = [
    __import__(__package__ + "." + submod, {}, {}, submod)
    for submod in module_names
]