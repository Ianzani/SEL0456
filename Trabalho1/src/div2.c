/*
Author: Ian Zaniolo Sirbone
Title: SEL0456 Project 1
*/

#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include "div2.h"

double *div2(double *x, int size){

    double *v = (double *) malloc(size * sizeof(double));
    
    int i;
    for (i=0; i<size; i++){
        v[i] = x[i]/2;
    }

    return v;
}