
# Set the default cube's location, rotation and scale

import bpy

cube = bpy.data.objects['Cube']

cube.location = 5, 0, 0
cube.rotation_euler = 0.5, 0, 0.2
cube.scale = 1, 1, 0.5



