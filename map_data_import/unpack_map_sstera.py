import bpy, os, sys, subprocess

from pathlib import Path
from tqdm import tqdm

from ..prefs import get_addon_prefs

class FILE_OT_unpack_terrain(bpy.types.Operator):
    """Unpack the Terrain folder's .sstera files"""

    bl_idname = "file.unpack_botw_terrain"
    bl_label = "Unpack Terrain"
    bl_options = {'REGISTER', 'UNDO'}

    def update_terrain_dir(self, context):
        prefs = get_addon_prefs(context)
        if not prefs.terrain_folder:
            prefs.terrain_folder = (Path(self.terrain_dir) / Path("Terrain Unpack")).as_posix()
    terrain_dir: bpy.props.StringProperty(name="Terrain Folder", description="The game's content/Terrain/A/MainField/ folder", subtype='FILE_PATH', update=update_terrain_dir)

    def check_dir(self):
        num_files = sum(1 for _ in Path(self.terrain_dir).rglob("*.sstera"))
        return num_files

    def invoke(self, context, _event):
        # Workaround: Having file selectors inside pop-ups doesn't work with this user preference.
        self.org_pref = context.preferences.view.filebrowser_display_type
        context.preferences.view.filebrowser_display_type = 'WINDOW'
        try:
            ensure_oead()
        except Exception as exc:
            self.report({'ERROR'}, f"{exc}\nFailed to install oead (library that extracts .sstera files).\nYou likely don't have write permission to Blender's Python installation.\nYou must run as administrator or use portable Blender.")
            return {'CANCELLED'}

        return context.window_manager.invoke_props_dialog(self, width=500)

    def draw(self, context):
        layout = self.layout
        layout.label(text="Do not run this operator without a terminal open.", icon='ERROR')
        layout.use_property_split=True
        layout.prop(self, 'terrain_dir')
        if not self.check_dir():
            row = layout.row()
            row.alert = True
            row.label(text="No .sstera files in selected folder.", icon='ERROR')
            return

        prefs = get_addon_prefs(context)
        layout.prop(prefs, 'terrain_folder', text="Output Folder")

    def execute(self, context):
        num_files = self.check_dir()
        if num_files == 0:
            self.report({'ERROR'}, 'No .sstera files to extract.')
            return {'CANCELLED'}
        prefs = get_addon_prefs(context)

        bar_format = "Completed: {n_fmt}/{total_fmt} {percentage:3.1f}% ({elapsed_s:.2f}s){bar}"
        with tqdm(bar_format=bar_format, total=num_files) as pgbar:
            for dirpath, dirnames, files in os.walk(self.terrain_dir):
                for name in files:
                    if 'sstera' in name:
                        filepath = os.path.abspath(os.path.join(dirpath, name))

                        if 'hght' in filepath:
                            subdir = 'terrain'
                        elif 'mate' in filepath:
                            subdir = 'mate'
                        elif 'grass' in filepath:
                            subdir = 'grass'
                        elif 'water' in filepath:
                            subdir = 'water'

                        unpack_sstera(filepath, Path(prefs.terrain_folder) / Path(subdir))
                        pgbar.update(1)

        context.preferences.view.filebrowser_display_type = self.org_pref
        return {'FINISHED'}

def unpack_sstera(filepath: str, output_dir=""):
    try:
        from oead import Sarc, yaz0
    except:
        ensure_oead()

    data = Path(filepath).read_bytes()

    if data[:4] == b'Yaz0':
        data = yaz0.decompress(data)
    else:
        return False

    if data[:4] == b'SARC':
        data = Sarc(data)
    else:
        return False

    for file in data.get_files():
        dir = Path(output_dir)
        write_path = dir / Path(file.name)
        if not dir.is_dir():
            dir.mkdir(parents=True)
        file_data = bytes(file.data)
        with open(write_path, "wb") as f:
            f.write(file_data)
            f.close()

    return

def ensure_oead():
    """I tried bundling the .whl files with the extension, tqdm works fine, oead does not."""

    # Blender's Python executable
    python_exe = sys.executable

    # Ensure pip is installed
    try:
        import pip
    except ModuleNotFoundError:
        print("Installing pip...")
        subprocess.check_call([python_exe, "-m", "ensurepip"])
        subprocess.check_call([python_exe, "-m", "pip", "install", "--upgrade", "pip"])

    print("Install oead module...")
    # Install oead
    subprocess.check_call([python_exe, "-m", "pip", "install", "oead"])

    # Optional: confirm installation
    try:
        import oead
        print(f"oead installed successfully!")
    except ModuleNotFoundError as exc:
        print(f"Failed to install oead: {exc}")
        raise exc

    return True

registry = [FILE_OT_unpack_terrain]