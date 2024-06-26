# 2023/8/8 by DKZ https://github.com/davidkingzyb/BlenderSlot

import bpy
import os
from .ui import MainPanel
root_path=os.path.dirname(__file__)


class DeleteCode(bpy.types.Operator):
    """delete script and remove slot from BlenderSlot"""
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
    
class UnlinkCode(bpy.types.Operator):
    """delete script from current blender file"""
    bl_idname='bs.unlinkcode'
    bl_label='unlink'
    bl_options = {'REGISTER', 'UNDO'}

    file_name:bpy.props.StringProperty(
        name="file_name",
        description="file name",
        default="",
    )

    def execute(self, context):
        for x in bpy.data.texts.items():
            if x[0]== self.file_name:
                bpy.data.texts.remove(x[1])
        bpy.utils.unregister_class(MainPanel)
        bpy.utils.register_class(MainPanel)
        return {'FINISHED'}

class SaveCode(bpy.types.Operator):
    """save script to BlenderSlot"""
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
    """exec custom script"""
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
    """open Text Editor"""
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
        print('',bpy.utils.script_path_user())
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

class RecordCode(bpy.types.Operator):
    """start record your operations"""
    bl_idname='bs.recordcode'
    bl_label='record'
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        records=getRecords()
        bpy.context.scene.bs_record_index=len(records)
        bpy.utils.unregister_class(MainPanel)
        bpy.utils.register_class(MainPanel)
        return {'FINISHED'}
    

class PauseRecord(bpy.types.Operator):
    """stop record your operations and generate script"""
    bl_idname='bs.pauserecord'
    bl_label='pause'
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
        records=getRecords()
        bs_record_index=bpy.context.scene.bs_record_index
        bpy.context.scene.bs_record_index=-1# init index for next record
        text='import bpy\n'
        for i in range(bs_record_index,len(records)):
            text=text+records[i]+'\n'
        self.code=text
        text_editor_area = None
        for area in context.screen.areas:
            if area.type == 'TEXT_EDITOR':
                text_editor_area = area
                break
        if text_editor_area is None:
            text_editor_area = split_area_to_text_editor(context)

        _t = bpy.data.texts.new(name=self.file_name)# if have same name file_name will add .001
        context.scene.bs_filename=_t.name
        _t.write(text)

        text_editor_area.spaces.active.text = _t
        # refresh ui
        bpy.utils.unregister_class(MainPanel)
        bpy.utils.register_class(MainPanel)
        return {'FINISHED'}

def getRecords():
    area = bpy.context.area
    old_type = area.type
    area.type = 'INFO'
    bpy.ops.info.select_all()
    bpy.ops.info.report_copy()
    pasted_text = bpy.context.window_manager.clipboard
    records=pasted_text.split('\n')
    area.type = old_type
    
    return records

def split_area_to_text_editor(context):
    area = context.area
    for region in area.regions:
        if region.type == 'WINDOW':
            override = {'area': area, 'region': region}
            bpy.ops.screen.area_split(direction='VERTICAL', factor=0.5)
            break
    new_area = context.screen.areas[-1]
    new_area.type = 'TEXT_EDITOR'
    return new_area