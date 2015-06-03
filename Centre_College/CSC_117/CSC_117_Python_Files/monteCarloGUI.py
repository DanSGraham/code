#
# An approximation of pi
#Daniel Graham
#This method should give an approximation of pi due to the ratio of circle to rectangle.
#Since the area of the circle = pi and the area of the rectangle will = 4 by multiplying by 4,
#the function returns an approximation of pi

import math
import random
from graphics import *

def distance_from_center(x,y):
    distance1 = math.sqrt((x)**2+(y)**2)
    return distance1

def mainGUI():
    win = GraphWin("Pi Approximation", 1000,1000)
    win.setCoords( -1.5,-1.5,1.5,1.5)
    square = Rectangle(Point(-1,1), Point(1,-1))
    circle = Circle(Point(0,0),1)
    title = Text(Point(0,1.25), "Pi Approximation")
    prompt = Text(Point(-.2,-1.25), "How many points would you like to use? \n Click after Entry!")
    prompt_entry = Entry(Point(0.4,-1.25), 8)
    


    title.draw(win)
    prompt.draw(win)
    prompt_entry.draw(win)
    circle.draw(win)
    square.draw(win)
    
    win.getMouse()
    while prompt_entry.getText() == "":
        win.getMouse()
    prompt.undraw()
    prompt_entry.undraw()
    number_of_dots = int(prompt_entry.getText())
    inside_circle = 0
    outside_circle = 0
    
    for a in xrange(number_of_dots):
        pointx = random.uniform(-1,1)
        pointy = random.uniform(-1,1)
        point = Point(pointx,pointy)
        point.draw(win)
        distance = distance_from_center(pointx, pointy)
        
        if distance <= 1.0:
            inside_circle += 1
            point.setFill('red')
        else:
            outside_circle +=1
            point.setFill('blue')
            
    pi_approx = inside_circle/float((inside_circle+outside_circle))*4
    text_string = "According to this approximation, pi = " + str(pi_approx)
    points_string = "You used " + str(number_of_dots) + " points to approximate pi. There were " + str(inside_circle) + " points inside the circle \n Click when Finished!"

    end_text = Text(Point(0,-1.2), text_string)
    points_text = Text(Point(0, -1.30), points_string)
    
    points_text.draw(win)
    end_text.draw(win)
    
    win.getMouse()
    win.close()
    


mainGUI()

