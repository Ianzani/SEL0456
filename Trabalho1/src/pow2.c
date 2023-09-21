/*
Author: Ian Zaniolo Sirbone
Title: SEL0456 Project 1
*/

#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include "pow2.h"

double *pow2(double *x, int size){

    double *v = (double *) malloc(size * sizeof(double));
    
    int i;
    for (i=0; i<size; i++){
        v[i] = pow(x[i], 2);
    }

    return v;
}