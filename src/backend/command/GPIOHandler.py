import sys
import RPi.GPIO as gpio
import time
# GPIO.setmode(GPIO.BOARD)


class GPIOHandler(object):
	"""docstring for GPIOHandler"""
	def __init__(self, pins=None, params=None, pull_up_down=None):
		super(GPIOHandler, self).__init__()
		self.pins = pins
		self.params = params
		self.bounce_time = bounce_time
		#initiate gpio
		gpio.setwarnings(False)
		gpio.setmode(gpio.BCM)
		gpio_setup = "out" if params==None else params["gpio_setup"]

		if pins != None:
			for i in pins:
				if gpio_setup=="in":
					gpio.setup(int(i),gpio.IN,pull_up_down=pull_up_down)
				else:
					gpio.setup(int(i),gpio.OUT,pull_up_down=pull_up_down)

	def Add_Event_Handler(self,gpiosetup,bouncetime,callback,pin=None):
		if (pin != None) & (self.pins == None):
			#new setup first
			gpio.add_event_detect(pin,gpiosetup,callback=callback,bouncetime=bouncetime)
		else:
			for i in self.pins:
				gpio.add_event_detect(int(i),gpiosetup,callback=callback,bouncetime=bouncetime)

	def CheckStatus(self,pin=False):
		return gpio.input(pin)

	def SetPin(self,pin=None,value=True,setupmode=None):
		if (pin != None) & (self.pins == None):
			#new setup first
			gpio.setup(pin,gpio.OUT if setupmode=="out" else "in")
			gpio.output(pin,value)
		else:
			for i in self.pins:
				gpio.output(int(i),value)
				print "pin %s set to %r" % (i,value)
		return gpio

	def SetTrueThenFalse(self,delaytime):
		self.SetPin(value=True)
		time.sleep(delaytime)
		return self.SetPin(value=False)

	def dip(self,delay,delaystop):
		self.SetPin(value=True)
		time.sleep(delay)
		self.SetPin(value=False)
		time.sleep(delaystop)

	def echo(self):
		print "Test Echo"
		self.dip(.1,.1)
		self.dip(.1,.1)
		self.dip(.1,.2)
		self.dip(.3,.2)
		self.dip(.5,.5)

	def Clean(self,pin=None):
		gpio.cleanup()

