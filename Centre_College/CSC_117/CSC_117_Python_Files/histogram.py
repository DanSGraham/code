#
#A program to roll dice
#This program will roll dice a given number of dice and plot the number
#of occurance of each roll as the output of a graph
#
#By Daniel Graham
#

import random
from graphics import *


def diceRoll():

    """This function 'rolls' two dice and returns the sum of their values"""

    ##I know I could use one die and just roll it twice, but having two
    ##die variables makes the code more intuitive.
    
    die1 = [1,2,3,4,5,6]
    die2 = [1,2,3,4,5,6]

    dice_sum = die1[random.randrange(6)] + die2[random.randrange(6)]

    return dice_sum

def getData(num_times):

    """This function gathers 100 sums calculated in diceRoll() and tallies each one into a myList"""
    myList = [0] *13
    for i in range(num_times):
        myList[diceRoll()] += 1
    return myList

def setUpGraphWindow(max_rolls):

    """This function draws the graph template"""
    
    window = GraphWin("Histogram of Dice Rolls", 700,500)
    window.setCoords(-1.3,-(max_rolls/5),12.1,max_rolls)
    x_axis = Line(Point(0,0),Point(max_rolls,0))
    y_axis = Line(Point(0,0),Point(0,max_rolls))
    x_label = Text(Point(6,-(max_rolls/7)), "Sum of Dice")
    x_label.draw(window)
    x_axis.draw(window)
    y_axis.draw(window)
    for i in range(11):
        label = Text(Point(i+0.5,-(max_rolls/20)), str(i+2))
        label.draw(window)
    for j in range(0,max_rolls,max_rolls/20):
        y_axis_marks = Line(Point(-.1,j),Point(.1,j))
        y_axis_marks.draw(window)

    return window

def displayMean(max_rolls,data_list, win):
    
    """This function calculates the mean roll value and displays it on the window"""

    total_each_roll = 0
    for i in range(2,13):
        total_each_roll += (data_list[i]*(i))

        
    mean = (total_each_roll/float(sum(data_list))) #this calculate the mean value
    mean_string = "The mean value is " + str(mean)
    mean_text = Text(Point(6, max_rolls/3.2), mean_string)
    mean_text.draw(win)

def drawGraph(data_list, win):

    """This function draws rectangles on a window to a certain width and height"""
    
    for i in range(11):
        graph_bar = Rectangle(Point(i,0),Point(i+1,data_list[i+2]))
        graph_bar.setOutline("black")
        graph_bar.setFill("white")
        graph_bar.draw(win)
    
def main():

    """The main function calls other functions and displays the likely dice rolls"""
    
    roll_number = input("How many times would you like to roll the dice?(at least 60) ")
    window = setUpGraphWindow(roll_number/3)
    drawGraph(getData(roll_number),window)
    displayMean(roll_number, getData(roll_number), window)
    window.getMouse()
    window.close()
    
main()



    
        
        
