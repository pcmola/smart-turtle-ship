/* motor_test3.c */
//역방향 회전 추가
#include <stdio.h>
#include <stdlib.h>
#include <wiringPi.h>
#include <signal.h>

#define MOTOR     1 // GPIO 18
#define DIRECTION 3 // GPIO 22

void INThandler(int);
void init();

// Main Function
int main() {

    printf("motor_test3\n");

    wiringPiSetup();
    signal(SIGINT, INThandler);

    pinMode(MOTOR,     OUTPUT);
    pinMode(DIRECTION, OUTPUT);
    
    pullUpDnControl (MOTOR, PUD_DOWN) ;
    pullUpDnControl (DIRECTION, PUD_DOWN) ;
    
    while(1) {
        digitalWrite(DIRECTION, HIGH);
        digitalWrite(MOTOR,     HIGH);
        usleep(1000*500);
        digitalWrite(MOTOR,     LOW);
        usleep(1000*500);     
        
        digitalWrite(DIRECTION, LOW);
        digitalWrite(MOTOR,     HIGH);
        usleep(1000*500);
        digitalWrite(MOTOR,     LOW);
        usleep(1000*500);     
         
    }
}

void INThandler(int sig)
{
    printf("\ngoodbye\n");
    init();
    exit(0);
}

void init() {
    digitalWrite(MOTOR, LOW);
    digitalWrite(DIRECTION, LOW);
}

