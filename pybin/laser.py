import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(19,GPIO.OUT)

print "Laser on"

try:
        while True:
		GPIO.output(19,GPIO.HIGH)
except KeyboardInterrupt:
        print "\nLaser off"
	GPIO.output(19,GPIO.LOW)
