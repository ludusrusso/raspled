#!/usr/bin/env python

'''
This service controls four leds using four
gpio pins in contrast with what the driver service does.
This service is simpler than the driver one 
and with few leds it is also faster but when you
have to control more leds you cannot control them
using the gpio pins singularly. In these cases is better to use 
the led driver.
'''

from led.srv import *
import time
import rospy
import signal
import RPi.GPIO as GPIO


# Setting GPIO pins, period ond duty cycle
T=1
duty=0.5
LedPin1=24
LedPin2=22
LedPin3=18
LedPin4=4

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(LedPin1,GPIO.OUT)
GPIO.setup(LedPin2,GPIO.OUT)
GPIO.setup(LedPin3,GPIO.OUT)
GPIO.setup(LedPin4,GPIO.OUT)

s=[0,0,0,0]

def signal_handler(signal,frame):
    print "Terminated"
    init()
    GPIO.cleanup()

# Converting the 1 and 0 sequence from decimal base to the corrispondent binary input
def conversion(req):
    for i in range(0,4):
        s[i]=req.a%2
        req.a=(req.a-s[i])/10
    handle_int(s)

def init():
    GPIO.output(LedPin1,False)
    GPIO.output(LedPin2,False)
    GPIO.output(LedPin3,False)
    GPIO.output(LedPin4,False)
    time.sleep(T*(1-duty))

def handle_int(v):
    while True:
        GPIO.output(LedPin1,v[0])
        GPIO.output(LedPin2,v[1])
        GPIO.output(LedPin3,v[2])
        GPIO.output(LedPin4,v[3])
        time.sleep(duty*T)
        init() 

def singular_server():
    print "Waiting for int"
    rospy.init_node('singular_server')
    b= rospy.Service('singular_service', Singular, conversion)
    rospy.spin()
    
if __name__== '__main__':
    signal.signal(signal.SIGINT, signal_handler)	
    singular_server()
