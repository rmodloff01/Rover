#!/usr/bin/python
# Last modified 2/6/2017 G. Oij
# Just turn all Wheel GPIO ports on PI3 Low
import os

import time
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)
DELAY=.01

#Both wheels BACKWARD
LB=23
RB=24

#Both wheels FORWARD
LF=21
RF=22

GPIO.setup(LF,GPIO.OUT)
GPIO.setup(RF,GPIO.OUT)
GPIO.setup(LB,GPIO.OUT)
GPIO.setup(RB,GPIO.OUT)
GPIO.setup(LF,GPIO.LOW)
GPIO.setup(RF,GPIO.LOW)
GPIO.setup(LB,GPIO.LOW)
GPIO.setup(RB,GPIO.LOW)

GPIO.cleanup()
