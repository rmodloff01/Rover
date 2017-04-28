#!/usr/bin/python
# Last modified 2/6/2017 G. Oij
# Just turn all GPIO ports on PI3 Low
import os

import time
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)
DELAY=.01

GPIO.setup(3,GPIO.OUT) # Set as output
GPIO.setup(5,GPIO.OUT) # Set as output
GPIO.setup(7,GPIO.OUT) # Set as output
GPIO.setup(8,GPIO.OUT) # Set as output
GPIO.setup(10,GPIO.OUT) # Set as output
GPIO.setup(11,GPIO.OUT) # Set as output
GPIO.setup(12,GPIO.OUT) # Set as output
GPIO.setup(13,GPIO.OUT) # Set as output
GPIO.setup(15,GPIO.OUT) # Set as output
GPIO.setup(16,GPIO.OUT) # Set as output
GPIO.setup(18,GPIO.OUT) # Set as output
GPIO.setup(19,GPIO.OUT) # Set as output
GPIO.setup(21,GPIO.OUT) # Set as output
GPIO.setup(22,GPIO.OUT) # Set as output
GPIO.setup(23,GPIO.OUT) # Set as output
GPIO.setup(24,GPIO.OUT) # Set as output
GPIO.setup(26,GPIO.OUT) # Set as output
#GPIO.setup(27,GPIO.OUT) # Complains about setting this port as output
#GPIO.setup(28,GPIO.OUT) # Complains about setting this port as output
GPIO.setup(29,GPIO.OUT) # Set as output
GPIO.setup(31,GPIO.OUT) # Set as output
GPIO.setup(32,GPIO.OUT) # Set as output
GPIO.setup(33,GPIO.OUT) # Set as output
GPIO.setup(35,GPIO.OUT) # Set as output
GPIO.setup(36,GPIO.OUT) # Set as output
GPIO.setup(37,GPIO.OUT) # Set as output
GPIO.setup(38,GPIO.OUT) # Set as output
GPIO.setup(40,GPIO.OUT) # Set as output


GPIO.output(3,GPIO.LOW) # Set the output to low
GPIO.output(5,GPIO.LOW) # Set the output to low
GPIO.output(7,GPIO.LOW) # Set the output to low
GPIO.output(8,GPIO.LOW) # Set the output to low
GPIO.output(10,GPIO.LOW) # Set the output to low
GPIO.output(11,GPIO.LOW) # Set the output to low
GPIO.output(12,GPIO.LOW) # Set the output to low
GPIO.output(13,GPIO.LOW) # Set the output to low
GPIO.output(15,GPIO.LOW) # Set the output to low
GPIO.output(16,GPIO.LOW) # Set the output to low
GPIO.output(18,GPIO.LOW) # Set the output to low
GPIO.output(19,GPIO.LOW) # Set the output to low
GPIO.output(21,GPIO.LOW) # Set the output to low
GPIO.output(22,GPIO.LOW) # Set the output to low
GPIO.output(23,GPIO.LOW) # Set the output to low
GPIO.output(24,GPIO.LOW) # Set the output to low
GPIO.output(26,GPIO.LOW) # Set the output to low
#GPIO.output(27,GPIO.LOW) # Set the output to low
#GPIO.output(28,GPIO.LOW) # Set the output to low
GPIO.output(29,GPIO.LOW) # Set the output to low
GPIO.output(31,GPIO.LOW) # Set the output to low
GPIO.output(32,GPIO.LOW) # Set the output to low
GPIO.output(33,GPIO.LOW) # Set the output to low
GPIO.output(35,GPIO.LOW) # Set the output to low
GPIO.output(36,GPIO.LOW) # Set the output to low
GPIO.output(37,GPIO.LOW) # Set the output to low
GPIO.output(38,GPIO.LOW) # Set the output to low
GPIO.output(40,GPIO.LOW) # Set the output to low

GPIO.cleanup()
