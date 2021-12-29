#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "../include/keygen.h"

void randomNumber(int up, int low);

void randomNumber(int up, int low) {
    int seed;
    int randomnum, finalValue;
        srand(time(NULL));
        randomnum = rand();
        finalValue = (randomnum % (up - low +1) ) + low;
    return finalValue;
}


void cdkey() {
    srand(time(0));
    int three = (rand() % (998 - 100 +1)) + 100;
    if(three == 333 || three == 444 || three == 555 || three == 666 || three == 777 || three == 888 || three == 999) {
        three = 635;
    }
    int seven[7];
    for(int i = 0; i <= 7; i++) {
        seven[i] = (rand() % (7 - 1 +1)) + 1;
    }

    while((seven[0] + seven[1] + seven[2] + seven[3] + seven[4] + seven[5] + seven[6]) % 7 !=  0) {
        for(int i = 0; i <= 5; i++) {
            
            seven[i] = (rand() % (9 - 1 +1)) + 1;
        }
        seven[6] = (rand() % (7 - 1 +1)) + 1;
    }


    printf("\nKey: %d-%d%d%d%d%d%d%d\n", three, seven[0], seven[1], seven[2], seven[3], seven[4], seven[5], seven[6]);
}