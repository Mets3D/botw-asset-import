# This script generated the texture_info.json found in this repo. 
# This accelerates the import process by not having to read the pixel data of images to determine what kind of color channels they have.

import glob, os, bpy, json
from bl_ext.MyExtensionsLaptop.botw_asset_import.utils.pixel_image import PixelImage

# Use double backslashes
png_files = glob.glob("D:\\BotW Assets\\Models Backup\\**\\*.png")
output_file = "D:/BotW Assets/Material Data Science/texture_info.json"

targ_dir = "D:/BotW Assets/Final/textures"

with open(output_file, "w", encoding="utf-8") as f:
    data = json.loads(f)

for i, file in enumerate(png_files):
    print(f"{i}/{len(png_files)} {file}")
    name = os.path.basename(file)
    if name in data:
        continue
    img = bpy.data.images.load(file)
    pixelimage = PixelImage.from_blender_image(img)
    targ_file = os.path.join(targ_dir, name)
    if not os.path.isfile(targ_file):
        print(targ_file)
    PixelImage.cache = {}
    data[name] = {
        'width':pixelimage.width,
        'height':pixelimage.height,
        'is_single_color':pixelimage.is_single_color,
        'has_red':pixelimage.has_red,
        'has_green':pixelimage.has_green,
        'has_blue':pixelimage.has_blue,
        'has_alpha':pixelimage.has_alpha,
        'average_color':pixelimage.average_color,
        'all_channels_match':pixelimage.all_channels_match,
    }

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)