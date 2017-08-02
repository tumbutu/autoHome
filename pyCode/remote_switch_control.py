import RPi.GPIO as GPIO
import time

file = open("/home/pi/Desktop/src/gh/remote_switch.txt","r")
switch = int(file.readline())	

GPIO.setmode(GPIO.BCM)	#Use board pin numbering
GPIO.setwarnings(False)
pinLight = 17
pinFan = 10

GPIO.setup(pinLight, GPIO.OUT)
GPIO.setup(pinFan, GPIO.OUT)

if switch == 1:
	GPIO.output(pinLight, True)
elif switch == 2:
	GPIO.output(pinLight, False)
elif switch == 3:
	GPIO.output(pinFan, True)
elif switch == 4:
	GPIO.output(pinFan, False)

