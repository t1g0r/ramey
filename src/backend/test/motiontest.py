import RPi.GPIO as gpio

gpio.setwarnings(False)
gpio.setmode(gpio.BCM)



gpio.setup(21,GPIO.IN,pull_up_down=gpio.PUD_DOWN)

def motionSensor(channel):
	if gpio.input(21):
		global counter
		counter += 1
		print "Motion Detected!"

#add event listener
gpio.add_event_detect(21,gpio.BOTH,callback=motionSensor,bouncetime=150)
counter=0

try:
	while True:
		sleep(1)

finally:
	gpio.cleanup()
	print "All cleaned up"