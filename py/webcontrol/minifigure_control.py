#minifigure_control.py
import webiopi

webiopi.setDebug()

GPIO = webiopi.GPIO

jong_pwm_pin = 13
jong_dir_pin = 19
book_pwm_pin = 16
book_dir_pin = 12   
jing_pwm_pin =  5
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
    GPIO.output(jong_pwm_pin, GPIO.LOW)
    GPIO.output(jong_dir_pin, GPIO.LOW)    
    
    GPIO.output(book_pwm_pin, GPIO.LOW)
    GPIO.output(book_dir_pin, GPIO.LOW) 
    
    GPIO.output(jing_pwm_pin, GPIO.LOW)
    GPIO.output(jing_dir_pin, GPIO.LOW)


@webiopi.macro
def jong_strike():
    GPIO.output(jong_dir_pin, GPIO.LOW)
    GPIO.pulseRatio(jong_pwm_pin, 0.2);
    webiopi.sleep(0.6)
    GPIO.pulseRatio(jong_pwm_pin, 0.65);
    webiopi.sleep(0.3)
    GPIO.pulseRatio(jong_pwm_pin, 0);
    
    webiopi.sleep(0.5)
    
    GPIO.output(jong_dir_pin, GPIO.HIGH)
    GPIO.pulseRatio(jong_pwm_pin, 0.54);
    webiopi.sleep(0.4)
    GPIO.pulseRatio(jong_pwm_pin, 0);

    
@webiopi.macro 
def book_strike():
    GPIO.output(book_dir_pin, GPIO.LOW)
    GPIO.pulseRatio(book_pwm_pin, 0.1);
    webiopi.sleep(0.6)
    GPIO.pulseRatio(book_pwm_pin, 0.75);
    webiopi.sleep(0.3)
    GPIO.pulseRatio(book_pwm_pin, 0);
    
    webiopi.sleep(0.5)
    
    GPIO.output(book_dir_pin, GPIO.HIGH)
    GPIO.pulseRatio(book_pwm_pin, 0.60);
    webiopi.sleep(0.3)
    GPIO.pulseRatio(book_pwm_pin, 0);
    
    
            
@webiopi.macro
def jing_strike():
    GPIO.output(jing_dir_pin, GPIO.LOW)
    GPIO.pulseRatio(jing_pwm_pin, 0.2);
    webiopi.sleep(0.7)
    GPIO.pulseRatio(jing_pwm_pin, 0.50);
    webiopi.sleep(0.2)
    GPIO.pulseRatio(jing_pwm_pin, 0);
    
    webiopi.sleep(0.5)
    
    GPIO.output(jing_dir_pin, GPIO.HIGH)
    GPIO.pulseRatio(jing_pwm_pin, 0.48);
    webiopi.sleep(0.2)
    GPIO.pulseRatio(jing_pwm_pin, 0);
    
   
       
    
