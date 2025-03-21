from ast import Attribute
import bpy
from bpy.props import IntProperty, StringProperty

class ProgressBar:
    instances = []

    @staticmethod
    def draw_progbar(self, context):
        wm = context.window_manager
        try:
            factor = wm.progressbar_progress/wm.progressbar_total
        except AttributeError:
            for instance in ProgressBar.instances:
                instance.destroy()
        self.layout.label(text=wm.progressbar_text + ":")
        self.layout.progress(text=f"{wm.progressbar_progress}/{wm.progressbar_total or 1}", factor=factor)

    def __init__(self, total=100, menu=bpy.types.STATUSBAR_HT_header, text="Progress"):
        self.total = max(1, total)
        self.text = text
        bpy.types.WindowManager.progressbar_total = IntProperty()
        bpy.types.WindowManager.progressbar_progress = IntProperty()
        bpy.types.WindowManager.progressbar_text = StringProperty()

        type(self).instances.append(self)

        menu.append(self.draw_progbar)
        self.menu = menu

    def update(self, context, value):
        context.window_manager.progressbar_total = self.total
        context.window_manager.progressbar_progress = value
        context.window_manager.progressbar_text = self.text

    def destroy(self):
        type(self).instances.remove(self)
        del bpy.types.WindowManager.progressbar_total
        del bpy.types.WindowManager.progressbar_progress
        self.menu.remove(self.draw_progbar)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.destroy()