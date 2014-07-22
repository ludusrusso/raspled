#!/usr/bin/env python

import rospy
from led.srv import pata
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)

def odd_led():	
    GPIO.output(22,True)
    time.sleep(0.3)
    GPIO.output(22, False)
def even_led():	
    GPIO.output(24,True)
    time.sleep(0.3)
    GPIO.output(24, False)


def handle_choice(req):
	if (req.a%2):
		#odd int
		odd_led()
	else:
		#even int
		even_led()
	return pata.pataResponse(req.a)

def my_server():
	rospy.init_node('my_server')
	s = rospy.Service('pata', pata , handle_choice)
	print "Ready to turn on leds"
	rospy.spin()

if __name__== "__main__":
	my_server()


