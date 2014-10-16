#!/usr/bin/env python

'''
This client sends the choice to its relatice
service that is able to control the Buzzer
'''

import rospy
import sys
from led.srv import Song


if __name__ == "__main__":
    rospy.wait_for_service('song_service')
    my_srv = rospy.ServiceProxy('song_service', Song)
    x=int(sys.argv[1])
    r=my_srv(x)
