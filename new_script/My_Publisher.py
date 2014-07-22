#!/usr/bin/env python

import rospy
import random
from led.msg import Num

a=1
b=100

def talker():
    pub=rospy.Publisher('chatter',Num, )
    rospy.init_node('my_talker',anonymous=True)
    r=rospy.Rate(2) # 2 Hertz
    while not rospy.is_shutdown():
        x=random.randint(a,b)
        print "Generating random int"
        rospy.loginfo(x)
        pub.publish(x)
        r.sleep()

if __name__=='__main__':
    try:
        talker()
    except rospy.ROSInterruptException: pass
