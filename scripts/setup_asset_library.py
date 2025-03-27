# This script automatically registers this .blend file's directory
# as an asset library.

import bpy, os

my_path = os.path.dirname(bpy.data.filepath)

asset_libs = bpy.context.preferences.filepaths.asset_libraries
for lib in asset_libs:
	if lib.path == my_path:
		break
else:
	lib = asset_libs.new(name="Breath of the Wild", directory=my_path)