# 2023/8/8 by DKZ https://github.com/davidkingzyb/BlenderSlot

import bpy
import os
from .ui import MainPanel

root_path=os.path.dirname(__file__)


class DeleteCode(bpy.types.Operator):
    bl_idname='bs.deletecode'
    bl_label='delete'
    bl_options = {'REGISTER', 'UNDO'}

    file_name:bpy.props.StringProperty(
        name="file_name",
        description="file name",
        default="",
    )

    def execute(self, context):
        try:
            os.remove(os.path.join(root_path,'slot\\'+self.file_name))
        except Exception as e:
            pass

        bpy.utils.unregister_class(MainPanel)
        bpy.utils.register_class(MainPanel)
        return {'FINISHED'}

class SaveCode(bpy.types.Operator):
    bl_idname='bs.savecode'
    bl_label='save'
    bl_options = {'REGISTER', 'UNDO'}

    file_name:bpy.props.StringProperty(
        name="file_name",
        description="file name",
        default="",
    )

    code:bpy.props.StringProperty(
        name="code",
        description="code",
        default="",
    )

    def execute(self, context):
        text = bpy.data.texts.get(self.file_name)
        self.code=text.as_string()
        with open(os.path.join(root_path,'slot\\'+self.file_name),'w') as f:
            f.write(self.code) 
        bpy.utils.unregister_class(MainPanel)
        bpy.utils.register_class(MainPanel)
        return {'FINISHED'}

class ExecCode(bpy.types.Operator):
    bl_idname='bs.execcode'
    bl_label='exec'
    bl_options = {'REGISTER', 'UNDO'}

    file_name:bpy.props.StringProperty(
        name="file_name",
        description="file name",
        default="",
    )

    code:bpy.props.StringProperty(
        name="code",
        description="code",
        default="",
    )

    def execute(self, context):
        text = bpy.data.texts.get(self.file_name)
        if text is not None:
            self.code=text.as_string()
        else:
            try:
                with open(os.path.join(root_path,'slot\\'+self.file_name),'r') as f:
                    self.code=f.read()
            except Exception as e:
                self.report({'ERROR'}, f"Error executing generated code: {e}")
                return {'CANCELLED'}
        global_namespace = globals().copy()
        try:
            exec(self.code,global_namespace)
        except Exception as e:
            self.report({'ERROR'}, f"Error executing generated code: {e}")
            return {'CANCELLED'}   
        return {'FINISHED'}

class ShowCode(bpy.types.Operator):
    bl_idname='bs.showcode'
    bl_label='show'
    bl_options = {'REGISTER', 'UNDO'}

    file_name:bpy.props.StringProperty(
        name="file_name",
        description="file name",
        default="",
    )

    code:bpy.props.StringProperty(
        name="code",
        description="code",
        default="",
    )

    def execute(self, context):
        print(self.file_name)       
        text = bpy.data.texts.get(self.file_name)
        if text is None:
            text = bpy.data.texts.new(self.file_name)
            try:
                with open(os.path.join(root_path,'slot\\'+self.file_name),'r') as f:
                    self.code=f.read()
            except Exception as e:
                # self.report({'ERROR'}, f"Error executing generated code: {e}")
                pass
            text.clear()
            text.write(self.code)
        else:
            self.code=text.as_string()

        text_editor_area = None
        for area in context.screen.areas:
            if area.type == 'TEXT_EDITOR':
                text_editor_area = area
                break

        if text_editor_area is None:
            text_editor_area = split_area_to_text_editor(context)
        
        text_editor_area.spaces.active.text = text

        return {'FINISHED'}
    
def split_area_to_text_editor(context):
    area = context.area
    for region in area.regions:
        if region.type == 'WINDOW':
            override = {'area': area, 'region': region}
            bpy.ops.screen.area_split(override, direction='VERTICAL', factor=0.5)
            break

    new_area = context.screen.areas[-1]
    new_area.type = 'TEXT_EDITOR'
    return new_area