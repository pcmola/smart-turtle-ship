#cannon_control.py
# -*- coding:utf-8 -*-
import os
import time

cannon_control_file = '/home/pi/py/turtle/files/cannon.conf'

try:
    while True:

        #play cannon when cannon_flag is on
        try:
            fin = open(cannon_control_file, 'r')
            cannon_flag = fin.read()
            fin.close()
        
        except IOError:
            print("file read error")

        if (cannon_flag[0:9] == "CANNON_ON") :
            os.system("sudo /home/pi/py/hub-ctrl -h 0 -P 2 -p 0")
            time.sleep(1)
            os.system("sudo /home/pi/py/hub-ctrl -h 0 -P 2 -p 1")
            os.system("aplay /home/pi/py/music/cannon.wav")
            try:
                fout = open(cannon_control_file, 'w')
                fout.write("CANNON_OFF\n")
                fout.close()

                print("CANNON ON->OFF")
            except IOError:
                print("Cannot find file: " + cannon_control_file)
        time.sleep(0.1)
 
#End
except:
    print("Program End")
