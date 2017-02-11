#include "stdio.h"

int squares(int n){
    int total = 0; 
    for(int i = 1; i <= n; i = i + 1){
       total = total + (i * i);
    }
    return total; 
}

int maxIndex(int listMax[], int numItems){
    int currMax = 0;
    int currIndex = -1;
    if(numItems > 0){
         currMax = listMax[0];
         currIndex = 0;
         for(int i = 0; i < numItems; i = i + 1){
            if(currMax < listMax[i]){
                currMax = listMax[i];
                currIndex = i;
             }
         }
     }
     return currIndex;
}

int seek(int listTarget[], int numItems, int target){
    if(numItems > 0){
        for(int i = 0; i < numItems; i = i + 1){
            if(listTarget[i] == target){
                return 1;
            }
        }
    }
    return 0;
}

int fib(int n){
    int first = 1;
    int second = 1;
    int third = 1;
    for (int i = 0; i < (n - 2); i = i + 1){
        third = second + first;
        first = second;
        second = third;
    }
    return third;
}
