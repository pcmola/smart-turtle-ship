#include <stdio.h>
#include <wiringPi.h>
#define JONG_PIN 13

int main(void)
{
   
    if (wiringPiSetupGpio() == -1) {
        return 1;
    }

    pinMode(JONG_PIN, OUTPUT);
    digitalWrite(JONG_PIN, LOW);
    
    while(1) {
        if (digitalRead (JONG_PIN) == HIGH) {
            printf("Jong, strike!!\n");
            system("omxplayer jong.mp3");
        }
        usleep(1000);
    }
    return 0; 
}


