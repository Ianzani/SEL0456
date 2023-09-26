/*
Author: Ian Zaniolo Sirbone
Title: SEL0456 Project 1
*/

#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include "sqrt2.h"

double *sqrt2(double *x, int size){

    double *v = (double *) malloc(size * sizeof(double));
    
    int i;
    for (i=0; i<size; i++){
        v[i] = sqrt(x[i]);
    }

    return v;
}