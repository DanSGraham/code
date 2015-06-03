#
#A program to ask who let the dogs out
#Author: Daniel Graham
#


def whoLetTheDogsOut():
    import time
    dogs_out=raw_input("Who let the dogs out? ") #Srsly tho who did!?
    if dogs_out == "Baha Men" :
        print "That's right DAWG"
    else:
        for j in range (1000):
            print "nope"
            time.sleep(0.1)

whoLetTheDogsOut()
