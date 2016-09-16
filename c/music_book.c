#include <stdio.h>
#include <wiringPi.h>
#define BOOK_PIN 16

int main(void)
{
   
    if (wiringPiSetupGpio() == -1) {
        return 1;
    }

    pinMode(BOOK_PIN, OUTPUT);
    digitalWrite(BOOK_PIN, LOW);
    
    while(1) {
        if (digitalRead (BOOK_PIN) == HIGH) {
            printf("Book, strike!!\n");
            system("omxplayer book.mp3");
        }
        usleep(1000);
    }
    return 0; 
}


