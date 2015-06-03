#
#A program to make pixelated art
#By Daniel Graham
#

from graphics import *
import glob

def createpixel(folder , size_of_pixel): #This line sets the parameters that I input from the main program
    for name in glob.glob(folder + "/*.gif"):   #this is the glob function. It goes through all the files in the folder specified in the parameter that end in .gif and does the following code to each of them.
        file_out_name = name[:-4] + ".art" #The next two lines create specific .art files for each .gif file
        fout = open(file_out_name, 'w')
        picture = Image(Point(0,0), name)
        pic_width = picture.getWidth()
        pic_height = picture.getHeight()
        pixel_size = size_of_pixel *2
        x = 0
        y = 0
        for j in range((pic_height/pixel_size)): 
            for i in range((pic_width/pixel_size)):
                color = picture.getPixel(x+size_of_pixel,y+size_of_pixel)
                to_write = str(x + (300-pic_width/2)) +' '+ str(y + (300-pic_height/2)) +' '+ str(x+pixel_size + (300-pic_width/2)) +' '+ str(y+pixel_size + (300-pic_height/2)) +' '+ str(color[0]) +' '+ str(color[1]) +' '+ str(color[2]) + '\n' 
                fout.write(to_write) #The preceding 7 lines create the art file that has the variables of the rectangles drawn in the view program. 
                x = x+pixel_size
            y = y+pixel_size
            x = 0
        
    

def createpixelbw(folder , size_of_pixel): #This code is the same as the first, only it converts to black and white using the equation on line greyscale
    for name in glob.glob(folder + "/*.gif"):
        file_out_name = name[:-4] + ".art"
        fout = open(file_out_name, 'w')
        picture = Image(Point(0,0), name)
        pic_width = picture.getWidth()
        pic_height = picture.getHeight()
        pixel_size = size_of_pixel *2
        x = 0
        y = 0
        for j in range((pic_height/pixel_size)): 
            for i in range((pic_width/pixel_size)):
                color = picture.getPixel(x+size_of_pixel,y+size_of_pixel)
                greyscale = (color[0])*0.2126 + (color[1])*0.7152 + (color[2])*0.0722    #Equation to calculate grey scale value from: http://www.johndcook.com/blog/2009/08/24/algorithms-convert-color-grayscale/
                to_write = str(x + (300-pic_width/2)) +' '+ str(y + (300-pic_height/2)) +' '+ str(x+pixel_size + (300-pic_width/2)) +' '+ str(y+pixel_size + (300-pic_height/2)) +' '+ str(int(greyscale)) +' '+ str(int(greyscale)) +' '+ str(int(greyscale)) + '\n' 
                fout.write(to_write)
                x = x+pixel_size
            y = y+pixel_size
            x = 0

if "___name___" =="___main___":
    createpixel('gallery', 4)
