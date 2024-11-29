import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from time import sleep # Import the sleep function from the time module

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW) 
GPIO.setup(10, GPIO.OUT, initial=GPIO.LOW) 

while True: # Run forever
 GPIO.output(8, GPIO.HIGH) # Turn on
 sleep(0.5) # Sleep for 1 second
 GPIO.output(8, GPIO.LOW) # Turn off
 sleep(0.4) # Sleep for one second
 
 GPIO.output(10, GPIO.HIGH) # Turn on
 sleep(0.3) # Sleep for 1 second
 GPIO.output(10, GPIO.LOW) # Turn off
 sleep(0.2) # Sleep for one second