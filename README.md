### What's this

This is a Blender extension to import BotW assets in .dae & .fbx format into Blender with a lot of automated clean-up. It includes various shaders which will be assigned automatically. I made it for the creation of an asset library for use in Blender for fan-art and modding purposes.

### Installation & file paths

Install like any other add-on that isn't on the Extension Platform:
- Download this repo as .zip
- In Blender, go to Edit->Preferences->Addons
- Little arrow on the top-right->Install From Disk...->Browse the .zip
- Enable the add-on.

- Follow the instruction on the "Textures/Icons/Animations Folder" inputs' tooltips (that appear on mouse hover) to browse the correct folders.

### How to use
- The add-on is meant to be used after a tool like Switch Toolbox has extracted the game's models, textures, and inventory icons into .dae+.fbx, .png, and .jpg formats respectively. You need to browse the folder with the textures in the user preferences, as already mentioned. This is necessary because plenty of assets don't have the textures in their own folders, so the importer will always check in the specified folder instead of next to the .dae/.fbx files.
- The add-on relies on Blender's .dae and .fbx importers. As of this writing, these are included in Blender 4.5, they just need to be enabled.
- Copy a sub-set of models you want to import to another folder, call it "Import Batch", because importing everything into a single file will probably run you out of memory and take ages. I never tried, it would just be silly.
- In Blender, go to "Window->Toggle System Console", so you can see that it's doing something.
- In Blender, go to "Import->BotW (.dae & .fbx)", then navigate to the "Import Batch" folder and hit Import.

### What it does
- Takes the armature from .fbx file if there is one, and tries to improve its aesthetic by assigning bone shapes.
- Uses the albedo texture assigned in the .fbx files to guess the rest of the textures and set up high quality materials for EEVEE using shaders made based on [thejudsub](https://www.youtube.com/watch?v=Sb3CRU2DufU)'s tutorial series on replicating the game's cel shading, which imo gives fantastic results, many thanks to him. Non-cel-shaded assets will be assigned a smooth shader.
- Renames assets to how they're named in-game where possible, based on an improved version of [this dictionary](https://github.com/MrCheeze/botw-tools/blob/master/botw_names.json) by MrCheeze. I added many entries to this as I came across cases where it didn't work. Assets that don't have a name in the game (like environment assets) will just use the file name with some clean-up.
- De-duplicates materials
- Sets up Bloom viewport compositing which is really important for all emission effects to look good.
- Adds a custom-made MatCap that makes the shaded viewport look a bit like BotW cel shading.
- Sets up assets with in-game inventory icons when possible. Some extra requirements for this are:
    - Use Switch Toolbox to extract the game's "content\UI\StockItem" folder. Make sure to switch the export format to .jpg, and to leave the "Create folders" option enabled.
    - In the add-on's preferences, browse the resulting folder of folders of .jpg files (yes, I typed that correctly) in the "Icons Folder" option.
- Adds some handy operators and a tweaked .seanim importer, see below.

### What it doesn't do
- Not every material setting can be guessed correctly by the importer, since it's working with very little data. Check the shader node that the textures are plugged into, and notice it has a "Settings" section. These may need manual tweaking, eg. for setting the Emission Color.
- Some materials also use a weird UV tiling workflow, where instead of the UV space repeating like normal, it repeats flipped, as if the textures are flipped horizontally to the left and right of the default UV square, and flipped vertically above and below the UV square. In these cases, you can manually load the "BotW: UMii Face UVs" nodegroup into the image texture nodes. These cases are obviously recognizable by the fact that half or quarter of the textures will look correct, and the objects are symmetrical.
- Reskins are obviously not handled. Since there's only 1 Bokoblin mesh, only 1 Bokoblin will be imported. To create the reskinned versions, you'll have to duplicate stuff and load textures manually.
- Some animations don't work. This is even true for Switch Toolbox. Eg. the animation of dragons is completely mangled.

### Operators
Also included is a number of handy operators for the asset browser. These may be split out into a separate add-on in the future, which I'll try to remember to mention here if it ever happens.
These are:
- Merge Actions (bpy.ops.asset.merge_actions): With any number of actions selected in the Asset Browser or the outliner, this operator merges them into one. In case of conflicts (two actions have an f-curve with the same data path), the active action will win, otherwise priority is random. So it's safest to merge two actions at a time. This is useful for things like Link, where he sometimes has unique animations split up into separate head/body actions when imported.
- Merge Armatures (bpy.ops.object.botw_merge_armatures): With any number of armatures selected, combine them while removing duplicate bones and preserving parenting relationships between objects and bones, as well as preserving Armature modifiers. Useful for combining clothes and characters.
- Focus Asset (bpy.ops.asset.focus_asset): Supports Collection and Action assets. When a Collection asset is selected, this will isolate that collection, and frame the viewport to its objects. With an Action, it will only work when there is an active armature object, and it will assign the action, set the scene's frame range, and focus the camera on the rig's visible child objects. Handy in combination with the next operator, especially if you use Blender's "Lock Camera to View" option.
- Thumbnail From Viewport (bpy.ops.asset.thumbnail_from_viewport): Makes a viewport snapshot and assigns it as the thumbnail of the active asset. Overlays will be disabled, but it's up to you to enter rendered view if you want to. Transparent pixels will be cropped, and the resolution is capped at 256 (by scaling it down if needed) which is Blender's hard limit for asset thumbnails.
- Crop Asset Thumbnails (bpy.ops.asset.crop_asset_thumbnails): Crops transparent pixels out of the selected assets' thumbnails.
- BotW: Auto-import .seanim: Loops over all visible or just the selected BotW armatures in the scene, and import all matching animations found in the directory specified in the add-on preferences.

### .seanim importer
The add-on also includes a modified version of the [.seanim importer](https://github.com/SE2Dev/io_anim_seanim) by [SE2DEV](https://github.com/SE2Dev). The following modifications were made:
- Clean up unnecessary keyframes, to shrink the amount of data stored on disk by about half, in the case of these baked game animations.
- Create a root bone on import as this is for some reason not imported with the .fbx files (the object is considered the root, which is dumb).
- Change the animation of the root bone by 90 degrees on X. It's unclear to me if this is related to the previous issue, but creating the root bone with different rotation doesn't matter. It just imports with a constant 90 degree offset on the root bone.
- If any scaling is applied on any animation of the armature being imported on, the children of that bone will have scale inheritance disabled. This results in correct looking animations. An example of this is animals breathing, where the upper spine bone would be scaled, which obviously shouldn't propagate to the head or front legs.
- It will print when trying to import animation for a bone which doesn't exist. This can only happen if you selected the wrong skeleton.

Note that a few characters might be re-using animations of other characters, so they won't be touched by the Auto-import operation, which means the missing root bone for them won't be created. For these cases, either manually import an animation with these armatures selected, or just create the root bone yourself, as you see them on the fixed armatures.

### Shading
To create the shaders included in this add-on, I initially followed this excellent [BotW shader tutorial series by Thejudsub](https://www.youtube.com/watch?v=Sb3CRU2DufU). I re-structured the nodes, added support for many other shader types such as non-cel-shaded environment props, glowing weapons with scrolling emissions, posable eyes, and so on. I also added support for a point light, figured out how to package it all up in a way that's easily re-usable, and used Attribute nodes instead of Drivers, to improve performance in complex scenes by about 100x. (Drivers in shader nodes are very bad for performance.)

### How the automatic shader set-up works

This section is for the technically curious. How does the add-on get so much material data? The answer is "mostly guessing".

- The only material data that actually imports is the albedo texture in the .fbx.
- From there, we can guess the rest of the textures by removing the "_Alb" suffix from the albedo's name, and looking for other textures that start with the same string. Sometimes this misleads us, since we might catch "Moblin_Gold_Alb" even though we started out with "Moblin_Alb". These cases need to be fixed manually, it is what it is.
- From there, we can find an _Spm texture, I don't know what it stands for but if it only has a red channel, it's usually non-metallic and it controls the sketch highlights, ie. specularity of the surface. If there is a green channel, it's either metallic, hair, or rubber. Rubber is pretty much only used for the Rubber Armor, and no other asset in the game. If it's hair, the word "hair", "beard", or "fur" is pretty much always in the name of the texture file. For nearly all other cases where there is a green channel, it's a metal mask.
- _Nrm suffix is obvious, but some normal maps have garbage data in their Blue channel, so that's discarded in the shader. AFAICT, there's no need to invert or shuffle the R/G channels for Eevee.
- _EmmMsk suffix is actually not the emission mask, instead this is always a scrolling emmission texture to give some glowing items a pulsating feel. A shader for this can easily be created by referencing the scene time and FPS, and hooking them up to a UV offset. This is done by the add-on whenever such texture is detected.
- _Emm suffix is actually the static emission mask.
- If a mesh has 2 UV channels, all textures except the Albedo usually use that 2nd one. Cases where this is not true need to be fixed manually.
- All textures except Albedo should be set to Non-Color colorspace. Although there are a handful of _Emm textures that are actually emission color, but we're talking like 3 textures in the whole game.

You get the idea. There are a bunch more texture suffixes, but the point is, we start with the name of the .dae file, its folder, and the albedo texture, and we just hard-code a bunch of stuff from there and hope for the best. After import, these strings are stored in custom properties in case they might be useful for anything in the future.