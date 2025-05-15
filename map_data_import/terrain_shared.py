import bpy
from itertools import count, islice

# TODO Met: Would be nice to understand where this magic number comes from.
HEIGHT_SCALE = 0.012207

MDB = list(islice((i for i in count() if i & 0x55555555 == i), 2**8))
def moser_de_brujin(x, y):
    # The map names correspond to their location in the world based on this funky grid pattern:
    # https://en.wikipedia.org/wiki/Moser%E2%80%93de_Bruijn_sequence
    # Different pieces of the map have different max detail levels, so missing pieces in the sequence make sense.
    return MDB[x] + 2*MDB[y]

# Import with Blender's world origin at the center rather than at top-left.
# (Easier to wrap head around numbers when this is turned off)
USE_CENTERED_WORLD = True

def calc_vert_world_pos(lod_level, grid_xy, vert_xy):
    num_chunks = 2**lod_level
    chunk_world_size = 16000/num_chunks
    grid_unit_size = chunk_world_size/256
    x = chunk_world_size * grid_xy[0] + grid_unit_size * vert_xy[0]
    y = -(chunk_world_size * grid_xy[1] + grid_unit_size * vert_xy[1])
    if USE_CENTERED_WORLD:
        return x-8000, y+8000
    else:
        return x, y

scale_multiplier = {
    1: 8,
    2: 4,
    3: 2,
    4: 1,
    5: .5,
    6: .25,
    7: .125,
    8: .0625
}

# TODO Met: Implement water and grass!
scale_multiplier_water = {
    key: value * 4 for key, value in scale_multiplier.items()
}


def sanitize_face_verts(bverts, border):
    for index in range(len(bverts)):
        bvert = bverts[index]
        if type(bvert) == str:
            bverts[index] = border.get(bvert)
    return bverts


def pair_face_verts_2_to_3(bverts: list):
    """returns groups of verts to make triangle faces"""
    if len(bverts) < 5:
        return None
    return [
        [
            bverts[0],
            bverts[1],
            bverts[2],
        ],
        [
            bverts[0],
            bverts[2],
            bverts[4],
        ],
        [
            bverts[2],
            bverts[3],
            bverts[4],
        ]
    ]


def get_face_verts_2_to_3(dist_1, bvert, border_1, border_2):
    dist_2 = dist_1/2

    connected_right_loc = str(bvert.co.x + dist_1) + str(bvert.co.y)
    # connected_left_loc = str(-dist_1 + bvert.co.x) + str(bvert.co.y)
    # connected_top_loc = str(bvert.co.x) + str(-dist_1 + bvert.co.y)
    connected_below_loc = str(bvert.co.x) + str(bvert.co.y + dist_1)

    bverts = [bvert]

    right = str(bvert.co.x + dist_1) + str(bvert.co.y)
    left = str(bvert.co.x - dist_2) + str(bvert.co.y)
    down = str(bvert.co.x) + str(bvert.co.y - dist_1)
    up = str(bvert.co.x) + str(bvert.co.y - dist_2)
    if bool(border_2.get(right)):
        bverts += [
            str(bvert.co.x + dist_1) + str(bvert.co.y),
            str(bvert.co.x + dist_1) + str(bvert.co.y + dist_2),
            str(bvert.co.x + dist_1) + str(bvert.co.y + dist_1),
            border_1.get(connected_below_loc)
        ]
    elif bool(border_2.get(left)):
        bverts += [
            str(bvert.co.x - dist_2) + str(bvert.co.y),
            str(bvert.co.x - dist_2) + str(bvert.co.y + dist_2),
            str(bvert.co.x - dist_2) + str(bvert.co.y + dist_1),
            border_1.get(connected_below_loc)
        ]
    elif bool(border_2.get(down)):
        bverts += [
            str(bvert.co.x)          + str(bvert.co.y - dist_1),
            str(bvert.co.x + dist_2) + str(bvert.co.y - dist_1),
            str(bvert.co.x + dist_1) + str(bvert.co.y - dist_1),
            border_1.get(connected_right_loc)
        ]
    elif bool(border_2.get(up)):
        bverts += [
            str(bvert.co.x)          + str(bvert.co.y - dist_2),
            str(bvert.co.x + dist_2) + str(bvert.co.y - dist_2),
            str(bvert.co.x + dist_1) + str(bvert.co.y - dist_2),
            border_1.get(connected_right_loc)
        ]
    bverts = sanitize_face_verts(bverts, border_2)
    return bverts


def pair_face_verts_2_to_5(bverts: list):
    """returns groups of verts to make triangle faces"""
    if len(bverts) < 7:
        return None
    return [
        [
            bverts[0],
            bverts[1],
            bverts[2],
        ],
        [
            bverts[0],
            bverts[2],
            bverts[3],
        ],
        [
            bverts[0],
            bverts[3],
            bverts[6],
        ],
        [
            bverts[3],
            bverts[4],
            bverts[6],
        ],
        [
            bverts[4],
            bverts[5],
            bverts[6],
        ],
    ]


def get_face_verts_2_to_5(dist_1, bvert, border_1, border_2):
    dist_2 = dist_1/4

    connected_right_loc = str(dist_1 + bvert.co.x) + str(bvert.co.y)
    connected_below_loc = str(bvert.co.x) + str(dist_1 + bvert.co.y)

    bverts = [bvert]

    c_r = str(dist_1 + bvert.co.x) + str(bvert.co.y)  # right
    c_l = str(-dist_2 + bvert.co.x) + str(bvert.co.y)  # left
    c_d = str(bvert.co.x) + str(dist_1 + bvert.co.y)  # down
    c_u = str(bvert.co.x) + str(-dist_2 + bvert.co.y)  # up
    if bool(border_2.get(c_r)):  # right
        bverts += [
            str(dist_1 + bvert.co.x) + str(bvert.co.y),
            str(dist_1 + bvert.co.x) + str(dist_2 + bvert.co.y),
            str(dist_1 + bvert.co.x) + str(2*dist_2 + bvert.co.y),
            str(dist_1 + bvert.co.x) + str(3*dist_2 + bvert.co.y),
            str(dist_1 + bvert.co.x) + str(dist_1 + bvert.co.y),
            border_1.get(connected_below_loc)
        ]
    elif bool(border_2.get(c_l)):  # left
        bverts += [
            str(-dist_2 + bvert.co.x) + str(bvert.co.y),
            str(-dist_2 + bvert.co.x) + str(dist_2 + bvert.co.y),
            str(-dist_2 + bvert.co.x) + str(2*dist_2 + bvert.co.y),
            str(-dist_2 + bvert.co.x) + str(2*dist_2 + bvert.co.y),
            str(-dist_2 + bvert.co.x) + str(dist_1 + bvert.co.y),
            border_1.get(connected_below_loc)
        ]
    elif bool(border_2.get(c_d)):  # down
        bverts += [
            str(bvert.co.x) + str(dist_1 + bvert.co.y),
            str(dist_2 + bvert.co.x) + str(dist_1 + bvert.co.y),
            str(2*dist_2 + bvert.co.x) + str(dist_1 + bvert.co.y),
            str(3*dist_2 + bvert.co.x) + str(dist_1 + bvert.co.y),
            str(dist_1 + bvert.co.x) + str(dist_1 + bvert.co.y),
            border_1.get(connected_right_loc)
        ]
    elif bool(border_2.get(c_u)):  # up
        bverts += [
            str(bvert.co.x) + str(-dist_2 + bvert.co.y),
            str(dist_2 + bvert.co.x) + str(-dist_2 + bvert.co.y),
            str(2*dist_2 + bvert.co.x) + str(-dist_2 + bvert.co.y),
            str(3*dist_2 + bvert.co.x) + str(-dist_2 + bvert.co.y),
            str(dist_1 + bvert.co.x) + str(-dist_2 + bvert.co.y),
            border_1.get(connected_right_loc)
        ]
    bverts = sanitize_face_verts(bverts, border_2)
    return bverts


def add_map_to_scene(map_name, bm):
    # add to scene
    bmesh_data = bpy.data.meshes.new(map_name)
    bm.to_mesh(bmesh_data)
    bmesh_object = bpy.data.objects.new(map_name, bmesh_data)
    bpy.context.view_layer.active_layer_collection.collection.objects.link(bmesh_object)

    # # fix normals
    bpy.ops.object.select_all(action='DESELECT')
    bmesh_object.select_set(True)
    bpy.context.view_layer.objects.active = bmesh_object
    bpy.ops.object.shade_smooth()

    default_collection = bpy.data.collections.get('Collection')
    if default_collection:
        default_collection.name = map_name

    return bmesh_object


def terrain_is_within_map_section(map_section, lod_level: int, grid_xy: tuple) -> bool:
    """target can be either a mubin string like \"E-4\" or a location like (7,7)"""
    # NOTE: This function only starts making sense at LOD level 4 because below that, a chunk of terrain is larger than a map section (1000m).
    # (The size of one .hght file is 16000/(2**lod_level), which at lod4 means 16000/16=1000.)
    # But LOD level 4 is still barely usable since it's 256 points across 1000 meters, 1 vertex every 4 meters.)
    map_xy = _mubin_xy[map_section.upper()]
    world_1 = calc_vert_world_pos(4, map_xy, (0, 0))
    world_2 = calc_vert_world_pos(4, map_xy, (256, 256))
    min_x = min(world_1[0], world_2[0])
    max_x = max(world_1[0], world_2[0])
    min_y = min(world_1[1], world_2[1])
    max_y = max(world_1[1], world_2[1])

    grid_1 = calc_vert_world_pos(lod_level, grid_xy, (0, 0))
    grid_2 = calc_vert_world_pos(lod_level, grid_xy, (256, 256))
    grid_min_x = min(grid_1[0], grid_2[0])
    grid_max_x = max(grid_1[0], grid_2[0])
    grid_min_y = min(grid_1[1], grid_2[1])
    grid_max_y = max(grid_1[1], grid_2[1])

    if grid_max_x > max_x or grid_min_x < min_x:
        return False
    if grid_max_y > max_y or grid_min_y < min_y:
        return False
    return True

# mubin size is 1000m
# Top left coordinate of each mubin relative to the 16x16 map
_mubin_xy = {
    'A-1': (3, 4),
    'B-1': (4, 4),
    'C-1': (5, 4),
    'D-1': (6, 4),
    'E-1': (7, 4),
    'F-1': (8, 4),
    'G-1': (9, 4),
    'H-1': (10, 4),
    'I-1': (11, 4),
    'J-1': (12, 4),
    'A-2': (3, 5),
    'B-2': (4, 5),
    'C-2': (5, 5),
    'D-2': (6, 5),
    'E-2': (7, 5),
    'F-2': (8, 5),
    'G-2': (9, 5),
    'H-2': (10, 5),
    'I-2': (11, 5),
    'J-2': (12, 5),
    'A-3': (3, 6),
    'B-3': (4, 6),
    'C-3': (5, 6),
    'D-3': (6, 6),
    'E-3': (7, 6),
    'F-3': (8, 6),
    'G-3': (9, 6),
    'H-3': (10, 6),
    'I-3': (11, 6),
    'J-3': (12, 6),
    'A-4': (3, 7),
    'B-4': (4, 7),
    'C-4': (5, 7),
    'D-4': (6, 7),
    'E-4': (7, 7),
    'F-4': (8, 7),
    'G-4': (9, 7),
    'H-4': (10, 7),
    'I-4': (11, 7),
    'J-4': (12, 7),
    'A-5': (3, 8),
    'B-5': (4, 8),
    'C-5': (5, 8),
    'D-5': (6, 8),
    'E-5': (7, 8),
    'F-5': (8, 8),
    'G-5': (9, 8),
    'H-5': (10, 8),
    'I-5': (11, 8),
    'J-5': (12, 8),
    'A-6': (3, 9),
    'B-6': (4, 9),
    'C-6': (5, 9),
    'D-6': (6, 9),
    'E-6': (7, 9),
    'F-6': (8, 9),
    'G-6': (9, 9),
    'H-6': (10, 9),
    'I-6': (11, 9),
    'J-6': (12, 9),
    'A-7': (3, 10),
    'B-7': (4, 10),
    'C-7': (5, 10),
    'D-7': (6, 10),
    'E-7': (7, 10),
    'F-7': (8, 10),
    'G-7': (9, 10),
    'H-7': (10, 10),
    'I-7': (11, 10),
    'J-7': (12, 10),
    'A-8': (3, 11),
    'B-8': (4, 11),
    'C-8': (5, 11),
    'D-8': (6, 11),
    'E-8': (7, 11),
    'F-8': (8, 11),
    'G-8': (9, 11),
    'H-8': (10, 11),
    'I-8': (11, 11),
    'J-8': (12, 11)
}
