#ht_lcd_control.py
# -*- coding:utf-8 -*-
import os
import time
import Adafruit_DHT
import I2C_LCD_driver
mylcd = I2C_LCD_driver.lcd()
ON_OFF_POINT = 50
movement_control_file = '/home/pi/py/turtle/files/move.conf'
humid_control_file    = '/home/pi/py/turtle/files/humid.conf'

# Set the umidty array the size 10
humArr = [100,100,100,100,100,100,100,100,100,100]
#print(humArr)
print ("Program Start")
mylcd.lcd_display_string("Program Start..")
 
# Calculate the average except MIN/MAX.
def avgval(humArr):  
    tempHum = 0.0 
    for i in humArr:
        tempHum += i  
    return (tempHum-max(humArr)-min(humArr))/(len(humArr)-2)  
 
 
#Save the origin humidity in all array values
humidity, temperature = Adafruit_DHT.read_retry(11, 27)  # GPIO27 (BCM notation)
mylcd.lcd_display_string("Program Start...")
 
#Sensing again when humidity is over 100 in case of sensing error
if humidity > 100 :
    humidity, temperature = Adafruit_DHT.read_retry(11, 27)  # GPIO27 (BCM notation)
for x in range(len(humArr)-1, -1, -1) :
    humArr[x] = humidity

try:
    while True:
        humidity, temperature = Adafruit_DHT.read_retry(11, 27)  # GPIO27 (BCM notation)
        for x in range(len(humArr)-1, -1, -1) :
            if (x > 0) :
                humArr[x] = humArr[x-1]
            elif (x == 0) :
                humArr[x] = humidity
        avgHum = round(avgval(humArr), 1)
        print ("Humidity = {} %; Temperature = {} C".format(avgHum, temperature))
        mylcd.lcd_display_string(u"{} %; {} C  ".format(avgHum, temperature), 1)
        
        try:
            fin = open(movement_control_file, 'r')
            move_flag = fin.read()
            fin.close()
        
        except IOError:
            print("file read error")

        mode = ""
        if (move_flag[0:9] == "MOVE_AUTO") :
            mode = "Auto)"
        else :
            mode = "Manual)"

        #When auto mode, If the humidity is under the ON_OFF_POINT, turn off the himidifier
        if (move_flag[0:9] == "MOVE_AUTO") :
            if (avgHum > ON_OFF_POINT) :
                mylcd.lcd_display_string(mode + "Humid Off  ", 2)
                os.system("sudo /home/pi/py/hub-ctrl -h 0 -P 2 -p 0")
            else :
                mylcd.lcd_display_string(mode + "Humid On   ", 2)
                os.system("sudo /home/pi/py/hub-ctrl -h 0 -P 2 -p 1")

        #Whdn manual mode, judge reading humid.conf file
        else :
            try:
                fin = open(humid_control_file, 'r')
                humid_flag = fin.read()
                fin.close()
            
            except IOError:
                print("file read error")
            if (humid_flag[0:9] == "HUMID_OFF") :
                mylcd.lcd_display_string(mode + "Humid Off  ", 2)
                os.system("sudo /home/pi/py/hub-ctrl -h 0 -P 2 -p 0")
            else :
                mylcd.lcd_display_string(mode + "Humid On   ", 2)
                os.system("sudo /home/pi/py/hub-ctrl -h 0 -P 2 -p 1")
        
        time.sleep(1)
 
#USB ON, LCD Initialize when exit
except:
    os.system("sudo /home/pi/py/hub-ctrl -h 0 -P 2 -p 1")
    mylcd.lcd_clear()
    print("Program End")
    mylcd.lcd_display_string("Program End")
    time.sleep(0.2)
    mylcd.lcd_display_string("Program End.")
    time.sleep(0.2)
    mylcd.lcd_display_string("Program End..")
    time.sleep(0.2)
    mylcd.lcd_display_string("Program End...")
    time.sleep(0.2)
    mylcd.lcd_clear()
