#!/usr/bin/env python

import rospy
from std_msgs.msg import String
import RPi.GPIO as GPIO


def callback(data):
    GPIO.output(18, callback.var)
    callback.var = not callback.var
    rospy.loginfo(rospy.get_caller_id()+"I heard %s",data.data)

def listener():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(18, GPIO.OUT)

    callback.var = True
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("/chatter", String, callback)

    rospy.spin()

if __name__ == '__main__':
    listener()
