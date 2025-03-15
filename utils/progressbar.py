import bpy
from bpy.props import IntProperty

class ProgressBar:
    @staticmethod
    def draw_progbar(self, context):
        wm = context.window_manager
        factor = wm.assets_progress/wm.assets_total
        self.layout.label(text="Rendering Thumbnail:")
        self.layout.progress(text=f"{wm.assets_progress}/{wm.assets_total}", factor=factor)

    def __init__(self, total=100):
        self.total = total
        bpy.types.WindowManager.assets_total = IntProperty()
        bpy.types.WindowManager.assets_progress = IntProperty()

        bpy.types.ASSETBROWSER_MT_editor_menus.append(self.draw_progbar)

    def update(self, context, value):
        context.window_manager.assets_total = self.total
        context.window_manager.assets_progress = value

    def destroy(self):
        del bpy.types.WindowManager.assets_total
        del bpy.types.WindowManager.assets_progress
        bpy.types.ASSETBROWSER_MT_editor_menus.remove(self.draw_progbar)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.destroy()