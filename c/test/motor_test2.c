/* motor_test2.c */
//PWM 함수로 테스트
#include <wiringPi.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

#define LED1 18 // GPIO 18

int main (void)
{
	int bright ;

	//printf ("Raspberry Pi wiringPi PWM test program\n") ;
    if (wiringPiSetupGpio() == -1) {
        return 1;
    }

	pinMode (LED1, PWM_OUTPUT) ;

	for (;;)
    {
        pwmWrite (LED1, 0) ;
        delay(500);
        
        pwmWrite (LED1, 1024) ;
        delay(500);
    }

	return 0 ;
}
