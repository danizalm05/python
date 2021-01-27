#https://www.youtube.com/watch?v=r8hqLh_HE08
# Artistic Coding in Blender by David Mignot
import   bpy
import random

mat1 = bpy.data.materials.new(name="Material001") #set new material to variable
mat2 = bpy.data.materials.new(name="Material002")  

spacing  = 2.2
for x in  range(8):
    for y in  range(4):
       s = (1, 1, 5*random.random())
       location=(x * spacing, y * spacing,random.random()*2) 
       bpy.ops.mesh.primitive_cube_add(location=location,scale = s)
       
#3:45  shader

#activeObject = bpy.context.active_object #Set active object to variable
       item = bpy.context.active_object #Set active object to variable
    
       if random.random()<0.1:
            item.data.materials.append(mat1) #add the material to the object
            bpy.context.object.active_material.diffuse_color = (25 , 233 , 2,0) #change color
          # bpy.context.object.active_material.intensity = (11)
       else: 
             item.data.materials.append(mat2) #add the material to the object
             bpy.context.object.active_material.diffuse_color = (0.7,0.4,233,0) #change color   
             #bpy.context.object.active_material.specular_color = (235, 45, 0.5) 
             
#bpy.context.object.active_material.diffuse_color=(0.7,0.4,0.8,0)             
"""
 bpy.context.object.active_material.diffuse_
                                               color
                                               fresnel
                                               fresnel_factor
                                               intensity
                                               ramp
                                               ramp_blend
                                               ramp_factor
                                               ramp_input
                                               shader
                                               toon_size
                                               toon_smooth
>>> bpy.context.object.active_material.diffuse_color=(0.7,0.4,0.8)



"""   



 
          