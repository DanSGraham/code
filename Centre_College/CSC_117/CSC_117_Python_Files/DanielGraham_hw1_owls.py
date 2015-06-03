## Author: daniel.graham@centre.edu
## Course: CSC 117 Spring 2013
## Assignment: Program 1 - Owl Racing
##
## Authorship & Assistance:
##     - I wrote this code with no assistance
##     - I provided assistance to the following:
##
##
## Self Assessment & Caveats:
##     - I believe my code definitely meets the criteria. It allows a user to input any number of owls and simulates a "race" with them. Then it prints who the victor is. It also tells the user when the race is finished and when it is starting.
##     -
##     - Printing the owl takes more time with more spaces in front of it, so the farther it goes, the more the program lags. Is there a way to stop that?
##
## Time:
##     - I probably spent 3 hours working on this project.
##     - I spent over 8 hours thinking about the project.
##
## Reflection:
##     - I loved this assignment because it provided guidelines but not strict qualifications.
##       I really like a challange and getting the multi-line owl to print was a huge one. I learned that a list
##       can only contain a certain number of objects, which is why my owls are split into two lists each.


#These lists will later print multi-line owls.
owla = [
    '__________-----____                 ____-----__________ \n',
    '\----____-------___--__---------__--___-------____----/ \n',
    ' \//////// / / / / / \   _-------_   / \ \ \ \ \ \\\\\\\\/ \n',
    '  \////-/-/------/_/_| /___   ___\ |_\_\------\-\-\\\\/ \n',
    '    --//// / /  /  //|| (O)\ /(O) ||\\  \  \ \ \\\\-- \n',
    '         ---__/  // /| \_  /V\  _/ |\ \\  \__--- \n',
    ]
owlb = [
    '              -//  / /\_ ------- _/\ \  \\- \n',
    '                \_/_/ /\---------/\ \_\_/ \n',
    '                    ----\   |   /---- \n',
    '                         | -|- | \n',
    '                         /|\ /|\  \n'
    ]
#Ascii owl character courtesy of http://www.ascii-art.de/ascii/mno/owl.txt

owlflapa=[
    '       _____             _____  \n',
    '      /     \ _-------_ /     \  \n',
    '     / _|  | /___   ___\ |_\_\ \  \n' ,
    '    / / / /|| (O)\ /(O) ||\ \ \ \  \n',
    '   / // /  | \_  /V\  _/ | \ \ \  \  \n'
    ]
owlflapb = [
    '  / -/ / / /\_ -------- _/\ \ \ \- \  \n' ,
    ' /\_/\_/\_/\/\----------/\\_\_\_\_/\ \n',
    '          ----\    |   /---- \n',
    '               |  -|- | \n',
    '                /|\ /|\  \n'
    ]
bludgera = [
     '                                 .o\n',                                        
     '                                 .y\n',                                        
     '               ``   -   .        .y\n',                                       
     '                `````/`. `       .y\n',                                        
     '                      :- .       .y\n',                                        
     '                   ``` ./.       .y\n',                                        
     ]
bludgerb = [
     '              `o-        -       .o                       ..\n',               
     '                :o/           `-::///:-.               :++:\n',               
     '                  -o/`    :++//-.`   `.://+/`       /++.\n',                   
     '                    `: -o+-                `/+/`\n',                           
     '                     .s/                      .o+\n',                          
     '                    +o                          -s`\n',                        
     ]
bludgerc = [
     '                   o:                            `y.\n',                      
     '                  :o                              .h\n',                       
     '                  h`                               s-\n',                      
    '-///////////////:  h                                :+ .///////////////////`\n',
     '                  d                                //\n',                      

     '                  s-                               h`\n',                      
     ]
bludgerd = [
     '                  `h                              /+\n',                      
     '    ``    ```      .y`                           /o\n',                        
     '    .-::-:--/--     `s:                        `s/\n',                         
     '     ```````          :o/                    .o+`\n',                          
     '                     // .++/.            `:++:\n',                             
     '                  `/o.     `:+////////////.          ++`\n',                   
     '                `+o.                                  `+o`\n',                 
     '                :`                  s        :/````     `++.\n',               
     ]


#Bludger converted to ascii by http://www.text-image.com/convert/ascii.html
import time
import random
import string
import datetime


def print_spaces(numSpaces):
    for i in range(numSpaces):
        print "",

def print_blank_lines(numBlankLines):
    for i in range(numBlankLines):
        print ""




def main():
    
    print "Welcome to THE OWL RACE 5000"
    time.sleep(1)
    print "Find out whooo is the best!"
    time.sleep(1)
    casualties = 0 #this stores the number of dead owls
    num_owls=input("How many owls will be racing today? ")
    if num_owls < 1: #The following two lines take into account the edge values
        print "You must submit at least one owl to race! (Nice try though)"
        main()
    else:
        winning_owl=0     #These two lines set up the accumulator for the winning owl name/distance
        winning_owl_distance=0

        for i in range(num_owls): #This loop begins the action of the program for as many owls as are racing.  It will run as many times as there are owls entered.
            if i==0:
                name_owl=raw_input("What is the first owl's name? ") #The if statement allows the two different input prompts to be different, but the resulting loop to use the same variable.
            else:
                name_owl=raw_input("What is the next owl's name? ")
            distance_owl=random.randrange(2,10)
            
            print "Here we go!"
            time.sleep(1)
            
            for j in range (distance_owl): #This part actually prints the owl j*5 spaces past the end.
                if j%2==0: #To simulate flapping wings, owl image a and b (open wings) had to be printed every other line with owlflap a and b printed.
                    for k in owla: #This line prints the first half of owla, line by line with spaces(j*5) in front of each line.
                        print_spaces(j*5),
                        print k,
                    for k in owlb: #This line prints the second half of owlb with the same amount of spaces in front.
                        print_spaces(j*5),
                        print k,
                    time.sleep(.25)
                    print_blank_lines(60)
                elif j%2==1: #This prints the other owl image on the odd j's to simulate flapping using two alternating images. The following code's purpose is the same as the preceeding loop.
                    for k in owlflapa:
                        print_spaces(j*5+10),
                        print k,
                    for k in owlflapb:
                        print_spaces(j*5+10),
                        print k,
                    time.sleep(.25)
                    print_blank_lines(60)
            if j< 3: #if the owl does not go further than a distance of 35 yards, the program displays a buldger animation in the same way it shows the owl.
                print "As", name_owl, "approached the finish line he could almost taste victory...But suddenly!"
                time.sleep(3)
                print
                print
                print
                for i in bludgera:
                    print_spaces(j*5+20)
                    print i,
                for i in bludgerb:
                    print_spaces(j*5+20)
                    print i,
                for i in bludgerc:
                    print_spaces(j*5+20)
                    print i,
                for i in bludgerd:
                    print_spaces(j*5+20)
                    print i,
                for i in bludgera:
                    print_spaces(j*5+20)
                    print i,
                print "A rogue bludger flys out of nowhere, clobbering", name_owl,". Healers attempted to revive him but it was too late. Time of death:", datetime.datetime.now() #Prints tod of current day.
                print
                print
                print
                time.sleep(3) #This provides time to mourn your lost owl.
                casualties = casualties + 1 #this stores the number of owl who do not make it past 35 yards
            if distance_owl > winning_owl_distance: #This line stores the highest distance an owl flies in the accumulator as well as which owl did it.
                winning_owl = name_owl
                winning_owl_distance = distance_owl
        if casualties == num_owls: #This if statement accounts for all the owls being hit by bludgers.
            print "Unfortunately no owls finished the race...bummer."
            time.sleep(3)
        else:
            print "The winning owl was",winning_owl,",","with a distance of ",str(winning_owl_distance*5), "yards."
            time.sleep(3)
        print "Number of casualties: ", casualties
        time.sleep(2)
        print "But then again, there were never really any 'owls', were there?"
    












##           time.sleep(5)
##           print "S1y7h3r1n ru1z"*10000
main()
