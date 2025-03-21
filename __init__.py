# SPDX-License-Identifier: GPL-3.0-or-later

from bpy.utils import register_class, unregister_class
import importlib

module_names = (
    "matcap",
    "utils",
    "botw_batch_fbx_import",
    "asset_names",
    "widgets",
    "prefs",
    "op_actions_merge",
    "op_armature_constrain_outfit",
    "op_armature_merge_outfit",
    "op_focus_asset",
    "op_rename_asset",
    "op_thumbnail_from_viewport",
    "io_anim_seanim",
    "batch_import_seanim",
    "dae_fixer",
    "ui_asset_metadata",
    "cleanup",
)


modules = [
    __import__(__package__ + "." + submod, {}, {}, submod)
    for submod in module_names
]

def register_unregister_modules(modules: list, register: bool):
    """Recursively register or unregister modules by looking for either
    un/register() functions or lists named `registry` which should be a list of
    registerable classes.
    """
    register_func = register_class if register else unregister_class
    un = 'un' if not register else ''

    for m in modules:
        if register:
            importlib.reload(m)
        if hasattr(m, 'registry'):
            for c in m.registry:
                try:
                    register_func(c)
                except Exception as e:
                    print(
                        f"Warning: Pie Menus failed to {un}register class: {c.__name__}"
                    )
                    print(e)

        if hasattr(m, 'modules'):
            register_unregister_modules(m.modules, register)

        if register and hasattr(m, 'register'):
            m.register()
        elif hasattr(m, 'unregister'):
            m.unregister()


def register():
    register_unregister_modules(modules, True)

def unregister():
    register_unregister_modules(reversed(modules), False)
