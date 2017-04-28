#!/usr/bin/python
# Last modified 1/29/2017 G. Oij
# initially from https://www.youtube.com/watch?v=XvOONPSoglY
# Modified to work with DC Motors through L298N 1/30/17
# mc is short for Motor Control

import curses
import os

#Works on Jessie, no display on Wheezy
screen=curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)


import time
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)
DELAY=.1
# CODE: LF means gpio to move the Left Motor / Wheel forward
# CODE: LB means gpio to move the Left Motor / Wheel backward
# CODE: RF means gpio to move the Right Motor / Wheel forward
# CODE: RB means gpio to move the Right Motor / Wheel backward
LF=21
LB=23
RF=22
RB=24
LEDGREEN=8
LEDBLUE=7
LEDRED=12


GPIO.setup(LF,GPIO.OUT) #Left Forward GPIO Port Output
GPIO.output(LF,GPIO.LOW) #Left Forward GPIO Port set to LOW
GPIO.setup(LB,GPIO.OUT)
GPIO.output(LB,GPIO.LOW)
GPIO.setup(RF,GPIO.OUT)
GPIO.output(RF,GPIO.LOW)
GPIO.setup(RB,GPIO.OUT)
GPIO.output(RB,GPIO.LOW)

GPIO.setup(LEDGREEN,GPIO.OUT)
GPIO.setup(LEDBLUE,GPIO.OUT)
GPIO.setup(LEDRED,GPIO.OUT)

try:
        while True:
                
		char= screen.getch()
                if char == ord('q'):
                        break
                elif char == curses.KEY_UP:
                        print"forward"
			GPIO.output(LEDGREEN,GPIO.HIGH)
			time.sleep(DELAY)
			GPIO.output(LF,GPIO.HIGH)
			GPIO.output(RF,GPIO.HIGH)	
			time.sleep(DELAY)
			GPIO.output(LB,GPIO.LOW)
			GPIO.output(RB,GPIO.LOW)
                elif char == curses.KEY_DOWN:
                        print"backward"
			GPIO.output(LEDRED,GPIO.HIGH)
			GPIO.output(LF,GPIO.LOW)
			GPIO.output(LB,GPIO.HIGH)
			GPIO.output(RF,GPIO.LOW)
			GPIO.output(RB,GPIO.HIGH)
                elif char == curses.KEY_RIGHT:
                        print"right"
			GPIO.output(LEDBLUE,GPIO.HIGH)
			GPIO.output(LF,GPIO.HIGH)
			GPIO.output(LB,GPIO.LOW)
			GPIO.output(RF,GPIO.LOW)
			GPIO.output(RB,GPIO.HIGH)
                elif char == curses.KEY_LEFT:
                        print"left"
			GPIO.output(LEDBLUE,GPIO.HIGH)
			GPIO.output(LF,GPIO.LOW)
			GPIO.output(LB,GPIO.HIGH)
			GPIO.output(RF,GPIO.HIGH)
			GPIO.output(RB,GPIO.LOW)
                elif char == 10: #The Enter Key
                        print"stop"
			GPIO.output(LF,GPIO.LOW)
			GPIO.output(RF,GPIO.LOW)
			GPIO.output(LB,GPIO.LOW)
			GPIO.output(RB,GPIO.LOW)
			GPIO.output(LEDRED,GPIO.LOW)
			GPIO.output(LEDBLUE,GPIO.LOW)
			GPIO.output(LEDGREEN,GPIO.LOW)
finally:
        #Close it down; turn echo back on.
        curses.nocbreak(); screen.keypad(0); curses.echo()
        curses.endwin()
	GPIO.cleanup()

