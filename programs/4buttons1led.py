#Westley Owens
# 4 buttons and 1 LED
#setup for buttons and LEDs

#Use a module for requesting data online
import requests
#use a module that control time
import time 

import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
#Set up each pin Number
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)






#start and infinite loop
while True:
    # wait for 1 second
    #check the first button
    if GPIO.input(6) == GPIO.LOW:
        print("button 6 was pressed")
        requests.get("http://192.168.10.53:5000/tutd?thumb=up")
    elif GPIO.input(13) == GPIO.LOW:
        print("button 13 was pressed")
        requests.get("http://192.168.10.53:5000/tutd?thumb=down")
    elif GPIO.input(19) == GPIO.LOW:
        print("button 19 was pressed")
        requests.get("http://192.168.10.53:5000/tutd?thumb=wiggle")
    elif GPIO.input(26) == GPIO.LOW:
        print ("button 26 was pressed")
        requests.get("http://192.168.10.53:5000/tutd?thumb=oopse")