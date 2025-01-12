import RPi.GPIO as GPIO

from time import sleep

GPIO.setmode(GPIO.BCM)

Motor1A = 24
Motor1B = 25
Motor1E = 18

Motor2A = 8
Motor2B = 7
Motor2E = 23



GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor1E,GPIO.OUT)

GPIO.setup(Motor2A,GPIO.OUT)
GPIO.setup(Motor2B,GPIO.OUT)
GPIO.setup(Motor2E,GPIO.OUT)

print "Motor going to Start"

GPIO.output(Motor1A,GPIO.LOW) # to run motor in clockwise direction
GPIO.output(Motor1B,GPIO.HIGH) # put it high to rotate motor in anti-clockwise direction
GPIO.output(Motor1E,GPIO.HIGH) # Should be always high to start motor

GPIO.output(Motor2A,GPIO.HIGH) # to run motor in clockwise direction
GPIO.output(Motor2B,GPIO.LOW) # put it high to rotate motor in anti-clockwise direction
GPIO.output(Motor2E,GPIO.HIGH) # Should be always high to start motor

sleep(20)

print "Stopping motor"

GPIO.output(Motor1E,GPIO.LOW) # to stop the motor
GPIO.output(Motor2E,GPIO.LOW) # to stop the motor

GPIO.cleanup()