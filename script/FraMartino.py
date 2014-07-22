#!/usr/bin/env python

import rospy
import RPi.GPIO as GPIO
import time
from led.srv import *

BuzzerPin=17
ledPin=4
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(BuzzerPin,GPIO.OUT)
GPIO.setup(ledPin,GPIO.OUT)

pwm=GPIO.PWM(17,50)
pwm.start(50)
 	
do=262
do_d=277
re=294
re_d=311
mi=330
fa=349
fa_d=370
sol=392
sol_d=415
la=440
la_d=466
si=494


def FraMartino():
    def go(freq):
        pwm.ChangeFrequency(freq)
        time.sleep(0.4)
        pwm.stop()
        time.sleep(0.1)
        pwm.start(50)

    def go2(freq):
        pwm.ChangeFrequency(freq)
        time.sleep(0.8)
        pwm.stop()
        time.sleep(0.1)
        pwm.start(50)

    def go3(freq):
        pwm.ChangeFrequency(freq)
        time.sleep(0.2)
        pwm.stop()
        time.sleep(0.1)
        pwm.start(50)

    for i in range(1,3):
        go(do)
        go(re)
        go(mi)
        go(do)
    for i in range(1,3):
        go(mi)
        go(fa)
        go2(sol)
    for i in range(1,3):
        go3(sol)
        go3(la)
        go3(sol)
        go3(fa)
        go(mi)
        go(do)
    for i in range(1,3):
        go(re)
        go(sol)
        go2(do)

    pwm.stop()
    GPIO.cleanup()

def led():
    for i in range(1,10):
        GPIO.output(ledPin,1)
        time.sleep(0.5)
        GPIO.output(ledPin,0)
        time.sleep(0.5)
    return 1

def choice(req):
    if req.led==1:
        led
    elif req.led==2:
        FraMartino
    else:
        print 'Choice not valid'
    return LedResponse(req.led)

def led_server():
    rospy.init_node('led_server')
    s=rospy.Service('led_server', Led , choice)
    print 'Waiting for choice'
    rospy.spin()

if __name__ == "__main__":
    led_server()
