#include <stdio.h>

int fcn4(int x){
    if(x < 0){
        return 0;
    }
    else{
        int rtnVal = 0;
        int sumVal = 0;
        do{
            rtnVal = rtnVal + sumVal;
            sumVal = sumVal + 1;
        }
        while(sumVal <= x);
        return rtnVal;
    }
}

int main( int argc, const char* argv[] ){
    return fcn4(10);
}
