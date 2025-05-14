import bpy, os, sys, subprocess

from pathlib import Path
from tqdm import tqdm

class FILE_OT_unpack_terrain(bpy.types.Operator):
    """Unpack the Terrain folder's .sstera files"""

    bl_idname = "file.unpack_botw_terrain"
    bl_label = "Unpack Terrain"
    bl_options = {'REGISTER', 'UNDO'}

    def update_terrain_dir(self, context):
        if not self.dest_dir:
            self.dest_dir = (Path(self.terrain_dir) / Path("map_extract")).as_posix()
    terrain_dir: bpy.props.StringProperty(name="Terrain Folder", description="The game's content/Terrain folder", subtype='FILE_PATH', update=update_terrain_dir)
    dest_dir: bpy.props.StringProperty(name="Output Folder", description="Result will be 4 folders adding up to 3.5GB", subtype='FILE_PATH')

    def invoke(self, context, _event):
        # Workaround: Having file selectors inside pop-ups doesn't work with this user preference.
        self.org_pref = context.preferences.view.filebrowser_display_type
        context.preferences.view.filebrowser_display_type = 'WINDOW'
        return context.window_manager.invoke_props_dialog(self, width=600)

    def draw(self, context):
        self.layout.label(text="Do not run this operator without a terminal open.", icon='ERROR')
        self.layout.use_property_split=True
        self.layout.prop(self, 'terrain_dir')
        self.layout.prop(self, 'dest_dir')

    def execute(self, context):
        num_files = sum(1 for _ in Path(self.terrain_dir).rglob("*.sstera"))

        bar_format = "Completed: {n_fmt}/{total_fmt} {percentage:3.1f}% ({elapsed_s:.2f}s){bar}"
        with tqdm(bar_format=bar_format, total=num_files) as pgbar:
            for dirpath, dirnames, files in os.walk(self.terrain_dir):
                for name in files:
                    if 'sstera' in name:
                        filepath = os.path.abspath(os.path.join(dirpath, name))

                        if 'hght' in filepath:
                            destination = 'terrain\\'
                        elif 'mate' in filepath:
                            destination = 'mate\\'
                        elif 'grass' in filepath:
                            destination = 'grass\\'
                        elif 'water' in filepath:
                            destination = 'water\\'

                        unpack_sstera(filepath, Path(self.dest_dir) / Path(destination))
                        pgbar.update(1)

        context.preferences.view.filebrowser_display_type = self.org_pref
        return {'FINISHED'}

def unpack_sstera(filepath: str, destination=""):
    try:
        from oead import Sarc, yaz0
    except:
        ret = install_oead()
        if ret == False:
            return ret
        from oead import Sarc, yaz0

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
        dir = Path(destination)
        write_path = dir / Path(file.name)
        if not dir.is_dir():
            dir.mkdir(parents=True)
        file_data = bytes(file.data)
        with open(write_path, "wb") as f:
            f.write(file_data)
            f.close()

    return

def install_oead():
    # Blender's Python executable
    python_exe = sys.executable

    print("Ensuring pip...")
    # Ensure pip is installed
    try:
        import pip
    except ImportError:
        subprocess.check_call([python_exe, "-m", "ensurepip"])
        subprocess.check_call([python_exe, "-m", "pip", "install", "--upgrade", "pip"])

    print("Install oead module...")
    # Install oead
    subprocess.check_call([python_exe, "-m", "pip", "install", "oead"])

    # Optional: confirm installation
    try:
        import oead
        print(f"oead installed successfully!")
    except ImportError:
        print("Failed to install oead.")
        return False

    return True

registry = [FILE_OT_unpack_terrain]