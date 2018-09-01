## IMPORTO LIBRERIE UTILIZZATE

import RPi.GPIO as GPIO # Import the GPIO Library
import time # Import the Time library
#import numpy as np

import pyfirmata
board = pyfirmata.Arduino('/dev/ttyUSB0')
# ########################B# \\

# CamJam EduKit 3 - Robotics
# Wii controller remote control script



# Set the GPIO modes
GPIO.setmode(GPIO.BOARD) #NUMERAZIONE CON NUM PIEDINO
GPIO.setwarnings(False)


#lista colori cavi
#EnA = bianco
#In1 = verde
#In2 = Blu

#In3=Viola
#In4= grigio
#EnB= Nero


# Set variables for the GPIO motor pins
#int enA = 11;
enA = board.get_pin('d:11:o')
#int in1 = 10;
pinMotorAForwards = board.get_pin('d:12:o')
#int in2 = 9;
pinMotorABackwards = board.get_pin('d:9:o')
#motor two
#int enB = 3;
enB = board.get_pin('d:3:o')
#int in3 = 6;
pinMotorBForwards = board.get_pin('d:6:o')
#int in4 = 5;
pinMotorBBackwards = board.get_pin('d:5:o')

#it = util.Iterator(board)
#it.start()
#board.analog[11].enable_reporting()
#board.analog[3].enable_reporting()
#board.analog[0].read()
#it.start()

vel = 190
enA.write(1)
enB.write(1)

#pinMotorAForwards = 10
#pinMotorABackwards = 9
#pinMotorBForwards = 8
#pinMotorBBackwards = 7

# Set the GPIO Pin mode
#GPIO.setup(pinMotorAForwards, GPIO.OUT)
#GPIO.setup(pinMotorABackwards, GPIO.OUT)
#GPIO.setup(pinMotorBForwards, GPIO.OUT)
#GPIO.setup(pinMotorBBackwards, GPIO.OUT)


# CODE 4 SERVO
DELAY = 1
MIN = 5
MAX = 175
MID = 90

servo = board.get_pin('d:10:s')
#servo_config(servo,MIN,MAX, angle=0)

def move_servo(v):
    servo.write(v)
    board.pass_time(DELAY)

# Turn all motors off
def StopMotors():
    pinMotorAForwards.write(0)
    pinMotorABackwards.write(0)
    pinMotorBForwards.write(0)
    pinMotorBBackwards.write(0)

# Turn both motors forwards
def Forwards():
    pinMotorAForwards.write(1)
    pinMotorABackwards.write(0)
    pinMotorBForwards.write(1)
    pinMotorBBackwards.write(0)

# Turn both motors backwards
def Backwards():
    pinMotorAForwards.write(0)
    pinMotorABackwards.write(1)
    pinMotorBForwards.write(0)
    pinMotorBBackwards.write(1)

def Left():
    pinMotorAForwards.write(1)
    pinMotorABackwards.write(0)
    pinMotorBForwards.write(0)
    pinMotorBBackwards.write(1)

def Right():
    pinMotorAForwards.write(0)
    pinMotorABackwards.write(1)
    pinMotorBForwards.write(1)
    pinMotorBBackwards.write(0)

StopMotors()
import sys, termios, tty, os

def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)

    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

#PIN_LED = 25
#GPIO.setup(PIN_LED, GPIO.OUT)
#GPIO.output(PIN_LED, 0)
button_delay = 0.1

#for x in range(0,3):
#    GPIO.output(PIN_LED, 1)
#    time.sleep(0.25)
#    GPIO.output(PIN_LED, 0)
 #   time.sleep(0.25)

while True:
    char = getch()

    if (char == "r"):
        move_servo(MIN)
        move_servo(MAX)
        move_servo(MID)
        
    if (char == "q"):
        StopMotors()
        exit(0)  

    if (char == "a"):
        print 'Left pressed'
        Left()
        time.sleep(button_delay)

    if (char == "d"):
        print 'Right pressed'
        Right()
        time.sleep(button_delay)          

    elif (char == "w"):
        print 'Up pressed' 
        Forwards()       
        time.sleep(button_delay)          
    
    elif (char == "s"):
        print 'Down pressed'      
        Backwards()
        time.sleep(button_delay)  
    
    StopMotors()
