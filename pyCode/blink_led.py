import RPi.GPIO as GPIO
				#Uses board pin numbering system GPIO.setmode(GPIO.BOARD)
import time
GPIO.setmode(GPIO.BCM)		#uses the GPIO numbering system
GPIO.setwarnings(False)
GPIO.setup(17, GPIO.OUT)	#Set GPIO pin to OUT

try:
	while 1:
		GPIO.output(17,True)
		time.sleep(0.2)
		GPIO.output(17,False)
		time.sleep(0.2)
except KeyboardInterrupt:
	print "\n user cancelled"
finally:
	GPIO.cleanup()