import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

RED = 17
BLUE = 27
GPIO.setup(RED, GPIO.OUT)
GPIO.setup(BLUE, GPIO.OUT)
LDR = 4

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
  
  if RCtime(LDR) < 10000:
    GPIO.output(RED, True)
    GPIO.output(BLUE, True)
  else:
    GPIO.output(RED, False)
    GPIO.output(BLUE, False)
