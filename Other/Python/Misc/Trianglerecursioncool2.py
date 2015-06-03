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

color_list = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

def triangle_recursive(n):

    turtle.pencolor(color_list[int((n % .6) * 10)])
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
    triangle_recursive(n + .001)
    
    
triangle_recursive(0)
