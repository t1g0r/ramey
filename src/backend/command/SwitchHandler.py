import sys
from CommandBase import CommandBase
from pprint import pprint
from GPIOHandler import GPIOHandler
import time


class SwitchHandler(CommandBase):
	"""docstring for SwitchHandler"""
	def __init__(self, *args):
		super(SwitchHandler, self).__init__(*args)
		params = {}
		params["gpio_setup"] = "out"
		self.ghandler = GPIOHandler(self.Pins,params)
		
		

	def execute(self):
		super(SwitchHandler,self).execute()
		method = getattr(self,self.params["method"])
		method()

	def switchon(self):
		print "hidupkan lampu"
		self.ghandler.SetPin(value=True)


	def switchoff(self):
		print "matikan lampu"
		self.ghandler.SetPin(value=False)

	def dip(self,seconds):
		self.ghandler.SetPin(value=True)
		time.sleep(seconds)
		self.ghandler.SetPin(value=False)

	def echo(self):
		print "Test Echo"
		self.dip(.2)
		self.dip(.2)
		self.dip(.2)
		self.dip(.5)
		self.dip(1)
