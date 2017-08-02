import RPi.GPIO as GPIO
import time
import socket
import datetime as dt
import json
import dht11

def sonarData():
    GPIO.setmode(GPIO.BCM)

    TRIG = 23
    ECHO = 24

    GPIO.setwarnings(False)
    GPIO.setup(TRIG, GPIO.OUT)
    GPIO.setup(ECHO, GPIO.IN)
    GPIO.setup(17, GPIO.OUT)

    disCtr = 1
    #**** temp $ humid pin 4
    instance = dht11.DHT11(pin=4)

    while True:
        GPIO.output(TRIG, False)
        time.sleep(1)
        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)

        timestamp = dt.datetime.now().isoformat()

        while GPIO.input(ECHO)==0:
            pulse_start = time.time()

        while GPIO.input(ECHO)==1:
            pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start
        distance = pulse_duration * 17150
        distance = round(distance,2)

	#**********************
	result = instance.read()
        if result.is_valid():
		temp = result.temperature
		humid = result.humidity
        #**********************
	if distance <= 100:
		GPIO.output(17,True)
	else:
		GPIO.output(17,False)
	#**********************
        transmit_data(timestamp, str(distance),disCtr,temp,humid)
        disCtr = 0

def transmit_data(timestamp,dist,disCtr,temp,humid):
    try:
        destIP = '192.168.56.10'
        destPORT = 23000
        
        clisock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        clisock.connect((destIP,destPORT))

        data_str_to_json = json.dumps({"timestamp": timestamp, "distance":dist, "temp":temp, "humid":humid})
        #print data_str_to_json
        clisock.send(data_str_to_json)
        
        if disCtr == 1:
            print "socket connection is streamng live data to the server via @ ",destIP,"on port", destPORT
            
    except socket.error, exc:
        print "Oops! Something went wrong with the connection : %s" % exc
            
            

if __name__ == "__main__":
    
    sonarData()
    
