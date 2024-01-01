# BlenderSlot !()[https://github.com/davidkingzyb/BlenderSlot]

import bpy

export_path = "C:/Users/DKZ/Desktop/"


def exportObj(obj):
    new_scene = bpy.data.scenes.new(obj.name)
    new_scene.frame_end = 1
    
    new_scene.collection.objects.link(obj)
    bpy.context.window.scene = new_scene

    bpy.ops.export_scene.fbx(
        filepath=export_path+obj.name+'.fbx',
        check_existing=False,
        use_selection=True,
        object_types={'MESH'},
        bake_space_transform=True
    )

    bpy.data.scenes.remove(new_scene)
    bpy.context.window.scene = bpy.context.scene
    
selected_objects = bpy.context.selected_objects

for obj in selected_objects:
    exportObj(obj)