#
#Program Summing odd numbers
#author: D-Graham
#

oddNum=1

biggestOdd=input("What is the highest number you wish to sum to?")

n=(biggestOdd-1)/2

sumofOdd=0

for i in range (n+1):
    sumofOdd=sumofOdd+oddNum
    oddNum=oddNum+2
    

print sumofOdd
    
