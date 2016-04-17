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

	def echo(self):
		print "Test Echo"
		self.ghandler.SetPin(value=True)
		time.sleep(.5)
		self.ghandler.SetPin(value=False)
		time.sleep(.5)
		self.ghandler.SetPin(value=True)
		time.sleep(1)
		self.ghandler.SetPin(value=False)
		time.sleep(.5)

		self.ghandler.SetPin(value=True)
		time.sleep(.5)
		self.ghandler.SetPin(value=False)
		time.sleep(.5)
		self.ghandler.SetPin(value=True)
		time.sleep(1)
		self.ghandler.SetPin(value=False)
