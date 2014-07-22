#!/usr/bin/env python

import rospy
from geometry_msgs/Twist import *
from led.srv import *

def callback(data):
    rospy.wait_for_service('pose_service')
    pose_srv = rospy.ServiceProxy('pose_service', Led)
    x=geometry_msgs/Twist.linear.x
    th=geometry_msgs/Twist.angular.z
    resp=(x,th)

def listener():
    rospy.init_node('our_node')
    rospy("/turtle1/cmd_vel", geometry_msgs/Twist ,callback)
    rospy.spin()

if __name__=='__main__':
    listener()
