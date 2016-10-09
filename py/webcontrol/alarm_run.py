import webiopi
import time
from time import sleep

import sys
sys.path.append('/home/pi/py/webcontrol')
import minifigure_control

webiopi.setDebug()

@webiopi.macro
def runAlarm():
    alarm_time_file = '/home/pi/py/webcontrol/files/alarm_time.txt'
    try:
        fin_time = open(alarm_time_file, 'r')
        alarm_time = fin_time.read()
        fin_time.close()     
    except IOError:
        webiopi.debug("Cannot find file: " + alarm_time_file)
        webiopi.debug("file read error")   
        
    alarm_flag_file = '/home/pi/py/webcontrol/files/alarm_flag.txt'
    try:
        fin_flag = open(alarm_flag_file, 'r')
        alarm_flag = fin_flag.read()
        fin_flag.close()
    except IOError:
        webiopi.debug("Cannot find file: " + alarm_flag_file)
        webiopi.debug("file read error")  
    
    fmt = "%I:%M:%S"
    t = time.localtime()
    current_time = time.strftime(fmt, t)
    
    if(current_time[0:5] == alarm_time[0:5] and alarm_flag[0:8] == "ALARM_ON"):
        webiopi.debug("Alarm Start!!! " + alarm_time_file[0:5])
        minifigure_control.jong_strike()
        minifigure_control.book_strike()
        minifigure_control.jing_strike()
        sleep(1)
    sleep(0.1)
    
