#A program to practice recursion.
#By Daniel Graham


import turtle
import time
turtle.speed(0)
turtle.penup()
turtle.right(90)
turtle.forward(150)
turtle.left(90)
turtle.forward(300)
turtle.pendown()
turtle.bgcolor('black')
turtle.colormode(255)
x = 255
y = 0
z = 0
color_list = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

def triangle_recursive(n, r,g,b):
    color = (r,g,b)
    turtle.pencolor(color)
    turtle.left(120 + n)
    turtle.forward(600)
    turtle.left(120 + n)
    turtle.forward(600)
    turtle.left(120 + n)
    turtle.forward(600)
    #Change how much n must be less than to change how many times run.
    #Change what adds to n to change the angle change.
    #if n <= .64:
        #triangle_recursive(n + .01)
    if (r > 0 and g > 0) or (r > 0 and b > 0):
        if 255 > g > 0:
            r -= 1
            b += 1
        if 255 > b > 0:
            r -= 1
            g += 1
    elif g > 0 and b > 0:
        if g > 0 and r < 255:
            g -=1
            r +=1
    elif r > 0:
        g += 1
        r -= 1
    triangle_recursive(n + .0001, r, g, b )   
    
triangle_recursive(0,x,y,z)
