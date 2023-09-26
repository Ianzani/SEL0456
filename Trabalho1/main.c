/*
Author: Ian Zaniolo Sirbone
Title: SEL0456 Project 1
*/

#include <stdio.h>
#include <math.h>
#include <stdlib.h>

double *sqrt2(double *x, int size){

    double *v = (double *) malloc(size * sizeof(double));
    
    int i;
    for (i=0; i<size; i++){
        v[i] = sqrt(x[i]);
    }

    return v;
}

double *pow2(double *x, int size){

    double *v = (double *) malloc(size * sizeof(double));
    
    int i;
    for (i=0; i<size; i++){
        v[i] = pow(x[i], 2);
    }

    return v;
}

double *div2(double *x, int size){

    double *v = (double *) malloc(size * sizeof(double));
    
    int i;
    for (i=0; i<size; i++){
        v[i] = x[i]/2;
    }

    return v;
}

int main(void){

    double array[] = {2, 4, 6, 8, 10};
    int size = sizeof(array)/sizeof(double);

    double *v1, *v2, *v3;
    v1 = div2(array, size);
    v2 = pow2(array, size);
    v3 = sqrt2(array, size);

    int i;
    for (i=0; i<size; i++){
        printf("Divisão de %.2f por 2: %.2f\n", array[i], v1[i]);
        printf("%.2f elevado à 2: %.2f\n", array[i], v2[i]);
        printf("Raiz de %.2f: %.2f\n", array[i], v3[i]);
        printf("\n");
    }

    free(v1);
    free(v2);
    free(v3);

    return 0;
}