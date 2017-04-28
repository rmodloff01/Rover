import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
RED=12
BLUE=7
GREEN=8
GPIO.setup(RED,GPIO.OUT)
GPIO.setup(BLUE,GPIO.OUT)
GPIO.setup(GREEN,GPIO.OUT)
print "LED on"
GPIO.output(RED,GPIO.HIGH)
GPIO.output(BLUE,GPIO.HIGH)
GPIO.output(GREEN,GPIO.HIGH)
time.sleep(5)
print "LED off"
GPIO.output(RED,GPIO.LOW)
GPIO.output(BLUE,GPIO.LOW)
GPIO.output(GREEN,GPIO.LOW)
