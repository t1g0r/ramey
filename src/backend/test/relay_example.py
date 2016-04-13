import threading
import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)

pinList = [23,25]

for i in pinList:
        print "setup GPIO  %d .. OK" % i
        GPIO.setup(i,GPIO.OUT)
        # GPIO.output(i,GPIO.HIGH)


print ""
print "RELAY TEST v0.1"
print "----------------"

time.sleep(1)
print "RELAY 1 ON"
GPIO.output(23,GPIO.LOW)
time.sleep(1)
print "RELAY 2 ON"
GPIO.output(25,GPIO.LOW)
time.sleep(1)
print ""
print "OK, GOODBYE!"
GPIO.cleanup()
