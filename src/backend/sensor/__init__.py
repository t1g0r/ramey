import sys
sys.path.append("backend/command/")
import time
from GPIOHandler import GPIOHandler
import RPi.GPIO as gpio
from utils import Parameter


class MotionSensor(object):
	"""docstring for MotionSensor"""
	def __init__(self, config):
		super(MotionSensor, self).__init__()
		self.active = False		
		self.config = config
		self.callback = {}
		self.counter = 0
		self.params = {}
		self.Pin = config["pin"].split(",")
		self.dbconn = config["dbconn"]
		self.params["gpio_setup"] = "in"
		self.ghandler = GPIOHandler(self.Pin,self.params,gpio.PUD_DOWN)
		self.ghandler.Add_Event_Handler(self.Pin,gpio.BOTH,callback=OnMotion,bouncetime=50)
		buzzerpin = Parameter.getValuebyFieldname(self.db,"sensor_motion","buzzer").split(",")
		params["gpio_setup"] = "out"
		self.buzzerHandler = GPIOHandler(buzzerpin,params)

	def OnMotion(self,channel):
		if (gpio.input(self.Pin)) and (self.active):
			self.buzzerHandler.echo()
			if len(self.callback) > 0:
				for call in self.callback:
					call()

	def Execute(self):
			try:
				while True:
					time.sleep(1)

			except KeyboardInterrupt, e:
				print "Error happened!"

	def AddCallback(self,callback):
		self.callback[counter] = callback
		self.counter += 1

	def test(self):
		print self.config