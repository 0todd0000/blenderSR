
import os
from blenderSR import BlenderScriptRunner

path2script = os.path.join(os.path.split(__file__)[0], 'move_cube.py')
bsr         = BlenderScriptRunner()
bsr.run(path2script)

