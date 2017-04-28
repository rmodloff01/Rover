import curses
import time
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
rightBackward = 24
rightForward = 22
leftBackward = 23
leftForward = 21
GPIO.setup(rightBackward, GPIO.OUT)
GPIO.setup(rightForward, GPIO.OUT)
GPIO.setup(leftBackward, GPIO.OUT)
GPIO.setup(leftForward, GPIO.OUT)
GPIO.output(rightBackward, GPIO.LOW)
GPIO.output(rightForward, GPIO.LOW)
GPIO.output(leftBackward, GPIO.LOW)
GPIO.output(leftForward, GPIO.LOW)
screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)
def killMotors():
    GPIO.output(rightBackward, False)
    GPIO.output(rightForward, False)
    GPIO.output(leftBackward, False)
    GPIO.output(leftForward, False)
try:
    while True:
        char = screen.getch()
        if char == ord('q'):
            print("DONE!\n")
            GPIO.output(rightBackward, GPIO.LOW)
            GPIO.output(rightForward, GPIO.LOW)
            GPIO.output(leftBackward, GPIO.LOW)
            GPIO.output(leftForward, GPIO.LOW)
            break
        elif char == curses.KEY_UP:
            print("FORWARD\n")
            killMotors()
            time.sleep(.5)
            GPIO.output(rightBackward, False)
            GPIO.output(rightForward, True)
            time.sleep(.01)
            GPIO.output(leftBackward, False)
            GPIO.output(leftForward, True)
        elif char == curses.KEY_DOWN:
            print("BACKWARD\n")
            killMotors()
            time.sleep(.5)
            GPIO.output(rightBackward, True)
            GPIO.output(rightForward, False)
            time.sleep(.01)
            GPIO.output(leftBackward, True)
            GPIO.output(leftForward, False)
        elif char == curses.KEY_RIGHT:
            print ("RIGHT\n")
            killMotors()
            time.sleep(.5)
            GPIO.output(rightBackward, False)
            GPIO.output(rightForward, False)
            GPIO.output(leftBackward, False)
            GPIO.output(leftForward, True)

        elif char == curses.KEY_LEFT:
            print ("LEFT\n")
            killMotors()
            time.sleep(.5)
            GPIO.output(rightBackward, False)
            GPIO.output(rightForward, True)
            GPIO.output(leftBackward, False)
            GPIO.output(leftForward, False)

        elif char == ord('s'):
            killMotors()

finally:
    # Close down curses properly, inc turn echo back on!
    curses.nocbreak();
    screen.keypad(0);
    curses.echo()
    curses.endwin()
    GPIO.cleanup()
