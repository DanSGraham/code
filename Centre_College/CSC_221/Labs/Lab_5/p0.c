#include <stdio.h>

int fcn0(int x, int y){
    int step1 = x + (y * 2);
    int step2 = step1 + step1;
    return step2;
}

int main(int argc, const char* argv[] ) {
    int a = 2;
    int b = 3;
    return fcn0(a, b);
}
