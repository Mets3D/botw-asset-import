### What's this

This is a Blender extension to import BotW assets in .dae & .fbx format (you kinda need both) into Blender with a lot of automated clean-up. It includes various shaders which will be assigned automatically. I made it to enable the creation of 3D fan-art, but it can be useful for previewing mod content as well.

### Preparing Game Files
I wrote a detailed guide on how to prepare the game files for use with this add-on, which you can find [here](https://open3dlab.com/tutorials/view/241/). As you follow that guide, Step 6 will lead you back to here. If you're already familiar with modding and Switch Toolbox, then you only need that guide if you want to import mod assets.

### Installation & file paths
The add-on was written for Blender 4.4. Other versions may have issues. (ie. AttributeErrors)
Install like any other add-on that isn't on the Extension Platform:
- Download this repo as .zip
- In Blender, go to Edit->Preferences->Addons
- Little arrow on the top-right->Install From Disk...->Browse the .zip
- Enable the add-on.

- Follow the instruction on the tooltips (that appear on mouse hover) of the folder selectors.

### Models
Once you've done everything described above, you can import models by following these steps:
- Make sure Blender's .dae and .fbx importer add-ons are enabled, since this add-on needs them.
- Go to "Window->Toggle System Console", so you can see that it's doing something. Avoid selecting text in this window, as that causes it to pause processing. You can press any key to resume.
- Copy the assets you want to import into another folder. This is necessary because Blender's importer interface can't select a sub-set of folders within a folder.
- Go to File->Import->BotW .dae & .fbx->browse the folder you just made->hit Import

Things to note:
- Reskins are not handled; Since there's only 1 Bokoblin mesh, only 1 Bokoblin will be imported. To create the reskinned versions, you'll have to duplicate things and hook up the textures yourself.
- I did my best to make materials look as close as possible to how they look in the game, but it can't be perfect.

### Asset Operators
Some of these operators are not strictly related to BotW and may be split out into a separate add-on in the future. They are for helping to create an actually usable asset library:
- Merge Actions: Merge any actions selected in the Asset Browser/Outliner. Useful for Link's animations, where he sometimes has unique animations split up into separate head/body actions that belong together.
- Merge Armatures: Merge selected armatures by removing duplicate bones and preserving parenting/modifier relationships. Useful for merging clothes onto characters.
- Focus Asset: Supports Collection and Action assets. When a Collection asset is selected, this will isolate that collection, and frame the viewport to its objects. With an Action, it will only work when there is an active armature object, and it will assign the action, set the scene's frame range, and focus the camera on the rig's visible child objects. Handy in combination with the next operator, especially if you use Blender's "Lock Camera to View" option.
- Thumbnail From Viewport: Makes a viewport snapshot and assigns it as the thumbnail of the active asset. Overlays will be disabled, but it's up to you to enter rendered view if you want to. Transparent pixels will be cropped, and the resolution is capped at 256 (by scaling it down if needed) which is Blender's hard limit for asset thumbnails.
- Crop Asset Thumbnails: Crops transparent pixels out of the selected assets' thumbnails.

### Animations
The add-on also includes a modified version of the [.seanim importer](https://github.com/SE2Dev/io_anim_seanim) by [SE2DEV](https://github.com/SE2Dev). The following modifications were made:
- Clean up unnecessary keyframes, to shrink the amount of data stored on disk by about half, in the case of these baked game animations.
- Create a root bone on import as this is for some reason not imported with the .fbx files, resulting in losing root motion.
- If any scaling is applied on any animation of the armature being imported on, the children of that bone will have scale inheritance disabled. This results in correct looking animations. An example of this is animals breathing, where the upper spine bone would be scaled, which obviously shouldn't propagate to the head or front legs.
- It will print when trying to import animation for a bone which doesn't exist. This can only happen if you selected the wrong skeleton.

There are also two operators besides importing animations:
- "Fix BotW Animations": This operator can be run on a selected armature to rotate the animation of the root bone by 90 degrees on all of its corresponding animations (by name prefix), without affecting its children. Without this, the root bone is always rotated by 90 degrees, and all of its children are counter-rotated. There is no visual difference from applying this fix, the result is just cleaner to work with.
- "BotW: Auto-import .seanim": Tries to automatically find, import, fix, and rename all animations of the selected armature's asset. This relies on the Animations directory being specified in the add-on preferences.

Things to note:
- A few characters re-use animations of other characters, so the Auto-import operation won't work on them.
- For the scale inheritance fix mentioned above, the armature itself needs to be modified, which is different from just importing animation data. The animations will only look right on armatures which had this fix applied to them.

### Map Import
The add-on has work-in-progress functionality to import maps. These are the "BotW: Build asset library for map import" and "BotW: Import Map Section" operators, only available through the search bar with Developer Extras enabled in your user preferences. The former will create .blend files for individual assets of the game (this can take a while), while the latter will instantiate those assets, if they indeed exist (this only takes a second).

Terrain importing is not implemented yet, but I'm working on it.

### Credits
This project wouldn't have been possible without at least the following open source projects:
- [Switch Toolbox](https://github.com/KillzXGaming/Switch-Toolbox)
- [bmubin](https://github.com/augmero/bmubin)
- [seanim importer](https://github.com/SE2Dev/io_anim_seanim)
- [Noesis](https://richwhitehouse.com/index.php?content=inc_projects.php&showproject=91)
Furthermore:
- A big thank you to [thejudsub](https://www.youtube.com/watch?v=Sb3CRU2DufU) for his Blender shading tutorial series which inspired this whole project.
- Thanks to [freestylized.com](https://freestylized.com/) for the sky texture I included.