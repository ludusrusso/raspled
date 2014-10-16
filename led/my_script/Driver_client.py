#!/usr/bin/env python

'''
In this service and client we drive eight
different leds defining only one number with eight digits that are 0 or 1
'''

from led.srv import Driver
import rospy
import sys

def drive():
    rospy.wait_for_service('driver_service')
    s=rospy.ServiceProxy('driver_service', Driver)
    x=int(sys.argv[1])
    resp=s(x)

if __name__=='__main__':
	drive()
	
