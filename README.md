# AutoHome
Automated home project using Raspberry and python. This is a mini IoT sample project: IoT project restricted to regulating
or control home appliances. It is based on open source software system. The project is aimed at students learning Programming
(Python) or anyone who wants to implement DIY IoT system for any purpose. Hopefully, this will be a useful resource.

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
works, most importantly the transister.


### Reference Pictures
picture 1 : 
![alt text][logo]

[logo]: https://github.com/nichieaaron/autoHome/blob/master/pictures/picture1.jpg "DHT11 Sensor"

picture 2 : 
![alt text][logo]

[logo]: https://github.com/nichieaaron/autoHome/blob/master/pictures/picture2.jpg "Ultra Sonar Sensor"

picture 3 : 
![alt text][logo]

[logo]: https://github.com/nichieaaron/autoHome/blob/master/pictures/picture3.jpg "130 Motor"




  

  

