module_names = [
    "build_asset_library",
    "build_asset",
    "load_map_section",
    "unpack_map_sstera",
    "terrain_shared",
    "terrain",
]

modules = [
    __import__(__package__ + "." + submod, {}, {}, submod)
    for submod in module_names
]