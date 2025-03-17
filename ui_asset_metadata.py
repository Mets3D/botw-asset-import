import bpy

def get_asset_library(context, asset):
     for asset_library in context.preferences.filepaths.asset_libraries:
          if asset.full_library_path.startswith(asset_library.path):
               return asset_library

def draw_more_metadata(self, context):
        layout = self.layout
        asset = context.asset
        if not asset:
             return

        header, panel = layout.panel("More Asset Metadata", default_closed=True)
        header.label(text="More")
        if not panel:
             return

        panel.enabled = False
        panel.prop(asset, 'full_library_path')
        panel.prop(asset, 'full_path')
        panel.prop(asset, 'id_type')
        if asset.local_id:
            panel.prop(asset, 'local_id')

        panel.separator()

        asset_library = get_asset_library(context, asset)
        if asset_library:
            panel.prop(asset_library, 'name', text="Asset Library")
            panel.prop(asset_library, 'path', text="Path")
            panel.prop(asset_library, 'import_method', text="Import Method")
            panel.prop(asset_library, 'use_relative_path', text="Use Relative")
            panel.separator()

        panel.prop(asset.metadata, 'author')
        panel.prop(asset.metadata, 'catalog_id')
        panel.prop(asset.metadata, 'catalog_simple_name')
        panel.prop(asset.metadata, 'copyright')
        panel.prop(asset.metadata, 'description')
        panel.prop(asset.metadata, 'license')

        panel.separator()


def register():
    bpy.types.ASSETBROWSER_PT_metadata.append(draw_more_metadata)

def unregister():
    bpy.types.ASSETBROWSER_PT_metadata.remove(draw_more_metadata)
