#!/usr/bin/env python

import rospy

from led.srv import *


if __name__ == "__main__":
    rospy.wait_for_service('led_service')
    led_srv = rospy.ServiceProxy('led_service', Led)
    v = 0;
    while(True):
        r = led_srv(v);
        v = (v + 1)%(2**8);
        rospy.sleep(0.1)
