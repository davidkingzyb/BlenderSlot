# 2023/8/8 by DKZ https://github.com/davidkingzyb/BlenderSlot

import bpy
import os
root_path=os.path.dirname(__file__)

class MainPanel(bpy.types.Panel):
    bl_idname='bs.mainpanel'
    bl_label='Blender Slot'
    bl_space_type='VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Blender Slot'
    bl_options={"HEADER_LAYOUT_EXPAND"}

    def draw(self, context):
        layout = self.layout
        column = layout.column(align=True)
        slots=os.listdir(os.path.join(root_path,'slot'))

        for slot in slots:
            box=column.box()
            row = box.row(align=True)
            row.label(text=slot.replace('.py',''))
            save_op=row.operator('bs.savecode', text='', icon='ADD')
            save_op.file_name=slot
            delete_op=row.operator('bs.deletecode', text='', icon='REMOVE')
            delete_op.file_name=slot
            show_op=row.operator('bs.showcode', text='', icon='SCRIPT')
            show_op.file_name=slot
            exec_op=row.operator('bs.execcode', text='', icon='PLAY')
            exec_op.file_name=slot

        box=column.box()
        row = box.row(align=True)
        row.prop(context.scene,'bs_filename')
        _type='' if '.py' in context.scene.bs_filename else '.py'# for 001
        # row.label(text=context.scene.bs_filename)
        if bpy.context.scene.record_index==-1:
            record_op=row.operator('bs.recordcode', text='', icon='REC')
        else:
            pause_op=row.operator('bs.pauserecord', text='', icon='PAUSE')
            pause_op.file_name=context.scene.bs_filename+_type
        show_op=row.operator('bs.showcode', text='', icon='SCRIPT')
        show_op.file_name=context.scene.bs_filename+_type
        exec_op=row.operator('bs.execcode', text='', icon='PLAY')
        exec_op.file_name=context.scene.bs_filename+_type
        save_op=row.operator('bs.savecode', text='', icon='ADD')
        save_op.file_name=context.scene.bs_filename+_type