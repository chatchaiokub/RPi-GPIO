#!/usr/bin/python
import sys
import time
import Adafruit_DHT
import requests
import json
from time import gmtime ,strftime

sensor = Adafruit_DHT.DHT22
pin = 4

while True:
  humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
  if humidity is not None and temperature is not None:
	
	#Setup Format Time
	dateTime =  strftime("%Y-%m-%d %H:%M:%S", gmtime())
	
	#POST API from Sheetsu to Google Sheet
	url = 'https://sheetsu.com/apis/v1.0/7ed611e1080b'
	data = {'Date_Time': dateTime, 'Temperature_C': '%0.2f'%temperature, 'Humidity_%': '%0.2f'%humidity}
	headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
	response = requests.post(url,data=json.dumps(data),headers=headers)
	
	print data
	time.sleep(2)

  else:
	print 'Failed to get reading. Try again!'
