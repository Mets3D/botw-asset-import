# These submodules should be kept mostly add-on agnostic and reusable.

module_names = (
    "catalogs",
    "collections",
    "deduplicate_materials",
    "progressbar",
    "timer",
    "pixel_image",
)


modules = [
    __import__(__package__ + "." + submod, {}, {}, submod)
    for submod in module_names
]