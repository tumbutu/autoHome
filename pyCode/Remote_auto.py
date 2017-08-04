import RPi.GPIO as GPIO
import time
import datetime as dt
import dht11
				#Uses board pin numbering system GPIO.setmode(GPIO.BOARD)

GPIO.setmode(GPIO.BCM)		#uses the GPIO numbering system
GPIO.setwarnings(False)
GPIO.setup(17, GPIO.OUT)	#Set GPIO pin to OUT
GPIO.setup(10, GPIO.OUT)

turnOnCall = 0

def blink_led():
    GPIO.output(17,True)
    time.sleep(0.05)
    GPIO.output(17,False)

def fanOn():
    global turnOnCall
    turnOnCall += 1				#turn on only if called 5X consecutively
    if turnOnCall >= 5:
	turnOnCall = 5				#resets turnOnCall to 5 else it will continue to grow
    	GPIO.output(10,True)

def fanOff():
    global turnOnCall
    turnOnCall = 0
    GPIO.output(10,False)

def msgDsp(code,ctr):
	if code == 0 and ctr==1:
		print 'Temp is above normal room temperature turning on Aircon'
	if code == 1 and ctr==1:
		print 'Temp is below normal room temperature turning on heater'
	

def gatherData():
	
    disCtr = 1
    disCtd = 1
    disCtrd = 1
    awake = True
    
    #**** temp $ humid pin 4
    instance = dht11.DHT11(pin=4)
 
    try:
	    while True:
	        	
	        time_now = dt.datetime.now()

	        result = instance.read()
	        if result.is_valid():
			temp = result.temperature
			humid = result.humidity

			file = open("/home/pi/Desktop/src/gh/humiTemp.txt","w")
                        file.writelines([str(humid),"\n",str(temp)])
                        file.close()
                        
			print str({"timestamp": time_now.isoformat(), "temp": temp, "humid": humid})
			if temp >= 24:
				
				msgDsp(0,disCtd)
				disCtd = 0
				
				blink_led()
				fanOn()
			elif temp <= 15:	
				msgDsp(1,disCtrd)
				disCtrd = 0
				
				blink_led()
				fanOff()	
		        else:
				fanOff()
				GPIO.output(17,False)
	
		
    except KeyboardInterrupt:
	print "\n user cancelled the process"

    finally:
	#GPIO.cleanup()
	GPIO.output(17,False)
	fanOff()

            
if __name__ == "__main__":
    
    gatherData()
