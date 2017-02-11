#include <stdio.h>
#include <math.h>

	/*
	This function takes an integer value between 0-15 (inclusive)
and returns a character representation of that number in hex.
	If the input is not within the legal range, return a space character.
	*/

char intToChar(int val){
    char c;

    if(val < 0 || val > 15){
        c = ' '; 
    }
    else{
        int baseAscii = 48;
        int asciiOfCharacter = baseAscii + (val % 10) + ((val / 10) * 17);
        c = asciiOfCharacter;
    }
    return c;
}

int charToInt(char val){
    int numVal = (int) val;
    int convertVal = -1;
    if (!(numVal < 48 || (numVal > 57 && numVal < 65) || (numVal > 70))){
        convertVal = numVal % 48 - ((numVal / 65) * 7); 
    }
    return convertVal;
}

void base10ToBaseAny(int num, int base, char output[]){
    char outputtemp[100];
    outputtemp[0] = '\0';
    outputtemp[1] = '0';
    int startingNum = 1;
    int length = 2;
    while (num > 0){
        outputtemp[startingNum] = intToChar(num % base);
        num = num / base;
        startingNum += 1;
        length = startingNum;
    }
    
    /*Reverse array correctly. -D */
   for(int i = 0; i < length; i += 1){
        output[i] = outputtemp[length - i - 1];
    }
}

int baseAnyToBase10(int base, char num[], int len){
    int sumOfValues = 0;
    int currVal;
    for(int i = 0; i < len; i += 1){
        currVal = charToInt(num[i]);
        sumOfValues += (currVal * pow(base, (len - i - 1)));
    }
    return sumOfValues;
}


void baseAnyToBaseAny(int inputBase, char inputNum[], int inputLen,
                      int outputBase, char outputNum[]){
    int baseInTen = baseAnyToBase10(inputBase, inputNum, inputLen);
    base10ToBaseAny(baseInTen, outputBase, outputNum);
}
 
