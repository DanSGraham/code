## Author(s): daniel.graham@centre.edu
## Course: CSC 117
## Assignment: Program 2 - Pointillism
##
## Description: This program converts images into .art files.
##
##
## Assistance:
##     - I wrote this code with no assistance 
##     - I provided assistance to the following:
##         
##
## Self Assessment & Caveats:
##     - I believe the program exceeds expectations. It can convert all .gif files in a folder into two different types of "art" in two distinct styles. I think I far exceeded the base parameters of the assignment.
##     -Something my program fails at is pathing to the folder with the images. In order for the program to convert and display the images, it has to be saved in the same folder as the gallery folder. Also the graphics window always went to the back of the windows when I played it.
##
## Time:
##     - 5 hours work time
##     - 3 hours think time
##
## Reflection:
##     - I think I learned a lot about how actual programs look. I am pretty sure this is the format that a lot of programs actually use (i.e. calling different modules.) I learned how to call modules and also how useful the graphics module is.
# A picture converting program
#By Daniel Graham





from graphics import *
from random import *
from time import *
from ArtMakerPixel import *
from ArtMakerPointilism import *
from artViewerpixels import *
from artViewerPointilism import *    #These lines import all my modules needed to run this code
import glob

def main():
    print "Sup!"   #Obligatory greeting
    sleep(1)
    art_style = raw_input("What style of art would you like to convert your pictures to today? (Pointilism, or Old school) ")
    while art_style != ("Pointilism, please.") and art_style != ("Old school, please."):
        print "ah ah ah....You didn't say the magic word!"    #This line is to ensure a certain level of class in the potential art admirer. Don't forget the comma!
        sleep(1)
        print "Slytherins never forget their manners or grammar!"
        sleep(1)
        art_style = raw_input("What style of art would you like to convert your pictures to today? (Pointilism, Old school, or Minimalist) ")
    folder = raw_input("Make sure the folder with .gif images is in the same folder as this file. Then enter the name of the folder: ") #This line specifies the folder name the art is drawn from.
    
    if art_style == "Pointilism, please.": 
        color_style = raw_input("Would you like it in color or grayscale? ")
        amount_circles = input("How many circles would you like to use per picture? (I recommend 800-4000) ")
        while color_style != "color" and color_style != "grayscale": #THis line ensure that a color or black and white is chosen
            color_style = raw_input("Would you like it in color or grayscale? ")
        if color_style == "color":
            createpointilism(folder, amount_circles) #These path to my programs that I imported.
        elif color_style == "grayscale":
            createpointilismbw(folder, amount_circles)
        artviewerpointilism(folder)
        
    if art_style == "Old school, please.":
        color_style = raw_input("Would you like it in color or grayscale? ")
        size_of_pixel = input("""On a scale of 1 to 5, how "old school" would you like the picture? (1 is not very old school, 5 is very old school)  """)
        while color_style != "color" and color_style != "grayscale":
            color_style = raw_input("Would you like it in color or grayscale? ")
        if color_style == "color":
            createpixel(folder, size_of_pixel)
        elif color_style == "grayscale":
            createpixelbw(folder, size_of_pixel)
        artviewerpixel(folder)
    
        
main()
