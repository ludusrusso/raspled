#!/usr/bin/env python

import rospy
import time
from led.srv import *

if __name__== "__main__":
    rospy.wait_for_service('choice_service')
    choice_srv=rospy.ServiceProxy('choice_service', Led)
    v=  int(sys.argv[1])
    r= choice_srv(v)
