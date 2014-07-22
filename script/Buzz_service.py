#!/usr/bin/env python

import rospy
from led.srv import *
import RPi.GPIO as GPIO
import time

LedPin=4
BuzzerPin=17
GPIO.setmode(GPIO.BCM)

def ledpirla():
    print "Blinking led"
    GPIO.setup(LedPin,GPIO.OUT)         
    for i in range(0,4):
        GPIO.output(LedPin,False)
        time.sleep(0.2)
        GPIO.output(LedPin,True)
        time.sleep(0.2)
	

def song():
	print "Executing song"
	GPIO.setup(BuzzerPin,GPIO.OUT)
	pwm=GPIO.PWM(BuzzerPin,50)
	note_time=0.2
	pause=0.1
	def go(freq):
		pwm.start(50)
		pwm.ChangeFrequency(freq)
		time.sleep(note_time)
		pwm.stop()
		time.sleep(pause)
	def go2(freq):
		pwm.start(50)	
		pwm.ChangeFrequency(freq)
		time.sleep(2*note_time)	
		pwm.stop()
		time.sleep(pause)
	def go4(freq):
		pwm.start(50)
		pwm.ChangeFrequency(freq)
		time.sleep(4*note_time)
		pwm.stop()
		time.sleep(pause)
	for i in range(0,2):
		go2(262)
		go2(294)
		go2(330)
		go2(262)
	for i in range(0,2):
		go2(330)
		go2(349)
		go4(392)
	for i in range(0,2):
		go(392)
		go(440)
		go(392)
		go(349)
		go2(330)
		go2(262)
	for i in range(0,2):
		go2(294)
		go2(392)
		go4(262)
	

def handle_choice(req):
    if req.led == 1:
        led()
    elif req.led == 2:
        song()
    print "Done"
    return LedResponse(req.led)

def choice_server():
    rospy.init_node('choice_server')
    s= rospy.Service('choice_service', Led, handle_choice)
    print "Ready to perform action"
    rospy.spin()

if __name__== "__main__":
	choice_server()

GPIO.cleanup()
