#
#A program to draw a quadratic
#Author: Daniel Graham
#

from graphics import*
def main():
    win = GraphWin( "A Graph", 400,400)
    win.setCoords(-3.0,-5.0, 3.0,20.0)
    xAxis = Line(Point(-3,0),Point(3,0))
    yAxis = Line(Point(0 , -5.0),Point(0,20.0))
    xAxis.draw(win)
    yAxis.draw(win)
    x = -3.0
    a_text = Text(Point(-2,19), "A : ")
    b_text = Text(Point(0,19), "B: ")
    c_text = Text(Point(2,19), "C: ")
    a_entry = Entry(Point(-1.5,19), 2)
    b_entry = Entry(Point(0.5,19), 2)
    c_entry = Entry(Point(2.5,19),2)
    a_text.draw(win)
    b_text.draw(win)
    c_text.draw(win)
    a_entry.draw(win)
    b_entry.draw(win)
    c_entry.draw(win)
    win.getMouse()
    plist = []
    a = float(a_entry.getText())
    b = float(b_entry.getText())
    c = float(c_entry.getText())
    if b**2-4*a*c > 0:
        circle1 = Oval(Point(((-b+(b**2-4*a*c)**.5)/(2*a))-.3,0.6),Point(((-b+(b**2-4*a*c)**.5)/(2*a))+.3,-0.6))
        circle1.setOutline('green')
        circle2 = Oval(Point(((-b-(b**2-4*a*c)**.5)/(2*a))-.3,0.6),Point(((-b-(b**2-4*a*c)**.5)/(2*a))+.3,-0.6))
        circle2.setOutline('green')
        circle1.draw(win)
        circle2.draw(win)
        Text(Point(0,-4.5), "The roots are at x= " + str((-b+(b**2-4*a*c)**.5)/(2*a))+ ',' + str((-b-(b**2-4*a*c)**.5)/(2*a))).draw(win)
    if b**2-4*a*c == 0:
        circle = Oval(Point(((-b)/(2*a))-.2,0.2),Point(((-b+(b**2-4*a*c)**.5)/(2*a))+.2,-0.2))
        circle.setOutline('red')
        circle.draw(win)
        Text(Point(0,-4.5), "The root is at x= " + str((-b)/(2*a))).draw(win)
    if b**2-4*a*c < 0:
        Text(Point(0, -4.5), "There are no real roots!").draw(win)
    for i in range(60):
        p = Point(x,(a*(x**2))+(b*x)+c)
        plist.append(p)
        x = x + 0.1
        p.draw(win)
    for i in range(len(plist)-1):
        segment = Line(plist[i],plist[i+1])
        segment.draw(win)
    win.getMouse()
    win.close()
main()
