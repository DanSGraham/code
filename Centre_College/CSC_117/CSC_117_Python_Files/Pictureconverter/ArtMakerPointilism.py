#
#A Program to turn images into txt data
#By Daniel Graham
from graphics import*
from random import*
import glob
def createpointilism(folder, amount_circles):
    for name in glob.glob(folder + "/*.gif"): #Completes the glob function described in ArtMakerpixel.py
        file_out_name = name[:-4] + ".art"
        fout = open(file_out_name, 'w')
        picture = Image(Point(0,0), name)
        pic_width = picture.getWidth()
        pic_height = picture.getHeight()
        for i in range(amount_circles): #creates the amount of circles specified by the user in the main program
            x = randrange(pic_width) 
            y = randrange(pic_height)
            circle_radius = randrange(1,8)
            color_pixel = picture.getPixel(x, y)
            to_write = str(x+ 300-pic_width/2) +' '+ str(y + 300-pic_height/2) +' '+ str(circle_radius) +' '+ str(color_pixel[0]) +' '+ str(color_pixel[1]) +' '+ str(color_pixel[2]) + '\n' #I added the 300-picwidth/2 so that the image would appear in the middle of the graph window.
            fout.write(to_write)
        fout.close()

def createpointilismbw(folder, amount_circles): #Following is the same as the first part, only black and white difference
    for name in glob.glob(folder + "/*.gif" ):
        file_out_name = name[:-4] + ".art"
        fout = open(file_out_name, 'w')
        picture = Image(Point(0,0), name)
        pic_width = picture.getWidth()
        pic_height = picture.getHeight()
        for i in range(amount_circles):
            x = randrange(pic_width) 
            y = randrange(pic_height)
            circle_radius = randrange(1,8)
            color = picture.getPixel(x, y)
            greyscale = (color[0])*0.2126 + (color[1])*0.7152 + (color[2])*0.0722    #Equation to calculate grey scale value from: http://www.johndcook.com/blog/2009/08/24/algorithms-convert-color-grayscale/
            to_write = str(x+ 300-pic_width/2) +' '+ str(y + 300-pic_height/2) +' '+ str(circle_radius) +' '+ str(int(greyscale)) +' '+ str(int(greyscale)) +' '+ str(int(greyscale)) + '\n' 
            fout.write(to_write)
        fout.close()
    

    
    
    
            
        
