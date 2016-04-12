import sys
from CommandBase import CommandBase
from pprint import pprint


class LampHandler(CommandBase):
	"""docstring for LampHandler"""
	def __init__(self, *args):
		super(LampHandler, self).__init__(*args)

	def execute(self):
		super(LampHandler,self).execute()
		# pprint(self.params)
		# print self.params["command"]["message"][1:]
		# print(self.params["text"][1:])
		method = getattr(self,self.params["command"]["message"][1:])
		method()

	def hidupkanlampu(self):
		print "hidupkan lampu"

	def matikanlampu(self):
		print "matikan lampu"
