#Circle Recursion
#By Daniel Graham

import turtle
import math

color_list = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

turtle.penup()
turtle.forward(400)
turtle.pendown()
turtle.right(90)
turtle.forward(1)
turtle.pencolor('red')
def circle(n):
    turtle.pencolor(color_list[int((n % 6))])
    turtle.right(n)
    turtle.forward(10)
    if n <= 500:
        circle(n + .1)

circle(0)
    



