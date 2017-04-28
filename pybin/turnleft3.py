#! /usr/bin/python
# Attempts to turn 180 degrees
import time
# Import the Raspberry Pi GPIO libraries that
# allow us to connect the Raspberry Pi to
# other physical devices via the General
# Purpose Input-Output (GPIO) pins
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
# Now we need to set-up the General Purpose
# Input-Ouput (GPIO) pins
# Clear the current set-up so that we can
# start from scratch
GPIO.cleanup()
# Set up the GPIO library to use Raspberry Pi
# board pin numbers
GPIO.setmode(GPIO.BOARD)
# Set Pin 12 on the GPIO header to act as
# the output port to control forward movement on LEFTWHEEL
OFFDELAY=.01
ONDELAY=.01

LEFTWHEEL=23
RIGHTWHEEL=22

LEDBLUE=7
GPIO.setup(LEFTWHEEL,GPIO.OUT)
GPIO.setup(RIGHTWHEEL,GPIO.OUT)
GPIO.setup(LEDBLUE,GPIO.OUT)
GPIO.setup(RIGHTWHEEL,GPIO.LOW)
GPIO.output(LEFTWHEEL,GPIO.LOW)
pulses=46
try:
        while pulses > 0:
                time.sleep(OFFDELAY)
                GPIO.output(LEFTWHEEL,GPIO.HIGH)
                GPIO.output(RIGHTWHEEL,GPIO.HIGH)
                GPIO.output(LEDBLUE,GPIO.HIGH)
                time.sleep(ONDELAY)
                GPIO.output(LEFTWHEEL,GPIO.LOW)
                GPIO.output(RIGHTWHEEL,GPIO.LOW)
                GPIO.output(LEDBLUE,GPIO.LOW)
                pulses = pulses - 1
except KeyboardInterrupt:
        #call("echo Hello World", shell=True)
        print "Please, oh please let me keep moving."
        GPIO.output(LEFTWHEEL,GPIO.LOW)
        GPIO.output(RIGHTWHEEL,GPIO.LOW)
        GPIO.output(LEDBLUE,GPIO.LOW)
        #import os
        #cmd = '/home/pi/bin/lo'
        #os.system(cmd)
