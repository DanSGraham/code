#
#A Program to view pointilism art
#By Daniel Graham
from graphics import*
import glob
def artviewerpointilism(folder):
    for name in glob.glob(folder + "/*.art" ): #completes the glob function described in artviewerpixel.py
        win = GraphWin("A Picture is worth 360000 pixels", 600, 600)
        fin = open(name , 'r')
        win.setBackground('black')
        for line in fin:     #The next lines decode the .art file and draw it on the window.
            list_of_comp = line.split()
            list_of_comp = map(int , list_of_comp)
            circle = Circle(Point(list_of_comp[0], list_of_comp[1]), list_of_comp[2])
            circle.setFill(color_rgb(list_of_comp[3],list_of_comp[4],list_of_comp[5]))
            circle.setOutline(color_rgb(list_of_comp[3],list_of_comp[4],list_of_comp[5]))
            circle.draw(win)
        win.getMouse()
        win.close()

