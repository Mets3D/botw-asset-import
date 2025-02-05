# Install the BotW matcap.

import bpy, os, shutil

def get_matcap_filepath() -> str:
    filedir = os.path.dirname(os.path.realpath(__file__))
    matcap = os.sep.join([filedir, 'botw.exr'])
    return matcap

def register():
    datafiles = bpy.utils.user_resource('DATAFILES')
    matcaps_dir = os.path.join(datafiles, "studiolights\\matcap")
    matcap = get_matcap_filepath()
    final_path = os.path.join(matcaps_dir, "botw.exr")

    os.makedirs(os.path.dirname(final_path), exist_ok=True)
    shutil.copy(matcap, final_path)