#! /usr/bin/env python

'''
The service receives from the client two ints that are
the vibration frequency and the period. The GPIO.PWM function
used with a Buzzer makes it produce the corrispondent note
'''

import rospy
from led.srv import Buzzer
import time
import signal
import RPi.GPIO as GPIO

# Setting up GPIO pins
BuzzerPin=17
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(BuzzerPin, GPIO.OUT)
pwm=GPIO.PWM(BuzzerPin,50)

# Handling the Ctrl+C combination used to kill the node
def signal_handler(signal,frame):
    print "Terminated"
    pwm.stop()
    GPIO.cleanup()


def execute(per,note):
    pwm.start(50)
    pwm.ChangeFrequency(note)
    time.sleep(0.8*per)
    pwm.stop()
    time.sleep(0.2*per)

def handle_buzz(req):
    while True:
    	execute(req.a,req.b)
    return BuzzerResponse(req.a)
    
def buzzer_server():
    rospy.init_node('buzzer_server')
    s = rospy.Service('buzzer_service', Buzzer , handle_buzz)
    print "Ready to control buzzer"
    rospy.spin()
    
if __name__=="__main__":
    signal.signal(signal.SIGINT, signal_handler)
    buzzer_server()
