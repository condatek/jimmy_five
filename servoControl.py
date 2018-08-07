#!/usr/bin/env python
# Servo Control for Raspberry Pi with Adafruit servo control board 
import pyfirmata
board = pyfirmata.Arduino('/dev/ttyUSB0')
#-------------------------------------------------------------------------------
#### Imports ####

import time
import sys

#from Adafruit_PWM_Servo_Driver import PWM

#### Constants ####

#-------------------------------------------------------------------------------
#### Servo Initialization

# I2C address is 0x40
#pwm = PWM(0x40)
# Servo frequency 60Hz
#pwm.setPWMFreq(60)

# These values cannot be smaller than 100 and more than 700.  
_PAN_SERVO_CHANNEL = 2
#_TILT_SERVO_CHANNEL = 3

_PAN_SERVO_LEFT = 250
_PAN_SERVO_RIGHT = 520
_PAN_SERVO_CENTER = 385

#_TILT_SERVO_UP = 605
#_TILT_SERVO_DOWN = 475
#_TILT_SERVO_CENTER = 605

#### Objects ####

servo = board.get_pin('d:10:s')

#-------------------------------------------------------------------------------
class ServoControl(object):
    # Make sure there is only one instance of ServoControl

	_instances=[]

	# Initialize the object
	def __init__(self):
		if ( len(self._instances)>1 ):
			print("ERROR: One instance of ServoControl is running already.")
			exit(1)

		self._instances.append(self)

		#servo_config(servo,MIN,MAX, angle=0)

#-------------------------------------------------------------------------------        
	# Move left
	def panLeft(self):
		servo.write(_PAN_SERVO_LEFT)

#-------------------------------------------------------------------------------        
	# Move left with exact degree
	def panExactLeft(self, degree):
		servo.write(degree)

#-------------------------------------------------------------------------------        
	# Move right
	def panRight(self):
		servo.write(_PAN_SERVO_RIGHT)

#-------------------------------------------------------------------------------        
	# Move right with exact degree
	def panExactRight(self, degree):
		servo.write(degree)
    
#-------------------------------------------------------------------------------        
	# Position pan servo in the middle
	def panCenter(self):
		servo.write(_PAN_SERVO_CENTER)

#-------------------------------------------------------------------------------        
	# Position pan servo exactly
	def panExactCenter(self, degree):
		servo.write(degree)

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------      
	# Reset servo orientation
	def resetServo(self):
		servo.write(PAN_SERVO_CENTER)
