# First pass 3/18/15 G. Oij
# If any of the three distance sensors detect a distance of less than 9",
# shut down all Python Scripts
# Run by typing "abort" (/home/pi/bin/abort)
import os
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.cleanup()
import time
GPIO.setmode(GPIO.BOARD)

# Distance Sensor GPIO ports
TRIG1 = 16
ECHO1 = 18
TRIG2 = 11
ECHO2 = 13
TRIG3 = 3
ECHO3 = 5
GREEN = 8
GPIO.setup(GREEN,GPIO.OUT)
GPIO.setup(GREEN,GPIO.LOW)
GPIO.setup(TRIG1,GPIO.OUT)
GPIO.setup(ECHO1,GPIO.IN)
GPIO.setup(TRIG2,GPIO.OUT)
GPIO.setup(ECHO2,GPIO.IN)
GPIO.setup(TRIG3,GPIO.OUT)
GPIO.setup(ECHO3,GPIO.IN)

#Laser
GPIO.setup(19,GPIO.OUT)

#Avoidance Sensors
GPIO.setup(32, GPIO.IN)
LF = GPIO.input( 32 )
GPIO.setup(31, GPIO.IN)
RF = GPIO.input( 31 )
GPIO.setup(26, GPIO.IN)
LB = GPIO.input( 26 )
GPIO.setup(29, GPIO.IN)
RB = GPIO.input( 29 )

try:
        while True:

		GPIO.output(19,GPIO.HIGH)		

		# Set up the Distance sensors for reading 
                GPIO.output(TRIG1, False)
                time.sleep(.01)
                GPIO.output(TRIG1, True)
                time.sleep(.01)
                GPIO.output(TRIG1, False)

                pulse_start1 = 0
                while GPIO.input(ECHO1)==0:
                        pulse_start1 = time.time()

                while GPIO.input(ECHO1)==1:
                        pulse_end1 = time.time()


                pulse_duration = pulse_end1 - pulse_start1
                

                distanceInCm1 = (pulse_duration * 34300) / 2
                if (distanceInCm1 < 6):
                        print "TOO CLOSE; SHUTTING DOWN"
                        #sudo killall python
                	os.system('python stop.py')
#			os.system('python turnright4.py')
		else:
                        print round(distanceInCm1,3), "cm (distance1)"
                GPIO.output(TRIG2, False)
                time.sleep(.1)
                GPIO.output(TRIG2, True)
                time.sleep(.1)
                GPIO.output(TRIG2, False)
	        pulse_start2 = 0
                while GPIO.input(ECHO2)==0:
                        pulse_start2 = time.time()
                while GPIO.input(ECHO2)==1:
                        pulse_end2 = time.time()


                pulse_duration = pulse_end2 - pulse_start2

                distanceInCm2 = (pulse_duration * 34300) / 2
                if (distanceInCm2 > 30000):
                        print "Erroneous reading, more than 200 cm"
                elif distanceInCm2 < 15:
                        print "TOO CLOSE; SHUTTING DOWN"	
                        #sudo killall python
                        #os.system('python stop.py')

			if LF == 0:
				os.system('backward1.py')
                        	print('Turning Right')
                       		os.system('python turnright2.py')
#				os.system('./getpic')
			elif RF == 0:
				os.system('backward1.py')
                        	print('Turning Left')
                        	os.system('python turnleft2.py')
#				os.system('./getpic')

			else:
				os.system('python stop.py')
				os.system('python backward1.py')
				os.system('python turnleft4.py')				
                else:
                        print round(distanceInCm2,3), "cm (distance2)"
                        os.system('python forward1.py')
		

	        GPIO.output(TRIG3, False)
                time.sleep(.001)
                GPIO.output(TRIG3, True)
                time.sleep(0.001)
                GPIO.output(TRIG3, False)

                pulse_start3 = 0
                while GPIO.input(ECHO3)==0:
                        pulse_start3 = time.time()
                while GPIO.input(ECHO3)==1:
                        pulse_end3 = time.time()

                pulse_duration = pulse_end3 - pulse_start3

                distanceInCm3 = (pulse_duration * 34300) / 2
                if distanceInCm3 < 6:
                        print "TOO CLOSE; SHUTTING DOWN"
                        #sudo killall python
                        os.system('python stop.py')
#			os.system('python turnleft4.py')
                print round(distanceInCm3,3), "cm (distance3)"
		
		LF = GPIO.input( 32 )
                RF = GPIO.input( 31 )
                LB = GPIO.input( 26 )
                RB = GPIO.input( 29 )

                if LF == 0 and distanceInCm1 < 6:

                        print( 'Left Front: Obstacle Detected' )
			os.system('python backward1.py')
                        os.system('python turnright4.py')
	        	#os.system('python forward2.py')
			time.sleep( 0.1 )

                if RF == 0 and distanceInCm3 < 6:

                        print( 'Right Front: Obstacle Detected' )
			os.system('python backward1.py')
                        os.system('python turnleft4.py')
                 #	os.system('python forward2.py')
			time.sleep( 0.1 )

                if LB == 0:

                        print( 'Left Back: Obstacle Detected' )
                        time.sleep( 0.1 )

                if RB == 0:

                        print( 'Right Back: Obstacle Detected' )
                        time.sleep( 0.1 )

                if LF == 0 and LB == 0:
                        os.system('python turnright4.py')
                        continue

                if RF == 0 and RB == 0:
                        os.system('python turnleft4.py')
                        continue

                if RF == 0 and LF == 0 and (distanceInCm2 < 15):
                        os.system('python backward1.py')
			
		time.sleep(0.1)

except KeyboardInterrupt:
        print "Hit Control-C"
        GPIO.cleanup()
