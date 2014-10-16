#! /usr/bin/env python

'''
Once this client node is executed it will wait
for the service to be run and then it
asks for the sentence to be converted 
'''

import rospy
import sys
from led.srv import Morse

def morse_client():
    rospy.wait_for_service('morse_service')
    mor = rospy.ServiceProxy('morse_service', Morse)
    st = raw_input('Sentence to convert\n')
    r = mor(st)

if __name__=='__main__':
    morse_client()
