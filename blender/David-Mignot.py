#https://www.youtube.com/watch?v=r8hqLh_HE08
# Artistic Coding in Blender by David Mignot
import   bpy
import random
spacing  = 2.2
for x in  range(10):
    for y in  range(10):
       location=(x * spacing, y * spacing,random.random()*2) 
       bpy.ops.mesh.primitive_cube_add(location=location)
#3:45  shader