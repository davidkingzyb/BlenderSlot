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
            row = column.box().row(align=True)
            # row.label(text=slot.replace('.py',''))
            exec_op=row.operator('bs.execcode', text=slot.replace('.py',''), icon='PLAY')  
            exec_op.file_name=slot
            delete_op=row.operator('bs.deletecode', text='', icon='REMOVE')
            delete_op.file_name=slot
            save_op=row.operator('bs.savecode', text='', icon='ADD')
            save_op.file_name=slot
            show_op=row.operator('bs.showcode', text='', icon='SCRIPT')
            show_op.file_name=slot
            
        for link_script in bpy.data.texts.items():
            row = column.box().row(align=True)
            # row.label(text=link_script[0].replace('.py',''))
            exec_op=row.operator('bs.execcode', text=link_script[0].replace('.py',''), icon='PLAY')
            exec_op.file_name=link_script[0]
            unlink_op=row.operator('bs.unlinkcode', text='', icon='X')
            unlink_op.file_name=link_script[0]
            save_op=row.operator('bs.savecode', text='', icon='ADD')
            save_op.file_name=link_script[0]
            show_op=row.operator('bs.showcode', text='', icon='SCRIPT')
            show_op.file_name=link_script[0]
            
        row = column.box().row(align=True)
        
        _type='' if '.py' in context.scene.bs_filename else '.py'# for 001
        
        if bpy.context.scene.bs_record_index==-1:
            record_op=row.operator('bs.recordcode', text='', icon='REC')
        else:
            pause_op=row.operator('bs.pauserecord', text='', icon='PAUSE')
            pause_op.file_name=context.scene.bs_filename+_type
        row.prop(context.scene,'bs_filename')
        # exec_op=row.operator('bs.execcode', text='', icon='PLAY')
        # exec_op.file_name=context.scene.bs_filename+_type
        # row.label(text=context.scene.bs_filename)
        # save_op=row.operator('bs.savecode', text='', icon='ADD')
        # save_op.file_name=context.scene.bs_filename+_type    
        show_op=row.operator('bs.showcode', text='', icon='SCRIPT')
        show_op.file_name=context.scene.bs_filename+_type
        
        # ollama
        
        ollama_box=column.box()
        ollama_text_row = ollama_box.row(align=True)
        ollama_text_row.prop(context.scene, 'bs_ollama_query')
        ollama_row=ollama_box.row(align=True)
        ollama_op=ollama_row.operator('bs.ask_ollama', text='', icon='QUESTION')
        ollama_op.file_name=context.scene.bs_filename+_type
        ollama_op.query=context.scene.bs_ollama_query
        ollama_row.prop(context.scene,'bs_ollama_model')

