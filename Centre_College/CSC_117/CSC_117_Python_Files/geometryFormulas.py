#Misc functions
#By Daniel Graham

import math

def boxVolume(length, width, height):
    return length*width*height

def boxArea(length, width, height):
    surface_area = 2*length*width +2*length*height + 2*height*width
    return surfaec_area

def sphereVolume(radius):
    volume = (4.0/3)*math.pi*radius**3
    return volume

def sphereArea(radius):
    area = 4*math.pi*radius**2
    return area
