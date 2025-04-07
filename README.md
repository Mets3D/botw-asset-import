### What's this

This is a Blender extension to import BotW assets in .dae & .fbx format into Blender with a lot of automated clean-up. It includes various shaders which will be assigned automatically. I made it to enable the creation of 3D fan-art, but it can be useful for previewing mod content as well.

### Installation & file paths

The add-on was written for Blender 4.4. Other versions may have issues. (AttributeError: X: attribute "Y" not found)
Install like any other add-on that isn't on the Extension Platform:
- Download this repo as .zip
- In Blender, go to Edit->Preferences->Addons
- Little arrow on the top-right->Install From Disk...->Browse the .zip
- Enable the add-on.

- Follow the instruction on the "Textures/Icons/Animations Folder" inputs' tooltips (that appear on mouse hover) to browse the correct folders.

### How to use
- Use [my modified Switch Toolbox](https://github.com/Mets3D/Switch-Toolbox/releases) to extract the game's models (.dae), textures (.png), inventory icons (.jpg), and animations (.seanim). Everything except .dae is optional but recommended.
- Convert the .dae files to .fbx using a tool like [Noesis](https://richwhitehouse.com/index.php?content=inc_projects.php&showproject=91), to fix bone rotations. The .fbx files must be directly next to the .dae files, with the same exact name. Without this step, animations will not work.
- Browse the appropriate folders in the add-on's preferences.
- Enable Blender's .dae and .fbx importers.
- Go to "Window->Toggle System Console", so you can see that it's doing something. Avoid selecting text in this window, as that causes it to pause processing. You can press any key to resume.
- Copy a sub-set of models you want to import to another folder, because importing the entire game at once will probably run you out of memory and take ages.
- In Blender, go to "Import->BotW (.dae & .fbx)", then navigate to the folder and hit Import.

### What it does
- Takes the armature from .fbx file if there is one, and tries to improve its aesthetic by assigning bone shapes.
- Sets up high quality EEVEE materials based on [thejudsub](https://www.youtube.com/watch?v=Sb3CRU2DufU)'s work. Non-cel-shaded assets will be assigned a regular shader. (Heavily modified)
- Renames assets to how they're named in-game where possible, based on [this dictionary](https://github.com/MrCheeze/botw-tools/blob/master/botw_names.json) by MrCheeze. (Heavily modified)
- Sets up Bloom viewport compositing which is vital for emission to look like in-game.
- Adds a custom-made MatCap that makes the shaded viewport look a bit like BotW cel shading. This requires one restart after installing the add-on.
- Sets up Blender Assets with in-game inventory icons when possible. This requires exporting the icons from the game:
    - Use Switch Toolbox to extract the game's "content\UI\StockItem" folder. Make sure to switch the export format to .jpg, and to leave the "Create folders" option enabled.
    - In the add-on's preferences, browse the resulting folder in the "Icons Folder" option.
- Adds some handy operators and a tweaked .seanim importer, see below.

### What it doesn't do
- Not every material setting can be guessed correctly by the importer, since the game's shading tech is not fully known. The shader nodegroups were designed to be easy to tweak, and you should only ever need to tweak things at the top level, never any nested node groups.
- Reskins are not handled. Since there's only 1 Bokoblin mesh, only 1 Bokoblin will be imported. To create the reskinned versions, you'll have to duplicate stuff and load textures manually.
- A very small set of animations don't work, ie. the Dragons. They don't even load correctly into Switch Toolbox.

### Operators
Also included is a number of handy operators for the asset browser. These may be split out into a separate add-on in the future, which I'll try to remember to mention here if it ever happens.
These are:
- Merge Actions (bpy.ops.asset.merge_actions): Merge any actions selected in the Asset Browser/Outliner. Useful Link's animations, where he sometimes has unique animations split up into separate head/body actions that belong together.
- Merge Armatures (bpy.ops.object.botw_merge_armatures): Merge selected armatures by removing duplicate bones and preserving parenting/modifier relationships. Useful for merging clothes onto characters.
- Focus Asset (bpy.ops.asset.focus_asset): Supports Collection and Action assets. When a Collection asset is selected, this will isolate that collection, and frame the viewport to its objects. With an Action, it will only work when there is an active armature object, and it will assign the action, set the scene's frame range, and focus the camera on the rig's visible child objects. Handy in combination with the next operator, especially if you use Blender's "Lock Camera to View" option.
- Thumbnail From Viewport (bpy.ops.asset.thumbnail_from_viewport): Makes a viewport snapshot and assigns it as the thumbnail of the active asset. Overlays will be disabled, but it's up to you to enter rendered view if you want to. Transparent pixels will be cropped, and the resolution is capped at 256 (by scaling it down if needed) which is Blender's hard limit for asset thumbnails.
- Crop Asset Thumbnails (bpy.ops.asset.crop_asset_thumbnails): Crops transparent pixels out of the selected assets' thumbnails.
- BotW: Auto-import .seanim: Loops over all visible or just the selected BotW armatures in the scene, and import all matching animations found in the directory specified in the add-on preferences.

### .seanim importer
The add-on also includes a modified version of the [.seanim importer](https://github.com/SE2Dev/io_anim_seanim) by [SE2DEV](https://github.com/SE2Dev). The following modifications were made:
- Clean up unnecessary keyframes, to shrink the amount of data stored on disk by about half, in the case of these baked game animations.
- Create a root bone on import as this is for some reason not imported with the .fbx files, resulting in losing root motion.
- If any scaling is applied on any animation of the armature being imported on, the children of that bone will have scale inheritance disabled. This results in correct looking animations. An example of this is animals breathing, where the upper spine bone would be scaled, which obviously shouldn't propagate to the head or front legs.
- It will print when trying to import animation for a bone which doesn't exist. This can only happen if you selected the wrong skeleton.
- As a separate and optional step after importing, a "Fix BotW Animations" operator can be run on a selected armature to rotate the animation of the root bone by 90 degrees on all of its corresponding animations (by name prefix), without affecting its children. Otherwise, the root bone is always rotated by 90 degrees, and all of its children are counter-rotated. There is no visual difference from applying this fix, the result is just cleaner to work with.

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

### Credits
This project wouldn't have been possible without at least the following open source projects:
- [Switch Toolbox](https://github.com/KillzXGaming/Switch-Toolbox)
- [bmubin](https://github.com/augmero/bmubin)
- [seanim importer](https://github.com/SE2Dev/io_anim_seanim)
- [Noesis](https://richwhitehouse.com/index.php?content=inc_projects.php&showproject=91)
Furthermore:
- A big thank you to [thejudsub](https://www.youtube.com/watch?v=Sb3CRU2DufU) for his Blender shading tutorial series which inspired this whole project.
- Thanks to [freestylized.com](https://freestylized.com/) for the sky texture I used (they have many more, really worth checking out!)