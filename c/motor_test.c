/* motor_test.c */
#include <stdio.h>
#include <wiringPi.h>
#include <signal.h>
#include <stdlib.h>

#define MOTOR 1 // GPIO 18

void INThandler(int);
void init();

// Main Function
int main() {

    printf("motor_test\n");

    wiringPiSetup();
    signal(SIGINT, INThandler);

    pinMode(MOTOR, OUTPUT);
    
    while(1) {
        digitalWrite(MOTOR, HIGH);
        usleep(1000*500);
        digitalWrite(MOTOR, LOW);
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
}

