#!/usr/bin/env python

import rospy
from led.srv import pata
from led.msg import Num

def callback(data):
	rospy.wait_for_service('pata')
	rospy.loginfo("I heard %d",data.num)
	print "Sending int via service"
	s=rospy.ServiceProxy('pata', pata)
	resp=s(data.num)
	
def listener():
	rospy.init_node('my_listener',anonymous=True)
	rospy.Subscriber('chatter', Num ,callback)
	rospy.spin()

if __name__=='__main__':
	listener()
