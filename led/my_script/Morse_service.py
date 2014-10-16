#!/usr/bin/env python

'''
The service as soon as receives from the client node 
the sentence will convert each letter to the upper case
and then transposes letter by letter in the corrispondent
in Morse code. In addition to letters and numbers 
it is possible to convert also some symbols. 
The Morse code is executed with both the Buzzer
and a led.
'''

import rospy
import RPi.GPIO as GPIO
import time
import signal
from led.srv import Morse


# Defining the Morse code alphabet
# N.B.: Don't use letter with stress e.g. è-->e
CODE = {' ': ' ',
        "'": '.----.',
        '(': '-.--.-',
        ')': '-.--.-',
        ',': '--..--',
        '-': '-....-',
        '.': '.-.-.-',
        '/': '-..-.',
        '0': '-----',
        '1': '.----',
        '2': '..---',
        '3': '...--',
        '4': '....-',
        '5': '.....',
        '6': '-....',
        '7': '--...',
        '8': '---..',
        '9': '----.',
        ':': '---...',
        ';': '-.-.-.',
        '?': '..--..',
        'A': '.-',
        'B': '-...',
        'C': '-.-.',
        'D': '-..',
        'E': '.',
        'F': '..-.',
        'G': '--.',
        'H': '....',
        'I': '..',
        'J': '.---',
        'K': '-.-',
        'L': '.-..',
        'M': '--',
        'N': '-.',
        'O': '---',
        'P': '.--.',
        'Q': '--.-',
        'R': '.-.',
        'S': '...',
        'T': '-',
        'U': '..-',
        'V': '...-',
        'W': '.--',
        'X': '-..-',
        'Y': '-.--',
        'Z': '--..',
        '_': '..--.-'}
        
dot_duration=0.3
dash_duration=0.6
pause_duration=0.3      
ledPin=4
BuzzerPin=17
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(ledPin,GPIO.OUT)
GPIO.setup(BuzzerPin,GPIO.OUT)
pwm=GPIO.PWM(BuzzerPin,50)


def signal_handler(signal,frame):
    print "Terminated"
    GPIO.cleanup()

# Defining the action to perform for dot or dash
def dot():
    GPIO.output(ledPin,1)
    pwm.start(50)
    pwm.ChangeFrequency(220)
    time.sleep(dot_duration)
    pwm.stop()
    GPIO.output(ledPin,0)
    time.sleep(0.1)

def dash():
    GPIO.output(ledPin,1)
    pwm.start(50)
    pwm.ChangeFrequency(220)
    time.sleep(dash_duration)
    pwm.stop()
    time.sleep(0.1)
    GPIO.output(ledPin,0)
    time.sleep(0.1)

def action(req):
    print "Converting "
    input = req.inp
    for letter in input:
        for symbol in CODE[letter.upper()]:
             if symbol == '-':
                  dash()
             elif symbol == '.':
                  dot()
             else:
                  time.sleep(pause_duration)
             time.sleep(pause_duration)

def morse_server():
    print "Ready to convert"
    rospy.init_node('morse_server')
    s = rospy.Service('morse_service', Morse , action)
    rospy.spin()

if __name__=='__main__':
    signal.signal(signal.SIGINT, signal_handler)
    morse_server()    
