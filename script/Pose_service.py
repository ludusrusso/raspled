#!/usr/bin/env python

import rospy
from led.srv import *
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)

def handle_choice(req):
	if req.a:
		moving_forward()
	if req.b:
		rotating()
	return PoseRepsonse(req.a)

def pose_server():
	rospy.init_node('pose_server')
	s = rospy.Service('pose_service', Pose,handle_choice)
	print "Ready"
	rospy.spin()

if __name__== "__main__":
	pose_server()

def moving_forward():	
	GPIO.output(22,True)
	time.sleep(0.2)
        GPIO.output(22, False)
def rotating():	
	GPIO.output(24,True)
	time.sleep(0.2)
        GPIO.output(24, False)
