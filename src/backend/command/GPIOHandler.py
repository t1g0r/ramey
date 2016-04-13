import sys
import RPi.GPIO as gpio
import time
# GPIO.setmode(GPIO.BOARD)


class GPIOHandler(object):
	"""docstring for GPIOHandler"""
	def __init__(self, pins=None, params=None):
		super(GPIOHandler, self).__init__()
		self.pins = pins
		self.params = params
		#initiate gpio
		gpio.setwarnings(False)
		gpio.setmode(GPIO.BOARD)
		gpio_setup = "out" if params==None else "in"

		if pins != None:
			for i in pins:
				if gpio_setup=="in":
					gpio.setup(i,gpio.IN)
				else:
					gpio.setup(i,gpio.OUT)


	def CheckStatus(self):
		pass

	def SetPin(self,pin=None,value=True,setupmode=None):
		if (pin != None) & (self.pins == None):
			#new setup first
			gpio.setup(pin,gpio.OUT if setupmode=="out" else "in")
			gpio.output(pin,value)
		else:
			for i in self.pins:
				gpio.output(i,value)

	def SetTrueThenFalse(self,delaytime):
		self.SetPin(value=True)
		time.sleep(delaytime)
		self.SetPin(value=False)

