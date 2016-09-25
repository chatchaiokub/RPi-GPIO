#!/usr/bin/python
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


GPIO.setup(4,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)

while 1:

	GPIO.output(4,GPIO.HIGH)
	GPIO.output(27,GPIO.HIGH)
	time.sleep(1)
	GPIO.output(4,GPIO.LOW)
	GPIO.output(27,GPIO.LOW)
	time.sleep(1)
