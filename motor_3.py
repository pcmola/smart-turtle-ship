#motor_3.py
#go/back
import RPi.GPIO as GPIO
import time

pwm_pin    = 26
goback_pin = 22

GPIO.setmode(GPIO.BCM)
GPIO.setup(pwm_pin,    GPIO.OUT)
GPIO.setup(goback_pin, GPIO.OUT)

pwm_motor = GPIO.PWM(pwm_pin, 500)
pwm_motor.start(0)

try:
    while True:
        gear = input("Press gear(-2, 1, 0, 1, 2) : ");
        if gear == "0":            
            pwm_motor.ChangeDutyCycle(0)   #stop
        elif gear == "1" or gear == "-1":
            pwm_motor.ChangeDutyCycle(50)  #go slow
        elif gear == "2" or gear == "-2":
            pwm_motor.ChangeDutyCycle(100) #go fast

        if gear > "0":
            GPIO.output(goback_pin, True)  #go 
        else:
            GPIO.output(goback_pin, False) #back    
        
finally:
    print("Cleaning up")
    GPIO.cleanup()
    
