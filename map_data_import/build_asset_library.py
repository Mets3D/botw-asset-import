import bpy, os, glob, sys, time, subprocess, shutil, io, zipfile, json
from bpy.props import BoolProperty, StringProperty, IntProperty, EnumProperty
from mathutils import Matrix, Vector, Euler
from math import pi, radians
import pickle

from concurrent.futures import ThreadPoolExecutor, as_completed
from multiprocessing import shared_memory

from ..operators.botw_batch_asset_import import ensure_caches
from ..prefs import get_addon_prefs
from ..utils.collections import ensure_collection

# TODO: Move these to the preferences or derive from existing preferences
BLEND_DIR = "D:\\BotW Assets\\bmubin asset library\\assets"

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
ADDON_DIR = os.sep.join(THIS_FOLDER.split(os.sep)[:-1])
INSTANCE_CACHE_ZIP = os.path.join(ADDON_DIR, "databases", "world_instance_cache.zip")
RESOURCE_BLEND = os.path.join(ADDON_DIR, "resources.blend")

DEFAULT_BLEND = os.path.join(THIS_FOLDER, "asset_blank_file.blend")

BLENDER = os.path.abspath(sys.argv[0])

ALL_MAP_SECTIONS = [f"{letter}-{number}" for letter in "ABCDEFGHIJ" for number in range(1, 9)]

class OBJECT_OT_botw_build_assetlib_for_map(bpy.types.Operator):
    """Build asset cache one .blend per asset for importing bmubin's map data"""
    bl_idname = "object.botw_build_assetlib_for_map"
    bl_label = "BotW: Build asset library for map import"
    bl_options = {'REGISTER', 'UNDO'}

    def count_dae(self, context):
        prefs = get_addon_prefs(context)
        model_dir = prefs.game_models_folder
        ignore_words = [word.strip() for word in self.ignore.split(",")]
        dae_map = get_dae_files_to_process(model_dir, self.target_dir, self.overwrite, ignore_words, self.asset_group)
        self.dae_count = len(list(dae_map.values()))
        self.dae_map = json.dumps(dae_map)

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
        default="_Far, _Animation, DgnMrgPrt, UMii_, Armor_, _Fxmdl, Animal_, Enemy_", 
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
        default=BLEND_DIR, 
        update=count_dae
    )
    asset_group: EnumProperty(
        name="Asset Group", 
        description="Which assets of the game to import. Either the whole game, only those found in the map, or only those found in a chunk of the map",
        items=[
            ("GAME", "Whole Game", "All assets in the game"), 
            ("MAP_ALL", "Whole Map", "All assets used in the map")
        ] + [(s, s, "Map Section "+s) for s in ALL_MAP_SECTIONS],
        default="B-7",
        update=count_dae,
    )

    # Internal values
    dae_count: IntProperty()
    dae_map: StringProperty()

    def invoke(self, context, _event):
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

        layout.prop(self, 'quiet')
        layout.prop(self, 'blender_instances')
        layout.prop(self, 'ignore')
        layout.prop(self, 'overwrite')
        layout.prop(self, 'target_dir')
        layout.prop(self, 'asset_group')

        layout.label(text=f"{self.dae_count} asset .blend files will be generated.")

    def execute(self, context):
        dae_to_blend_map = json.loads(self.dae_map)
        build_asset_library(dae_to_blend_map, self.quiet, self.blender_instances)
        return {'FINISHED'}


class OBJECT_OT_botw_import_map_section(bpy.types.Operator):
    """Import one chunk of the overworld"""
    bl_idname = "object.botw_import_map_section"
    bl_label = "BotW: Import Map Section"
    bl_options = {'REGISTER', 'UNDO'}

    blend_dir: StringProperty(
        name="Asset Folder", 
        subtype='DIR_PATH', 
        description="Folder where the .blend files containing the map's assets can be found. Missing assets will be printed to the system console.", 
        default=BLEND_DIR, 
    )
    map_section: EnumProperty(
        name="Map Section", 
        description="Section of the map to import",
        items=[(s, s, "Map Section "+s) for s in ALL_MAP_SECTIONS],
        default="B-7",
    )

    def invoke(self, context, _event):
        return context.window_manager.invoke_props_dialog(self, width=400)

    def draw(self, context):
        layout = self.layout
        layout.use_property_split=True
        layout.use_property_decorate=False
        layout.prop(self, 'blend_dir')
        layout.prop(self, 'asset_group')

    def execute(self, context):
        map_data = load_instance_database()[self.map_section+"_instance_cache.json"]

        dynamic_assets = map_data[self.map_section+"_Dynamic"]["models"]
        static_assets = map_data[self.map_section+"_Static"]["models"]

        coll_root = ensure_collection(context, self.map_section, context.scene.collection)
        coll_root_temp = ensure_collection(context, self.map_section+"_temp", context.scene.collection)
        for is_dynamic, assets in zip((True, False), (dynamic_assets, static_assets)):
            for asset_name, data in assets.items():
                coll_linked_asset = ensure_asset_collection(self.blend_dir, asset_name)
                if not coll_linked_asset:
                    # NOTE: Could make an argument for creating these empties even if the asset is missing. 
                    # That way, a botcher import can be resumed later instead of starting from scratch. 
                    # But I think this will be quick anyways.
                    print(f"Missing asset file: {asset_name}")
                    coll_missing = ensure_collection(context, self.map_section + " Missing Assets", coll_root)
                    coll_asset = ensure_collection(context, asset_name, coll_missing)
                else:
                    coll_asset = ensure_collection(context, asset_name, coll_root_temp)
                for transforms in data['positions']:
                    loc = transforms['location']
                    rot = transforms['rotate']
                    scale = transforms['scale']
                    empty = bpy.data.objects.new(name=asset_name, object_data=None)

                    # this is a bit complicated, but it works
                    # useful link for explaining order of matrix operations
                    # https://blender.stackexchange.com/questions/44760/rotate-objects-around-their-origin-along-a-global-axis-scripted-without-bpy-op
                    r_m0 = Matrix.Rotation(radians(-90), 4, 'X')
                    t_m = Matrix.Translation(loc)
                    r_m1 = Matrix.Rotation(radians(90), 4, 'X')
                    r_m2 = Euler(rot).to_matrix().to_4x4()
                    empty.matrix_world = r_m1 @ t_m @ r_m2 @ r_m0
                    empty.scale = scale
                    empty['is_dynamic'] = is_dynamic
                    empty.empty_display_size = 0.01
                    empty.instance_type = 'COLLECTION'
                    empty.instance_collection = coll_linked_asset
                    coll_asset.objects.link(empty)

        # Sort the asset collections alphabetically.
        for coll in sorted(coll_root_temp.children, key=lambda c: c.name):
            coll_root.children.link(coll)
            coll_root_temp.children.unlink(coll)
        bpy.data.collections.remove(coll_root_temp)

        return {'FINISHED'}


def ensure_asset_collection(blend_dir, asset_name) -> bpy.types.Collection or None:
    """Link asset .blend to the file, without assigning it to the scene."""
    abs_path = os.path.join(blend_dir, asset_name+".blend")

    # Check if it already exists locally.
    existing_coll = next((c for c in bpy.data.collections if c.name==asset_name and c.library), None)
    if existing_coll:
        # Collection exists, so just return it.
        return existing_coll

    if not os.path.isfile(abs_path):
        return

    # Link collection from asset .blend file.
    with bpy.data.libraries.load(abs_path, link=True, relative=True) as (
        data_from,
        data_to,
    ):
        for coll in data_from.collections:
            if coll == asset_name:
                data_to.collections.append(coll)

    new_coll = bpy.data.collections.get(asset_name)
    if not new_coll:
        return

    return new_coll


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
    start_times = {}
    futures = []

    for dae_file, blend_file in file_pairs:
        start_time = time.time()  # Record start time
        future = executor.submit(build_asset, dae_file, blend_file, quiet, True, timeout)
        start_times[future] = start_time  # Track when each future started
        futures.append(future)

    num_completed = 0
    timedout_assets = []

    total = len(list(dae_to_blend_map.keys()))

    for i, future in enumerate(as_completed(futures)):
        dae_file = file_pairs[i][1]

        res = future.result()

        if res == 'complete':
            start_time = start_times[future]
            end_time = time.time()
            duration = end_time - start_time
            print(f"File ({i}/{total}) {dae_file} completed in {duration:.2f} seconds", flush=True)
            num_completed += 1
        else:
            timedout_assets.append(dae_file)

    print(f'\nAssets completed: {num_completed}')
    print(f'Assets timed out: {len(timedout_assets)}')
    for timedout_asset in timedout_assets:
        print(timedout_asset)
    print(f'\nCompleted in {time.time() - start_time:.2f} seconds.\n')

    # free up memory
    shared_memory.close()
    shared_memory.unlink()

def build_asset(dae_path, blend_path, quiet=True, background=True, timeout_s=180, shared_mem=("", 0)):
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
    OBJECT_OT_botw_import_map_section,
]
