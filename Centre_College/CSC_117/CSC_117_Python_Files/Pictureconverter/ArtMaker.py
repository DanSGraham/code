#
#A Program to turn images into txt data
#By Daniel Graham
from graphics import*
from random import*
def createpointilism(filename, amount_circles):
    fout = open('artinfo.art', 'w')
    picture = Image(Point(0,0), filename)
    pic_width = picture.getWidth()
    pic_height = picture.getHeight()
    for i in range(amount_circles):
        x = randrange(pic_width) 
        y = randrange(pic_height)
        circle_radius = randrange(1,8)
        color_pixel = picture.getPixel(x, y)
        to_write = str(x+ 300-pic_width/2) +' '+ str(y + 300-pic_height/2) +' '+ str(circle_radius) +' '+ str(color_pixel[0]) +' '+ str(color_pixel[1]) +' '+ str(color_pixel[2]) + '\n' #THIS IS A CHEATERS METHOD. I NEED TO MAKE THIS SHORTER. USE A LIST?
        fout.write(to_write)
    fout.close()

def createpointilismbw(filename, amount_circles):
    fout = open('artinfo.art', 'w')
    picture = Image(Point(0,0), filename)
    pic_width = picture.getWidth()
    pic_height = picture.getHeight()
    for i in range(amount_circles):
        x = randrange(pic_width) 
        y = randrange(pic_height)
        circle_radius = randrange(1,8)
        color = picture.getPixel(x, y)
        greyscale = (color[0])*0.2126 + (color[1])*0.7152 + (color[2])*0.0722    #Equation to calculate grey scale value from: http://www.johndcook.com/blog/2009/08/24/algorithms-convert-color-grayscale/
        to_write = str(x+ 300-pic_width/2) +' '+ str(y + 300-pic_height/2) +' '+ str(circle_radius) +' '+ str(greyscale) +' '+ str(greyscale) +' '+ str(greyscale) + '\n' #THIS IS A CHEATERS METHOD. I NEED TO MAKE THIS SHORTER. USE A LIST?
        fout.write(to_write)
    fout.close()
    

    
    
    
            
        
