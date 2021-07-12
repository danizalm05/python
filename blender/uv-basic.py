import csv
import bpy

#bpy.ops.curve.primitive_bezier_curve_add(enter_editmode=False, align='WORLD', location=(0, 0, 0),scale=(3, 3,31))
#https://www.youtube.com/watch?v=4zytiZczsps

bpy.ops.object.empty_add(type='PLAIN_AXES', align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))



bpy.ops.mesh.primitive_cube_add(size=2, align='WORLD', location=(20, 0, 0), scale=(1, 1, 1))


 
bpy.ops.object.modifier_add(type='ARRAY')
bpy.context.object.modifiers["Array"].count = 12



 
bpy.context.object.modifiers["Array"].curve = bpy.data.objects["Empty"]
#bpy.context.object.modifiers["Array"].fit_type = 'FIT_CURVE'
bpy.context.object.modifiers["Array"].use_object_offset = True
bpy.context.object.modifiers["Array"].offset_object = bpy.data.objects["Empty"]
bpy.context.object.modifiers["Array"].use_constant_offset = True

bpy.ops.object.transform_apply(location=True, rotation=False, scale=False)# ctr A /location
 
bpy.context.object.rotation_euler[2] = 0.523599#360/12
 
