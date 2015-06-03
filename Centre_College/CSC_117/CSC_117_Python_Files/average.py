#
#Summing given numbers and giving an average program
#
#Author:Daniel Graham

def main():

    n=input("How many numbers do you wish to sum? ")
    accum=0
    for i in range(n):
        numSum=input ("What number would you like to add? ")
        accum=accum+numSum

    print
    print "The total is", accum
    avg= float(accum)/n
    print
    print "The average is", avg

main ()
