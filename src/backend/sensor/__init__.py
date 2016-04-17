import sys
sys.path.append("backend/command/")
import time
from GPIOHandler import GPIOHandler
import RPi.GPIO as gpio
from utils import Parameter
from pprint import pprint


class MotionSensor(object):
	"""docstring for MotionSensor"""
	def __init__(self, config):
		super(MotionSensor, self).__init__()
		self.active = True		
		self.config = config
		self.callback = {}
		self.counter = 0
		self.params = {}
		self.Pin = config["pin"]
		self.dbconn = config["dbconn"]
		self.params["gpio_setup"] = "in"
		self.ghandler = GPIOHandler(self.Pin.split(","),self.params,gpio.PUD_DOWN)

		self.ghandler.Add_Event_Handler(pin=self.Pin.split(","),gpiosetup=gpio.BOTH,callback=self.OnMotion,bounce_time=50)

		buzzerpin = Parameter.getValuebyFieldname(self.dbconn,"sensor_motion","buzzer")
		# print buzzerpin
		self.params["gpio_setup"] = "out"
		pprint(buzzerpin.split(","))
		self.buzzerHandler = GPIOHandler(buzzerpin.split(","),self.params)

	def OnMotion(self,channel):
		if ((gpio.input(int(self.Pin))) and (self.active)):
			self.buzzerHandler.echo()
			if len(self.callback) > 0:
				for call in self.callback:
					pprint(call)

	def Execute(self):
			try:
				while True:
					time.sleep(1)

			except KeyboardInterrupt, e:
				print "Error happened!"

	def AddCallback(self,callback):
		self.callback[self.counter] = callback
		pprint(self.callback[self.counter])
		self.counter += 1

	def test(self):
		print self.config