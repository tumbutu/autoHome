import RPi.GPIO as GPIO
import time
import datetime as dt
import dht11
				#Uses board pin numbering system GPIO.setmode(GPIO.BOARD)

GPIO.setmode(GPIO.BCM)		#uses the GPIO numbering system
GPIO.setwarnings(False)

def getData():
	
    #**** temp $ humid pin 4
    instance = dht11.DHT11(pin=4)
 
    try:
	    while True:
	        result = instance.read()
	        if result.is_valid():
			temp = result.temperature
			humid = result.humidity

			file = open("/home/pi/Desktop/pyCode/humiTemp.txt","w")
                        file.writelines([str(humid),"\n",str(temp)])
                        file.close()
                        
		time.sleep(180) 		#sleep for 3min
    except KeyboardInterrupt:
	print "\n user cancelled the process"
            
if __name__ == "__main__":
    
    getData()
