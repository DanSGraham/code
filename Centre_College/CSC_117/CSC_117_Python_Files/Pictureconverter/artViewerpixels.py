#
#A Program to view pixellated art
#By Daniel Graham

from graphics import*
import glob
def artviewerpixel(folder):
    for name in glob.glob(folder + "/*.art"): #The glob function allows the viewer to go through all the files automatically.
        win = GraphWin("Old School...", 600, 600)
        fin = open(name , 'r')
        win.setBackground('black')
        for line in fin: #The next lines decode the information in the .art file and translate it into drawing on the graphwindow.
            list_of_comp = line.split()
            list_of_comp = map(int , list_of_comp)
            rectangle = Rectangle(Point(list_of_comp[0], list_of_comp[1]), Point(list_of_comp[2], list_of_comp[3]))
            rectangle.setFill(color_rgb(list_of_comp[4],list_of_comp[5],list_of_comp[6]))
            rectangle.setOutline(color_rgb(list_of_comp[4],list_of_comp[5],list_of_comp[6]))
            rectangle.draw(win)
        win.getMouse()
        win.close()
