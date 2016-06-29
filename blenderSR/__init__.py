

__version__ = '0.0.1'   #(2016.06.28) 


import os
import user_settings as user



class BlenderScriptRunner(object):
	def __init__(self):
		self.path2blender       = user.path2blender
		self.path2setpath       = os.path.join(os.path.split(__file__)[0], 'set_path.py')
		self.path2usersettings  = os.path.join(os.path.split(__file__)[0], 'user_settings.py')
		self._check_blender_path()
		self._check_user_paths()


	def _check_blender_path(self):
		if not os.path.exists(self.path2blender):
			raise( UserWarning('The specified Blender path does not exist:\n   %s\n\nEdit "path2blender" in:\n   %s'%(self.path2blender, self.path2usersettings)) )
	def _check_script_path(self, path2script):
		if not os.path.exists(self.path2blender):
			raise( UserWarning('The specified script does not exist:\n   %s\n   %s'%path2script) )
	def _check_user_paths(self):
		for p in user.paths2add:
			if not os.path.exists(p):
				raise( UserWarning('The specified path does not exist:\n   %s\n\nEdit "paths2add" in:\n   %s'%(p, self.path2usersettings)) )


	def run(self, path2script):
		self._check_script_path(path2script)
		command = '%s -P %s -P %s' %(self.path2blender, self.path2setpath, path2script)
		os.system(command)

