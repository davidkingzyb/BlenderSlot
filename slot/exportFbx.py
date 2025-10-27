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
        bake_space_transform=True,
        axis_forward='-Y',
        axis_up='Z',
        apply_unit_scale=True,
        apply_scale_options='FBX_SCALE_UNITS'
        
    )

    bpy.data.scenes.remove(new_scene)
    bpy.context.window.scene = bpy.context.scene
    
selected_objects = bpy.context.selected_objects

for obj in selected_objects:
    exportObj(obj)

"""
bpy.ops.export_scene.fbx(filepath='', check_existing=True, filter_glob='*.fbx', use_selection=False, use_visible=False, use_active_collection=False, global_scale=1.0, apply_unit_scale=True, apply_scale_options='FBX_SCALE_NONE', use_space_transform=True, bake_space_transform=False, object_types={'ARMATURE', 'CAMERA', 'EMPTY', 'LIGHT', 'MESH', 'OTHER'}, use_mesh_modifiers=True, use_mesh_modifiers_render=True, mesh_smooth_type='OFF', colors_type='SRGB', prioritize_active_color=False, use_subsurf=False, use_mesh_edges=False, use_tspace=False, use_triangles=False, use_custom_props=False, add_leaf_bones=True, primary_bone_axis='Y', secondary_bone_axis='X', use_armature_deform_only=False, armature_nodetype='NULL', bake_anim=True, bake_anim_use_all_bones=True, bake_anim_use_nla_strips=True, bake_anim_use_all_actions=True, bake_anim_force_startend_keying=True, bake_anim_step=1.0, bake_anim_simplify_factor=1.0, path_mode='AUTO', embed_textures=False, batch_mode='OFF', use_batch_own_dir=True, use_metadata=True, axis_forward='-Z', axis_up='Y')

filepath (string, (optional, never None)) – File Path, Filepath used for exporting the file

check_existing (boolean, (optional)) – Check Existing, Check and warn on overwriting existing files

filter_glob (string, (optional, never None)) – filter_glob

use_selection (boolean, (optional)) – Selected Objects, Export selected and visible objects only

use_visible (boolean, (optional)) – Visible Objects, Export visible objects only

use_active_collection (boolean, (optional)) – Active Collection, Export only objects from the active collection (and its children)

global_scale (float in [0.001, 1000], (optional)) – Scale, Scale all data (Some importers do not support scaled armatures!)

apply_unit_scale (boolean, (optional)) – Apply Unit, Take into account current Blender units settings (if unset, raw Blender Units values are used as-is)

apply_scale_options (enum in ['FBX_SCALE_NONE', 'FBX_SCALE_UNITS', 'FBX_SCALE_CUSTOM', 'FBX_SCALE_ALL'], (optional)) –

Apply Scalings, How to apply custom and units scalings in generated FBX file (Blender uses FBX scale to detect units on import, but many other applications do not handle the same way)

FBX_SCALE_NONE All Local – Apply custom scaling and units scaling to each object transformation, FBX scale remains at 1.0.

FBX_SCALE_UNITS FBX Units Scale – Apply custom scaling to each object transformation, and units scaling to FBX scale.

FBX_SCALE_CUSTOM FBX Custom Scale – Apply custom scaling to FBX scale, and units scaling to each object transformation.

FBX_SCALE_ALL FBX All – Apply custom scaling and units scaling to FBX scale.

use_space_transform (boolean, (optional)) – Use Space Transform, Apply global space transform to the object rotations. When disabled only the axis space is written to the file and all object transforms are left as-is

bake_space_transform (boolean, (optional)) – Apply Transform, Bake space transform into object data, avoids getting unwanted rotations to objects when target space is not aligned with Blender’s space (WARNING! experimental option, use at own risk, known to be broken with armatures/animations)

object_types (enum set in {'EMPTY', 'CAMERA', 'LIGHT', 'ARMATURE', 'MESH', 'OTHER'}, (optional)) –

Object Types, Which kind of object to export

EMPTY Empty.

CAMERA Camera.

LIGHT Lamp.

ARMATURE Armature – WARNING: not supported in dupli/group instances.

MESH Mesh.

OTHER Other – Other geometry types, like curve, metaball, etc. (converted to meshes).

use_mesh_modifiers (boolean, (optional)) – Apply Modifiers, Apply modifiers to mesh objects (except Armature ones) - WARNING: prevents exporting shape keys

use_mesh_modifiers_render (boolean, (optional)) – Use Modifiers Render Setting, Use render settings when applying modifiers to mesh objects (DISABLED in Blender 2.8)

mesh_smooth_type (enum in ['OFF', 'FACE', 'EDGE'], (optional)) –

Smoothing, Export smoothing information (prefer ‘Normals Only’ option if your target importer understand split normals)

OFF Normals Only – Export only normals instead of writing edge or face smoothing data.

FACE Face – Write face smoothing.

EDGE Edge – Write edge smoothing.

colors_type (enum in ['NONE', 'SRGB', 'LINEAR'], (optional)) –

Vertex Colors, Export vertex color attributes

NONE None – Do not export color attributes.

SRGB sRGB – Export colors in sRGB color space.

LINEAR Linear – Export colors in linear color space.

prioritize_active_color (boolean, (optional)) – Prioritize Active Color, Make sure active color will be exported first. Could be important since some other software can discard other color attributes besides the first one

use_subsurf (boolean, (optional)) – Export Subdivision Surface, Export the last Catmull-Rom subdivision modifier as FBX subdivision (does not apply the modifier even if ‘Apply Modifiers’ is enabled)

use_mesh_edges (boolean, (optional)) – Loose Edges, Export loose edges (as two-vertices polygons)

use_tspace (boolean, (optional)) – Tangent Space, Add binormal and tangent vectors, together with normal they form the tangent space (will only work correctly with tris/quads only meshes!)

use_triangles (boolean, (optional)) – Triangulate Faces, Convert all faces to triangles

use_custom_props (boolean, (optional)) – Custom Properties, Export custom properties

add_leaf_bones (boolean, (optional)) – Add Leaf Bones, Append a final bone to the end of each chain to specify last bone length (use this when you intend to edit the armature from exported data)

primary_bone_axis (enum in ['X', 'Y', 'Z', '-X', '-Y', '-Z'], (optional)) – Primary Bone Axis

secondary_bone_axis (enum in ['X', 'Y', 'Z', '-X', '-Y', '-Z'], (optional)) – Secondary Bone Axis

use_armature_deform_only (boolean, (optional)) – Only Deform Bones, Only write deforming bones (and non-deforming ones when they have deforming children)

armature_nodetype (enum in ['NULL', 'ROOT', 'LIMBNODE'], (optional)) –

Armature FBXNode Type, FBX type of node (object) used to represent Blender’s armatures (use the Null type unless you experience issues with the other app, as other choices may not import back perfectly into Blender…)

NULL Null – ‘Null’ FBX node, similar to Blender’s Empty (default).

ROOT Root – ‘Root’ FBX node, supposed to be the root of chains of bones….

LIMBNODE LimbNode – ‘LimbNode’ FBX node, a regular joint between two bones….

bake_anim (boolean, (optional)) – Baked Animation, Export baked keyframe animation

bake_anim_use_all_bones (boolean, (optional)) – Key All Bones, Force exporting at least one key of animation for all bones (needed with some target applications, like UE4)

bake_anim_use_nla_strips (boolean, (optional)) – NLA Strips, Export each non-muted NLA strip as a separated FBX’s AnimStack, if any, instead of global scene animation

bake_anim_use_all_actions (boolean, (optional)) – All Actions, Export each action as a separated FBX’s AnimStack, instead of global scene animation (note that animated objects will get all actions compatible with them, others will get no animation at all)

bake_anim_force_startend_keying (boolean, (optional)) – Force Start/End Keying, Always add a keyframe at start and end of actions for animated channels

bake_anim_step (float in [0.01, 100], (optional)) – Sampling Rate, How often to evaluate animated values (in frames)

bake_anim_simplify_factor (float in [0, 100], (optional)) – Simplify, How much to simplify baked values (0.0 to disable, the higher the more simplified)

path_mode (enum in ['AUTO', 'ABSOLUTE', 'RELATIVE', 'MATCH', 'STRIP', 'COPY'], (optional)) –

Path Mode, Method used to reference paths

AUTO Auto – Use relative paths with subdirectories only.

ABSOLUTE Absolute – Always write absolute paths.

RELATIVE Relative – Always write relative paths (where possible).

MATCH Match – Match absolute/relative setting with input path.

STRIP Strip Path – Filename only.

COPY Copy – Copy the file to the destination path (or subdirectory).

embed_textures (boolean, (optional)) – Embed Textures, Embed textures in FBX binary file (only for “Copy” path mode!)

batch_mode (enum in ['OFF', 'SCENE', 'COLLECTION', 'SCENE_COLLECTION', 'ACTIVE_SCENE_COLLECTION'], (optional)) –

Batch Mode

OFF Off – Active scene to file.

SCENE Scene – Each scene as a file.

COLLECTION Collection – Each collection (data-block ones) as a file, does not include content of children collections.

SCENE_COLLECTION Scene Collections – Each collection (including master, non-data-block ones) of each scene as a file, including content from children collections.

ACTIVE_SCENE_COLLECTION Active Scene Collections – Each collection (including master, non-data-block one) of the active scene as a file, including content from children collections.

use_batch_own_dir (boolean, (optional)) – Batch Own Dir, Create a dir for each exported file

use_metadata (boolean, (optional)) – Use Metadata

axis_forward (enum in ['X', 'Y', 'Z', '-X', '-Y', '-Z'], (optional)) – Forward

axis_up (enum in ['X', 'Y', 'Z', '-X', '-Y', '-Z'], (optional)) – Up
"""

