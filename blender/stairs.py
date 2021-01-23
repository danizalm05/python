#Stairs - Olav3D Tutorials
 
# https://www.youtube.com/watch?v=ky2Mp5yDGDA
#  

import bpy
from math  import sin, pi
 
 
for i in range(0,10):
   #  bpy.ops.mesh.primitive_cube_add(size=2,  location=(i, 0, 0), scale=(1, i*2, i*2))
      bpy.ops.mesh.primitive_cube_add(size=2,  location=(0, i*2, i*2)   )
      bpy.ops.transform.resize(value=(10, 1, 1))



 