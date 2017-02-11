
/*
This function takes an integer value between 0-15 (inclusive)
and returns a character representation of that number in Hex.
If the input is not within the legal range, return a space character.

for instance, for the input 10, this function should return 'A'
 */
char intToChar(int val);


/*
This function takes a character that represents a Hex digit (A-F are all in caps)
and returns the integer that corresponds to that digit.  If the input is
not in within the legal range, return -1.


For instance, with an input of 'A', this function should return 10.

*/

int charToInt(char val);


/*
Write a function that will take three parameters, an int,num, to
indicate the starting number, an int,base, to indicate what base to
convert the num to, and a character array to store the num in the
provided base.  This function does not return anything.   When calling
the function, you should ensure that the character array can hold 100 characters.
Inside of your function make sure that the last character is set to
'\0' to allow you to print or compare the string.   (You may assume
that you do not have to translate any base higher than 16) 

Notes:
    previously designed functions will help you here....

    On page 38, the authors provide a technique on converting a number
    from base 10 to base 16 (hexadecimal).    Remember that you can
    find the quotient using integer division and a the remainder by
    using the modulus operation.  How could you alter this algorithm
    to work with any base?
*/
void base10ToBaseAny(int num,int base, char output[]);

/*
Create a function that will take 3 parameters, an int, to indicate
what base the number is in, a character array, num,  representing a
number in the given base, and an int, len, representing the length of
the string.  The function will return an int representing the number
given in base 10. (You may assume that you do not have to translate
anybase higher than 16)

Note:

   Keep reading on page 38 for hints on this algorithm.
*/

int baseAnyToBase10(int base,char num[], int len);


/*
Create a function that will convert a number (represented with a
string) of one base to another number string in another base.
(You may assume that you do not have to translate any base higher than
16.)

Note: An algebraically clever person could derive a formula to convert a
number in one base to another.  If you can, by all means provide it.
However, a lazy computer scientist might reuse other functions
*/
void baseAnyToBaseAny(int inputBase, char inputNum[],int inputLen,
		      int outPutBase,char outputNum[]); 



