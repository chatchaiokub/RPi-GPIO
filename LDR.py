#!/usr/bin/python

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

#define the pin that goes to the circuit
LDR = 4 

def rc_time (LDR):
    count = 0
  
    #Output on the pin for 
    GPIO.setup(LDR, GPIO.OUT)
    GPIO.output(LDR, GPIO.LOW)
    time.sleep(0.1)

    #Change the pin back to input
    GPIO.setup(LDR, GPIO.IN)
  
    #Count until the pin goes high
    while (GPIO.input(LDR) == GPIO.LOW):
        count += 1

    return count

#Catch when script is interrupted, cleanup correctly
try:
    # Main loop
    while True:
        print rc_time(LDR)
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
