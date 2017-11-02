#motor.py
import RPi.GPIO as GPIO
import time

motor_pin = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup(motor_pin, GPIO.OUT)

try:
    while True:
       GPIO.output(motor_pin, True)
       time.sleep(0.5) #go(0.5s)
       GPIO.output(motor_pin, False)
       time.sleep(0.5) #stop(0.5s)
finally:
    print("Cleaning up")
    GPIO.cleanup()
    
