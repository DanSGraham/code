#
#Summing given numbers program
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

main ()
