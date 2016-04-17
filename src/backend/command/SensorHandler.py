import sys
from CommandBase import CommandBase
from pprint import pprint
from GPIOHandler import GPIOHandler
import time

class SensorHandler(CommandBase):
	"""docstring for SensorHandler"""
	def __init__(self, *args):
		super(SensorHandler, self).__init__(*args)
		# self.arg = arg

	def execute(self):
		super(SensorHandler,self).execute()
		method = getattr(self,self.params["method"])
		method()

	def switchon(self):
		self.sensor.active=True
		self.callback("Sensor telah dihidupkan!")

	def switchoff(self):
		self.sensor.active=False
		self.callback("Sensor telah dimatikan!")
