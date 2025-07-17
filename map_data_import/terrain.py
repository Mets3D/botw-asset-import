import os, bpy, bmesh, struct, math
from tqdm import tqdm
from pathlib import Path

from ..prefs import get_addon_prefs
from .build_asset_library import map_section_enum_items
from ..operators.botw_asset_import.process_material import init_nodetree, ensure_loaded_img
from ..operators.botw_asset_import.constants import TERRAIN_TEX_MAPPING
from .terrain_shared import (
    terrain_is_within_map_section, 
    moser_de_brujin, 
    calc_vert_world_pos, 
    HEIGHT_SCALE, 
    get_face_verts_2_to_3, 
    get_face_verts_2_to_5,
    pair_face_verts_2_to_3,
    pair_face_verts_2_to_5,
    add_map_to_scene,
)

class TerrainBuilder:
    def __init__(self, terrain_dir, map_section="A-1"):
        self.map_section = map_section
        self.terrain_dir = terrain_dir

        self.bm: bmesh.types.BMesh = bmesh.new()
        self.mat0_mats: set[int] = set()
        self.mat1_mats: set[int] = set()
        self.mat0 = self.bm.verts.layers.int.new("material0")
        self.mat1 = self.bm.verts.layers.int.new("material1")
        self.mat_blend = self.bm.verts.layers.float.new("material_blend")

        self.blocks = []
        self.bvert_location_cache = {}

    def build(self, lod_level):
        assert lod_level < 9
        
        # Store the internal edges of all LODs by location, for use in combining LODs.
        lod_borders = [None, {}, {}, {}, {}, {}, {}, {}, {}, None]
        for lod_current in range(lod_level, 0, -1):
            # We use the bvert_location_cache
            # to ignore vertices that have already been accounted for by lower LOD meshes, as we add 
            # more vertices in-between from the higher LODs.
            # This assumes that the data in lower LOD meshes for a given vertex is the same as the data for the same vertex in a lower LOD mesh, which is hopefully and probably true.
            lod_verts = self.build_blocks_lod(lod_current)
            lod_borders[lod_current] = {
                str(v.co.x)+str(v.co.y): v 
                for v in lod_verts
                if len(v.link_edges) < 4
            }
            self.connect_lod_borders(lod_current, lod_borders)

    def build_blocks_lod(self, lod_current) -> list[bmesh.types.BMVert]:
        """tl - top left, br - bottom right"""
        tl, br = (0, 0), (1, 1)
        grid_size = 2**lod_current
        grid_tl = tuple([int(x*grid_size) for x in tl])
        grid_br = tuple([math.ceil(x*grid_size) - 1 for x in br])
        lod_verts = []
        
        count = 0
        for grid_y in range(grid_tl[1], grid_br[1] + 1):
            for grid_x in range(grid_tl[0], grid_br[0] + 1):
                if terrain_is_within_map_section(self.map_section, lod_current, (grid_x, grid_y)):
                    count += 1
        
        if count == 0:
            return []

        bar_format = f"LOD {lod_current}:" + "{n_fmt}/{total_fmt} ({elapsed_s:.2f}s){bar}"
        with tqdm(total=count, bar_format=bar_format) as pbar:
            for grid_y in range(grid_tl[1], grid_br[1] + 1):
                self.blocks_new_row()
                for grid_x in range(grid_tl[0], grid_br[0] + 1):
                    # handle LOD focus, ignore if far away
                    if not terrain_is_within_map_section(self.map_section, lod_current, (grid_x, grid_y)):
                        self.blocks_add_entry(None)
                        continue
                    block_name = '5' + str(lod_current) + format(moser_de_brujin(grid_x, grid_y), '0>8X')
                    new_verts = self.build_block(block_name, lod_current, (grid_x, grid_y))
                    lod_verts += new_verts
                    pbar.update(1)
                    # if new_verts:
                    #     print(f"Added ({grid_x}, {grid_y}) at level {lod_current} from {block_name}")
                    # else:
                    #     print(f"No data for {grid_x}, {grid_y} at level {lod_current} (so no {block_name})")
        self.blocks_new_row()
        self.blocks_new_row()

        return lod_verts

    def build_block(self, block_name, lod_current, grid_xy) -> list[bmesh.types.BMVert]:
        # https://zeldamods.org/wiki/Water.extm
        # https://zeldamods.org/wiki/MATE
        byte_structure_mate = '<BBBB'
        byte_entry_size_mate = 4
        file_name_mate = self.terrain_dir + '/mate/' + block_name + '.mate'
        # https://zeldamods.org/wiki/HGHT
        byte_structure_hght = '<H'
        byte_entry_size_hght = 2
        file_name_hght = self.terrain_dir + '/terrain/' + block_name + '.hght'
        # https://zeldamods.org/wiki/Grass.extm

        if os.path.isfile(file_name_hght):
            try:
                hfile = open(file_name_hght, 'rb')
                mfile = open(file_name_mate, 'rb')
            except:
                print(f'open {file_name_hght} failed')
                self.blocks_add_entry(None)
                return []
        else:
            # print(f'{file_name_hght} does not exist')
            self.blocks_add_entry(None)
            return []

        # https://docs.python.org/3/library/struct.html
        h_data = struct.unpack(byte_structure_hght, hfile.read(byte_entry_size_hght))
        m_data = struct.unpack(byte_structure_mate, mfile.read(byte_entry_size_mate))
        heights = []
        material0 = []
        material1 = []
        blend_weight = []
        while h_data:
            heights.append(h_data[0])
            material0.append(m_data[0])
            material1.append(m_data[1])
            blend_weight.append(m_data[2])
            try:
                h_data = struct.unpack(byte_structure_hght, hfile.read(byte_entry_size_hght))
                m_data = struct.unpack(byte_structure_mate, mfile.read(byte_entry_size_mate))
            except:
                h_data = None
                m_data = None

        assert len(heights) == 65536, "Not enough heights?"
        assert len(material0) == 65536, "Not enough material data?"

        # Make verts.
        block_verts = []
        vert_x_idx = 0
        vert_y_idx = 0

        rows = []
        row = []
        for index in range(len(heights)):
            height = heights[index]
            mat0 = material0[index]
            mat1 = material1[index]
            mat_blend = blend_weight[index]
            if vert_x_idx > 255:
                vert_x_idx = 0
                vert_y_idx += 1
                rows.append(row)
                row = []
            assert vert_y_idx <= 255

            world_xy = calc_vert_world_pos(lod_current, grid_xy, (vert_x_idx, vert_y_idx))
            location_cache_key = str(world_xy)
            vert_x_idx += 1
            if location_cache_key in self.bvert_location_cache:
                if self.bvert_location_cache[location_cache_key] == False:
                    self.bvert_location_cache[location_cache_key] = True
                else:
                    row.append(None)
                    continue
            else:
                self.bvert_location_cache[location_cache_key] = True

            bvert = self.bm.verts.new((
                world_xy[0],
                world_xy[1],
                height * HEIGHT_SCALE
            ))
            block_verts.append(bvert)
            row.append(bvert)

            # Set custom attributes (used by the material to blend textures)
            # We don't need a UVMap, since it's easiest to just use the vert positions as texture coords. (done in the material)
            bvert[self.mat0] = mat0
            bvert[self.mat1] = mat1
            self.mat0_mats.add(mat0)
            self.mat1_mats.add(mat1)
            bvert[self.mat_blend] = mat_blend/255

        rows.append(row)
        self.blocks_add_entry(rows)

        # Make faces.
        previous_row = rows[0]
        for row in rows[1:]:
            for bvert_index in range(len(row)-1):
                face_verts = [
                    previous_row[bvert_index],
                    previous_row[bvert_index+1],
                    row[bvert_index+1],
                    row[bvert_index],
                ]
                if None in face_verts:
                    continue
                self.make_a_face(face_verts)

            previous_row = row

        hfile.close()
        mfile.close()

        return block_verts

    def merge_blocks(self):
        """Connect the faces of adjacent blocks."""
        blocks = self.blocks
        block_row_len = len(blocks[0])
        for block_index in range(block_row_len):
            # print(f'block_index {block_index}')
            block = blocks[0][block_index]
            if not block:
                continue

            block_below = None
            if len(blocks) > 1 and len(blocks[1]) == len(blocks[0]):
                block_below = blocks[1][block_index]
            # print(f'block_below {bool(block_below)}')
            if block_below:
                # print(len(block[0]))
                # print(len(block[-1]))
                max_range = min(len(block[-1])-1, len(block_below[0])-1)
                for bvert_index in range(max_range):
                    face_verts = [
                        block[-1][bvert_index],
                        block[-1][bvert_index+1],
                        block_below[0][bvert_index+1],
                        block_below[0][bvert_index],
                    ]
                    if None in face_verts:
                        continue
                    self.make_a_face(face_verts)

            block_right = None
            if block_index < block_row_len-1:
                block_right = blocks[0][block_index+1]
            # print(f'block_right {bool(block_right)}')
            if block_right:
                for bvert_index in range(len(block)-1):
                    face_verts = [
                        block[bvert_index][-1],
                        block_right[bvert_index][0],
                        block_right[bvert_index+1][0],
                        block[bvert_index+1][-1],
                    ]
                    if None in face_verts:
                        continue
                    self.make_a_face(face_verts)

            # handle corner face
            block_diagonal = None
            if block_below and block_index < block_row_len-1:
                block_diagonal = blocks[1][block_index+1]
            if block_right and block_below and block_diagonal:
                face_verts = [
                    block[-1][-1],
                    block_right[-1][0],
                    block_diagonal[0][0],
                    block_below[0][-1],
                ]
                if None not in face_verts:
                    self.make_a_face(face_verts)

        blocks.pop(0)

    def blocks_add_entry(self, entry):
        self.blocks[-1].append(entry)

    def blocks_new_row(self):
        if len(self.blocks) > 1:
            self.merge_blocks()
        self.blocks.append([])

    def make_a_face(self, face_verts):
        bm = self.bm
        if None in face_verts:
            return None
        new_face = None
        try:
            new_face = bm.faces.new(face_verts)
        except:
            pass
        if not new_face:
            return None

    def connect_lod_borders(self, lod, lod_borders):
        border_1 = lod_borders[lod]
        border_2 = lod_borders[lod+1]
        border_3 = None
        if lod < 7:
            if len(lod_borders[lod+2]) > 0:
                border_3 = lod_borders[lod+2]
        if not border_2 or not border_1:
            # print(f"connect_lod_borders {lod} input sanitization did not pass")
            return
        dist_1 = vert_dist(lod)
        # dist_2 = vert_dist(lod+1)
        for bvert in border_1.values():
            bverts = get_face_verts_2_to_3(dist_1, bvert, border_1, border_2)
            if len(bverts) < 5 and border_3:
                # print(f'2 to 5, lod {lod}')
                bverts = get_face_verts_2_to_5(dist_1, bvert, border_1, border_3)

            faces = None
            if len(bverts) == 5:
                faces = pair_face_verts_2_to_3(bverts)
            if len(bverts) == 7:
                faces = pair_face_verts_2_to_5(bverts)

            if not faces:
                continue
            for face_verts in faces:
                self.make_a_face(face_verts)

def vert_dist(lod_level):
    num_chunks = 2**lod_level
    chunk_world_size = 16000/num_chunks
    grid_unit_size = chunk_world_size/256
    return grid_unit_size

def create_material(terrainbuilder, object):
    material = bpy.data.materials.new(object.name)
    object.data.materials.append(material)

    material.use_nodes = True
    nodes = material.node_tree.nodes
    links = material.node_tree.links

    shader_node = init_nodetree(material, "BotW: Terrain")
    out_node = nodes['BotW Output']
    out_node.target = 'CYCLES'
    out_eevee_node = nodes.new('ShaderNodeOutputMaterial')
    out_eevee_node.target = 'EEVEE'
    links.new(shader_node.outputs['Eevee'], out_eevee_node.inputs[0])

    spacing = 400

    def make_img_node(img_name, y_coord):
        node = nodes.new('ShaderNodeTexImage')
        node.image = ensure_loaded_img(img_name)
        if "Cmb" in img_name:
            node.image.colorspace_settings.name = 'Non-Color'
        node.width = 300
        node.location = (0, y_coord)
        position_node = nodes.get("Position")
        if not position_node:
            uv_node = nodes.new('ShaderNodeNewGeometry')
            position_node = nodes.new('ShaderNodeMapping')
            position_node.inputs['Scale'].default_value = (0.1, 0.1, 1)
            links.new(uv_node.outputs['Position'], position_node.inputs[0])
            position_node.name = "Position"
            uv_node.location = (-spacing*2, 0)
            position_node.location = (-spacing, 0)
        links.new(position_node.outputs[0], node.inputs[0])
        return node

    mat0_mats = sorted(terrainbuilder.mat0_mats)
    mat1_mats = sorted(terrainbuilder.mat1_mats)
    y_offset = 0
    for k, mat_list in enumerate((mat0_mats, mat1_mats)):
        attr_node = nodes.new('ShaderNodeAttribute')
        attr_node.attribute_name = f'material{k}'
        attr_node.location = (-spacing, y_offset+spacing)
        for mat_type in ("Alb", "Cmb"):
            img_node = None
            node_chain = []
            for i, mat_id in enumerate(mat_list):
                tex_id = TERRAIN_TEX_MAPPING[mat_id]
                img_node = make_img_node(f"Material{mat_type}_Slice_{tex_id}_", y_offset+i*spacing)
                if i > 0:
                    compare_node = nodes.new('ShaderNodeMath')
                    compare_node.operation = 'COMPARE'
                    compare_node.location = (img_node.location.x + i*spacing, img_node.location.y)
                    compare_node.inputs[1].default_value = mat_id
                    compare_node.inputs[2].default_value = 0.01
                    links.new(attr_node.outputs[2], compare_node.inputs[0])
                    mix_node = nodes.new('ShaderNodeMix')
                    mix_node.data_type = 'RGBA'
                    mix_node.location = (compare_node.location.x + spacing/2, compare_node.location.y)
                    links.new(compare_node.outputs[0], mix_node.inputs[0])
                    prev_node = node_chain[-1]
                    if prev_node.type == 'TEX_IMAGE':
                        output = prev_node.outputs[0]
                    else:
                        output = prev_node.outputs['Result']
                    links.new(output, mix_node.inputs['A'])
                    links.new(img_node.outputs[0], mix_node.inputs['B'])
                    node_chain.append(mix_node)
                else:
                    node_chain.append(img_node)
            y_offset = img_node.location[1] + spacing
            result = node_chain[-1].outputs.get('Result')
            if not result:
                result = node_chain[-1].outputs['Color']
            links.new(result, shader_node.inputs[f"Mat{k} {mat_type}"])

        shader_node.location = (node_chain[-1].location.x + 2*spacing, node_chain[-1].location.y/2)
        out_node.location = (shader_node.location.x + spacing, shader_node.location.y)
        out_eevee_node.location = (out_node.location.x, out_node.location.y-spacing)

class SCENE_OT_botw_import_terrain(bpy.types.Operator):
    """Import BotW terrain chunk"""
    bl_idname = "scene.botw_import_terrain"
    bl_label = "BotW: Import Terrain"
    bl_options = {'REGISTER', 'UNDO'}

    lod_level: bpy.props.IntProperty(
        name="Max LOD Level", 
        max=8, min=0, soft_min=4, default=6, 
        description="""The game world is 16000x16000 meters.
        The LOD level corresponds to a vertex density of 16000/2^LOD/256
        LOD level 0 means 1 vertex per 62.5 meters.
        LOD level 8 means 1 vertex per 0.24 meters.
        Not all chunks of terrain have all LODs present in the game files, so this operator merges LODs up to the max that you select here.
        Higher LOD results in massive file size and import time.
        LOD level 6 is recommended, 7 if you want to go crazy. 8 is truly overkill."""
    )

    map_section: bpy.props.EnumProperty(
        name="Map Section", 
        description="Section of the map to import",
        items=map_section_enum_items(),
        default="B-7",
    )

    def invoke(self, context, _event):
        self.org_pref = context.preferences.view.filebrowser_display_type
        context.preferences.view.filebrowser_display_type = 'WINDOW'
        return context.window_manager.invoke_props_dialog(self, width=500)
    
    def check_dirs(self):
        prefs = get_addon_prefs()
        path = Path(prefs.terrain_folder)
        return all( [(path / Path(dir)).is_dir() for dir in ('mate', 'terrain')] )

    def draw(self, context):
        layout = self.layout
        layout.label(text="Do not run this operator without a terminal open.", icon='ERROR')
        layout.use_property_split = True

        prefs = get_addon_prefs(context)

        layout.prop(prefs, 'terrain_folder')
        if not self.check_dirs():
            col = layout.column()
            col.alert = True
            col.row().label(text="Extracted terrain folders not found (terrain/mate)", icon='ERROR')
            col.row().label(text="Use 'Unpack Terrain' operator first.", icon='ERROR')
            return
        layout.prop(self, 'lod_level')
        layout.prop(self, 'map_section')

    def execute(self, context):
        if not self.check_dirs():
            self.report({'ERROR'}, "Extracted terrain folders not found.")
            return {'CANCELLED'}

        for area in bpy.data.screens["Layout"].areas:
            if area.type == 'VIEW_3D':
                for space in area.spaces:
                    if space.type == 'VIEW_3D':
                        space.clip_end = 100000
            if area.type == 'OUTLINER':
                space = area.spaces[0]
                space.show_restrict_column_viewport = True

        terrain_dir = get_addon_prefs(context).terrain_folder
        builder = TerrainBuilder(terrain_dir, self.map_section)
        builder.build(self.lod_level)
        bmesh = builder.bm
        map_name = f'terrain_map {self.map_section}'
        map_object = add_map_to_scene(map_name, bmesh)
        create_material(builder, map_object)

        context.preferences.view.filebrowser_display_type = self.org_pref
        return {'FINISHED'}

registry = [SCENE_OT_botw_import_terrain]
