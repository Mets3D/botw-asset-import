# These submodules should be kept mostly add-on agnostic and reusable.

module_names = (
    "action",
    "catalogs",
    "collections",
    "dae_fixer",
    "material",
    "pixel_image",
    "progressbar",
    "timer",
    "resources",
    "mesh",
    "string",
)


modules = [
    __import__(__package__ + "." + submod, {}, {}, submod)
    for submod in module_names
]