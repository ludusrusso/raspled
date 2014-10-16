#!/usr/bin/env python

'''
This service uses the possibility to control
the Buzzer with the Raspberry Pi to execute some
songs. First we define the frequency of each note,
then for each song we created two list: one gives the note
and the second gives its duration.
'''

import rospy
import signal
import sys
import time
import RPi.GPIO as GPIO
from led.srv import Song

BuzzerPin=17

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(BuzzerPin,GPIO.OUT)
    
pwm=GPIO.PWM(BuzzerPin,50)

# Defining the frequency of the used notes
C3 = 131
C_D3 = 139
D3 = 147
D_D3 = 156
E3 = 165
F3 = 175
F_D3 = 185
G3  = 196
G_D3 = 208
A3 = 220
A_D3 = 233
B3  = 247
C4 = 262
C_D4 = 277
D4 = 294
D_D4 = 311
E4 = 330
F4 = 349
F_D4 = 370
G4  = 392
G_D4 = 415
A4 = 440
A_D4 = 466
B4  = 494
C5  = 523
C_D5 = 554
D5  = 587
D_D5 = 622
E5  = 659
F5  = 698
F_D5 = 740
G5  = 784
G_D5 = 831
A5  = 880
A_D5 = 932
B5  = 988
C6 = 1046


# Defining the notes and their duration for each song
For_Elisa=[
    E4,D_D4,E4,D_D4,E4,B3,D4,C4,A3,
    C3,E3,A3,B3,E3,G_D3,B3,C4,E3,
    E4,D_D4,E4,D_D4,E4,B3,D4,C4,A3,
    C3,E3,A3,B3,E3,C4,B3,A3,
    E4,D_D4,E4,D_D4,E4,B3,D4,C4,A3,
    C3,E3,A3,B3,E3,G_D3,B3,C4,E5,
    E4,D_D4,E4,D_D4,E4,B3,D4,C4,A3,
    C3,E3,A3,B3,E3,C4,B3,A3,
    B3,C4,D4,E4,G3,F4,E4,D4,F3,E4,D4,C4,
    E3,D4,C4,B3,E3,E4,E3,E4,E3,E4,E3,
    E4,D_D4,E4,D_D4,E4,B3,D4,C4,A3,
    C3,E3,A3,B3,E3,G_D3,B3,C4,E3,
    E4,D_D4,E4,D_D4,E4,B3,D4,C4,A3,
    C3,E3,A3,B3,E3,C4,B3,A3
]

FE_Duration=[
    0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,1.5,
    0.5,0.5,0.5,1.5,0.5,0.5,0.5,1.5,0.5,
    0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,1.5,
    0.5,0.5,0.5,1.5,0.5,0.5,0.5,2,
    0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,1.5,
    0.5,0.5,0.5,1.5,0.5,0.5,0.5,1.5,0.5,
    0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,1.5,
    0.5,0.5,0.5,1.5,0.5,0.5,0.5,1.5,
    0.5,0.5,0.5,1.5,0.5,0.5,0.5,1.5,0.5,0.5,0.5,1.5,
    0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,
    0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,1.5,
    0.5,0.5,0.5,1.5,0.5,0.5,0.5,1.5,0.5,
    0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,1.5,
    0.5,0.5,0.5,1.5,0.5,0.5,0.5,2.5
]

Ode_to_Joy=[
    B3,B3,C4,D4,D4,C4,B3,A3,G3,G3,A3,B3,B3,A3,A3,
    B3,B3,C4,D4,D4,C4,B3,A3,G3,G3,A3,B3,A3,G3,G3,
    A3,A3,B3,G3,A3,B3,C4,B3,G3,A3,B3,C4,B3,A3,G3,A3,D3,
    B3,B3,C4,D4,D4,C4,B3,A3,G3,G3,A3,B3,A3,G3,G3,
    A3,A3,B3,G3,A3,B3,C4,B3,G3,A3,B3,C4,B3,A3,G3,A3,D3,
    B3,B3,C4,D4,D4,C4,B3,A3,G3,G3,A3,B3,A3,G3,G3
]


OtJ_Duration=[
    1,1,1,1,1,1,1,1,1,1,1,1,1.5,0.5,2,
    1,1,1,1,1,1,1,1,1,1,1,1,1.5,0.5,2,
    1,1,1,1,1,0.5,0.5,1,1,1,0.5,0.5,1,1,1,1,1,
    2,1,1,1,1,1,1,1,1,1,1,1,1.5,0.5,2,
    1,1,1,1,1,0.5,0.5,1,1,1,0.5,0.5,1,1,1,1,1,
    2,1,1,1,1,1,1,1,1,1,1,1,1.5,0.5,2
]

Tetris=[
    B3,F_D3,G3,A3,B3,A3,G3,F_D3,E3,E3,G3,B3,
    A3,G3,F_D3,G3,A3,B3,G3,E3,E3,1,
    A3,C4,E4,D4,C4,B3,G3,B3,A3,G3,F_D3,
    F_D3,G3,A3,B3,G3,E3,E3,
    B3,G3,A3,F_D3,G3,E3,D_D3,F_D3,B3,G3,A3,F_D3,
    G3,B3,E4,D_D4,1,
    B3,F_D3,G3,A3,B3,A3,G3,F_D3,E3,E3,G3,B3,
    A3,G3,F_D3,G3,A3,B3,G3,E3,E3,1,
    A3,C4,E4,D4,C4,B3,G3,B3,A3,G3,F_D3,
    F_D3,G3,A3,B3,G3,E3,E3
]

T_Duration=[
    1,0.5,0.5,0.5,0.25,0.25,0.5,0.5,1,0.5,0.5,1,
    0.5,0.5,1.5,0.5,1,1,1,1,2,0.5,
    1,0.5,1,0.5,0.5,1.5,0.5,1,0.5,0.5,1,
    0.5,0.5,1,1,1,1,2,
    2,2,2,2,2,2,2,2,2,2,2,2,
    1,1,2,2,2,
    1,0.5,0.5,0.5,0.25,0.25,0.5,0.5,1,0.5,0.5,1,
    0.5,0.5,1.5,0.5,1,1,1,1,2,0.5,
    1,0.5,1,0.5,0.5,1.5,0.5,1,0.5,0.5,1,
    0.5,0.5,1,1,1,1,2
]

Fra_Martino=[
    C4,D4,E4,C4,C4,D4,E4,C4,
    E4,F4,G4,E4,F4,G4,
    G4,A4,G4,F4,E4,C4,G4,A4,G4,F4,E4,C4,
    D4,G4,C4,D4,G4,C4
]

FM_Duration=[
    1,1,1,1,1,1,1,1,
    1,1,2,1,1,2,
    0.5,0.5,0.5,0.5,1,1,0.5,0.5,0.5,0.5,1,1,
    1,1,2,1,1,2
]

Happy_Birthday=[
    D3,D3,E3,D3,G3,F_D3,
    D3,D3,E3,D3,A3,G3,
    D3,D3,D4,B3,G3,F_D3,E3,
    C4,C4,B3,G3,A3,G3
]

HB_Duration=[
    0.5,0.5,1,1,1,2,
    0.5,0.5,1,1,1,2,
    0.5,0.5,1,1,1,1,1,
    0.5,0.5,1,1,1,2
]

Super_Mario=[
    E4,E4,E4,C4,E4,G4,1,G3,1,
    C4,G3,E3,1,A3,B3,A_D3,A3,
    G3,E4,G4,A4,F4,G4,E4,C4,D4,B3,1,
    C3,G4,E3,1,A3,B3,A_D3,A3,
    G3,E4,G4,A4,F4,G4,E4,C4,D4,B3,1,
    G4,F_D4,F4,D_D4,E4,1,G_D3,A3,C4,1,A3,C4,D4,1,
    G4,F_D4,F4,D_D4,E4,1,C5,1,C5,C5,1,
    G4,F_D4,F4,D_D4,E4,1,G_D3,A3,C4,1,A3,C4,D4,1,
    D_D4,1,D4,1,C4,1,
    C4,C4,C4,C4,D4,E4,C4,A3,G3,1,
    C4,C4,C4,C4,D4,E4,1,
    C4,C4,C4,C4,D4,E4,C4,A3,G3,1,
    E4,E4,E4,C4,E4,G4,1,G3,1,
    C4,G3,E3,1,A3,B3,A_D3,A3,
    G3,E4,G4,A4,F4,G4,E4,C4,D4,B3,1,
    C4,G3,E3,1,A3,B3,A_D3,A3,
    G3,E4,G4,A4,F4,G4,E4,C4,D4,B3,1,
    E4,C4,G3,G_D3,A3,F4,F4,A3,1,
    B3,A4,A4,A4,G4,F4,E4,C4,A3,G3,1,
    E4,C4,G3,G_D3,A3,F4,F4,A3,1,
    B3,F4,F4,F4,E4,D4,C4,1,C3,1,
    C4,G3,E3,A3,B3,A3,G_D3,A_D3,G_D3,G3
]

SM_Duration=[
    0.5,1,1,0.5,1,1,1,1,1,
    1.5,1.5,1,0.5,1,1,0.5,1,
    0.66,0.66,0.67,1,0.5,1,1,0.5,0.5,0.5,1,
    1.5,1.5,1,0.5,1,1,0.5,1,
    0.66,0.66,0.67,1,0.5,1,1,0.5,0.5,0.5,2,
    0.5,0.5,0.5,1,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,1,
    0.5,0.5,0.5,1,0.5,0.5,0.5,0.5,0.5,1,2,
    0.5,0.5,0.5,1,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,1,
    1,0.5,1,0.5,2,2,
    0.5,1,1,0.5,1,0.5,1,0.5,1,1,
    0.5,1,1,0.5,0.5,1,3,
    0.5,1,1,0.5,1,0.5,1,0.5,1,1,
    0.5,1,1,0.5,1,1,1,1,1,
    1.5,1.5,1,0.5,1,1,0.5,1,
    0.66,0.66,0.67,1,0.5,1,1,0.5,0.5,0.5,1,
    1.5,1.5,1,0.5,1,1,0.5,1,
    0.66,0.66,0.67,1,0.5,1,1,0.5,0.5,0.5,1,
    0.5,1,1.5,1,0.5,1,0.5,1,1,
    0.66,0.66,0.67,0.66,0.66,0.67,0.5,1,0.5,1,1,
    0.5,1,1.5,1,0.5,1,0.5,1,1,
    0.66,0.66,0.67,0.66,0.66,0.67,1,1,1,1,
    1.5,1.5,1,0.66,0.66,0.67,0.66,0.66,0.67,4
]



def signal_hndlr(signal,frame):
    print "Terminated"
    GPIO.cleanup()

# Buzzer control
def execution(freq,dur):
    pwm.start(50)
    pwm.ChangeFrequency(freq)
    time.sleep(0.4*dur)
    pwm.stop()
    time.sleep(0.01)

#Handling the choice
def choice(req):
    if req.a == 1:
        print "\nExecuting For Elisa"
        for note in range(0,len(For_Elisa)):
            execution(For_Elisa[note],FE_Duration[note])
    elif req.a == 2:
	print "\nExecuting Happy Birthday to you"        
	for note in range(0,len(Happy_Birthday)):
            execution(Happy_Birthday[note],HB_Duration[note])
    elif req.a == 3:
	print "\nExecuting Ode to Joy"
        for note in range(0,len(Ode_to_Joy)):
            execution(Ode_to_Joy[note],OtJ_Duration[note])
    elif req.a == 4:
	print "\nExecuting Fra Martino"
        for note in range(0,len(Fra_Martino)):
            execution(Fra_Martino[note],FM_Duration[note])
    elif req.a == 5:
	print "\nExecuting Tetris Theme"
        for note in range(0,len(Tetris)):
            execution(Tetris[note],T_Duration[note])
    elif req.a == 6:
	print "\nExecuting Super Mario Theme"
        for note in range(0,len(Super_Mario)):
            execution(Super_Mario[note],SM_Duration[note])    
    else:
        print "Choice not valid"
    
    print "\nThe end\nI hope you enjoyed it"
    pwm.stop()

def my_server():
    rospy.init_node('song_server')
    s=rospy.Service('song_service', Song , choice)
    print 'Waiting for choice'
    rospy.spin()

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_hndlr)
    my_server()
