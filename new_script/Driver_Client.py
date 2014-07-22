#!/usr/bin/env python

from led.srv import driver
import rospy
import sys


if __name__=='__main__':
    rospy.wait_for_service('pata2')
    s=rospy.ServiceProxy('pata2', driver)
    x=0
    resp=s(x)
