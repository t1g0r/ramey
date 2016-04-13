import time
from threading import Thread,Timer,Event
import RPi.GPIO as GPIO

class Leds(Thread):
        """docstring for Leds"""
        def __init__(self):
                super(Leds, self).__init__()
                self.state = False
                self._stop = Event()
                #GPIO.cleanup()
                GPIO.setwarnings(False)
                GPIO.setmode(GPIO.BCM)
                GPIO.setup(5,GPIO.OUT)
                GPIO.setup(6,GPIO.OUT)

        def flipflop(self):
                self.state = not self.state
                print "set gpio 5 to : %r" % (self.state)
                GPIO.output(5,self.state)
                print "set gpio 6 to : %r" % (not self.state)
                GPIO.output(6,not self.state)
                print "----------------------------"

        def run(self):
                try:
                        while True:
                                self.flipflop()
                                time.sleep(1)
                except KeyboardInterrupt:
                        GPIO.cleanup()
                        exit


oLed = Leds()
oLed.start()

