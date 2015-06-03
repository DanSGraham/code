#
#A program to make pixelated art
#By Daniel Graham
#

from graphics import*
from random import*
def createpixel(filename):
    fout = open('FILENAME.art', 'w')
    picture = Image(Point(0,0), filename)
    pic_width = picture.getWidth()
    pic_height = picture.getHeight()
    x = 0
    y = 0
    for j in range((pic_width/4)): 
        for i in range((pic_height)/4):
            point1 = Point(x,y)
            point2 = Point(x+4,y+4)
    ##        write_list = [point1, point2]
    ##        write_list.append(getPixel(x+1, y+1))
    ##        write_list.append(fout)
    ##        write_list = []
            color = getPixel(x+2,y+2)
            x = x+4
            to_write = str(point1) +' '+ str(point2) +' '+ str(color[0]) +' '+ str(color[1]) +' '+ str(color[2]) + '\n' #THIS IS A CHEATERS METHOD. I NEED TO MAKE THIS SHORTER. USE A LIST?
        y = y+4
    print to_write

