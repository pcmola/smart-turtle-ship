#motor_2.py
import RPi.GPIO as GPIO
import time

pwm_pin = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup(pwm_pin, GPIO.OUT)

pwm_motor = GPIO.PWM(pwm_pin, 500)
pwm_motor.start(0)

try:
    while True:
        gear = input("Press gear(0, 1, 2) : ");
        if gear == "0":            
            pwm_motor.ChangeDutyCycle(0)
        elif gear == "1":
            pwm_motor.ChangeDutyCycle(50)
        elif gear == "2":
            pwm_motor.ChangeDutyCycle(100)

finally:
    print("Cleaning up")
    GPIO.cleanup()
    
