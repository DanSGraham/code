#
#A program to draw a quadratic
#Author: Daniel Graham
#

from graphics import*
def main():
    win = GraphWin( "A Graph", 400,400)
    win.setCoords(-4.0,-4.0, 4.0,10.0)
    xAxis = Line(Point(-4,0),Point(4,0))
    yAxis = Line(Point(0 , -4.0),Point(0,10.0))
    xAxis.draw(win)
    yAxis.draw(win)
    x = -4.0
    plist = []
    for i in range(81):
        p = Point(x,x**2+2*x-3.0)
        plist.append(p)
        x = x + 0.1
        y_location = p.getY()
        if y_location >= 0:
            if y_location <= 0.00001:
                circle = Circle(Point(p.getX(),p.getY()), 0.1)
                circle.setOutline('red')
                circle.draw(win)
                label_text = str(p.getX()) + ',' + str(0)
                label_point = Text(Point(p.getX(),p.getY()-1), label_text)
                label_point.draw(win)
        elif y_location <=0:
            if y_location >= -0.000001:
                circle = Circle(Point(p.getX(),p.getY()), 0.1)
                circle.setOutline('red')
                circle.draw(win)
                label_text = str(p.getX()) + ',' + str(0)
                label_point = Text(Point(p.getX(),p.getY()-1), label_text)
                label_point.draw(win)
        p.draw(win)
    for i in range(len(plist)-1):
        segment = Line(plist[i],plist[i+1])
        segment.draw(win)
    
main()
