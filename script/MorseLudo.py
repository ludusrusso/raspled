#!/usr/bin/env python

import RPi.GPIO as GPIO
import time


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
ledPin=4
BuzzerPin=17
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(ledPin,GPIO.OUT)
GPIO.setup(BuzzerPin,GPIO.OUT)

pwm=GPIO.PWM(17,50)
pwm.start(50)

def dot():
	GPIO.output(ledPin,1)
	pwm.ChangeFrequency(200)
	time.sleep(0.2)
	GPIO.output(ledPin,0)
	pwm.ChangeFrequency(10)
	time.sleep(0.1)

def dash():
	GPIO.output(ledPin,1)
	pwm.ChangeFrequency(200)
	time.sleep(.5)
	GPIO.output(ledPin,0)
	pwm.ChangeFrequency(10)
	time.sleep(0.1)


try:
	while True:
		input = raw_input('What would you like to send? ')
		for letter in input:
				for symbol in CODE[letter.upper()]:
					if symbol == '-':
						dash()
					elif symbol == '.':
						dot()
					else:
						time.sleep(0.5)
				time.sleep(0.5)
except KeyboardInterrupt:
	print "\nTerminated"
	GPIO.cleanup()
