#
#A program to make pixelated art
#By Daniel Graham
#

from graphics import*
from random import*
def createpixelbw(filename):
    fout = open(FILENAME, 'w')
    picture = Image(Point(0,0), filename)
    pic_width = picture.getWidth()
    pic_height = picture.getHeight()
    x = 0
    y = 0
    for i in range((pic_width*pic_height)/9):
        point1 = Point(x,y)
        point2 = Point(x+2,y+2)
        write_list = [point1, point2]
        color_of_pixel = getPixel(Point((x+1),(y+1)))
        grey_scale_value = 116*((color_of_pixel[0]**2.2)*0.2126 + (color_of_pixel[1]**2.2)*0.7152 + (color_of_pixel[2]**2.2)*0.0722)**(1/3)-16    #Equation to calculate grey scale value from: http://stackoverflow.com/questions/687261/converting-rgb-to-grayscale-intensity
        write_list.append(color_rgb(grey_scale_value,grey_scale_value, grey_scale_value)))
        write_list.append(fout)
        write_list = []
