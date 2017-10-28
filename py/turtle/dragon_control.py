#dragon_control.py
# -*- coding:utf-8 -*-
import os
import time

dragon_control_file = '/home/pi/py/turtle/files/dragon.conf'

try:
    while True:

        #play dragon when dragon_flag is on
        try:
            fin = open(dragon_control_file, 'r')
            dragon_flag = fin.read()
            fin.close()
        
        except IOError:
            print("file read error")

        if (dragon_flag[0:9] == "DRAGON_ON") :
            os.system("aplay /home/pi/py/music/dragon.wav")

            try:
                fout = open(dragon_control_file, 'w')
                fout.write("DRAGON_OFF\n")
                fout.close()

                print("DRAGON ON->OFF")
            except IOError:
                print("Cannot find file: " + dragon_control_file)
        time.sleep(0.1)
 
#End
except:
    print("Program End")
