## Author: **your email goes here**
## Course: CSC 117 Spring 2013
## Assignment: Program 1 - Owl Racing
##
## Authorship & Assistance:
##     - I wrote this code with no assistance other than that listed here
##         - ** list who / what helped you, other than the instructor, 
##             and the nature of the help
##     - I provided assistance to the following:
##         - ** list anyone you helped with this assignment
##
## Self Assessment & Caveats:
##     - ** Explain whether you believe the program meets the
##         assignment requirements.
##     - ** If the answer above is not "It meets the requirements"
##         then what are your concerns?
##     - ** If your answer is "It meets the requirements" then list caveats:
##         anything you think I should know you are aware of that
##         might be a concern about your program even though it meets the
##         requirements
##
## Time:
##     - ** estimate how much time you spent at the computer working on the assignment
##     - ** estimate how much time you spent thinking about the assignment
##          but were not actually working on it
##
## Reflection:
##     - ** list anything you believe you learned from this assignment,
##         general feelings about the experience, concerns about the
##         assignment or the experience, whether you enjoyed it (why),
##         or not (why)? 

import time

# This function prints a row of spaces, so that the next thing printed 
# after this will appear shifted to the right on the screen.
def printSpaces(numSpaces):
    for i in range(numSpaces):
        print "",   # <-- the comma at the end means don't-print-a-NEW-LINE!

# This function prints a specified number of blank lines
# (You should NOT need to MODIFY this function -- just call it!)
def printBlankLines(numBlankLines):
    for i in range(numBlankLines):
        print ""  # we're printing an 


def main():
    #   WRITE THE CODE FOR YOUR GAME HERE INSIDE THE MAIN FUNCTION
    #
    #  (Read the assignment handout carefully to make sure your program
    #   does what it is supposed to.)  
    #  (Delete these worthless comments, and write your own GOOD comments
    #   before turning in your program.)

main()

#Hint #0: Start working on this early!  Very early!

#Hint #1: Experiment.  Build your game bit by bit.  Add one little part,
#         and then test it. Add another little piece, and test it.
#         DO NOT TRY TO WRITE THE WHOLE PROGRAM TOP-TO-BOTTOM BEFORE 
#         RUNNING ANY CODE!  IT WON'T WORK!

#Hint #2: Try running just these two lines of code, and see what happens.
# printSpaces(15)
# print "Hi!"

#Hint #3: Try running just these five lines of code, and see what happens.
# printBlankLines(30)
# print "Boo!"
# time.sleep(0.1)     #pause for a bit
# printBlankLines(30)
# print "   Here!"

#Hint #4:  How can you combine these ideas to accomplish what you want, 
#          up inside main?

#Hint #5:  In the end, I suspect you'll need to use a loop 
#          inside of another loop.  Sounds a bit wild, but it
#          should make sense once you think about it enough.

#Hint #6:  Think about it enough.

#Hint #7:  "Loops inside loops?  I'm overwhelmed!"
#          Okay, remember Hint #1 about getting it working one piece
#          at a time?  How about you just get ONE owl to fly first.  Then
#          you wouldn't need to loop through the owls.  You just need a 
#          loop to animate owl when it's flying, by changing how many
#          spaces are printed in front of the whole each time.
#          After that's working, you can surround it all with another
#          loop, so you can have multiple owls fly.
#
#Hint #8:  If you followed HINT #0, then you started early.  That means
#          if things aren't working, you still have plenty of time to get help.
#          So ask for help if you need it!
