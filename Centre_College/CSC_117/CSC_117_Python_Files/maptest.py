from graphics import *
import random




def move_test():
    win = GraphWin("j",200,1000, autoflush = False)
    x = Circle(Point(100,100), 20)
    x.draw(win)
    j = 0
    while True:
        x.move(0,.001)
        j += 1
        if j%3000 == 0:
            update()
            print "update"
        
        
        
