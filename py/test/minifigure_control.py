#minifigure_control.py
import webiopi

#import sys
#sys.path.append('/home/pi/py/python-omxplayer-wrapper-develop')
#sys.path.append('/usr/local/lib/python2.7/dist-packages/decorator-4.0.10-py2.7.egg')
#from omxplayer import OMXPlayer

webiopi.setDebug()

GPIO = webiopi.GPIO

jong_pwm_pin = 13
jong_dir_pin = 19
book_pwm_pin = 16
book_dir_pin = 12   
jing_pwm_pin = 11
jing_dir_pin =  6

def setup():
    webiopi.debug("Script with macros - Setup")
    GPIO.setFunction(jong_pwm_pin, GPIO.PWM)
    GPIO.setFunction(jong_dir_pin, GPIO.OUT)
    GPIO.pulseRatio(jong_pwm_pin, 0);
    GPIO.output(jong_dir_pin, GPIO.LOW)    

    GPIO.setFunction(book_pwm_pin, GPIO.PWM)
    GPIO.setFunction(book_dir_pin, GPIO.OUT)
    GPIO.pulseRatio(book_pwm_pin, 0);
    GPIO.output(book_dir_pin, GPIO.LOW)
        
    GPIO.setFunction(jing_pwm_pin, GPIO.PWM)
    GPIO.setFunction(jing_dir_pin, GPIO.OUT)
    GPIO.pulseRatio(jing_pwm_pin, 0)
    GPIO.output(jing_dir_pin, GPIO.LOW)
    
def loop():
    webiopi.sleep(1)

def destroy():
    webiopi.debug("Script with macros - Destroy")
    GPIO.pulseRatio(jong_pwm_pin, 0);
    GPIO.output(jong_dir_pin, GPIO.LOW)    
    
    GPIO.pulseRatio(book_pwm_pin, 0);
    GPIO.output(book_dir_pin, GPIO.LOW) 
    
    GPIO.pulseRatio(jing_pwm_pin, 0)
    GPIO.output(jing_dir_pin, GPIO.LOW)


@webiopi.macro
def jong_strike():
    webiopi.debug("Jong Strike!!!")
    GPIO.output(jong_dir_pin, GPIO.LOW)
    GPIO.pulseRatio(jong_pwm_pin, 0.2);
    webiopi.sleep(0.45)
    GPIO.pulseRatio(jong_pwm_pin, 0.50);
    webiopi.sleep(0.2)
    GPIO.pulseRatio(jong_pwm_pin, 0);
    
    webiopi.sleep(0.5)
    
    GPIO.output(jong_dir_pin, GPIO.HIGH)
    GPIO.pulseRatio(jong_pwm_pin, 0.45);
    webiopi.sleep(0.2)
    GPIO.pulseRatio(jong_pwm_pin, 0);

    
@webiopi.macro 
def book_strike():
    webiopi.debug("Book Strike!!!")
    GPIO.output(book_dir_pin, GPIO.LOW)
    GPIO.pulseRatio(book_pwm_pin, 0.2);
    webiopi.sleep(0.45)
    GPIO.pulseRatio(book_pwm_pin, 0.63);
    webiopi.sleep(0.2)
    GPIO.pulseRatio(book_pwm_pin, 0);
    
    webiopi.sleep(0.5)
    
    GPIO.output(book_dir_pin, GPIO.HIGH)
    GPIO.pulseRatio(book_pwm_pin, 0.61);
    webiopi.sleep(0.2)
    GPIO.pulseRatio(book_pwm_pin, 0);
    
    
            
@webiopi.macro
def jing_strike():
    webiopi.debug("Jing Strike!!!")
    GPIO.output(jing_dir_pin, GPIO.LOW)
    GPIO.pulseRatio(jing_pwm_pin, 0.2);
    webiopi.sleep(0.45)
    GPIO.pulseRatio(jing_pwm_pin, 0.50);
    webiopi.sleep(0.18)
    GPIO.pulseRatio(jing_pwm_pin, 0);
    
    webiopi.sleep(0.5)
    
    GPIO.output(jing_dir_pin, GPIO.HIGH)
    GPIO.pulseRatio(jing_pwm_pin, 0.45);
    webiopi.sleep(0.18)
    GPIO.pulseRatio(jing_pwm_pin, 0);
      
    
