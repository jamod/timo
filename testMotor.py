import RPi.GPIO as GPIO
import time

# Pin Definitions (BCM)
motor1_pin1 = 17  # GPIO pin for Motor 1
motor1_pin2 = 18  # GPIO pin for Motor 1
motor2_pin1 = 22  # GPIO pin for Motor 2
motor2_pin2 = 23  # GPIO pin for Motor 2
enable_pin1 = 27  # Enable pin for Motor 1
enable_pin2 = 24  # Enable pin for Motor 2

# Pin Setup
GPIO.setwarnings(False)  # Disable warnings
GPIO.setmode(GPIO.BCM)
GPIO.setup(motor1_pin1, GPIO.OUT)
GPIO.setup(motor1_pin2, GPIO.OUT)
GPIO.setup(motor2_pin1, GPIO.OUT)
GPIO.setup(motor2_pin2, GPIO.OUT)
GPIO.setup(enable_pin1, GPIO.OUT)
GPIO.setup(enable_pin2, GPIO.OUT)

# Enable Motors
GPIO.output(enable_pin1, GPIO.HIGH)
GPIO.output(enable_pin2, GPIO.HIGH)

def motor_forward():
    # Motor 1 forward
    GPIO.output(motor1_pin1, GPIO.HIGH)
    GPIO.output(motor1_pin2, GPIO.LOW)
    # Motor 2 forward
    GPIO.output(motor2_pin1, GPIO.HIGH)
    GPIO.output(motor2_pin2, GPIO.LOW)

def motor_turn_right():
    # Motor 1 forward
    GPIO.output(motor1_pin1, GPIO.HIGH)
    GPIO.output(motor1_pin2, GPIO.LOW)
    # Motor 2 forward
    GPIO.output(motor2_pin1, GPIO.LOW)
    GPIO.output(motor2_pin2, GPIO.HIGH)   

def motor_turn_left():
    # Motor 1 forward
    GPIO.output(motor1_pin1, GPIO.LOW)
    GPIO.output(motor1_pin2, GPIO.HIGH)
    # Motor 2 forward
    GPIO.output(motor2_pin1, GPIO.LOW)
    GPIO.output(motor2_pin2, GPIO.HIGH)     

'''def motor_backward():
    # Motor 1 backward
    GPIO.output(motor1_pin1, GPIO.LOW)
    GPIO.output(motor1_pin2, GPIO.HIGH)
    # Motor 2 backward
    GPIO.output(motor2_pin1, GPIO.LOW)
    GPIO.output(motor2_pin2, GPIO.HIGH)'''

def stop_motors():
    # Stop both motors
    GPIO.output(motor1_pin1, GPIO.LOW)
    GPIO.output(motor1_pin2, GPIO.LOW)
    GPIO.output(motor2_pin1, GPIO.LOW)
    GPIO.output(motor2_pin2, GPIO.LOW)

try:
    while True:
        motor_forward()
        time.sleep(5)
        stop_motors()
        time.sleep(1)
        '''motor_backward()'''
        motor_turn_right()
        time.sleep(2)
        motor_turn_left()
        time.sleep(5)
        stop_motors()
        time.sleep(1)
        stop_motors()
        time.sleep(1)
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
