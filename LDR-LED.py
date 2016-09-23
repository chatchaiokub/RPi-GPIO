#!/usr/bin/python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

#########################

RED = 27
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

################################
z = 0  
while True:
 
 if z==0:
  if RCtime(LDR) > 5000:
   GPIO.output(RED,GPIO.HIGH)
   time.sleep(5)
   GPIO.output(RED,GPIO.LOW)
   z=1
  else:
   GPIO.output(RED,GPIO.LOW)
 elif z==1:
  if RCtime(LDR) < 5000:
   z = 0
  else:
   GPIO.output(RED,GPIO.LOW)
  
 print RCtime(LDR)
	
  	  
