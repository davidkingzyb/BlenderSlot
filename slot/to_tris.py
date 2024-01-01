# BlenderSlot !()[https://github.com/davidkingzyb/BlenderSlot]

import bpy

obj = bpy.context.active_object

bpy.ops.object.mode_set(mode='EDIT')
bpy.ops.mesh.select_all(action='SELECT')
bpy.ops.mesh.quads_convert_to_tris()
bpy.ops.mesh.normals_make_consistent(inside=False)
bpy.ops.object.mode_set(mode='OBJECT')