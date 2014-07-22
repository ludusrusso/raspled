#!/usr/bin/env python

import rospy
from led.srv import *
import time
import RPi.GPIO as GPIO

def handle_led(req):
    while True:
        t = tuple(1 & (req.led/(2**n)) for n in range(0,8))
        print t
        GPIO.output(4,t[0])
        GPIO.output(17,t[ 1])
        time.sleep(1)
        GPIO.output(4,0)
        GPIO.output(17,1)
        time.sleep(1)
    return LedResponse(req.led)

def led_server():
    rospy.init_node('led_server')
    s = rospy.Service('led_service', Led , handle_led)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(4,GPIO.OUT)
    GPIO.setup(17, GPIO.OUT)
    print "Ready to control led."
    rospy.spin()

if __name__ == "__main__":
    led_server()

