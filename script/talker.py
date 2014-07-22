#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String
import RPi.GPIO as GPIO

def talker():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(18, GPIO.OUT)
    pub = rospy.Publisher('chatter', String, 10)
    rospy.init_node('talker', anonymous=True)
    r = rospy.Rate(10) # 10hz
    var = True
    while not rospy.is_shutdown():
        GPIO.output(18, var)
        var = not var
        str = "hello world %s"%rospy.get_time()
        rospy.loginfo(str)
        pub.publish(str)
        r.sleep()


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException: pass
