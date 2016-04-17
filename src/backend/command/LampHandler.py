import sys
from CommandBase import CommandBase
from pprint import pprint
# from GPIOHandler import GPIOHandler


class LampHandler(CommandBase):
	"""docstring for LampHandler"""
	def __init__(self, *args):
		super(LampHandler, self).__init__(*args)
		params = {}
		params["gpio_setup"] = "out"
		self.ghandler = GPIOHandler(self.Pins,params)
		
		

	def execute(self):
		super(LampHandler,self).execute()
		method = getattr(self,self.params["method"])
		method()

	def hidupkanlampu(self):
		print "hidupkan lampu"
		self.ghandler.SetPin(value=True)


	def matikanlampu(self):
		print "matikan lampu"
		self.ghandler.SetPin(value=False)
