#
#
#By Daniel Graham


from graphics import*

window = GraphWin("Almost Triforce",300,300)
triangle1= Polygon(Point(100,237),Point(150,150),Point(200,237))
triangle1.draw(window)
triangle2 = triangle1.clone()
triangle2.move(50,-87)
triangle2.draw(window)
triangle3 = triangle1.clone()
triangle3.move(-50,-87)
triangle3.draw(window)
Text(Point(150,20), "Please click to exit!").draw(window)
window.getMouse()
window.close()
