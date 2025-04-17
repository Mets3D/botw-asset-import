import os, json, pickle, zipfile, io
from multiprocessing import shared_memory
from ...prefs import get_models_folder

# These things are case-sensitive but it shouldn't matter.
# TODO: Could make this extension-agnostic.
ICON_EXTENSION = ".jpg"
TEXTURE_EXTENSION = ".png"

DYES = ["Default", "Blue", "Red", "Yellow", "White", "Black", "Purple", "Green", "Light Blue", "Navy", "Orange", "Peach", "Crimson", "Light Yellow", "Brown", "Gray"]
OBJ_PREFIXES = ["Obj_", "TwnObj_", "TwnObjVillage_", "FldObj_", "DgnObj_", "DgnMrgPrt_"]
PRIMITIVE_NAMES = ["_polySurface", "_pCylinder", "_pSphere", "_pCube", "_pCone", "_pPlane", "pSolid", "_plantroot", "_pPipe"]
GARBAGE_MATS = ["InsideArea", "InsideMat"]

# I really wanted to make wind work, but it's impossible to get perfect results from 
# just the material data because it's all inconsistent nonsense.
# So, I just hardcoded some stuff.
LEAF_WIND_UV_ROTATIONS = {
    'PlantTreeTropicalLeaf_A_Alb' : 90,
    'Leaf_TreeWillow_A_02_Alb' : 90,
    'Leaf_TreeWillow_A_01_Alb' : 180,
    'Plant_PalmJungle_A_Leaf_01_Alb': 90,
    'Plant_TreeBananaMiniLeaf_S_A_Alb' : -90,
    'Plant_TreeBananaLeaf_S_A_Alb' : -90,
    'PlantPalmBeach_A_Leaf_Alb' : -90,
    'TreeLeafPalmMini_A_Alb' : -90,
    'Plant_PalmMini_B_Alb': 180,
    'Plant_Palm_A_Leaf_01_Alb' : -90,

    # No rotation, but materials using these textures sometimes don't get detected as wind-blown materials, which is wrong.
    'Plant_TreeLeaf_B_Alb' : 0,
    'Plant_TreeBroadleaf_A_Alb' : 0,
    'Plant_TreeBroadleaf_B_Alb' : 0,
    'Plant_TreeBroadleaf_C_Alb' : 0,
    'TreeCherry_Leaf01_Alb' : 0,
    'TreeCherry_Leaf02_Alb' : 0,
    'Plant_TreeConiferousLow_Leaf_Alb' : 0,
    'Tree_TreeConiferousLeaf_A_Alb' : 0,
    'Tree_TreeConiferousLeaf_B_Alb' : 0,
    'Tree_TreeConiferousLeaf_C_Alb' : 0,
    'Plant_TreePine_Leaf_A_Alb' : 0,
    'Plant_TreePine_Leaf_B_Alb' : 0,
    'Plant_TreeZoraLow_A_Branch_Alb' : 0,
    'Plant_TreeZoraLow_B_Branch_Alb' : 0,

    'Cloth_GerudoMayerBedRoom_I_Alb' : 0,
    'Cloth_GerudoMayerBedRoom_K_Alb' : 0,
}
WIND_FORCE_USE_HEIGHT = [
    'Plant_ChiliPepper_A_01_Alb',
    'Plant_MelonAGrass_A_01_Alb',
    'PlantPumpkinGrass_A_Alb',
    'Obj_Plant_Juniperus_Snow_Alb',
    'Plant_LotusLeaf_A_Alb',
    'Obj_Plant_Weed_A_Alb',
    'Obj_Plant_Weed_B_Alb',
    'Obj_Plant_Weed_C_Alb',
    'Plant_Weed_A_Alb',
    'Plant_Weed_B_Alb',
    'CmnTex_Plant_Tropical_A_Alb',
    'CmnTex_Plant_Tropical_B_Alb',
    'Plant_VioletCliff_A_Alb',
    'Plant_LightGrass_A_Alb',
]
WIND_FORCE_NOWIND = [
    'CmnTex_Plant_KorokWood_A_01_Alb',
    'Plant_KorokColor_Chg_0_Alb',
    'Plant_Korok_Chg_0_Alb',
]
LEAF_ZFIGHT_HACK = [
    # These tree leaf meshes z-fight with the snowy leaves and win, when they shouldn't.
    ('Obj_TreeConiferous_A_Snow_01', 'A21__Mt_Treeleaf_01'),
    ('Obj_TreeConiferous_A_Snow_02', 'A1__Mt_Treeleaf_01'),
    ('Obj_TreeConiferous_A_Snow_03', 'A10__Mt_Treeleaf_01'),
]

METAL_ROUGHNESS = 0.5

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
ADDON_DIR = os.sep.join(THIS_FOLDER.split(os.sep)[:-2])
MATERIAL_DATA_ZIP = os.path.join(ADDON_DIR, "databases", "materials.zip")
MATERIAL_DEFAULTS_JSON = os.path.join(ADDON_DIR, "databases", "material_defaults.json")
TEXTURE_INFO_JSON = os.path.join(ADDON_DIR, "databases", "texture_info.json")

CACHE_mat_defaults = {}
CACHE_tex_info = {}
CACHE_shader_data = {}
CACHE_image_paths = {}

def read_shared_dict(shm_name="my_shared_dict") -> dict:
    """Reads a dictionary from shared memory and deserializes it."""
    shm = shared_memory.SharedMemory(name=shm_name)  # Attach to shared memory
    serialized_data = bytes(shm.buf[:])  # Read bytes from shared memory
    data = pickle.loads(serialized_data)  # Deserialize back to dictionary

    return data

def ensure_caches(force=False, shared_mem_name="") -> dict:
    """Load a bunch of useful data into memory.
    Only needs to be done once per Blender session.
    Done when the the import operator is first used.
    """
    global CACHE_mat_defaults   # 18 kb
    global CACHE_tex_info       # 4.5 mb
    global CACHE_image_paths    # a few kb
    global CACHE_shader_data    # 100 mb (!!!)

    if shared_mem_name:
        data = read_shared_dict(shared_mem_name)
        CACHE_mat_defaults = data['material_defaults']
        CACHE_tex_info = data['tex_info']
        CACHE_image_paths = data['image_paths']
        CACHE_shader_data = data['shader_data']
        return {'material_defaults':CACHE_mat_defaults, 'tex_info': CACHE_tex_info, 'image_paths': CACHE_image_paths, 'shader_data': CACHE_shader_data}

    if not CACHE_mat_defaults or force:
        cache_get_mat_defaults()

    if not CACHE_tex_info or force:
        cache_get_tex_info()

    if not CACHE_image_paths or force:
        cache_get_img_paths()

    if not CACHE_shader_data or force:
        cache_get_shader_data()

    return {'material_defaults':CACHE_mat_defaults, 'tex_info': CACHE_tex_info, 'image_paths': CACHE_image_paths, 'shader_data': CACHE_shader_data}

def cache_get_mat_defaults():
    global CACHE_mat_defaults
    if not CACHE_mat_defaults:
        with open(MATERIAL_DEFAULTS_JSON, "r", encoding="utf-8") as f:
            CACHE_mat_defaults = json.load(f)
    return CACHE_mat_defaults

def cache_get_tex_info():
    global CACHE_tex_info
    if not CACHE_tex_info:
        with open(TEXTURE_INFO_JSON, "r", encoding="utf-8") as f:
            CACHE_tex_info = json.load(f)
    return CACHE_tex_info

def cache_get_img_paths() -> dict[str, str]:
    """Create a mapping from image names to full filepaths in the Game Models folder."""

    global CACHE_image_paths
    if not CACHE_image_paths:
        models_dir = get_models_folder()
        for dirpath, _subfolders, files in os.walk(models_dir):
            for file in files:
                dirpath = os.path.join(models_dir, os.path.basename(dirpath))
                filepath = os.path.join(dirpath, file)

                if file.lower().endswith(TEXTURE_EXTENSION):
                    CACHE_image_paths[file[:-len(TEXTURE_EXTENSION)]] = filepath

    return CACHE_image_paths

def cache_get_shader_data() -> dict:
    global CACHE_shader_data
    if not CACHE_shader_data:
        print("Ensure shader data...")
        with open(MATERIAL_DATA_ZIP, "rb") as f:
            zip_data = f.read()

        with zipfile.ZipFile(io.BytesIO(zip_data)) as z:
            for file_name in z.namelist():
                with z.open(file_name) as file:
                    CACHE_shader_data[file_name] = json.loads(file.read())

    return CACHE_shader_data
