import json
import urllib.request
import bpy
from .operators import split_area_to_text_editor

ollama_host='http://127.0.0.1:11434'

class AskOllama(bpy.types.Operator):
    bl_idname='bs.ask_ollama'
    bl_label='ollama'
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

    query:bpy.props.StringProperty(
        name="query",
        description="ollama query",
        default="",
    )

    def execute(self, context):
        resp=reqOllama(self.query,context.scene.bs_ollama_model)    
        self.code=resp
        text_editor_area = None
        for area in context.screen.areas:
            if area.type == 'TEXT_EDITOR':
                text_editor_area = area
                break
        if text_editor_area is None:
            text_editor_area = split_area_to_text_editor(context)

        _t = bpy.data.texts.new(name=self.file_name)# if have same name file_name will add .001
        context.scene.bs_filename=_t.name
        _t.write(resp)

        text_editor_area.spaces.active.text = _t
        return {'FINISHED'}
    
def reqOllama(query,model=None):
    if not model:
        return f'\n\'\'\'\nquery:{query}\n\nollama:can\'t connect to ollama, please check network.\n\'\'\''
    print(query,model)
    req={
        "model": model,
        "messages": [
            {
                "role": "user",
                "content": f"{query}"
            }
        ],
        "stream":False
    }
    data=bytes(json.dumps(req),'utf8')
    try:
        response=urllib.request.urlopen(urllib.request.Request(ollama_host+'/api/chat',data=data))
        content=json.loads(response.read().decode('utf-8')).get('message',{}).get('content','')
        result=content.replace('```python','\n\'\'\'').replace('```','\n\'\'\'\n')
        return f'\n\'\'\'\nquery:{query}\n\nollama:{result}\n\'\'\''
    except Exception as err:
        return f'\n\'\'\'\nquery:{query}\n\nollama:can\'t connect to ollama, please check network.\n\'\'\''

def getOllamaModels():
    items=[]
    try:
        response=urllib.request.urlopen(ollama_host+'/api/tags')
        models=json.loads(response.read().decode('utf-8')).get('models',[])
        for m in models:
            items.append((m.get('name',''),m.get('name',''),''))
    except Exception as err:
        print('get ollama models fail')
    return bpy.props.EnumProperty(
        name="",
        items=items
    )