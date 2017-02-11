#include <stdio.h>

int fcn2(int x, int y){
    int step1 = x + y;
    return step1;
}

int fcn1(int a, int b, int c, int d, int e, int f){
    int step1 = fcn2(a,b);
    int step2 = fcn2(c, b);
    int step3 = f + e;

    int step4 = step1 + step3;
    int step5 = step4 * step2;
    int step6 = step1 + step5;
    int step7 = step6 - d;
    return step7;
}

int main( int argc, const char* argv[] ) {
    return fcn1(2, 7, 10, 3, 1, 5);
}
