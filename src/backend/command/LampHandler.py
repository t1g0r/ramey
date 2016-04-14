import sys
from CommandBase import CommandBase
from pprint import pprint
import GPIOHandler.GPIOHandler


class LampHandler(CommandBase):
	"""docstring for LampHandler"""
	def __init__(self, *args):
		super(LampHandler, self).__init__(*args)
		params = {}
		params["gpio_setup"] = "out"
		ghandler = GPIOHandler(self.Pins,params)
		
		

	def execute(self):
		super(LampHandler,self).execute()
		method = getattr(self,self.methodStr)
		method()

	def hidupkanlampu(self):
		print "hidupkan lampu"
		ghandler.SetPin(value=True)


	def matikanlampu(self):
		print "matikan lampu"
		ghandler.SetPin(value=False)
