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
    GPIO.setFunction(jong_pwm_pin, GPIO.OUT)
    GPIO.setFunction(jong_dir_pin, GPIO.OUT)
    GPIO.output(jong_dir_pin, GPIO.LOW)
    GPIO.output(jong_pwm_pin, GPIO.LOW)    

    GPIO.setFunction(book_pwm_pin, GPIO.OUT)
    GPIO.setFunction(book_dir_pin, GPIO.OUT)
    GPIO.output(book_dir_pin, GPIO.LOW)
    GPIO.output(book_pwm_pin, GPIO.LOW)   
        
    GPIO.setFunction(jing_pwm_pin, GPIO.OUT)
    GPIO.setFunction(jing_dir_pin, GPIO.OUT)
    GPIO.output(jing_dir_pin, GPIO.LOW)
    GPIO.output(jing_pwm_pin, GPIO.LOW)
    
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
    GPIO.output(jong_pwm_pin, GPIO.HIGH)
    webiopi.sleep(0.065)
    GPIO.output(jong_pwm_pin, GPIO.LOW)
    
    webiopi.sleep(0.5)
    
    GPIO.output(jong_dir_pin, GPIO.HIGH)
    GPIO.output(jong_pwm_pin, GPIO.HIGH)
    webiopi.sleep(0.06)
    GPIO.output(jong_pwm_pin, GPIO.LOW)

    
@webiopi.macro
def book_strike():
    GPIO.output(book_dir_pin, GPIO.LOW)
    GPIO.output(book_pwm_pin, GPIO.HIGH)
    webiopi.sleep(0.091)
    GPIO.output(book_pwm_pin, GPIO.LOW)
    
    webiopi.sleep(0.5)
    
    GPIO.output(book_dir_pin, GPIO.HIGH)
    GPIO.output(book_pwm_pin, GPIO.HIGH)
    webiopi.sleep(0.075)
    GPIO.output(book_pwm_pin, GPIO.LOW)
    
    
            
@webiopi.macro
def jing_strike():
    GPIO.output(jing_dir_pin, GPIO.LOW)
    GPIO.output(jing_pwm_pin, GPIO.HIGH)
    webiopi.sleep(0.091)
    GPIO.output(jing_pwm_pin, GPIO.LOW)
    
    webiopi.sleep(0.5)
    
    GPIO.output(jing_dir_pin, GPIO.HIGH)
    GPIO.output(jing_pwm_pin, GPIO.HIGH)
    webiopi.sleep(0.085)
    GPIO.output(jing_pwm_pin, GPIO.LOW)
    
   
       
    
