import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)

def distance(GPIO_TRIGGER, GPIO_ECHO):
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
	GPIO.setup(GPIO_ECHO, GPIO.IN)
	GPIO.output(GPIO_TRIGGER, True)
	time.sleep(0.00001)
	GPIO.output(GPIO_TRIGGER, False)
	
	StartTime = time.time()
	StopTime = time.time()

	while GPIO.input(GPIO_ECHO) == 0:
		StartTime = time.time()

	while GPIO.input(GPIO_ECHO) == 1:
		StopTime = time.time()
	GPIO.cleanup()

	TimeElapsed = StopTime - StartTime
	distanceInCm = (TimeElapsed * 34300) / 2

	if (distanceInCm > 150):
		distanceInCm=150
	return distanceInCm

print (distance(3,5))
TRIG = 3
ECHO = 5

