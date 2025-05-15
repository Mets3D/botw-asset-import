import bpy, os, glob, sys, time, subprocess, shutil, json, io, zipfile
from bpy.props import BoolProperty, StringProperty, IntProperty, EnumProperty
import pickle

from concurrent.futures import ThreadPoolExecutor, as_completed
from multiprocessing import shared_memory
from tqdm import tqdm

from ..operators.botw_asset_import.constants import ensure_caches
from ..prefs import get_addon_prefs

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
ADDON_DIR = os.sep.join(THIS_FOLDER.split(os.sep)[:-1])
RESOURCE_BLEND = os.path.join(ADDON_DIR, "resources.blend")
INSTANCE_CACHE_ZIP = os.path.join(ADDON_DIR, "databases", "world_instance_cache.zip")

DEFAULT_BLEND = os.path.join(THIS_FOLDER, "asset_blank_file.blend")

BLENDER = os.path.abspath(sys.argv[0])

ALL_MAP_SECTIONS = [f"{letter}-{number}" for letter in "ABCDEFGHIJ" for number in range(1, 9)]
MAP_SECTION_NAMES = {
    'A-4': "Statue of 8th",
    'A-8': "Gerudo Great Skeleton",
    'B-2': "Flight Range",
    'B-3': "Rito Village",
    'B-7': "Gerudo Town",
    'C-4': "Tabantha Stable",
    'C-7': "Canyon Stable",
    'D-2': "Snowfield Stable",
    'D-3': "Serene Stable",
    'D-8': "South Labyrinth",
    'E-1': "North Labyrinth",
    'E-2': "Korok Forest",
    'E-3': "Hyrule Castle",
    'E-4': "Hyrule Castle",
    'E-6': "Forest of Time",
    'E-7': "Hylia Island",
    'F-2': "Korok Forest",
    'F-3': "Korok Forest",
    'F-5': "Wetland Stable",
    'F-6': "Riverside Stable",
    'F-7': "Spring of Courage",
    'F-8': "Highland Stable",
    'G-2': "Goron City",
    'G-3': "Woodland Stable",
    'G-6': "Dueling Peaks",
    'G-8': "Lakeside Stable",
    'H-1': "Gut Check Rock",
    'H-2': "Death Mountain",
    'H-3': "Foothill Stable",
    'H-4': "Zora River",
    'H-8': "Lurelin Village",
    'I-1': "Skill Lake",
    'I-2': "Spring of Power",
    'I-3': "Tarrey Town",
    'I-4': "Zora's Domain",
    'I-6': "Spring of Wisdom",
    'I-7': "Hateno Village",
    'I-8': "Lurelin Village",
    'J-1': "Akkala Tech Lab",
    'J-2': "East Akkala Stable",
    'J-3': "Tarrey Town",
    'J-8': "Eventide Island",
}

def map_section_enum_items():
    enum_items = []
    for identifier in ALL_MAP_SECTIONS:
        name = MAP_SECTION_NAMES.get(identifier)
        if name:
            name = identifier + ": " + name
        else:
            name = identifier
        enum_items.append((identifier, name, name))
    # Add separators.
    for i, _ in reversed(list(enumerate(enum_items))):
        if (i + 1) % 8 == 0:
            enum_items.insert(i + 1, None)
    return enum_items

class OBJECT_OT_botw_build_assetlib_for_map(bpy.types.Operator):
    """Build asset library consisting of a .blend file per each game asset"""
    bl_idname = "object.botw_build_assetlib_for_map"
    bl_label = "BotW: Build Asset Library"
    bl_options = {'REGISTER', 'UNDO'}

    def count_dae(self, context):
        prefs = get_addon_prefs(context)
        model_dir = prefs.game_models_folder
        ignore_words = [word.strip() for word in self.ignore.split(",")]
        dae_map = get_dae_files_to_process(model_dir, self.target_dir, self.overwrite, ignore_words, self.asset_group)
        self.dae_count = len(list(dae_map.values()))
        self.dae_map = json.dumps(dae_map)
        prefs = get_addon_prefs()
        prefs.assets_output_folder = self.target_dir

    quiet: BoolProperty(
        name="Quiet", 
        default=True, 
        description="Suppress prints of slave Blender instances, leaving only the prints of the main loop"
    )
    blender_instances: IntProperty(
        name="Blender Instances",
        description="More instances is faster, until your computer can't handle it anymore, at which point it will not only be slower but probably cause you to crash. Setting it to 1 is just useful for debugging.",
        min=1,
        max=16,
        default=8,
    )

    ignore: StringProperty(
        name="Ignore", 
        default="_Far, _Animation, DgnMrgPrt, UMii_, _Fxmdl",
        description="If a .dae file has any of these words, do not import it", 
        update=count_dae
    )
    overwrite: BoolProperty(
        name="Overwrite", 
        description="Still process a .dae file even if it already has a corresponding .blend file in the provided directory", 
        default=False, 
        update=count_dae
    )
    target_dir: StringProperty(
        name="Output Folder", 
        subtype='DIR_PATH', 
        description="Folder where a .blend file will be created for each .dae file", 
        update=count_dae
    )
    asset_group: EnumProperty(
        name="Asset Group", 
        description="Which assets of the game to import. Either the whole game, only those found in the map, or only those found in a chunk of the map",
        items=[
            ("GAME", "Whole Game", "All assets in the game"), 
            ("MAP_ALL", "Whole Map", "All assets used in the map"),
            None,
        ] + map_section_enum_items(),
        default="B-7",
        update=count_dae,
    )

    # Internal values
    dae_count: IntProperty()
    dae_map: StringProperty()

    def invoke(self, context, _event):
        self.org_pref = context.preferences.view.filebrowser_display_type
        context.preferences.view.filebrowser_display_type = 'WINDOW'

        prefs = get_addon_prefs(context)
        if not prefs.assets_output_folder and prefs.game_models_folder:
            # Auto-initialize it to a sibling of the chosen textures folder.
            prefs.assets_output_folder = os.path.dirname(os.path.normpath(prefs.game_models_folder)) + os.sep + "Asset Library"
        self.target_dir = prefs.assets_output_folder

        self.count_dae(context)
        return context.window_manager.invoke_props_dialog(self, width=400)

    def draw(self, context):
        layout = self.layout
        layout.use_property_split=True
        layout.use_property_decorate=False
        layout.label(text="Do not run this operator without a terminal open.", icon='ERROR')
        layout.separator()
        prefs = get_addon_prefs(context)
        row = layout.row()
        row.enabled = False
        row.prop(prefs, 'game_models_folder', text="Models Folder (Preferences)")
        layout.separator()

        layout.prop(self, 'blender_instances')
        layout.prop(self, 'quiet')
        layout.separator()

        layout.prop(self, 'target_dir')
        layout.prop(self, 'overwrite')
        layout.separator()

        layout.prop(self, 'asset_group')
        layout.prop(self, 'ignore')
        layout.label(text=f"{self.dae_count} asset .blend files will be generated.")

    def execute(self, context):
        assert os.path.exists(self.target_dir) and not os.path.isfile(self.target_dir), "Output folder not found: "+self.target_dir
        dae_to_blend_map = json.loads(self.dae_map)
        build_asset_library(dae_to_blend_map, self.quiet, self.blender_instances)
        
        context.preferences.view.filebrowser_display_type = self.org_pref
        return {'FINISHED'}

all_dae_paths_cached = []
def get_all_dae_paths(dae_dir):
    global all_dae_paths_cached
    if not all_dae_paths_cached:
        all_dae_paths_cached = glob.glob(os.path.join(dae_dir, "**", "*.dae"), recursive=True)

    return all_dae_paths_cached

def get_dae_files_to_process(dae_dir, blend_dir, overwrite=False, ignore=[], asset_group=None):
    dae_paths = get_all_dae_paths(dae_dir)

    # Filter ignored words.
    if ignore != ['']:
        dae_paths = [f for f in dae_paths if not any([word in f for word in ignore])]

    # Map the .dae paths to the corresponding .blend file path that should be created.
    dae_to_blend_map = {dae_path: os.path.join(blend_dir, os.path.splitext(os.path.basename(dae_path))[0] + ".blend") for dae_path in dae_paths}

    if not overwrite:
        # Filter out .blend files that already exist.
        dae_to_blend_map = {dae:blend for dae, blend in dae_to_blend_map.items() if not os.path.isfile(blend)}

    if asset_group != 'GAME':
        # Filter out assets that aren't used by the chosen asset_group (which is a map section or whole map)
        map_data = load_instance_database()
        assets_of_map = []
        for key, value in map_data.items():
            if asset_group != 'MAP_ALL' and key != asset_group+"_instance_cache.json":
                continue
            dynamic_assets = list(value[key[:3]+"_Dynamic"]["models"].keys())
            static_assets = list(value[key[:3]+"_Static"]["models"].keys())
            assets_of_map += dynamic_assets
            assets_of_map += static_assets
    
        dae_to_blend_map = {dae:blend for dae, blend in dae_to_blend_map.items() if os.path.splitext(os.path.basename(dae))[0] in assets_of_map}

    return dae_to_blend_map

def load_instance_database() -> dict:
    # This cache and database was taken from the source code of bmubin.
    # No idea how the bmubin dev generated this, but likely the same way as projects like ice-spear,
    # by being much smarter than me and reading .sbfres binary data.
    # Many thanks!
    instance_database = {}

    with open(INSTANCE_CACHE_ZIP, "rb") as f:
        zip_data = f.read()

        # Load the .zip file into memory
        with zipfile.ZipFile(io.BytesIO(zip_data)) as z:
            for file_name in z.namelist():
                with z.open(file_name) as file:
                    instance_database[file_name] = json.loads(file.read())

    return instance_database

def create_shared_memory(data):
    """Serializes a dictionary and writes it to shared memory."""
    serialized_data = pickle.dumps(data)  # Convert dict to bytes
    try:
        shm = shared_memory.SharedMemory(create=True, size=len(serialized_data), name="BOTW_ASSET_CACHE")
    except FileExistsError:
        shm = shared_memory.SharedMemory(name="BOTW_ASSET_CACHE")

    # Write to shared memory
    shm.buf[:len(serialized_data)] = serialized_data

    print(f"Shared memory '{shm.name}' ensured.")

    return shm

def build_asset_library(dae_to_blend_map: dict[str, str], quiet=True, workers=8, timeout=180):
    start_time = time.time()
    print("Building asset library")
    caches = ensure_caches()
    # NOTE: EVEN THOUGH THIS VARIABLE IS NEVER USED, IT MUST BE ASSIGNED!!!
    # OTHERWISE THE GARBAGE COLLECTOR WILL NUKE THE SHARED MEMORY FROM ORBIT!!!
    # IT TOOK ME HOURS TO TROUBLESHOOT THIS AND I WANT TO KILL MYSELF
    shared_memory = create_shared_memory(caches)

    # Limit to just 5 items for testing.
    # dae_to_blend_map = dict(list(dae_to_blend_map.items())[:5])

    target_dir = os.path.dirname(list(dae_to_blend_map.values())[0])
    try:
        shutil.copy(RESOURCE_BLEND, os.path.join(target_dir, os.path.basename(RESOURCE_BLEND)))
    except shutil.SameFileError:
        # This is happening because I symlinked resources.blend.
        pass

    executor = ThreadPoolExecutor(max_workers=workers)
    file_pairs = list(dae_to_blend_map.items())
    futures = []

    dae_of_future = {}
    blend_of_future = {}

    for dae_file, blend_file in file_pairs:
        future = executor.submit(subprocess_import_asset, dae_file, blend_file, quiet, True, timeout)
        blend_of_future[future] = blend_file
        dae_of_future[future] = dae_file
        futures.append(future)

    num_completed = 0
    timedout_assets = []
    failed_assets = []

    total = len(list(dae_to_blend_map.keys()))
    bar_format = "Completed: {n_fmt}/{total_fmt} ({elapsed_s:.2f}s){bar}"

    for i, future in tqdm(enumerate(as_completed(futures)), total=total, bar_format=bar_format):
        dae_file = dae_of_future[future]
        blend_file = blend_of_future[future]

        res = future.result()

        if not os.path.exists(blend_file):
            tqdm.write(f"FAILED: ({i}/{total}) {dae_file}\n     Try importing this file manually to see what goes wrong.")
            failed_assets.append(dae_file)
        elif res == 'complete':
            tqdm.write(f"Created: ({i}/{total}) {blend_file}")
            num_completed += 1
        else:
            timedout_assets.append(dae_file)

    if timedout_assets:
        print(f"Assets timed out: {len(timedout_assets)}\n" + "\n".join(timedout_assets))
    if failed_assets:
        print(f"Assets failed: {len(failed_assets)}\n" + "\n".join(failed_assets))
    print(f'\nCompleted in {time.time() - start_time:.2f} seconds.\n')

    # free up memory
    shared_memory.close()
    shared_memory.unlink()

def subprocess_import_asset(dae_path, blend_path, quiet=True, background=True, timeout_s=180, shared_mem=("", 0)):
    bg = None
    if background:
        bg = '--background'
    launch_file = DEFAULT_BLEND
    if not os.path.isfile(launch_file):
        launch_file = None
    args = [
        BLENDER,
        launch_file,
        bg,
        "--python",
        os.path.join(THIS_FOLDER, "build_asset.py"),
        # "--factory-startup", # NOTE: We need to import this add-on in the blender instance, so we can't use factory start-up. That said, if you have a lot of add-ons enabled, it will slow down the process.
        dae_path,
        blend_path,
    ]
    # kinda stinky way to remove any None from the tuple
    args = tuple(x for x in args if x is not None)

    popen_args = {
        'stdout': subprocess.PIPE,
        'universal_newlines': True
    }
    if quiet:
        popen_args['stdout'] = subprocess.DEVNULL
        popen_args['stderr'] = subprocess.DEVNULL
    try:
        sprocess = subprocess.Popen(args, **popen_args)
        if not quiet:
            for line in sprocess.stdout:
                print(line.strip())

        sprocess.wait(timeout=timeout_s)
    except subprocess.TimeoutExpired:
        print(f'Timeout for {args} ({timeout_s}s) expired', file=sys.stderr)
        sprocess.terminate()
        return 'timeout'
    return 'complete'

registry = [
    OBJECT_OT_botw_build_assetlib_for_map,
]
