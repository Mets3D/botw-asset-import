import bpy, os, re, json
from pathlib import Path
from collections import OrderedDict
from math import radians
from mathutils import Vector, Color

from ...utils.resources import ensure_lib_datablock
from ...utils.material import hash_material
from ...utils.timer import Timer
from ...utils.pixel_image import PixelImage
from ...utils.string import increment_name
from ...utils.customprop import make_property

from .constants import (
    METAL_ROUGHNESS, DYES, OBJ_PREFIXES, GARBAGE_MATS, TEXTURE_EXTENSION, IGNORE_ALPHA, 
    cache_get_img_paths, cache_get_mat_defaults, cache_get_shader_data, cache_get_tex_info,
    LEAF_WIND_UV_ROTATIONS, WIND_FORCE_NOWIND, WIND_FORCE_USE_HEIGHT, 
)

### MAIN MATERIAL PROCESSING FUNCTION ###

def process_mat(collection, obj, material) -> bpy.types.Material or None:
    """My best effort at setting up materials based on data exported from my custom 
    Switch Toolbox, and included in this add-on inside materials.zip.
    """

    ### STORE SHADER DATA. ###

    json_mat_name = ".".join((collection['dirname'], collection['file_name'], material['import_name'] + ".json"))
    material['json_name'] = json_mat_name
    mat_data = get_shader_data(material)
    if mat_data:
        # Store as string because Blender doesn't let us store 
        # an arbitrary structure of lists/dicts.
        material['shader_data'] = json.dumps(mat_data)
    else:
        # TODO: This might happen for modded files? So we need to implement a fallback for processing and reading json files that aren't shipped with the add-on.
        material['WARNING: MISSING DATA'] = f"Couldn't find material .json: {json_mat_name}"
        return

    ### IN SOME CASES, SIMPLY REPLACE THIS MATERIAL. ###

    if is_waterfall(material):
        # I hooked up these material settings to object properties so they can be controlled per-object.
        # This way we don't need to duplicate the water material, but instead all water can share just the one.
        make_property(obj, 'flow_speed', -5.0, min=-1000, max=1000, soft_min=-10, soft_max=10)
        make_property(obj, 'flow_axis', 1.0)
        return ensure_lib_datablock('materials', "BotW Water")
    elif is_water(material):
        make_property(obj, 'flow_speed', 0.75, min=-1000, max=1000, soft_min=-10, soft_max=10)
        make_property(obj, 'flow_axis', 0.0)
        return ensure_lib_datablock('materials', "BotW Water")
    elif is_lava(material):
        make_property(obj, 'flow_speed', 0.2, min=-1000, max=1000, soft_min=-10, soft_max=10)
        make_property(obj, 'flow_axis', 1.0)
        return ensure_lib_datablock('materials', "BotW Lava")
    elif is_malice(material):
        make_property(obj, 'malice_speed', 1.0, min=-10, max=10)
        make_property(obj, 'malice_glow', 1.0, min=0, max=10)
        return ensure_lib_datablock('materials', "BotW Malice")

    ### IN SOME CASES, SIMPLY HIDE THIS OBJECT. ###

    if any([s in material.name for s in GARBAGE_MATS]):
        # This is some sorta gameengine mesh, we don't care.
        obj.hide_viewport, obj.hide_render = True, True
        return

    ### IF THIS MATERIAL WAS ALREADY PROCESSED, DO NOTHING. ###

    nodes = material.node_tree.nodes
    if 'BotW Output' in nodes:
        # This material was already processed, skip.
        # NOTE: Could be useful to allow re-processing while developing this add-on, but I tend to just delete and re-import everything.
        return

    ### GUESS AND LOAD SHADER AND TEXTURES. ###
    
    # 1. Most textures are referenced by the json data, these are never false positives, so we always load them.
    textures = load_assigned_json_textures(material)
    # 2. Knowing the assigned textures is useful in guessing which shader to use and where to plug stuff.
    shader_name = guess_shader(collection, obj, material, textures)
    socket_map = guess_sockets_for_textures(material, textures, shader_name)
    # 3. And "knowing" the shader type is useful in guessing further used textures which aren't in the json, 
    # such as dye textures and blended terrain (MaterialAlb/MaterialCmb) textures.
    if shader_name == 'BotW: Material Blend':
        more_textures = load_blend_textures(material, socket_map)
        if not more_textures:
            shader_name = 'BotW: Smooth Shade'
        socket_map.update(more_textures)
    elif shader_name == 'BotW: Cel Shade':
        albedo = next((img for img, socket_name in socket_map.items() if socket_name=='Albedo'), None)
        if albedo and "." in os.path.splitext(albedo.name)[0]:
            dye_textures = guess_dye_textures(albedo)
            socket_map.update([(tex, 'Albedo') for tex in dye_textures])

    ### CREATE THE NODE TREE. ###

    shader_node = init_nodetree(material, shader_name)

    # Create image nodes, guess UV layer by name, set image color spaces.
    with Timer("Hookup tex nodes", material.name):
        spm_has_green = hookup_texture_nodes(collection, obj, material, shader_node, socket_map)
        hookup_rgb_nodes(material, shader_node)

    set_shader_socket_values(collection, obj, material, shader_node, spm_has_green)
    fix_material_viewport_display(material)
    material['hash'] = hash_material(material)

### GUESSING ###

def guess_shader(collection, obj, material, all_textures):
    fallback_shader = "BotW: Cel Shade"
    for prefix in OBJ_PREFIXES:
        if collection['dirname'].startswith(prefix):
            fallback_shader = "BotW: Smooth Shade"
            break

    if get_shader_prop(material, 'shaderassign>options>uking_material_behave') == 104:
        # TODO: I think this doesn't catch everything, eg. Octarock, Sandworm, Dragon, etc.
        return "BotW: Eye"
    if any(["Glass" in img.name and "RitoLight" not in img.name for img in all_textures]) or "Mt_Lens" in material.name:
        #get_shader_prop(material, 'shaderassign>options>uking_material_behave') == 102:
        return "BotW: Glass"
    if get_shader_prop(material, 'shaderassign>samplers>_a0') == '_fx0':
        return "BotW: Ancient Weapon Blade"
    if any(["EmmMsk.1" in img.name for img in all_textures]) and not any([word in material['import_name'].lower() for word in ('handle', '_02')]):
        return "BotW: Elemental Weapon"
    if any(["Emm_Emm" in img.name for img in all_textures]) and 'Divine' in collection['asset_name']:
        return "BotW: Divine Eye"
    elif any(["clrmak" in img.name.lower() or "clrmsk" in img.name.lower() for img in all_textures]):
        return "BotW: Generic NPC"

    if (
        get_shader_prop(material, 'shaderassign>options>uking_texcoord_toon_spec_srt') == 3 # Strong correspondance to regular Cel shading. (not 100% perfect, eg. Link's earrings) (NOTE: Make sure this is caught AFTER other, more specific types of Cel Shading!)
        or get_shader_prop(material, 'shaderassign>options>uking_specular_hair')==402 # This is the flag for hair Cel shading (3 cels instead of 2 in hair) (I think this is 100%) (It's also the same as `shaderassign>options>uking_material_behave`==100)
    ):
        return "BotW: Cel Shade"

    albedo = next((img for img in all_textures if img.colorspace_settings.name=='sRGB'), None)
    if albedo:
        wind_enabled = is_blown_by_wind(material, os.path.splitext(albedo.name)[0])
        if wind_enabled:
            # NOTE: We store this property even if we don't think this material uses height-based wind, 
            # since detection for that is unreliable, and if we were to manually enable that checkbox in 
            # a material, we'll need this property to be present.
            obj['wind_height'] = max([bboxpoint[2] for bboxpoint in obj.bound_box])
            if 'custom_normal' in obj.data.attributes:
                # Disable custom normals without deleting them.
                # They tend to make the leaves look a lot worse in Blender.
                obj.data.attributes['custom_normal'].name = 'custom_normal_bkp'
            material.displacement_method = 'BOTH'
            return "BotW: Fauna"
    else:
        material['WARNING: Albedo Missing!'] = True

    blend_indicies = get_indicies_for_material_blend(material)
    if blend_indicies:
        material['blend_indicies'] = blend_indicies
        return "BotW: Material Blend"
    elif len(obj.data.color_attributes) > 0 and len([img for img in all_textures if img.colorspace_settings.name=='sRGB']) > 1:
        if not is_a_tree(material):
            material['WARNING'] = "Using material blend shader because there is a vertex color and >1 albedos."
            return "BotW: Material Blend"

    material['FALLBACK USED'] = "Couldn't confidently guess the shader type of this material, but fell back to a default."
    return fallback_shader

def guess_sockets_for_textures(material, textures, shader_name) -> OrderedDict[bpy.types.Image, str]:
    socket_map = OrderedDict()
    tex_types = []
    for img in textures:
        tex_data = get_tex_data(material, img)
        print(material.name, img.name)
        if not tex_data:
            continue
        type = tex_data['Type'].strip()
        if type == 'Unknown':
            sampler = tex_data['SamplerName']
            # If the material data doesn't give us the texture type, we have some fallbacks to guess.
            if '_Alb' in img.name:
                type = 'Diffuse'
            elif '_Spm' in img.name:
                type = 'Specular'
            elif '_Nrm' in img.name:
                type = 'Normal'
            elif '_Msk' in img.name:
                type = 'Alpha'
            elif sampler in ('_ms0', 'ms0', '_ms1', 'ms1'):
                type = 'Alpha'
            elif sampler in ('_n0', 'n0', '_n1', 'n1'):
                type = 'Normal'
            elif sampler in ('_a0', 'a0', '_a1', 'a1'):
                type = 'Diffuse'
            elif sampler in ('_e0', 'e0', '_e1', 'e1'):
                type = 'Emission'
            elif sampler in ('_ao0', 'ao0', '_ao1', 'ao1'):
                type = 'AO'
            elif sampler in ('_s0', 's0', '_s1', 's1'):
                type = 'Specular'
            elif sampler in ('_mt0', 'mt0', '_mt1', 'mt1'):
                type = 'Metallic'
            elif sampler in ('_gn0'):
                # These sampler names have proved unreliable for determining texture type.
                pass
            else:
                # There may be other useful sampler names for determining texture type.
                pass
        tex_types.append((type, img))

    for type, img in tex_types:
        # NOTE: Can add support for more shader socket names here.
        if type == 'Diffuse':
            if "_Red_Alb" in img.name and shader_name=='BotW: Cel Shade':
                socket_map[img] = "Skin Red Albedo"
            elif "_Damage_Alb" in img.name and shader_name=='BotW: Cel Shade':
                socket_map[img] = "Skin Damage Albedo"
            else:
                socket_map[img] = "Albedo"
        elif type == 'Alpha':
            if any(ignore_alpha in img.name for ignore_alpha in IGNORE_ALPHA):
                # Very explicitly don't want to hook up this weird texture. 
                # If anything, add a custom socket for it, but I don't think it's doing anything in-game either.
                socket_map[img] = "None"
            else:
                socket_map[img] = "Alpha"
        elif type == 'Specular':
            socket_map[img] = "SPM"
        elif type == 'Normal':
            socket_map[img] = "Normal Map"
        elif type == 'Emission':
            if "EmmMsk.1" in img.name:
                # TODO: sampler type _e01 might be a better indicator than EmmMsk.1 in the name.
                socket_map[img] = "Emission Scroll"
            else:
                socket_map[img] = "Emission Mask"
        elif type == 'AO':
            socket_map[img] = "AO"
        elif type == 'Metallic':
            socket_map[img] = "Metallic"
        else:
            socket_map[img] = type

    return socket_map

def guess_colorspace(material, img):
    """This is a dangerously simple guess, but it works surprisingly alright."""
    tex_data = get_tex_data(material, img)
    if tex_data:
        if tex_data['Type'] == 'Diffuse':
            return 'sRGB'
        elif tex_data['Type'] == 'Unknown' and "_Alb" in img.name or "MaterialAlb" in img.name:
            return 'sRGB'

    if "_Alb" in img.name or "MaterialAlb" in img.name:
        if "_Red_Alb" in img.name or "Damage_Alb" in img.name:
            return 'Non-Color'
        return 'sRGB'

    return 'Non-Color'

def guess_socket_name(img, shader_name="BotW: Cel Shade") -> str:
    """Guess what shader socket the given image should be plugged into."""

    if type(img) == bpy.types.Image:
        lc_img_name = img.name.lower()
    elif type(img) == str:
        lc_img_name = img.lower()
    else:
        assert False, 'img must be an Image or str'

    if shader_name == 'BotW: Eye' and 'shadow' in lc_img_name:
        return "Eye Shadow"

    if "_alb" in lc_img_name:
        if "_red_alb" in lc_img_name and shader_name=='BotW: Cel Shade':
            return "Skin Red Albedo"
        elif "_damage_alb" in lc_img_name and shader_name=='BotW: Cel Shade':
            return "Skin Damage Albedo"
        return "Albedo"
    elif "clrmak_00" in lc_img_name or "clrmsk_00" in lc_img_name:
        return "Tint Mask 0"
    elif "clrmak_01" in lc_img_name or "clrmsk_01" in lc_img_name:
        return "Tint Mask 1"
    elif "clrmak_02" in lc_img_name or "clrmsk_02" in lc_img_name:
        return "Tint Mask 2"
    elif "_spm" in lc_img_name:
        return "SPM"
    elif "_nrm" in lc_img_name:
        return "Normal Map"
    elif "_ao" in lc_img_name:
        return "AO"
    elif "_emm_emm" in lc_img_name:
        return "Emm_Emm"
    elif "_emmmsk_" in lc_img_name:
        # Scrolling textures for the Obliterator only.
        pass
    elif "_emmmsk.2" in lc_img_name:
        # This only happens for elemental weapons and obliterator.
        # Red channel is actual emission mask, green is a gradient for how charged the weapon is,
        # but in the shader I just use a UV gradient instead of the green channel.
        return "Emission Mask"

    elif "_emmmsk.1" in lc_img_name or "_emmmsk" in lc_img_name:
        # It's a scrolling texture for the glow.
        return "Emission Scroll"
    elif "_emmmsk" in lc_img_name:
        # Regular scrolling textures for most of the game.
        return "Emission Scroll"
    elif "_emm" in lc_img_name:
        return "Emission Mask"
    elif shader_name == 'BotW: Ancient Weapon Blade' and "_fx" in lc_img_name:
        return "Fx Texture"
    elif "_mtl" in lc_img_name:
        return "Metallic"
    elif "_msk" in lc_img_name:
        return "Alpha"

    return ""

def guess_tex_uses_first_uv(material, img, socket_name) -> bool or None:
    """Trying to make an educated guess but I really wish I could find a sure way to tell what texture uses what UVMap."""
    if socket_name in ('Skin Red Albedo', 'Skin Damage Albedo'):
        return True
    tex_data = get_tex_data(material, img)
    if not tex_data:
        return True
    tex_idx = tex_data['textureUnit'] - 1
    if tex_data['SamplerName'] == "_fx0":
        return True

    # There are some values that sound relevant but I can't find solid correlations...

    # Possible values: None, 1
    # enable_texcoord = get_shader_property(material, f'shaderassign>options>uking_enable_texcoord{<0 to 5>}')

    # Possible values: None, 1, 2, 3, 10, 11, 20, 22, 23, 104, 105, 107 (wtf...?)
    # texcoord_mapping = get_shader_property(material, f'shaderassign>options>uking_texcoord{<0 to 7>}_mapping')

    # NOTE: TotK equivalent is apparently `o_texture{tex_idx}_texcoord`.
    # Index can be from 0 to 7.
    # Values can be None, 1 to 8
    uv_idx = get_shader_prop(material, f'shaderassign>options>uking_texture{tex_idx}_texcoord')
    # This sounds like it should refer to what UVMap is used by a texture at the given index in the texturelist
    # but the fact that it works very often is more of a coincidence of the fact that tex_idx of Albedos is usually 0
    # and the default value of uking_texture0_texcoord is usually None. So, we might as well be returning `"_Alb" in img.name`,
    # which is a bit disappointing.
    return uv_idx == None

### SHADER DATA READING ###

def is_a_tree(material):
    return get_shader_prop(material, "shaderassign>options>uking_enable_lumberjack") == 1

def is_blown_by_wind(material, albedo_name=""):
    """I couldn't find a reliable indicator for this, which is very frustrating."""

    if not albedo_name:
        textures = get_shader_prop(material, 'TextureMaps')
        if textures:
            albedo_name = next((name for name, data in textures.items() if "_Alb" in name), "")

    # By adding only a handful of hard-coded exceptions, guessing when a material should be blown by wind can become pretty accurate. 
    # False negatives are hard to find but not nearly as important as false positives.
    force_no_wind = albedo_name in WIND_FORCE_NOWIND
    if force_no_wind or is_a_tree(material):
        return False

    # NOTE: I do allow some false-positives where it looks good, eg. plants that can be picked up by the player are not blown by wind in-game but it looks fine.
    # 141 assets.
    wind_enable = get_shader_prop(material, "shaderassign>options>uking_enable_wind_vtx_transform") == 1 and get_shader_prop(material, "matparam>uking_wind_vtx_transform_intensity>ValueFloat", index=0) not in (0.1, None)
    # 71 assets, 42 of them new.
    wind_enable_lie = get_shader_prop(material, "shaderassign>options>uking_enable_wind_vtx_transform_lie") == 1 and get_shader_prop(material, "matparam>uking_wind_vtx_transform_lie_intensity>ValueFloat", index=0) != 3.0
    # 159 assets, 69 of them new.
    wind_enable_height = get_shader_prop(material, "shaderassign>options>uking_enable_wind_vtx_transform_height") == 1
    # NOTE: shaderassign>options>uking_enable_wind_vtx_transform_coreinfo == 1: 71 assets, 24 of them new. Mostly false positives
    # NOTE: shaderassign>options>uking_material_behave == 105: 667 assets, 496 of them new. Pretty much exclusively false positives.
    # NOTE: shaderassign>options>uking_wind_vtx_transform_channel == 41 shaderassign>options>uking_enable_wind_vtx_transform_normal_lock != 1: 805 assets, 630 of them new, mostly false positives or arguable at best.

    # 101 assets, 64 of them new, a small handful of false positives (especially the core of crowns of palm trees, meh.)
    uses_a_windy_albedo = (albedo_name in LEAF_WIND_UV_ROTATIONS or albedo_name in WIND_FORCE_USE_HEIGHT)
    wind_enabled = (
        wind_enable_height or
        wind_enable_lie or
        wind_enable or
        uses_a_windy_albedo
    )
    # In total, only 398 materials across 297 assets return True here 
    # which probably doesn't cover anywhere close to all things that should be blown by wind, 
    # but I give up.
    return wind_enabled

def is_water(material) -> bool:
    textures = get_shader_prop(material, 'TextureMaps')
    if not textures:
        return False

    water_names = ['TerraWater', 'CmnTex_Water', 'DungeonWater', 'Water_HatenoDyeingShop']
    if any_in_any(water_names, textures):
        return True

    not_water = ['Grass', 'Ibt', 'FairySpringWater', 'Grudge', 'Seaweed', 'Lily', 'Frogbit', 'ChaseBullet']
    if any_in_any(not_water, textures):
        return False

    if any_in_any(['Water'], textures):
        return True

    return False

def is_malice(material) -> bool:
    textures = get_shader_prop(material, 'TextureMaps')
    if not textures:
        return False

    malice_names = ['CmnTex_Grudge']
    if any_in_any(malice_names, textures):
        return True

    return False

def is_waterfall(material) -> bool:
    textures = get_shader_prop(material, 'TextureMaps')
    if not textures:
        return False

    return any_in_any(['CmnWaterFall'], textures)

def is_lava(material) -> bool:
    textures = get_shader_prop(material, 'TextureMaps')
    if not textures:
        return False

    lava_names = ['CmnTex_Lava_Alb']
    return any_in_any(lava_names, textures)

def any_in_any(words, textures) -> bool:
    return any([any([word in texture for word in words]) for texture in textures])

def get_tex_data(material, img) -> dict:
    tex_maps = get_shader_prop(material, 'TextureMaps')
    if not tex_maps:
        return {}
    img_name = Path(img.filepath).stem
    tex_data = next((data for name, data in tex_maps.items() if name == img_name), {})
    if not tex_data and not img.name.startswith("Far_"):
        tex_data = next((data for name, data in tex_maps.items() if name == "Far_"+img_name), {})
    return tex_data

def get_shader_prop(shader_or_material, prop_path, index=None):
    if type(shader_or_material) == bpy.types.Material:
        shader_data = get_shader_data(shader_or_material)
        if not shader_data:
            return "N/A"
    elif type(shader_or_material) == dict:
        shader_data = shader_or_material
    else:
        assert False, "This should be a material or a dictionary: "+str(shader_or_material)

    prop = shader_data
    for part in prop_path.split(">"):
        if isinstance(prop, dict):
            # NOTE: "N/A" (Not Available) is used rather than None or 0 or anything else, since all of those are valid and potentially meaningful values.
            prop = prop.get(part, "N/A")
        if prop == "N/A":
            break
    
    mat_defaults = cache_get_mat_defaults()

    if prop == "N/A":
        prop = mat_defaults.get(prop_path, "N/A")
    if prop == "N/A":
        for key, value in mat_defaults.items():
            if "*" in key and re.match(key.replace("*", ".*"), prop_path):
                prop = value
                break
    if prop == "N/A":
        return

    if type(prop) == list:
        if index == None and len(prop)==1:
            index = 0
        if index != None:
            return prop[index]

    return prop

def get_shader_data(material) -> dict:
    """Tried to optimize json loading by caching but it's insignificant."""
    assert 'json_name' in material, f"Material doesn't have .json filename stored: {material.name}"

    shader_data = cache_get_shader_data()

    return shader_data.get(material['json_name'], {})

def get_indicies_for_material_blend(material):
    # texture_array_index has 6 integers between 0-82.
    # These definitely correspond directly to the textures inside content/Terrain,
    # and their order seems to matter too.
    tex_array_index_props = []
    shader_array_index_props = []

    for i in range(5):
        # Skipping last value on purpose because it's the same value across the whole game.
        val = get_shader_prop(material, f'matparam>texture_array_index{i}>ValueFloat')
        tex_array_index_props.append(val)
        shader_array_index_props.append(get_shader_prop(material, f'shaderassign>options>uking_texture_array_texture{i}'))

    all_default = all([v==-1 for v in shader_array_index_props])
    tex_indicies = []
    for tex_index_value, shader_array_value in zip(tex_array_index_props, shader_array_index_props):
        if tex_index_value in (-1, None):
            continue
        if shader_array_value == -1 and not all_default:
            # If not all ShaderOptions are -1 but this one is,
            # the corresponding terrain texture is not actually used.
            # This most commonly happens for tex_array_prop==0.
            continue

        if tex_index_value in tex_indicies:
            continue
        if tex_index_value == 0 and all_default:
            # Terrain texture index 0 is a grass texture, but if the corresponding 
            # ShaderOptions values are all defaults, it's the same as if it existed with a value of -1;
            # So just like in the above case, this is not actually a reference to that grass texture.
            continue
        tex_indicies.append(int(tex_index_value))

    return tex_indicies

def get_alpha_mode(material) -> str:
    """Trying to guess what EEVEE alpha blending mode to use based on the 
    horrendous material data available."""

    alpha_flag = get_shader_prop(material, 'MaterialU>RenderState>_flags') or 1

    # NOTE: The keys are all the keys that occur in the game's materials, but the values are my guesses.
    zelda_blend_modes = {
        1: 'Opaque',        # 13553 cases
        2: 'AlphaMask',     # 3785 cases
        16: 'Custom',       # 108 cases
        19: 'Translucent',  # 1249 cases
        None: 'Unknown',    # 165 cases
    }
    blend_mode = zelda_blend_modes.get(alpha_flag, "AlphaMask")

    maybe_translucency_flag = get_shader_prop(material, 'shaderassign>options>gsys_gbuffer_xlu')
    if maybe_translucency_flag:
        return 'BLENDED'
    # shaderassign.options.uking_enable_gbuffer_xlu_blend
    # shaderassign.options.gsys_force_zprepass

    return 'BLENDED' if blend_mode == 'Translucent' else 'DITHERED'

def is_transparent(material):
    # Switch Toolbox is definitely not always correct about its isTransparent flag, 
    # eg. Mt_Builparts_HyruleCastleInside_SpiderWeb_A has it on False.
    texture_maps = get_shader_prop(material, 'TextureMaps')
    if not texture_maps:
        return False
    if any(("Him" in name for name, data in texture_maps.items())):
        return False

    switch_toolbox_thinks = get_shader_prop(material, 'isTransparent') != 1
    alb_node = get_albedo_img_node(material)
    albedo_has_alpha = None
    if alb_node:
        albedo_has_alpha = PixelImage.from_blender_image(alb_node.image).has_alpha
    # i_think = get_shader_prop(material, 'shaderassign>options>gsys_gbuffer_xlu') == 1
    return switch_toolbox_thinks or albedo_has_alpha

def get_color_values(material) -> list[Vector]:
    colors = []
    matparam = get_shader_prop(material, 'matparam')
    if not matparam:
        return colors
    for name, data in matparam.items():
        if name.startswith("const_color"):
            vec = Vector((data['ValueFloat']))
            vec.normalize()
            colors.append(vec)
    return colors

### SHADER NODE (CREATE & CONNECT NODES) ###

def init_nodetree(material, shader_name) -> bpy.types.ShaderNode:
    nodes = material.node_tree.nodes
    links = material.node_tree.links

    # Nuke the nodes as imported by .fbx, it's easier to build from scratch.
    nodes.clear()

    # Create central shader node by loading node tree from resources.blend.
    shader_node = nodes.new("ShaderNodeGroup")
    shader_node.node_tree = ensure_nodetree(shader_name)
    shader_node.location = (200, 0)
    shader_node.width = 300
    shader_node.name = "Main Shader"

    # Output node
    output_node = nodes.new("ShaderNodeOutputMaterial")
    output_node.location = (600, 0)
    output_node.name = "BotW Output"
    links.new(shader_node.outputs[0], output_node.inputs[0])
    if 'Displacement' in shader_node.outputs:
        links.new(shader_node.outputs['Displacement'], output_node.inputs['Displacement'])

    return shader_node

def ensure_nodetree(nodetree_name) -> bpy.types.NodeTree:
    """Append or link the nodetree, depending on add-on preferences."""
    return ensure_lib_datablock('node_groups', nodetree_name)

def create_helper_nodes(collection, object, material, img_node, pixel_image, socket_name, shader_node):
    shader_name = shader_node.node_tree.name
    nodes = material.node_tree.nodes
    links = material.node_tree.links

    lc_assetname = (collection.get('asset_name') or "").lower()

    ensure_UV_node(object, material, img_node, socket_name, shader_name)

    if shader_name == 'BotW: Eye' and socket_name in ('Albedo', 'Emission Color', 'Emission Mask', 'Normal Map') and len(img_node.inputs) > 0:
        eye_rig_node = nodes.get("Eye Rig")
        if not eye_rig_node:
            eye_rig_nt = ensure_nodetree("BotW: Eye Rig")
            eye_rig_node = nodes.new("ShaderNodeGroup")
            eye_rig_node.node_tree = eye_rig_nt
            eye_rig_node.location = img_node.location + Vector((-400, 0))
            eye_rig_node.width = 300
            eye_rig_node.name = "Eye Rig"
        links.new(eye_rig_node.outputs[0], img_node.inputs[0])
    elif socket_name == 'Fx Texture':
        distorted_img = nodes.new("ShaderNodeTexImage")
        distorted_img.image = img_node.image
        distorted_img.width = img_node.width
        distorted_img.location = img_node.location + Vector((0, 300))
        distortion_shader = ensure_nodetree('BotW: Ancient Weapon Blade Heat Distortion')
        distortion_node = nodes.new("ShaderNodeGroup")
        distortion_node.location = distorted_img.location + Vector((-400, 0))
        distortion_node.width = 350
        distortion_node.node_tree = distortion_shader
        links.new(distortion_node.outputs[0], distorted_img.inputs[0])
        links.new(distorted_img.outputs[0], shader_node.inputs['Fx Texture Distorted'])
        links.new(distorted_img.outputs[1], shader_node.inputs['Alpha'])
    elif socket_name == 'Emission Scroll':
        # Only on elemental weapons and obliterator.
        scroll_node = nodes.get("UV Scroll")
        if not scroll_node:
            scroll_shader = ensure_nodetree('BotW: Emission Scroll')
            scroll_node = nodes.new("ShaderNodeGroup")
            scroll_node.location = img_node.location + Vector((-400, 0))
            scroll_node.width = 350
            scroll_node.node_tree = scroll_shader
            scroll_node.name = "UV Scroll"
        if len(img_node.inputs[0].links) > 0:
            # We may have created a UV node earlier. Don't need it.
            link = img_node.inputs[0].links[0]
            uv_node = link.from_node
            links.remove(link)
            if len(uv_node.outputs[0].links) == 0:
                if len(uv_node.inputs[0].links) > 0:
                    from_node = uv_node.inputs[0].links[0].from_node
                    if from_node:
                        nodes.remove(from_node)
                nodes.remove(uv_node)
        links.new(scroll_node.outputs[0], img_node.inputs[0])
        if 'guardian' in lc_assetname or 'ancient' in lc_assetname:
            set_socket_value(shader_node, 'Emission Color', [1.000000, 0.245151, 0.025910, 1.000000])
    elif socket_name == 'SPM':
        if pixel_image.all_channels_match:
            img_node.label = "(channels match; not metal or rubber)"
        elif pixel_image.has_green:
            img_node.label = "(has green; usually metal mask)"
        else:
            img_node.label = "(no green; sketch highlight mask)"
    elif socket_name == 'Metallic':
        set_socket_value(shader_node, 'Roughness', METAL_ROUGHNESS)

def ensure_UV_node(object, material, img_node, socket_name, shader_name):
    if img_node.type != 'TEX_IMAGE':
        return

    nodes = material.node_tree.nodes
    links = material.node_tree.links

    img = img_node.image
    tex_data = get_tex_data(material, img)
    if tex_data:
        pong_x = tex_data.get('WrapModeS', "Repeat") == 'Mirror'
        pong_y = tex_data.get('WrapModeT', "Repeat") == 'Mirror'
        if pong_x or pong_y:
            pingpong_node = nodes.get("PingPong UVs")
            if not pingpong_node:
                pingpong_nt = ensure_nodetree("BotW: UMii Face UVs")
                pingpong_node = nodes.new("ShaderNodeGroup")
                pingpong_node.node_tree = pingpong_nt
                pingpong_node.name = "PingPong UVs"
                pingpong_node.location = img_node.location + Vector((-400, 0))
                pingpong_node.width = 300
            if pong_x:
                set_socket_value(pingpong_node, 'PingPong X', True)
            if pong_y:
                set_socket_value(pingpong_node, 'PingPong Y', True)
            links.new(pingpong_node.outputs[0], img_node.inputs[0])
            # I think non-default WrapModes always use the first UV map, so imma just return here.
            return

    lc_img_name = img_node.image.name.lower()
    if len(object.data.uv_layers) > 1:
        uses_first_uvmap = guess_tex_uses_first_uv(material, img_node.image, socket_name)
        if "_alb" in lc_img_name and "damage" in lc_img_name:
            uses_first_uvmap = False
        if shader_name == 'BotW: Generic NPC' and "_ao" in lc_img_name:
            uses_first_uvmap = True
        if "clrmak" in lc_img_name or "clrmsk" in lc_img_name:
            uses_first_uvmap = True

        if not uses_first_uvmap:
            fallback_node = nodes.get("Second UV Channel")
            if not fallback_node:
                fallback_node = nodes.new(type="ShaderNodeGroup")
                fallback_nt = ensure_nodetree("BotW: UV Fallback")
                fallback_node.node_tree = fallback_nt
                fallback_node.location = img_node.location + Vector((-200, 0))
                fallback_node.name = "Second UV Channel"
                uv_node = nodes.new(type="ShaderNodeUVMap")
                uv_node.uv_map = "SPM" # UVs[1].name
                uv_node.location = fallback_node.location + Vector((-200, 0))
                links.new(uv_node.outputs[0], fallback_node.inputs[0])
            links.new(fallback_node.outputs[0], img_node.inputs[0])

def set_shader_socket_values(collection, obj, material, shader_node, spm_has_green):
    lc_obname = obj.name.lower()
    lc_dirname = (collection.get('dirname') or "").lower()
    lc_assetname = (collection.get('asset_name') or "").lower()

    links = material.node_tree.links
    behave = get_shader_prop(material, 'shaderassign>options>uking_material_behave')
    metal_color = get_shader_prop(material, 'shaderassign>options>uking_metal_color')

    # Hardcode some other values.
    if collection['asset_name'] == "Majora's Mask":
        set_socket_value(shader_node, 'Emission Strength', 1.0)
        set_socket_value(shader_node, 'Fake Rimlights', 0.0)
        set_socket_value(shader_node, 'Sketch Highlight Spread', 0.0)
        return False
    if "Mt_Lens" in material['import_name']:
        set_socket_value(shader_node, 'Alpha', 0.2)
    if 'ancient' in lc_assetname:
        # TODO: Is this still necessary?
        set_socket_value(shader_node, 'Emission Color', [1.000000, 0.245151, 0.025910, 1.000000])
    if collection['asset_name'] == 'Fierce Deity Mask' and material['import_name'] == 'Mt_Eyeemm':
        set_socket_value(shader_node, 'Emission Color', [0.700000, 0.700000, 0.700000, 1.000000])
        set_socket_value(shader_node, 'Emission Mask', 1.0)
        if shader_node.inputs['Emission Mask'].links:
            links.remove(shader_node.inputs['Emission Mask'].links[0])
    if 'Hylian Hair' in collection['asset_name'] or 'Hylian Child Hair' in collection['asset_name']:
        set_socket_value(shader_node, 'Albedo', [0.833908, 0.530669, 0.151620, 1.000000])
    if 'Hylian Beard' in collection['asset_name']:
        set_socket_value(shader_node, 'Albedo', [0.314406, 0.314406, 0.314406, 1.000000])
    if 'Hylian Glasses' in collection['asset_name']:
        set_socket_value(shader_node, 'Tint 0 Color', [0.023805, 0.023805, 0.023805, 1.000000])
        set_socket_value(shader_node, 'Metal', True)
    if 'Hylian Nose' in collection['asset_name']:
        set_socket_value(shader_node, 'Albedo Tint', [0.291138, 0.190097, 0.088846, 1.000000])

    if shader_node.node_tree.name == 'BotW: Material Blend':
        # Transparent edges are used by meshes that sometimes help blend between different terrain objects.
        # (But idk yet how to detect them. The commented line below had way too many false positives.)
        # set_socket_value(shader_node, "Transparent Edges", is_transparent(material))
        ensure_edge_attribute(bpy.context, obj)
        # Whenever the moss is used it just looks way too much/bad and idk how to fix it, let's just turn it down.
        albedo = get_albedo_img_node(material)
        if albedo.image and 'Moss' in albedo.image.name or 'MaterialAlb_Slice_8' in albedo.image.name:
            set_socket_value(shader_node, "Blend 1 Factor", 0)

    if shader_node.node_tree.name == 'BotW: Fauna':
        # Interpreting `uking_enable_backface_modify` as backface culling seems to do more harm than good.
        # On the leaves it's no longer necessary since I use Displacement to pull apart z-fighting planes,
        # and this value is set on branch materials which are obviously double-sided in-game.
        # material.use_backface_culling = get_shader_property(material, 'shaderassign.options.uking_enable_backface_modify') == 1
        wind_intensity = get_shader_prop(material, "matparam>uking_wind_vtx_transform_intensity>ValueFloat")
        if wind_intensity:
            set_socket_value(shader_node, 'Wind Intensity', min(wind_intensity, 0.1))
        wind_use_height = get_shader_prop(material, "shaderassign>options>uking_enable_wind_vtx_transform_height")
        if not wind_use_height:
            albedo = get_albedo_img_node(material)
            if albedo and albedo.image and os.path.splitext(albedo.image.name)[0] in WIND_FORCE_USE_HEIGHT:
                wind_use_height = True
        if wind_use_height:
            # Store how high the object reaches above the origin. This value is then used in the Fauna shader.
            set_socket_value(shader_node, 'Wind Use Height', True)
        alb_node = get_albedo_img_node(material)
        if alb_node and alb_node.image:
            img_name = os.path.splitext(alb_node.image.name)[0]
            if img_name in LEAF_WIND_UV_ROTATIONS:
                set_socket_value(shader_node, 'Wind UV Rotation', radians(LEAF_WIND_UV_ROTATIONS[img_name]))

    metal = spm_has_green
    if "arrow" in lc_dirname:
        metal = True
    if (
        (behave == 1) or 
        (behave == 2 and metal_color == 2)
    ):
        # TODO: Check if other behave/metal_color value combos should also be metal.
        metal = True

    if get_shader_prop(material, 'shaderassign>options>uking_specular_hair') == 402:
        set_socket_value(shader_node, "Hair", True)
    elif metal:
        set_socket_value(shader_node, "Metal", True)
        set_socket_value(shader_node, "Metallic", 1.0)
        set_socket_value(shader_node, "Roughness", METAL_ROUGHNESS)
    elif spm_has_green and "rubber" in lc_obname:
        set_socket_value(shader_node, "Rubber", True)
    if 'Metallic' in shader_node.inputs and len(shader_node.inputs['Metallic'].links) > 0:
        set_socket_value(shader_node, "Roughness", METAL_ROUGHNESS)

def ensure_edge_attribute(context, object):
    if 'edge' in object.data.attributes:
        return

    edge_nt = ensure_nodetree("Mark Edges")
    gn_modifier = object.modifiers.new("Store Edge Attribute", "NODES")
    gn_modifier.node_group = edge_nt
    with context.temp_override(active_object=object):
        bpy.ops.object.modifier_apply(modifier=gn_modifier.name)

def set_socket_value(group_node, socket_name, socket_value, output=False):
    socket = group_node.inputs.get(socket_name)
    if not socket or output:
        socket = group_node.outputs.get(socket_name)
    if socket:
        socket.default_value = socket_value

def hookup_texture_nodes(collection, object, material, shader_node, socket_map) -> bool:
    nodes = material.node_tree.nodes
    links = material.node_tree.links

    shader_name = shader_node.node_tree.name
    # Only use dye labels if the number of albedo textures is exactly the number of dyes in the game.
    use_dye_labels = len([img for img, socket in socket_map.items() if socket=='Albedo']) == len(DYES)
    albedo_count = 0
    dye_count = 0
    spm_has_green = False
    for i, (img, socket_name) in enumerate(socket_map.items()):
        img.colorspace_settings.name = guess_colorspace(material, img)

        pixel_image = PixelImage.from_blender_image(img)
        if socket_name != 'Albedo' and pixel_image.is_single_color:
            # If the whole image is just one color, use an RGB node instead.
            img_node = nodes.new(type="ShaderNodeRGB")
            img_node.outputs[0].default_value = list(pixel_image.average_color) + [1]
        else:
            img_node = nodes.new(type="ShaderNodeTexImage")
            img_node.image = img
            img_node.width = 400
        img_node.label = img.name

        if socket_name in ("", "Unknown"):
            socket_name = guess_socket_name(img, shader_name)

        img_node.location = (-300, (i-dye_count)* -300)

        if socket_name == 'Skin Red Albedo':
            make_property(object, 'skin_cold', default=0.0, min=0, max=1)
        if socket_name == 'Skin Damage Albedo':
            make_property(object, 'skin_damaged', default=0.0, min=0, max=1)

        if socket_name == 'Albedo' and shader_name == 'BotW: Cel Shade':
            existing_albedo = get_albedo_img_node(material)
            if existing_albedo and existing_albedo.image and existing_albedo.image.name.split(".")[0] == img_node.image.name.split(".")[0]:
                dye_count += 1
                img_node.label = str(dye_count)
                if use_dye_labels:
                    img_node.label += ": " + DYES[dye_count]
                img_node.location = (-300, dye_count*60)
                img_node.hide = True
            albedo_count += 1

        if socket_name == 'SPM' and pixel_image.has_green and not pixel_image.all_channels_match:
            spm_has_green = True

        create_helper_nodes(collection, object, material, img_node, pixel_image, socket_name, shader_node)

        # Hook up texture to target socket on the shader node group.
        shader_socket = shader_node.inputs.get(socket_name)

        img_node.label = socket_name + " " + img_node.label
        if not shader_socket:
            img_node.label = "No socket: " + socket_name
            continue

        if socket_name == "Albedo Blend 1":
            set_socket_value(shader_node, f"Blend 1 Factor", 1)

        if len(shader_socket.links) == 0:
            if shader_socket.name == 'Alpha' and is_transparent(material):
                pass
            else:
                links.new(img_node.outputs['Color'], shader_socket)
        else:
            # The shader socket where we want to plug this image is already taken. 
            # This can happen with dye textures, reskins, etc.
            pass

        if is_transparent(material):
            material.surface_render_method = get_alpha_mode(material)
        # Since transparency doesn't (always) get its own texture node, hook up the Alpha of the Albedo.
        alpha_socket = shader_node.inputs.get('Alpha')
        if socket_name in ('Albedo', 'Fx Texture Distorted') and is_transparent(material) and pixel_image.has_alpha and not any(ignore_alpha in img.name for ignore_alpha in IGNORE_ALPHA):
            if alpha_socket and len(alpha_socket.links) == 0 and 'Alpha' in img_node.outputs:
                links.new(img_node.outputs['Alpha'], alpha_socket)
        # But if after those steps we didn't hook up any alpha, don't set it to Blended, since that will cause sorting issues.
        transparent_edges = shader_node.inputs.get('Transparent Edges')
        if not alpha_socket or len(alpha_socket.links) == 0 and not (transparent_edges and transparent_edges.default_value==True):
            material.surface_render_method = 'DITHERED'

    first_plugged_img = next((s.links[0].from_node for s in shader_node.inputs if len(s.links)>0 and s.links[0].from_node.type == 'TEX_IMAGE'), None)
    if first_plugged_img:
        nodes.active = first_plugged_img

    return spm_has_green

def hookup_rgb_nodes(material, shader_node):
    """Load color values from the json material data, create RGB nodes for them, 
    and connect them to the shader node based on some rudimentary logic.
    Said logic is based on what's already connected to the shader node sockets, which means
    hookup_texture_nodes should run before this.
    """
    nodes = material.node_tree.nodes
    links = material.node_tree.links
    lowest_y = min((node.location.y for node in nodes), default=0)

    color_nodes = []

    for i, color in enumerate(get_color_values(material)):
        col_node = nodes.new(type='ShaderNodeRGB')
        col_node.outputs[0].default_value = color
        col_node.location = (-50, lowest_y - 300*(i+1))
        color_nodes.append(col_node)
    
    if len(color_nodes) > 0:
        # If there's at least one proper color constant, 
        # there's a very solid chance for it to be emmission color.
        # (But only if an emission mask is already plugged in, otherwise it must be somehting else.)
        if 'Emission Color' in shader_node.inputs and len(shader_node.inputs['Emission Mask'].links) > 0:
            is_albedo = False
            if 'Albedo' in shader_node.inputs:
                albedo_socket = shader_node.inputs['Albedo']
                if len(albedo_socket.links) == 0:
                    links.new(color_nodes[0].outputs[0], albedo_socket)
                    is_albedo = True
            if not is_albedo:
                links.new(color_nodes[0].outputs[0], shader_node.inputs['Emission Color'])
                set_socket_value(shader_node, "Emission Strength", 0.1)

### SHADER NODE (READING ONLY) ###

def get_average_albedo_color(material) -> tuple or None:
    albedo_socket = get_albedo_socket(material)
    if not albedo_socket:
        return material.diffuse_color
    if len(albedo_socket.links) == 0:
        return albedo_socket.default_value
    albedo_node = albedo_socket.links[0].from_node
    if albedo_node.type != 'TEX_IMAGE' or albedo_node.image == None:
        return
    if 'average_color' in albedo_node.image:
        return albedo_node.image['average_color'].to_list()
    pixel_image = PixelImage.from_blender_image(albedo_node.image)
    average_color = pixel_image.average_color
    albedo_node.image['average_color'] = average_color
    return pixel_image.average_color

def get_albedo_socket(material):
    if not material.use_nodes:
        return
    nodes = material.node_tree.nodes
    output_node = next((n for n in nodes if n.type=='OUTPUT_MATERIAL'), None)
    if not output_node:
        return
    if len(output_node.inputs[0].links) == 0:
        return
    shader_node = output_node.inputs[0].links[0].from_node
    albedo_socket = shader_node.inputs.get('Albedo')
    return albedo_socket # can be None.

def get_albedo_img_node(material) -> bpy.types.ShaderNodeTexImage or None:
    if not material.use_nodes:
        return
    albedo_socket = get_albedo_socket(material)
    if not albedo_socket or len(albedo_socket.links) == 0:
        return
    albedo_node = albedo_socket.links[0].from_node
    if albedo_node.type != 'TEX_IMAGE':
        return
    return albedo_node

### TEXTURE LOADING ###

def ensure_loaded_img(img_name, allow_missing=False) -> bpy.types.Image or None:
    if not img_name.endswith(TEXTURE_EXTENSION):
        img_name = img_name + TEXTURE_EXTENSION

    real_img_path = get_image_path(img_name)
    if not real_img_path:
        if not img_name.startswith("Far_"):
            return ensure_loaded_img("Far_"+img_name, allow_missing=allow_missing)
        elif not allow_missing:
            raise FileNotFoundError(f"Can't find image in the image path cache (it probably doesn't exist): {img_name}")
        else:
            return

    img = bpy.data.images.get(img_name)
    if img:
        img.filepath = real_img_path
    else:
        img = bpy.data.images.load(real_img_path, check_existing=True)

    tex_info = cache_get_tex_info()

    if img.name in tex_info:
        tex_info = tex_info[img.name]
        img['is_single_color'] = tex_info['is_single_color']
        img['has_red'] = tex_info['has_red']
        img['has_green'] = tex_info['has_green']
        img['has_blue'] = tex_info['has_blue']
        img['has_alpha'] = tex_info['has_alpha']
        img['average_color'] = tex_info['average_color']
        img['all_channels_match'] = tex_info['all_channels_match']
    else:
        # I guess this can happen with textures of mods, so let's not print anything. 
        # Importing those will just be a little slower.
        # print(f"Couldn't find in texture info cache: {img.name}")
        pass

    if img.name != img_name:
        try:
            img.name = img_name
        except AttributeError:
            # Sometimes it's read-only, idk why.
            print(f"Couldn't rename texture: {img.name}")

    return img

def get_image_path(image_name: str) -> str:
    with Timer("Image path cache"):
        image_paths = cache_get_img_paths()
    # Allow passing a full path, why not.
    image_name = Path(image_name).stem
    return image_paths.get(image_name, "")

def guess_dye_textures(albedo) -> list[bpy.types.Image]:
    """Find alt textures of an albedo.""" # TODO: rename this function to load_dye_textures
    img = albedo
    dye_textures = []
    next_name = albedo.name
    while img:
        next_name = increment_name(next_name)
        if next_name == albedo.name:
            # No numbers in the name.
            break

        img = ensure_loaded_img(next_name, allow_missing=True)
        if not img:
            break

        dye_textures.append(img)
    return dye_textures

def load_assigned_json_textures(material) -> list[bpy.types.Image]:
    """If a material was assigned a 'shader_data' custom property, that's data
    we extracted from the .bmat using my modified version of Switch Toolbox.
    """

    texture_maps = get_shader_prop(material, 'TextureMaps')
    if not texture_maps:
        return []

    textures = []

    for name, tex_data in texture_maps.items():
        if name in ('MaterialAlb', 'MaterialCmb', 'ForReplace_Lumberjack'):
            continue
        # NOTE: allow_missing=True because there is actually a very small number of textures referenced by materials that just... don't exist.
        # Eg. Armor_181_Head references an Emm_Nrm texture.
        img = ensure_loaded_img(name, allow_missing=True)
        if img:
            textures.append(img)

    return textures

def load_blend_textures(material, socket_map) -> OrderedDict[bpy.types.Image, str]:
    alb_blend_idx = 1
    nrm_blend_idx = 1
    new_socket_map = OrderedDict()
    tex_indicies = material.get('blend_indicies', [])
    for i, tex_index in enumerate(tex_indicies):
        albedo = ensure_loaded_img(f"MaterialAlb_Slice_{tex_index}_.png")
        if albedo:
            if 'Albedo' not in list(socket_map.values()):
                new_socket_map[albedo] = "Albedo"
            else:
                new_socket_map[albedo] = f'Albedo Blend {alb_blend_idx}'
                alb_blend_idx += 1
        normal = ensure_loaded_img(f"MaterialCmb_Slice_{tex_index}_.png")
        if normal:
            if 'Normal Map' not in list(socket_map.values()):
                new_socket_map[normal] = "Normal Map"
            else:
                new_socket_map[normal] = f'Normal Blend {nrm_blend_idx}'
                nrm_blend_idx += 1

    return new_socket_map

### VIEWPORT DISPLAY ###

def fix_material_viewport_display(mat):
    if mat.library:
        return
    mat.metallic = 0
    mat.roughness = 0.8
    mat.diffuse_color = [0.8, 0.8, 0.8, 1.0]
    if not mat.use_nodes:
        return
    albedo_node = get_albedo_img_node(mat)
    if albedo_node:
        mat.node_tree.nodes.active = albedo_node
    average_color = get_average_albedo_color(mat)
    if average_color:
        average_color = Color(average_color[:3])
        if average_color.s < 0.4:
            average_color.s = 0.4
        if average_color.v < 0.4:
            average_color.v = 0.4
        mat.diffuse_color = (average_color.r, average_color.g, average_color.b, 1.0)
