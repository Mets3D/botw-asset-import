import numpy as np

def are_uv_maps_identical(obj, index_1, index_2):
    """Returns True if the UVMaps at the passed indicies are identical."""

    assert index_1 != index_2
    assert len(obj.data.uv_layers) > max(index_1, index_2)
    assert obj.type == 'MESH'

    uv_layer_1 = obj.data.uv_layers[index_1].data
    uv_layer_2 = obj.data.uv_layers[index_2].data

    if len(uv_layer_1) != len(uv_layer_2):
        return False

    uv1 = np.array([loop.uv[:] for loop in uv_layer_1])
    uv2 = np.array([loop.uv[:] for loop in uv_layer_2])

    return np.allclose(uv1, uv2)

def is_uvmap_all_zero(obj, uvmap_index=0):
    """Returns True if all UV coordinates in the specified UV map are (0,0)."""
    
    assert obj.type == 'MESH'
    assert len(obj.data.uv_layers) > uvmap_index

    uv_layer = obj.data.uv_layers[uvmap_index].data

    if not uv_layer:  
        return True  # An empty UV map counts as all zero

    # Convert UV coordinates to a NumPy array for fast processing
    uv_coords = np.array([loop.uv[:] for loop in uv_layer])

    # Check if all coordinates are exactly (0,0)
    return np.all(uv_coords == 0)
