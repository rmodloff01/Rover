import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(32, GPIO.IN)
GPIO.setup(31, GPIO.IN)
GPIO.setup(26, GPIO.IN)
GPIO.setup(29, GPIO.IN)

try:

        while True:

		LF = GPIO.input( 32 )
		RF = GPIO.input( 31 )
		LB = GPIO.input( 26 )
		RB = GPIO.input( 29 )

                if LF == 0:

                        print( 'Left Front: Obstacle Detected' )
                        time.sleep( 0.1 )

	 	if RF == 0:

                        print( 'Right Front: Obstacle Detected' )
                        time.sleep( 0.1 )

		if LB == 0:

                        print( 'Left Back: Obstacle Detected' )
                        time.sleep( 0.1 )

	 	if RB == 0:

                        print( 'Right Back: Obstacle Detected' )
                        time.sleep( 0.1 )


except KeyboardInterrupt:

        GPIO.cleanup()
