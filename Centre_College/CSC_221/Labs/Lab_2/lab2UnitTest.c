#include "assert.h"
#include "dan_lab2.c"

int squareSumTest(){
    assert(squares(1) == 1);
    assert(squares(2) == 5);
    assert(squares(10) == 385);
    printf("squares test pass :)\n");
    return 0;
}
int maxIndexTest(){
    int testArray1Len = 11;
    int testArray2Len = 0;
    int testArray3Len = 30;

    int testArray1[11] = {-1, 0, -4, 5, 32, 4, 1, -1, 0, 0, 50};
    int testArray2[0] = {};
    int testArray3[30] = {0, 1, 2, 3, 4, 5, 6, 7, 28, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 32, 22, 23,24,25, 26, 27, 28, 31};

    assert(maxIndex(testArray1, testArray1Len) == 10);
    assert(maxIndex(testArray2, testArray2Len) == -1);
    assert(maxIndex(testArray3, testArray3Len) == 21);
    printf("maxIndex test pass :)\n");
    return 0;
}
int seekTest(){

    int testArray1Len = 11;
    int testArray2Len = 0;
    int testArray3Len = 5;

    int testArray1[11] = {-1, -1, 0, 0, 4, 5, 6, 7, 0, -1, 4};
    int testArray2[0] = {};
    int testArray3[5] = {10, 10, 10, 10, 10};

    assert(seek(testArray1, testArray1Len, 0) == 1);
    assert(seek(testArray1, testArray1Len, -1) == 1);
    assert(seek(testArray1, testArray1Len, 4) == 1);
    assert(seek(testArray1, testArray1Len, -5) == 0);
    assert(seek(testArray2, testArray2Len, 4) == 0);
    assert(seek(testArray3, testArray3Len, 10) == 1);
    assert(seek(testArray3, testArray3Len, 3) == 0);

    printf("seek test pass :)\n");
    return 0;
}

int fibTest(){

    //assert(fib(0) == 0);
    assert(fib(1) == 1);
    assert(fib(2) == 1);
    assert(fib(3) == 2);
    assert(fib(4) == 3);
    assert(fib(7) == 13);
    assert(fib(20) == 6765);
    printf("fib test pass :)\n");
    return 0;
}

int main(){
    squareSumTest();
    maxIndexTest();
    seekTest();
    fibTest(); 

    printf("all tests pass :) \n");
    return 0;
}
