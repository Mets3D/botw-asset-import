# These submodules should be kept mostly add-on agnostic and reusable.

module_names = (
    "action",
    "catalogs",
    "collections",
    "dae_fixer",
    "deduplicate_materials",
    "pixel_image",
    "progressbar",
    "timer",
    "widgets",
)


modules = [
    __import__(__package__ + "." + submod, {}, {}, submod)
    for submod in module_names
]