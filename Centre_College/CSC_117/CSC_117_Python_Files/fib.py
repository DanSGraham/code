#
#Fibonacci Sequence
#
#Author: Daniel Graham
#

def main():
    n=input("Which number of the Fibonacci Sequence do you want to compute? ")
    firstNum=1
    secondNum=1
    #n-2 because first two are given as variables already
    for i in range (n-2):
        cNum=firstNum+secondNum
        firstNum=secondNum
        secondNum=cNum

    print "The value is", cNum

main()
