
import os,sys

dir0  = os.path.join(os.path.split(__file__)[0])
if dir0 not in sys.path:
	sys.path.insert(0, dir0)

from user_settings import paths2add
sys.path.pop(0)

for dir0 in paths2add:
	if dir0 not in sys.path:
		sys.path.insert(0, dir0)


