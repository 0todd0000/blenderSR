
import os
from blenderSR import BlenderScriptRunner

print( '\n\n\nHello world! (from outside Blender)\n\n\n'  )


thisdir     = os.path.split(__file__)[0]
path2script = os.path.join(thisdir, 'hello_world.py')
bsr         = BlenderScriptRunner()
bsr.run(path2script)

