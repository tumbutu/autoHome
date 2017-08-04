# AutoHome
Automated home project using Raspberry and python. This is a mini IoT sample project: IoT project restricted to regulating
or control home appliances. It is based on open source software system. The project is aimed at students learning Programming
(Python) or anyone who wants to implement DIY IoT system for any purpose. Hopefully, this will be a useful resource. In this 
project, LED, Buzzer and 130 Motor with FAN will server as Lamp, Alarm Bell and aircondition in our home respectively. 

## Summary of the Project
1. The Humidity-temperature sensor provides current temperature and humidity
 * The aircodition (Motor Fan) automatically turns on/off following the temperature Levels
 * *It can be expanded to do same for heator as well*
 * *The humidity level can be used turn on/off a humidifier or dehumidifier*
2. The Ultra Sonar sensor is used to monitor the home door if an object comes in range then the alarm buzzer is triggered
3. The LED Serves as a Lamp in  the house.
 * IF the temperature level is abnormal the LED blink red for sometime to singal the home owner about the abnormality in tempera
 ture. If no action is taken the the system automatically takes the appropriate action(Aircon on or Off).
 * LED also blinks red continously when the alarm in triggered.
4. Though the whole system is automated, the home owner has an overriding remote control on a mobile phone via a mobile web 
interface.
5. The current temperature and humidity levels in the house is also deplayed at the mobile web interface.

# Components used in this project
1. Hardware
  * Raspsberry Pi 3 Model B
  * Temperature - Humidity Sensor (DHT11)
  * Ultra Sonar (HC-SR04)
  * LED
  * Alarm Buzzer
  * 130 Motor
  * 220 Ohms Resistors
  * 2222A NPN Transistor
  * Jump Wires
  * Breadboard
  * Smart Phone (For Remote Access and Control Over Wifi)

With the exception of the Raspberry Pi & the smart phone all components are available in **Arduino Beginner Kits** 

2. Software

| Software Name     | Comment                                       |
| ----------------- |:---------------------------------------------:|
| Apache Web Server | Mobile Web Interface                          |
| Python 2.7        | Comes pre-installed on Pi                     |
| MongbDB(Optional) | To persistently Save Sensor data for analysis |       

3. Programming / Scripting Language Skill
 * Python 
 * Batch
 * HTML With CSS & JavaScript

# Setting Up The system
With the afforementioned components available, the following describes how to configure the entire system: the hardware 
wiring and software installation and settings. For beginners, pay attention to the **pin connections from the sensor unit to the
Raspberry Pi GPIO pins**

## Install GPIO in python
The Pi for this project is running on Raspbian which comes with python already installed however GPIO library which is use in 
python to control the Pi's GPIO pins is not pre-installed. At the terminal install GPIO following using this command:
`sudo pip install RPi.GPIO`.

## Connecting the sensors to Raspberry Pi
With GPIO Library installed follow the following steps to connect the sensors properly to the right GPIO pins on the Pi.

1. Familarize yourself with the Raspberry Pi 3 Model B labelled diagram to understand the PIN numbering System.
2. Connect wires to the humidity-temperature sensor shown in **picture 1**
3. Connect wires to the Ultra Sonar Sensor as shown in **picture 2**
4. Connect wires to the 130 Motor as shown in **picture 3**

### Building the Electrical Curcuit
Follow the steps below to connect the electrical components on the breadboard (**Shown in picture 4**). 
The steps will not be explained, thus it is highly recommended that you search other sources to understand how each component 
works, most importantly the **transistor** and how to use the **breadboard**

| Step     | Comment                                       |
| ----------------- |:---------------------------------------------|
|1. Connect the LED unto the breadboard | Check the polarity of the LED legs |
|2. Connect of the 220 Ohm resistors to the *positive* leg of the LED | The **+ve** leg is the Long longer leg |
|3. Connect the **NPN 2222A** transistor | Position it at the other half of the breadboard |
|4. Connect another 220 Ohms resistor to the BASE of the transistor | The Base is the Middle Pin|

Connect a wire to the Collector-Leg of the transistor and terminate it at an empty vertical lane on the breadboard. This will serve as our *ground voltage* I will refer to this as **gnd-Zero**. Be sure to identify the collector leg correctly.

With the curcuit built, it is time to connect our sensors and "home appliances" (The LED, Buzzer and 130 Motor with FAN will server as Lamp, Alarm Bell and aircondition in our home respectively)

### Connecting The Humidity & temperature Sensor
It is better to check the ratings of the sensor device in the datasheet.

| Step     | Comment                                       |
| ----------------- |:---------------------------------------------|
|1. connect the *vcc* wire to 3.3v on raspberry pi | PIN 1 |
|2. Connect a wire from Pi's pin 6 (*ground pin*) to **gnd-Zero** | It is now a real ground voltage |
|2. Connect the *GND* wire of the Humidity & temperature to sensor **gnd-Zero** |                   | 
|3. Connect the *DOUT(**Data out**)* wire Pi's GPIO4 | PIN 7 |

At this point, the Humidity & temperature Sensor is properly connected. Proceed to connect the Ultra Sonar Sensor

### Connecting The Ultra Sonar Sensor
It is better to check the ratings of the sensor device in the datasheet.

| Step     | Comment                          |
| ----------------- |:-----------------------|
| 1. Vcc goes to 5v on Pi | PIN 2 |
| 2. Trig goes to GPIO23 | PIN 16 |
| 3. Echo goes to GPIO24 | PIN 18 |
| 4. Echo goes to GND | **gnd-Zero** |

At this point, the Ultra Sonar sensor is properly connected. Proceed to connect the motor fan

### Connecting the motor fan
It is better to check the ratings of the sensor device in the datasheet. This is where the transistor comes in. Basically, Raspberry Pi cannot supply the power required to drive the motor hence the use of the transistor. To fully
understand the configuration, [take a look at this post](https://hackernoon.com/how-to-control-a-fan-to-cool-the-cpu-of-your-raspberrypi-3313b6e7f92c)

| Step     | Comment                          |
| ----------------- |:-----------------------|
| 1. Connect one end of the motor 5v | PIN 4  |
| 2. Connect the other end to emiiter leg of the transistor on the breadboard | Be sure to identify the emitter leg correctly |
| 3. Connect the collector-leg to **gnd-Zero**| Be sure to identify the collector leg correctly |

We will programmatically supply a 3.3v to the transistor through the 220 ohms resistor connected at the *BASE*. At this point, the motor fan is properly connected.

### Running the Codes

### Adding Remote Control Via mobile web interface

### Reference Pictures

![alt text][a]

 [a]: https://github.com/nichieaaron/autoHome/blob/master/pictures/picture1.jpg "DHT11 Sensor"                     


![alt text][b]

[b]: https://github.com/nichieaaron/autoHome/blob/master/pictures/picture2.jpg "Ultra Sonar Sensor"


![alt text][c]

[c]: https://github.com/nichieaaron/autoHome/blob/master/pictures/picture3.jpg "130 Motor"

  

  

