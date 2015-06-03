#
#
#By: Daniel Graham

from graphics import*
import time
window = GraphWin("Circle Frenzy!",500,500)
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'blue4', 'purple', 'purple4']
t1=Text(Point(250,250), "Please click where you would like circles to begin!")
t1.draw(window)
click_point = window.getMouse()
t1.undraw()
for i in range(500):
    circle=Circle(click_point, i)
    circle.setOutline(colors[i%8])
    circle.setWidth(10)
    circle.draw(window)
    time.sleep(0.01)
window.getMouse()
window.close()
