#
#A Program to turn images into txt data
#By Daniel Graham
from graphics import*
from random import*
def createpointilism(filename):
    fout = open('artinfo.art', 'w')
    picture = Image(Point(0,0), filename)
    pic_width = picture.getWidth()
    pic_height = picture.getHeight()
    for i in range(600):
        x = randrange(pic_width + 1)
        y = randrange(pic_width + 1) #There is a small chance that I will end up with the same point twice. Need to account for that.
        write_list = [x , y]
        write_list.append(randrange(2,8))
        write_list.append(getPixel(x, y))
        write_list.append(fout)
        write_list = []
    

    
    
    
            
        
