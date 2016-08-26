/* motor_test5.c */
//PWM 사용해서 속도 제어
#include <stdio.h>
#include <stdlib.h>
#include <wiringPi.h>
#include <signal.h>
#include <time.h>
#include <string.h>

#define MOTOR     1 // GPIO 18
#define DIRECTION 3 // GPIO 22
#define SEC       2
void INThandler(int);
void init();

// Main Function
int main() {
    time_t timer;

    unsigned char strFormat[7];

    printf("motor_test5\n");

    wiringPiSetup();
    signal(SIGINT, INThandler);

    pinMode(MOTOR,     PWM_OUTPUT);
    pinMode(DIRECTION, OUTPUT);
    
    pullUpDnControl (MOTOR, PUD_DOWN) ;
    pullUpDnControl (DIRECTION, PUD_DOWN) ;
    
    
    while(1) {
        time(&timer);
        strftime(strFormat, 7, "%I%M%S", localtime(&timer));
        //SEC 초마다 실행
        if( (strFormat[5]-48) % SEC == 0) {
            printf("Current TIME(HH/MM/SS) : %s\n", strFormat);
            
            digitalWrite(DIRECTION, HIGH);
            pwmWrite(MOTOR, 150);
            //digitalWrite(MOTOR,     HIGH);
            delay(180);       
            
            digitalWrite(DIRECTION, LOW);
            pwmWrite(MOTOR, 150);
            //digitalWrite(MOTOR,     HIGH);
            delay(105);
            pwmWrite(MOTOR, 0);
            //digitalWrite(MOTOR,     LOW);
            delay(1000);     
            
         }
    }
 
}

void INThandler(int sig)
{
    printf("\ngoodbye\n");
    init();
    exit(0);
}

void init() {
    pwmWrite(MOTOR, 0);
    digitalWrite(DIRECTION, LOW);
}

