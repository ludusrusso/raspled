#!/usr/bin/env python

import rospy
import time
from led.srv import driver
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(4,GPIO.OUT)

def clo():
	GPIO.output(18,True)
	time.sleep(0.5)
	GPIO.output(18,False)
	time.sleep(0.5)

def handle_driver(req):
	t = tuple(1 & (req.inp/(2**n)) for n in range(0,8))
	clo()
	for k in range(0,8):
		GPIO.output(4,t[k])
		time.sleep(1)
	return driverResponse(req.inp)

def driver_server():
    rospy.init_node('pata_server')
    s = rospy.Service('pata2', driver , handle_driver)
    print "Ready to control led."
    rospy.spin()

if __name__=='__main__':
	driver_server()
