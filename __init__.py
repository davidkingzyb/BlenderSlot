# 2023/8/8 by DKZ https://github.com/davidkingzyb/BlenderSlot

bl_info = {
    "name": "BlenderSlot",
    "description": "manage scripts and customize your own functions",
    "author": "DKZ",
    "version": (1, 0, 0),
    "blender": (2, 93, 0),
    "location": "View3D > Sidebar > Blender Slot",
    "category": "System",
    "doc_url":"https://github.com/davidkingzyb/BlenderSlot"
}


import bpy
from .operators import ShowCode,ExecCode,SaveCode,DeleteCode
from .ui import MainPanel




##### Registration #####

def register():
    print('blender slot register')
    bpy.utils.register_class(MainPanel)
    bpy.utils.register_class(ShowCode)
    bpy.utils.register_class(ExecCode)
    bpy.utils.register_class(SaveCode)
    bpy.utils.register_class(DeleteCode)
    bpy.types.Scene.bs_filename=bpy.props.StringProperty(
        name="",
        description="bs_temp_file_name",
        default="new_script",
    )



def unregister():
    bpy.utils.unregister_class(MainPanel)
    bpy.utils.unregister_class(ShowCode)
    bpy.utils.unregister_class(ExecCode)
    bpy.utils.unregister_class(SaveCode)
    bpy.utils.unregister_class(DeleteCode)
    del bpy.types.Scene.bs_filename


if __name__ == "__main__":
    register()