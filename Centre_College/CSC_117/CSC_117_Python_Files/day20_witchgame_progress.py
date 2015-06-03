from graphics import *
import random
import time

#import gui_input

#def askUserSettings():
    #this will pop up dialog windows that ask for setting choices
    # and return a list of settings, like:
    # ["hard", 10, "fast"]
    
    
def setupWindow():
    # create the graphics window, set coordinates, background color...
    # return the GraphWin object that gets created
    win = GraphWin("Witch game!", 600, 600)
    win.setBackground("white")
    win.setCoords(0,0,100,100)
    return win

def dropSpider(win):
    # takes in GraphWin object,
    # creates a spider Image at a random place near the top
    # returns the Spider image
    randX = random.randrange(5,95)
    spidey = Image(Point(randX,95),"owl_tree.gif")
    spidey.draw(win)
    return spidey

def mainGameLoop(win,numSpiders):
    witch = Image(Point(50,20),"owl.gif")
    witch.draw(win)
    spiderList = []

    witchVelocity = 0
    
    while True:
        if len(spiderList) < numSpiders and random.randrange(10) == 0:  #if we need more spiders
            newSpidey = dropSpider(win)
            spiderList.append(newSpidey)
        for spidey in spiderList:
            spidey.move(0,random.uniform(-2.0,1.0))
            if spidey.getAnchor().getY() < - 5:
                spiderList.remove(spidey)
                spidey.undraw()

        mousePt = win.checkMouse()
        
        if mousePt != None:
            if (mousePt.getX() > witch.getAnchor().getX()):
                witchVelocity = 1
            else:
                witchVelocity = -1

        witch.move(witchVelocity,0)
           
        
        time.sleep(0.1)
        
        
        
    # big loop
    # if there aren't enough spiders, then call dropSpider(win)
    #   and add the result to a list of spiders (spiderList)
    # go through each spider in spiderList, and move it downward
    #
    # move the witch (separate function?)
    # wait a little bit (time.sleep)


def main():
    #settings = askUserSettings()
    win = setupWindow()
    #mainGameLoop(win,settings[0],settings[1],settings[2])
    mainGameLoop(win,10)
    win.getMouse()
    win.close()


main()

    
