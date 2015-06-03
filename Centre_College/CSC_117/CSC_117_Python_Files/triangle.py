#
#
#

from graphics import*
import time
linewin = GraphWin('Three Points', 500,500)
prompt = Text(Point(250,20), "Click three places.")
prompt.draw(linewin)
points=[]
for i in range(3):
    click_point = linewin.getMouse()
    points.append(click_point)
    circle1 = Circle(click_point, 5)
    circle1.setOutline('red')
    circle1.draw(linewin)
triangle = Polygon(points[0],points[1],points[2])
triangle.setFill("yellow")
triangle.setOutline("blue")
triangle.draw(linewin)
Text(Point(250,480), "Good Job!").draw(linewin) 


linewin.setBackground('white')
linewin.getMouse()
linewin.close()


