module_names = [
    "build_asset_library",
    "build_asset"
]

modules = [
    __import__(__package__ + "." + submod, {}, {}, submod)
    for submod in module_names
]