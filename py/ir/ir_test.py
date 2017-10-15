#ir_test.py

import RPi.GPIO as GPIO
import lirc
import time

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

socketid = lirc.init("irtest", blocking=False)
print "ir_test started"
try:
    while(True):
        
        codeIR = lirc.nextcode()
        
        if len(codeIR) != 0 :
            print codeIR
            
            if codeIR[0] == KEY_UP:
                print "KEY_UP pressed"
            elif codeIR[0] == KEY_DOWN:
                print "KEY_DOWN pressed"
            elif codeIR[0] == KEY_RIGHT:
                print "KEY_RIGHT pressed"
            elif codeIR[0] == KEY_LEFT:
                print "KEY_LEFT pressed"
            elif codeIR[0] == KEY_UP_LEFT:
                print "KEY_UP_LEFT pressed"
            elif codeIR[0] == KEY_UP_RIGHT:
                print "KEY_UP_RIGHT pressed"
            elif codeIR[0] == KEY_DOWN_LEFT:
                print "KEY_DOWN_LEFT pressed"
            elif codeIR[0] == KEY_DOWN_RIGHT:
                print "KEY_DOWN_RIGHT pressed"
            elif codeIR[0] == KEY_F1:
                print "KEY_F1 pressed"
            elif codeIR[0] == KEY_F2:
                print "KEY_F2 pressed"
            elif codeIR[0] == KEY_F3:
                print "KEY_F3 pressed"
            elif codeIR[0] == KEY_F4:
                print "KEY_F4 pressed"
            elif codeIR[0] == KEY_F5:
                print "KEY_F5 pressed"
            elif codeIR[0] == KEY_F6:
                print "KEY_F6 pressed"
        
except KeyboardInterrupt:
    lirc.deinit()
