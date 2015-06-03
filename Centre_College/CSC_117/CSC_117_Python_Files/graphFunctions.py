#
#A program to create a button
# By Daniel Graham



def isInside(rectangle_x1,rectangle_y1,rectangle_x2, rectangle_y2, point_x, point_y):
    if rectangle_x1 > rectangle_x2:
        rectangle_x1,rectangle_x2 = rectangle_x2,rectangle_x1
    if rectangle_y1 > rectangle_y2:
        rectangle_y1, rectangle_y2 = rectangle_y2, rectangle_y1
        
    

    if point_x > rectangle_x1 and point_x < rectangle_x2 and point_y > rectangle_y1 and point_y < rectangle_y2:
        return True
    else:
        return False

def biggerCircle(radius_circle1, radius_circle2):
    if radius_circle1 > radius_circle2:
        return 1
    elif radius_circle1 < radius_circle2:
        return 2
    else:
        print "The circles are the same area!"

def listOfRectangles(rectangle_list, point_x, point_y):
    for j in range(0,len(rectangle_list),4):
        if point_x > rectangle_list[j] and point_x < rectangle_list[j+2] and point_y > rectangle_list[j+1] and point_y < rectangle_list[j+3]:
            return rectangle_list[j], rectangle_list[j+1], rectangle_list[j+2], rectangle_list[j+3], j
    return -1
        
    
    
