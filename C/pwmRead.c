#include <stdio.h>
#include <wiringPi.h>

#define PWM_IN 18
#define BUTTON 6

void main () {
    wiringPiSetupGpio (void);
    pinMode (PWM_IN, INPUT);
    pinMode (BUTTON, INPUT);

    while(true){
        if(digitalRead(BUTTON == 1))
            printf("button is pressed\n");
        else
            printf("button is not pressed\n");
    }
}
