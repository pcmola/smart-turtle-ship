#ht_lcd_control.py
# -*- coding:utf-8 -*-
import os
import time
import Adafruit_DHT
import I2C_LCD_driver
mylcd = I2C_LCD_driver.lcd()
ON_OFF_POINT = 50
movement_control_file = '/home/pi/py/turtle/files/move.conf'
humid_control_file = '/home/pi/py/turtle/files/humid.conf'

# 최초에 10개로 배열 크기 지정
humArr = [100,100,100,100,100,100,100,100,100,100]
#print(humArr)
print ("Program Start")
mylcd.lcd_display_string("Program Start..")
 
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
 
        #습도가 기준치 이하이고 상태가 AUTO면 가습기 OFF
        try:
            fin = open(movement_control_file, 'r')
            move_flag = fin.read()
            fin.close()
        
        except IOError:
            print("file read error")

        mode = ""
        if (move_flag[0:9] == "MOVE_AUTO") :
            mode = "(Auto)"
        else :
            mode = "(Manual)"

        #auto일 때에만, 습도가 기준치 이상일 때 USB(가습기/LED) OFF
        if (move_flag[0:9] == "MOVE_AUTO") :
            if (avgHum > ON_OFF_POINT) :
                mylcd.lcd_display_string(mode + "HumidOff  ", 2)
                os.system("sudo /home/pi/py/hub-ctrl -h 0 -P 2 -p 0")
            else :
                mylcd.lcd_display_string(mode + "HumidOn   ", 2)
                os.system("sudo /home/pi/py/hub-ctrl -h 0 -P 2 -p 1")

        #manual일 때에는 humid.conf 파일 읽어서 판단
        else :
            try:
                fin = open(humid_control_file, 'r')
                humid_flag = fin.read()
                fin.close()
            
            except IOError:
                print("file read error")
            print humid_flag
            if (humid_flag[0:9] == "HUMID_OFF") :
                mylcd.lcd_display_string(mode + "HumidOff  ", 2)
                os.system("sudo /home/pi/py/hub-ctrl -h 0 -P 2 -p 0")
            else :
                mylcd.lcd_display_string(mode + "HumidOn   ", 2)
                os.system("sudo /home/pi/py/hub-ctrl -h 0 -P 2 -p 1")
        
        time.sleep(1)
 
#종료시 USB ON, LCD 초기화
except:
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
 

