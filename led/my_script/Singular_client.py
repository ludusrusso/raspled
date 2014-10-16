#!/usr/bin/env python

'''
This service and client controls four leds. 
The client wants as argument a four digits number
in which each digit is the corrispondent input
value of each led.
'''

from led.srv import *
import sys
import rospy

# Accepts as input a sequence of 1 and 0
rospy.wait_for_service('singular_service')
fun=rospy.ServiceProxy('singular_service', Singular)
x=int(sys.argv[1])
res=fun(x)
