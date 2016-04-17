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

	def dip(self,seconds,delay):
		self.ghandler.SetPin(value=True)
		time.sleep(seconds)
		self.ghandler.SetPin(value=False)
		time.sleep(delay)

	def echo(self):
		print "Test Echo"
		self.dip(.1,.1)
		self.dip(.1,.1)
		self.dip(.1,.2)
		self.dip(.3,.2)
		self.dip(.5,.5)
