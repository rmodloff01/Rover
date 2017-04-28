import time
# Import the Raspberry Pi GPIO libraries that
# allow us to connect the Raspberry Pi to
# other physical devices via the General
# Purpose Input-Output (GPIO) pins
import RPi.GPIO as GPIO
import os
GPIO.setwarnings(False)
# Now we need to set-up the General Purpose
# Input-Ouput (GPIO) pins
# Clear the current set-up so that we can
# start from scratch
GPIO.cleanup()
# Set up the GPIO library to use Raspberry Pi
# board pin numbers
GPIO.setmode(GPIO.BOARD)
# Set Pin 16 on the GPIO header to act as
# the output port to control forward movement on RIGHTWHEEL
OFFDELAY=.01
ONDELAY=.01
RIGHTWHEELDELAY=.002
RIGHTWHEEL=22
LEFTWHEEL=21
LEDGREEN=8
GPIO.setup(LEDGREEN,GPIO.OUT)
GPIO.output(LEDGREEN,GPIO.LOW)
GPIO.setup(RIGHTWHEEL,GPIO.OUT)
GPIO.setup(LEFTWHEEL,GPIO.OUT)
GPIO.output(RIGHTWHEEL,GPIO.LOW)
GPIO.output(LEFTWHEEL,GPIO.LOW)

try:
	while True:
		time.sleep(OFFDELAY)
		GPIO.output(LEDGREEN,GPIO.HIGH)
		GPIO.output(LEFTWHEEL,GPIO.HIGH)
		time.sleep(RIGHTWHEELDELAY)
		GPIO.output(RIGHTWHEEL,GPIO.HIGH)
		time.sleep(ONDELAY)
		GPIO.output(LEFTWHEEL,GPIO.LOW)
		GPIO.output(RIGHTWHEEL,GPIO.LOW)
except KeyboardInterrupt:
	print "Please, oh please let me keep moving."
	GPIO.output(LEDGREEN,GPIO.LOW)
	GPIO.output(RIGHTWHEEL,GPIO.LOW)
	GPIO.output(LEFTWHEEL,GPIO.LOW)

