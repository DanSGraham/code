#
#This is a quest game
#Author: Daniel Graham
#

from graphics import *
from random import *
from time import *
win = GraphWin('EpiQuest')
t1= Text(Point(100,20), "Begin Your Magical Quest?")
yes_text,yes_box = Text(Point(34,100,), "Yes!" ), Rectangle(Point(18,90),Point(50,110))
no_text, no_box = Text(Point(166,100,), "No...." ), Rectangle(Point(182,90),Point(150,110))
yes_box.setFill('yellow')
yes_box.draw(win)
yes_text.draw(win)
no_box.setFill('red')
no_box.draw(win)
no_text.draw(win)
t1.draw(win)
win.setBackground("light blue")
x = win.getMouse()
for j in range(200):
    if x.getX() == range(18,50):
        print "YES!"
        sleep(3)
        win.close()
