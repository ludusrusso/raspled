#! /usr/bin/env python

'''
This simple service and client shows how it is
possible to control the Buzzer with the Raspberry Pi board
in order to produce a sound with a specified frequency and that repeats cyclically
with a specified period. 
'''
import rospy
import sys
from led.srv import Buzzer


if __name__ == "__main__":
    rospy.wait_for_service('buzzer_service')
    buz = rospy.ServiceProxy('buzzer_service', Buzzer)
    if len(sys.argv)== 3:
        x=float(sys.argv[1])
        y=float(sys.argv[2])
	s=buz(x,y)
    else :
        print "Please insert sound period (sec) and vibration frequency(Hz)"
