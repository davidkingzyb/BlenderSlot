# BlenderSlot !()[https://github.com/davidkingzyb/BlenderSlot]

import bpy

def DeleteAttributeByName(Attribs, Name):
    AttIndex = Attribs.find(Name)
    if(AttIndex != -1):
        Attribs.remove(Attribs[AttIndex])

def gressVertexColor(obj):
    mesh=obj.data
    att = mesh.attributes
    DeleteAttributeByName(att, "Color")
    DeleteAttributeByName(att, "Attribute")
    vc=mesh.color_attributes.new(
        name='Color',
        type='FLOAT_COLOR',
        domain='POINT',
    )
    max=0
    min=999
    for i,v in enumerate(mesh.vertices):
        if v.co[2]>max:
            max=v.co[2]
        if v.co[2]<min:
            min=v.co[2]
        #print(i,v.co,v.co[2])
    l=max-min
    for i,v in enumerate(mesh.vertices):
        r=(v.co[2]-min)/l
        #print(i,r)
        mesh.attributes['Color'].data[i].color=[r,r,r,1.0]
        
    


selected_objects = bpy.context.selected_objects

for obj in selected_objects:
    gressVertexColor(obj)
    
    