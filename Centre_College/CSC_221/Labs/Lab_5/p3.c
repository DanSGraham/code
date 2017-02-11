#include <stdio.h>

int fcn3(int x){
    int rtnVal = 2;
    int xVal1 = x - 1;
    int xVal2 = x - 2;
    if(x > 2){
       int rtnVal1 = fcn3(xVal1);
       int rtnVal2 = fcn3(xVal2);
       rtnVal = rtnVal1 + rtnVal2;
    }        
    return rtnVal;
}

int main( int argc, const char* argv[]){
    return fcn3(10);
}
