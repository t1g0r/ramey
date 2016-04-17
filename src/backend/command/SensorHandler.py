import sys
from CommandBase import CommandBase
from pprint import pprint
from GPIOHandler import GPIOHandler
import time

class SensorHandler(CommandBase):
	"""docstring for SensorHandler"""
	def __init__(self, *arg):
		super(SensorHandler, self).__init__()
		# self.arg = arg

	def execute(self):
		super(SwitchHandler,self).execute()
		method = getattr(self,self.params["method"])
		method()

	def switchon(self):
		self.sensor.active=True

	def switchoff(self):
		self.sensor.active=False
