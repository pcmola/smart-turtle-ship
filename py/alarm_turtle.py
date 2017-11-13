#alarm_turtle.py
import time
import RPi.GPIO as GPIO
import os

goback_pwm_pin = 16  #GO, BACK PWM(SPEED) PIN
goback_dir_pin = 12  #GO, BACK DIRECTION PIN
lr_pwm_pin     = 19  #LEFT, RIGHT PWM(SPEED) PIN
lr_dir_pin     = 13  #LEFT, RIGHT DIRECTION PIN

GPIO.setmode(GPIO.BCM)
GPIO.setup(goback_pwm_pin, GPIO.OUT)
GPIO.setup(goback_dir_pin, GPIO.OUT)
GPIO.setup(lr_pwm_pin,     GPIO.OUT)
GPIO.setup(lr_dir_pin,     GPIO.OUT)

lr_speed = GPIO.PWM(lr_pwm_pin, 500)
lr_speed.start(0)

fmt = "%H:%M:%S"
t = time.localtime()
current_time = time.strftime(fmt, t)

try:
    while True:
        t = time.localtime()
        current_time = time.strftime(fmt, t)
        #if(current_time[0:2] >= "09" and current_time[0:2] <= "18" and (current_time[3:5] == "00" or current_time[3:5] == "30") and current_time[6:8] <= "50"):                 print "KEY_UP pressed"
        if(current_time[0:2] == "22"):
            print ("{}".format(current_time))
            
            #Go
            print "GO"
            GPIO.output(goback_pwm_pin, True)
            GPIO.output(goback_dir_pin, False)        
            time.sleep(2)
            
            #Stop
            GPIO.output(goback_pwm_pin, False)
            GPIO.output(goback_dir_pin, False)  
            time.sleep(1)
            
            #Back
            print "BACK"
            GPIO.output(goback_pwm_pin, True)
            GPIO.output(goback_dir_pin, True)        
            time.sleep(2)
            
            #Stop
            GPIO.output(goback_pwm_pin, False)
            GPIO.output(goback_dir_pin, False)  
            time.sleep(1)

            #Left
            print "LEFT"
            lr_speed.ChangeDutyCycle(40) 
            GPIO.output(lr_dir_pin, False)
            time.sleep(0.4)
            lr_speed.ChangeDutyCycle(0) 

            time.sleep(1)

            #Right
            print "RIGHT"
            lr_speed.ChangeDutyCycle(40) 
            GPIO.output(lr_dir_pin, True)
            time.sleep(0.4)
            lr_speed.ChangeDutyCycle(0) 

            time.sleep(1)
            
            #Dragon Sound
            print "DRAGON"
            os.system("sudo /home/pi/py/hub-ctrl -h 0 -P 2 -p 0")
            time.sleep(1)
            os.system("sudo /home/pi/py/hub-ctrl -h 0 -P 2 -p 1")                
            os.system("aplay /home/pi/py/music/dragon.wav")
            
            time.sleep(1)
            
            #Cannon Sound
            print "CANNON"
            os.system("sudo /home/pi/py/hub-ctrl -h 0 -P 2 -p 0")
            time.sleep(1)
            os.system("sudo /home/pi/py/hub-ctrl -h 0 -P 2 -p 1")                
            os.system("aplay /home/pi/py/music/cannon.wav")

            time.sleep(1)


except KeyboardInterrupt:
    print ""


finally:
    print "Program End"
    GPIO.cleanup()
