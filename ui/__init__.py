module_names = (
    "ui_asset_metadata",
    "import_menu",
)


modules = [
    __import__(__package__ + "." + submod, {}, {}, submod)
    for submod in module_names
]