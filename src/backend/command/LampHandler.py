import sys
from CommandBase import CommandBase


class LampHandler(CommandBase):
	"""docstring for LampHandler"""
	def __init__(self, *args):
		super(LampHandler, self).__init__(*args)
		self.args = args

	def execute(self):
		super(LampHandler,self).execute()
