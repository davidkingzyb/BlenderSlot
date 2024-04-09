# 2023/8/8 by DKZ https://github.com/davidkingzyb/BlenderSlot

bl_info = {
    "name": "BlenderSlot",
    "description": "A blender addon for record your operations and manage your customize scripts.",
    "author": "DKZ",
    "version": (1, 1, 0),
    "blender": (3, 6, 0),
    "location": "View3D > Sidebar > Blender Slot",
    "category": "System",
    "doc_url":"https://github.com/davidkingzyb/BlenderSlot"
}


import bpy
from .operators import ShowCode,ExecCode,SaveCode,DeleteCode,RecordCode,PauseRecord,AskOllama
from .ui import MainPanel




##### Registration #####

def register():
    print('blender slot register')
    bpy.utils.register_class(MainPanel)
    bpy.utils.register_class(ShowCode)
    bpy.utils.register_class(ExecCode)
    bpy.utils.register_class(SaveCode)
    bpy.utils.register_class(DeleteCode)
    bpy.utils.register_class(RecordCode)
    bpy.utils.register_class(PauseRecord)
    bpy.utils.register_class(AskOllama)
    bpy.types.Scene.bs_filename=bpy.props.StringProperty(
        name="",
        description="bs_temp_file_name",
        default="new_script",
    )
    bpy.types.Scene.bs_ollama_query = bpy.props.StringProperty(
        name="",
        description="bs_ollama_query",
        default="write a blender script to",
    )
    bpy.types.Scene.record_index = bpy.props.IntProperty(default=-1)



def unregister():
    bpy.utils.unregister_class(MainPanel)
    bpy.utils.unregister_class(ShowCode)
    bpy.utils.unregister_class(ExecCode)
    bpy.utils.unregister_class(SaveCode)
    bpy.utils.unregister_class(DeleteCode)
    bpy.utils.unregister_class(RecordCode)
    bpy.utils.unregister_class(PauseRecord)
    bpy.utils.unregister_class(AskOllama)
    del bpy.types.Scene.bs_filename
    del bpy.types.Scene.record_index


if __name__ == "__main__":
    register()