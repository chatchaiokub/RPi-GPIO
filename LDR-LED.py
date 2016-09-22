#!/usr/bin/python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

#########################

BLUE = 17
RED = 27
GPIO.setup(BLUE, GPIO.OUT)
GPIO.setup(RED, GPIO.OUT)

LDR = 4

#########################

def RCtime (LDR):

  reading = 0

  GPIO.setup(LDR, GPIO.OUT)
  GPIO.output(LDR, GPIO.LOW)
  time.sleep(0.1)
  
  GPIO.setup(LDR, GPIO.IN)
  while (GPIO.input(LDR) == GPIO.LOW):
    reading += 1
  return reading
  
while True:
  print RCtime(LDR)

#########################

z = 0

if z==0:
	if RCtime(LDR) > 10000:
		GPIO.output(RED, True)
    		GPIO.output(BLUE, True)
		time.sleep(5)
		GPIO.output(RED, False)
		GPIO.output(BLUE, False)
		z=1
	else:
		GPIO.output(RED, False)
		GPIO.output(BLUE, False)
elif z==1:
	if RCtime(LDR) < 10000:
		z = 0
	else:
		GPIO.output(RED, False)
		GPIO.output(BLUE, False)

	
  	  
