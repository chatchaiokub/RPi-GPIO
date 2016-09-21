#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BCM)

#My addition for LEDs
BLUE = 17
RED = 27
LDR = 4
GPIO.setup(BLUE, GPIO.OUT)
GPIO.setup(RED, GPIO.OUT)
#End my code

def RCtime (LDR):
  reading = 0
  GPIO.setup(LDR, GPIO.OUT)
  GPIO.output(LDR, GPIO.LOW)
  time.sleep(0.1)
  
  GPIO.setup(LDR, GPIO.IN)
  # This takes about 1 millisecond per loop cycle
  while (GPIO.input(LDR) == GPIO.LOW):
    reading += 1
  return reading
  
while True:
  print RCtime(LDR) # Read RC timing using pin #18
  
  #Begin my code for the LEDs
  if RCtime(LDR) <2100:
    GPIO.output(RED, False)
    GPIO.output(BLUE, False)
  else:
    GPIO.output(RED, True)
    GPIO.output(BLUE, True)
  
