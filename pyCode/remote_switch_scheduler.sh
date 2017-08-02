#!/bin/sh

echo scheduler is running 
while true; do
	python /home/pi/Desktop/src/gh/remote_switch_control.py
	sleep 0.05	
done