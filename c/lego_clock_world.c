/* lego_clock_input.c */
#include <stdio.h>
#include <wiringPi.h>
#include <wiringShift.h>
#include <time.h>
#include <string.h>
#include <signal.h>
#include <stdlib.h>

// PIN 정보 : http://wiringpi.com/pins/ 참고
#define DS      PIN[0]  // BCM GPIO 17
#define SHCP    PIN[1]  // BCM GPIO 18
#define STCP    PIN[2]  // BCM GPIO 27

#define CITY1 3  // BCM GPIO 22
#define CITY2 4  // BCM GPIO 23
#define CITY3 5  // BCM GPIO 24


#define ON_OFF  6  // BCM GPIO 25

#define INTERVAL_GREEN  2000 // us
#define INTERVAL_COMMON  500 // us

#define SEOUL   0
#define NEWYORK 1
#define BEIJING 2
#define LONDON  3
#define PARIS   4
#define SYDNEY  5

#define OFFSET_SEOUL     0
#define OFFSET_NEWYORK  -1
#define OFFSET_BEIJING  -1
#define OFFSET_LONDON   -8 //런던은 3월 마지막 일요일~10월 마지막 일요일 써머타임
#define OFFSET_PARIS    -7
#define OFFSET_SYDNEY    1

unsigned char PIN[3] = {0, 1, 2} ;  // DS(Data), SHCP(CLK), STCP(Latch)

/*
74HC595 Q0 Q1 Q2 Q3 Q4 Q5 Q6 Q7 Q0 Q1 Q2 Q3 Q4 Q5 Q6 Q7 Q0 Q1 Q2 Q3 Q4 Q5 Q6  Q7
LED     H1 H2 M1 M2 CO          0  1  2  3  4  5  6  7  8  9  10 11 12    H1' CO'
*/

unsigned char common[5] = {
    0b01111111, // IC1 : 시간의 10의 자리
    0b10111111, // IC1 : 시간의  1의 자리
    0b11011111, // IC1 :   분의 10의 자리
    0b11101111, // IC1 :   분의  1의 자리
    0b11110111  // IC1 : 시간과 분 사이 콜론
    };

/*
  LED 별 배열 순서 :
  [ 0][ 1][ 2]
  [ 3]    [ 4]
  [ 5][ 6][ 7]
  [ 8]    [ 9]
  [10][11][12]
*/

/*
    '0' : 1111 1101 1111 1000
    '1' : 0010 1001 0100 1000
    '2' : 1110 1111 1011 1000
    '3' : 1110 1111 0111 1000
    '4' : 1011 1111 0100 1000
    '5' : 1111 0111 0111 1000
    '6' : 1111 0111 1111 1000
    '7' : 1111 1101 0100 1000
    '8' : 1111 1111 1111 1000
    '9' : 1111 1111 0111 1000
*/

unsigned char digit1[10] = {
    0b11111101, // IC2 : '0' 앞의 8자리
    0b00101001, // IC2 : '1' 앞의 8자리
    0b11101111, // IC2 : '2' 앞의 8자리
    0b11101111, // IC2 : '3' 앞의 8자리
    0b10111111, // IC2 : '4' 앞의 8자리
    0b11110111, // IC2 : '5' 앞의 8자리
    0b11110111, // IC2 : '6' 앞의 8자리
    0b11111101, // IC2 : '7' 앞의 8자리
    0b11111111, // IC2 : '8' 앞의 8자리
    0b11111111  // IC2 : '9' 앞의 8자리
    };
unsigned char digit2[10] = {
    0b11111000, // IC3 : '0' 뒤의 5자리
    0b01001000, // IC3 : '1' 뒤의 5자리
    0b10111000, // IC3 : '2' 뒤의 5자리
    0b01111000, // IC3 : '3' 뒤의 5자리
    0b01001000, // IC3 : '4' 뒤의 5자리
    0b01111000, // IC3 : '5' 뒤의 5자리
    0b11111000, // IC3 : '6' 뒤의 5자리
    0b01001000, // IC3 : '7' 뒤의 5자리
    0b11111000, // IC3 : '8' 뒤의 5자리
    0b01111000  // IC3 : '9' 뒤의 5자리
    };

unsigned char strFormat[7];
unsigned char digitNum;


//INPUT PIN에 따라 offset 세팅


void Latch();
void LED_out(unsigned char no);
void INThandler(int);
void init();


// Main Function
int main() {
    time_t timer;
    int i;
    int temp = 0;
    int hour_offset = 0;
    int city = SEOUL;
    int seoul_hour, city_hour;
    unsigned char strTimeTemp[7];
    char tmp_str[3];

    printf("lego_clock_world\n");

    wiringPiSetup();
    signal(SIGINT, INThandler);

    for(i=0; i<3; i++) {
        pinMode(PIN[i], OUTPUT);
        pullUpDnControl(PIN[i], PUD_DOWN);
    }

    pinMode(CITY1,  OUTPUT);
    pinMode(CITY2,  OUTPUT);
    pinMode(CITY3,  OUTPUT);
    pinMode(ON_OFF, OUTPUT);
    pullUpDnControl(CITY1,  PUD_DOWN);
    pullUpDnControl(CITY2,  PUD_DOWN);
    pullUpDnControl(CITY3,  PUD_DOWN);
    pullUpDnControl(ON_OFF, PUD_DOWN);
    
    digitalWrite(ON_OFF, 1);
    while(1) {
        if (digitalRead(ON_OFF) == HIGH) {

            time(&timer);

            //extract hour/minute/second
            strftime(strFormat, 7, "%I%M%S", localtime(&timer));

            /*
            PIN 세 개 ON/OFF에 따라 표시할 지역 결정
            000 : 서울
            001 : 뉴욕
            010 : 베이징
            011 : 런던
            100 : 파리
            101 : 시드니
            */
            city = digitalRead(CITY1) << 2 | digitalRead(CITY2) << 1 | digitalRead(CITY3);

            switch(city) {
                case SEOUL:
                hour_offset = OFFSET_SEOUL;
                break;

                case NEWYORK:
                hour_offset = OFFSET_NEWYORK;
                break;

                case BEIJING:
                hour_offset = OFFSET_BEIJING;
                break;

                case LONDON:
                hour_offset = OFFSET_LONDON;
                break;

                case PARIS:
                hour_offset = OFFSET_PARIS;
                break;
                
                case SYDNEY:
                hour_offset = OFFSET_SYDNEY;
                break;

            }

            seoul_hour = atoi(strFormat)/10000;
            if( (seoul_hour+hour_offset) > 12 ) {
                city_hour = seoul_hour+hour_offset-12;
            }
            else if( (seoul_hour+hour_offset) <= 12 && (seoul_hour+hour_offset) > 0 ) {
                city_hour = seoul_hour+hour_offset;
            }
            else if( (seoul_hour+hour_offset) <= 0 ) {
                city_hour = seoul_hour+hour_offset+12;
            }

            snprintf (tmp_str, sizeof(tmp_str), "%d", city_hour);
            if( city_hour >= 10 ) {
                strFormat[0] = tmp_str[0];
                strFormat[1] = tmp_str[1];
            }
            else {
                strFormat[0] = '0';
                strFormat[1] = tmp_str[0];
            }

            //printf("hour :%s\n", strFormat);
            //sleep(1);

            LED_out(0);
            if(strFormat[0] == '1') {
                usleep(INTERVAL_GREEN);
            }

            LED_out(1);
            usleep(INTERVAL_COMMON);

            LED_out(2);
            usleep(INTERVAL_COMMON);

            LED_out(3);
            usleep(INTERVAL_COMMON);

            LED_out(4);
            usleep(INTERVAL_GREEN);
        } else {
            init();
        }
    }
}

void Latch() {
    digitalWrite(STCP, HIGH) ;
    digitalWrite(STCP, LOW) ;
}

void LED_out(unsigned char no) {
    digitNum = strFormat[no] - 48;

    // 시간의 1자리, 분의 10자리, 분의 1자리
    if(no == 1 || no == 2 || no == 3) {

        shiftOut(DS, SHCP, LSBFIRST, digit2[digitNum]);
        shiftOut(DS, SHCP, LSBFIRST, digit1[digitNum]);
        shiftOut(DS, SHCP, LSBFIRST, common[no]);

        Latch();
    }

    // 시간의 10의 자리
    if(no == 0) {
        if(digitNum == 1) {
            shiftOut(DS, SHCP, LSBFIRST, 0b00000010);
        } else {
            shiftOut(DS, SHCP, LSBFIRST, 0b00000000);
        }
        shiftOut(DS, SHCP, LSBFIRST, 0b00000000);
        shiftOut(DS, SHCP, LSBFIRST, common[no]);
        Latch();
    }

    // Colon
    if(no == 4) {
        //if( strFormat[3] % 2 == 0) {  // [분:초] 테스트 시
        if( strFormat[5] % 2 == 0) {
            shiftOut(DS, SHCP, LSBFIRST, 0b00000001);
        } else {
            shiftOut(DS, SHCP, LSBFIRST, 0b00000000);
        }
        shiftOut(DS, SHCP, LSBFIRST, 0b00000000);
        shiftOut(DS, SHCP, LSBFIRST, common[no]);
        Latch();

    }
}

void INThandler(int sig)
{
    printf("\ngoodbye\n");
    init();
    exit(0);
}

void init() {
    int i;
    shiftOut(DS, SHCP, LSBFIRST, 0x00);  // digit2
    shiftOut(DS, SHCP, LSBFIRST, 0x00);  // digit1
    shiftOut(DS, SHCP, LSBFIRST, 0xFF);  // common
    Latch();
}

