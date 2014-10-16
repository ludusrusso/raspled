#!/usr/bin/env python

'''
This service allows us to control eight leds using only four gpio pins.
One is the Clock that sinconizes the acquisition; then there are two pins
used to control the latch enable and the output enable: 
the first makes the acquired values shift to the corrispondent led,
while the second enalbes the output and gives supply to the leds;
finally there is the Serial input which receives the sequence of 1 or 0 as input.
Using this driver it is possible to drive more than eight leds since it as another pin,
not used in this experience, that can bring another sequence of 1 or 0 to another led driver
'''

import rospy
import time
from led.srv import Driver
import RPi.GPIO as GPIO

on_duration=1
n=4
LePin=18
OePin=22
ClkPin=24
SdiPin=25

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(LePin,GPIO.OUT)
GPIO.setup(OePin,GPIO.OUT)
GPIO.setup(ClkPin,GPIO.OUT)
GPIO.setup(SdiPin,GPIO.OUT)


s=[0,0,0,0,0,0,0,0]

# Setting the default value for Latch enable and Output enable pins
def default():
    GPIO.output(LePin,GPIO.LOW)
    GPIO.output(OePin,GPIO.HIGH)

# Converting the sequence of 1 and 0 from decimal form to the corrispondent binary value
def conversion(req):
    print "Conversion"
    for i in range(0,8):
        s[i]=req.a%2
        req.a=(req.a-s[i])/10
    handle_choice(s)

# Sending the serial sequence of 1 and 0 to the Serial input pin
def handle_choice(v):
    for led in range(0,8):
        pass_value(v[led])
    enable_out()

# Enabling the latch and the output
def enable_out():
    GPIO.output(LePin,GPIO.HIGH)
    time.sleep(0.2)
    GPIO.output(LePin,GPIO.LOW)
    time.sleep(0.1)
# The pins will blink n times
    for iteration in range(0,n):    
        GPIO.output(OePin,GPIO.LOW)
        time.sleep(on_duration)
        GPIO.output(OePin,GPIO.HIGH)
        time.sleep(0.1)
    default()
# Defining the function used to send the serial values to the led driver
def pass_value(val):
    GPIO.output(SdiPin,val)
    time.sleep(0.1)
    GPIO.output(ClkPin,GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(ClkPin,GPIO.LOW)
    GPIO.output(SdiPin,GPIO.LOW)

def drive_server():
    print "Service ready to drive leds"
    rospy.init_node('driver_server')
    s=rospy.Service('driver_service', Driver, conversion)
    rospy.spin()

if __name__=='__main__':
    default()
    drive_server()
