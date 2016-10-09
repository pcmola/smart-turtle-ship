import webiopi

webiopi.setDebug()

@webiopi.macro
def getAlarmTime():

    alarm_time_file = '/home/pi/py/webcontrol/files/alarm_time.txt'
    try:
        f = open(alarm_time_file, 'r')
        alarm_time = f.read()
        f.close()
        webiopi.debug(alarm_time_file + "read ok")    
    except IOError:
        print("Cannot find file: " + alarm_time_file)
        webiopi.debug("file write error")    
    return alarm_time

@webiopi.macro       
def setAlarmTime(alarm_time):
    webiopi.debug("Alarm is set to " + alarm_time)

    alarm_time_file = '/home/pi/py/webcontrol/files/alarm_time.txt'
    try:
        f = open(alarm_time_file, 'w')
        f.write(alarm_time + "\n")
        f.close()
        webiopi.debug("file write ok")    
    except IOError:
        print("Cannot find file: " + alarm_time_file)
        webiopi.debug("file write error")     
        
@webiopi.macro
def getAlarmFlag():
    alarm_flag_file = '/home/pi/py/webcontrol/files/alarm_flag.txt'
    try:
        fin_flag = open(alarm_flag_file, 'r')
        alarm_flag = fin_flag.read()
        fin_flag.close()
    except IOError:
        webiopi.debug("Cannot find file: " + alarm_flag_file)
        webiopi.debug("file read error")
        alarm_flag = alarm_flag_file + " doesn't exists"    
    return alarm_flag


@webiopi.macro
def setAlarmFlag(alarm_flag):
    webiopi.debug("Alarm Flag is set to " + alarm_flag)
    alarm_flag_file = '/home/pi/py/webcontrol/files/alarm_flag.txt'
    try:
        fin_flag = open(alarm_flag_file, 'w')
        fin_flag.write(alarm_flag + "\n")
        fin_flag.close()
        webiopi.debug("file write ok")    
    except IOError:
        webiopi.debug("Cannot find file: " + alarm_flag_file)
        webiopi.debug("file read error")
        alarm_flag = alarm_flag_file + " doesn't exists"    
    return alarm_flag
    
