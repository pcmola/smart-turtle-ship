#turtle.py
# -*- coding:euc-kr -*-

import RPi.GPIO as GPIO
import lirc
import time
import os
import Adafruit_DHT
import I2C_LCD_driver
mylcd = I2C_LCD_driver.lcd()
ON_OFF_POINT = 50

KEY_UP = "up"
KEY_DOWN = "down"
KEY_RIGHT = "right"
KEY_LEFT = "left"
KEY_UP_RIGHT = "upright"
KEY_UP_LEFT = "upleft"
KEY_DOWN_RIGHT = "downright"
KEY_DOWN_LEFT = "downleft"
KEY_F1 = "f1"
KEY_F2 = "f2"
KEY_F3 = "f3"
KEY_F4 = "f4"
KEY_F5 = "f5"
KEY_F6 = "f6"

goback_pwn_pin = 16
goback_dir_pin = 12
lr_pwn_pin     = 19
lr_dir_pin     = 13

GPIO.setmode(GPIO.BCM)
GPIO.setup(goback_pwn_pin, GPIO.OUT)
GPIO.setup(goback_dir_pin, GPIO.OUT)
GPIO.setup(lr_pwn_pin,     GPIO.OUT)
GPIO.setup(lr_dir_pin,     GPIO.OUT)

lr_speed = GPIO.PWM(lr_pwn_pin, 500)
lr_speed.start(0)

print("Smart Turtle Ship started")

socketid = lirc.init("irtest", blocking=False)
usb_control_file = '/home/pi/py/turtle/files/usb.conf'

# USB Initialize
try:
    fout = open(usb_control_file, 'w')
    fout.write("USB_ON\n")
    fout.close()
    os.system("sudo /home/pi/py/hub-ctrl -h 0 -P 2 -p 1")
    print("USB Conf. has been initialized.")
except IOError:
    print("Cannot find file: " + usb_control_file)


# Set Hum Arrary
humArr = [100,100,100,100,100,100,100,100,100,100]
#print(humArr)
print ("H/T Check Start")
mylcd.lcd_display_string("H/T Check Start")
 

def changeUSBState():
    try:
        fin = open(usb_control_file, 'r')
        usb_flag = fin.read()
        fin.close()
    
    except IOError:
        print("file read error")
    
    if usb_flag[0:6] == "USB_ON":
        os.system("sudo /home/pi/py/hub-ctrl -h 0 -P 2 -p 0")

        try:
            fout = open(usb_control_file, 'w')
            fout.write("USB_OFF\n")
            fout.close()
            print("USB ON->OFF")
        except IOError:
            print("Cannot find file: " + usb_control_file)
    else :
        os.system("sudo /home/pi/py/hub-ctrl -h 0 -P 2 -p 1")

        try:
            fout = open(usb_control_file, 'w')
            fout.write("USB_ON\n")
            fout.close()
            print("USB OFF->ON")
        except IOError:
            print("Cannot find file: " + usb_control_file)


# 평균 구하기. 최소값, 최대값 제외
def avgval(humArr):  
    tempHum = 0.0 
    for i in humArr:
        tempHum += i  
    return (tempHum-max(humArr)-min(humArr))/(len(humArr)-2)  


#배열 내 모든 값에 최초 습도값 저장
humidity, temperature = Adafruit_DHT.read_retry(11, 27)  # GPIO27 (BCM notation)
mylcd.lcd_display_string("Program Start...")
 
#센서 오작동하는 경우가 있어, 습도 100 넘으면 다시 측정
if humidity > 100 :
    humidity, temperature = Adafruit_DHT.read_retry(11, 27)  # GPIO27 (BCM notation)
for x in range(len(humArr)-1, -1, -1) :
    humArr[x] = humidity
#print(humArr)

try:
    while(True):
        
        codeIR = lirc.nextcode()
        
        if len(codeIR) != 0 :
            print codeIR
            
            #Go
            if codeIR[0] == KEY_UP:
                print "KEY_UP pressed"
                GPIO.output(goback_pwn_pin, True)
                GPIO.output(goback_dir_pin, False)

            #Back
            elif codeIR[0] == KEY_DOWN:
                print "KEY_DOWN pressed"
                GPIO.output(goback_pwn_pin, True)
                GPIO.output(goback_dir_pin, True)

            #Left
            elif codeIR[0] == KEY_LEFT:
                print "KEY_LEFT pressed"
                lr_speed.ChangeDutyCycle(40) 
                GPIO.output(lr_dir_pin, False)

            #RIGHT
            elif codeIR[0] == KEY_RIGHT:
                print "KEY_RIGHT pressed"
                lr_speed.ChangeDutyCycle(40) 
                GPIO.output(lr_dir_pin, True)

            
            elif codeIR[0] == KEY_UP_LEFT:
                print "KEY_UP_LEFT pressed"
            elif codeIR[0] == KEY_UP_RIGHT:
                print "KEY_UP_RIGHT pressed"
            elif codeIR[0] == KEY_DOWN_LEFT:
                print "KEY_DOWN_LEFT pressed"
            elif codeIR[0] == KEY_DOWN_RIGHT:
                print "KEY_DOWN_RIGHT pressed"
            
            #Change the USB state
            elif codeIR[0] == KEY_F1:
                print "KEY_F1 pressed"
                changeUSBState()
            
            #Dragon Sound
            elif codeIR[0] == KEY_F2:
                print "KEY_F2 pressed"
                os.system('aplay /home/pi/py/music/dragon.wav')

            #Cannon Sound
            elif codeIR[0] == KEY_F3:
                print "KEY_F3 pressed"
                os.system("sudo /home/pi/py/hub-ctrl -h 0 -P 2 -p 0")
                time.sleep(1)
                os.system("sudo /home/pi/py/hub-ctrl -h 0 -P 2 -p 1")
                os.system('aplay /home/pi/py/music/cannon.wav')

            elif codeIR[0] == KEY_F4:
                print "KEY_F4 pressed"
            elif codeIR[0] == KEY_F5:
                print "KEY_F5 pressed"
            elif codeIR[0] == KEY_F6:
                print "KEY_F6 pressed"
            
            time.sleep(0.35)
            GPIO.output(goback_pwn_pin, False)
            #GPIO.output(lr_pwn_pin, False)
            lr_speed.ChangeDutyCycle(0) 
        
        humidity, temperature = Adafruit_DHT.read_retry(11, 27)  # GPIO27 (BCM notation)
        for x in range(len(humArr)-1, -1, -1) :
            if (x > 0) :
                humArr[x] = humArr[x-1]
            elif (x == 0) :
                humArr[x] = humidity
        avgHum = round(avgval(humArr), 1)
        print ("Humidity = {} %; Temperature = {} C".format(avgHum, temperature))
        mylcd.lcd_display_string(u"{} %; {} C  ".format(avgHum, temperature), 1)
 
        #습도가 기준치 이하면 가습기 OFF
        if (avgHum < ON_OFF_POINT) :
            mylcd.lcd_display_string(u"Humidifier On   ", 2)
            os.system("sudo /home/pi/py/hub-ctrl -h 0 -P 2 -p 1")
        else :
            mylcd.lcd_display_string(u"Humidifier Off  ", 2)
            os.system("sudo /home/pi/py/hub-ctrl -h 0 -P 2 -p 0")

except KeyboardInterrupt:
    lirc.deinit()

finally:
    print ""
    GPIO.cleanup()

    os.system("sudo /home/pi/py/hub-ctrl -h 0 -P 2 -p 1")
    mylcd.lcd_clear()
    print("Program End")
    mylcd.lcd_display_string("Program End")
    time.sleep(0.5)
    mylcd.lcd_display_string("Program End.")
    time.sleep(0.5)
    mylcd.lcd_display_string("Program End..")
    time.sleep(0.5)
    mylcd.lcd_display_string("Program End...")
    time.sleep(0.5)
    mylcd.lcd_clear()
 
