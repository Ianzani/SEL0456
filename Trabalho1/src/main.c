/*
Author: Ian Zaniolo Sirbone
Title: SEL0456 Project 1
*/

#include <stdio.h>
#include <math.h>
#include "pow2.h"
#include "sqrt2.h"
#include "div2.h"

// void sqrt2(double x){
//     printf("Raiz de %.2f: %.2f\n", x, sqrt(x));
// }

// void pow2(double x){
//     printf("%.2f elevado à 2: %.2f\n", x, pow(x, 2));
// }

// void div2(double x){
//     printf("%.2f dividido por 2: %.2f\n", x, x/2);
// }

int main(void){

    double array[] = {2, 4, 6, 8, 10};

    int i;
    for (i=0; i<sizeof(array)/sizeof(double); i++){
        sqrt2(array[i]);
        pow2(array[i]);
        div2(array[i]);
        printf("\n");
    }

    return 0;
}