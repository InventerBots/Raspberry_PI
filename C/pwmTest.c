#include <stdio.h>
#include <wiringPi.h>

#define PWM_IN 18
#define BUTTON 6

int main () {
    wiringPiSetupGpio ();
    pinMode (PWM_IN, INPUT);
    pinMode (BUTTON, INPUT);

    while(1){
        if(digitalRead(BUTTON == 0)){
            putchar('\f');
            printf("button is pressed\n");
        }
        else {
            putchar('\f');
            printf("button is not pressed\n");
        }
    }
}
