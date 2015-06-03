from random import *
from time import *
#A program to express my feelings about this physics test wednesday.
#By Daniel Graham
fuck_list = ["Fuck", 'FUCK', 'FUUUUUUUUUUUUU', 'fuck', 'FUCK!!!!!!!!', 'fck', "fUck", "FUCKKKKKKKKKKK!", "GIMME AN F, GIMME A U, GIMME A C, GIMME A FUUUUUUUUUUUUUUUCK..."]
while True:
    string_to_print = ""
    for i in range(randrange(1,100)):
        string_to_print += fuck_list[randrange(0,len(fuck_list))]
    print string_to_print
    sleep(.4)
    
                   
