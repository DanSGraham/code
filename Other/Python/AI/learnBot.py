#A program to be intentional about what I do with spare time.
#By Daniel Graham
from random import *
import time

subject_list = ["English", "History", "Math", "Chemistry", "Physics", "Biology", "Psychology", "Philosophy", "Computer Science", "Logic", "Religion", "Art", "Cooking", "Politics"]
subject_list_length = len(subject_list)
def main():
    print("Alright Daniel what are we going to learn today?...\n")
    time.sleep(1)
    print subject_list[randrange(0,subject_list_length)]
    
    for i in range(20):
        print (str(60-(i*5)) + " minutes left")
        time.sleep(300)

    print "Now reflect on the material for 10 minutes. Really let it sink in and make connections with other areas\n"

    for j in range(10):
        print (str(10-j) + " minutes left")
        time.sleep(60)

    print "Great job! Don't you feel smarter already?"

again = True
while again:
    main()
    again = input("Learn more?")
    
    
