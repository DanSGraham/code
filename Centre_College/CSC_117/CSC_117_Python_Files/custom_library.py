###
### A custom library to make CSC 117 labs quicker
###By Daniel Graham
##
from graphics import *



#These save the buttons for use later
button_list = []
points_list = []
button_text_list = []

def button(win_name, button_name, x1,y1,x2,y2,buttontext, button_outline = None, button_fill=None, text_color=None, text_size = 12, text_style = 'normal', default = None):
    """Given 12 inputs window name, button name, points,
        text to input, and other options, this function draws a button and saves its points/name to lists for checking
        in button_checker. Order of input is:
        win_name, button name, position, text, outline, fill, text color, text size, text style"""

    #these lines establish the buttons_list and points_list as global variables

    global button_list
    global points_list
    global button_text_list
    
    #If the points are not given in the correct order this code rearranges them.
    if x1 > x2:
        x1,x2 = x2,x1
    if y1 > y2:
        y1, y2 = y2, y1


        
    #This code draws the button
    button_name = Rectangle(Point(x1, y1), Point(x2, y2))
    button_text = Text(Point((x1 + (x2-x1)/2), (y1+ (y2-y1)/2)), str(buttontext))
    button_name.draw(win_name)
    button_text.draw(win_name)

    #The next parts allow for colors!!!

    if button_outline != default or button_outline != '':
        button_name.setOutline(button_outline)
    if button_fill != default or button_fill != '':
         button_name.setFill(button_fill)
    if text_color != default or text_color != '':
        button_text.setTextColor(text_color)
    if text_size != default or text_size != '':
        button_text.setSize(text_size)
    if text_style != default or text_style != '':
        button_text.setStyle(text_style)
        
    #These lines store the button name and points for use later in the checker
    
    button_list.append(button_name)
    button_text_list.append(button_text)
    points_list.append(x1)
    points_list.append(y1)
    points_list.append(x2)
    points_list.append(y2)

    return button_name

    
def button_check(win_name):
    """This function takes button points and a window name and checks which button was clicked. Must have the lists named button_list and points_list"""

    #establishes global variables

    global button_list

    global points_list
    
    while True:
        clicked_point = win_name.getMouse()
        clicked_x = clicked_point.getX()
        clicked_y = clicked_point.getY()
        for i in range(len(button_list)):
            if clicked_x > points_list[i*4] and clicked_x < points_list[(2)+(4*i)] and clicked_y > points_list[1+4*i] and clicked_y < points_list[3 + 4*i]:
                return button_list[i]

def button_undraw(to_undraw):
    """This function undraws a list of buttons or single button from the window"""
    global button_text_list
    global button_list
    
    if type(to_undraw) == list :
        for button in to_undraw:
            button.undraw()
            index_of_text_undraw = to_undraw.index(button)
            button_text_list[index_of_text_undraw].undraw()
    elif type(to_undraw) != list :

        button = to_undraw
        button.undraw()
        index_of_text_undraw = button_list.index(button)
        button_text_list[index_of_text_undraw].undraw()
        button_list.remove(button)
        button_text_list.remove(button_text_list[index_of_text_undraw])
        

def test():
    window = GraphWin('Test Window')
    close_button = 0     #initialize the button variable
    close_button = button(window, close_button, 1,1,150,150, "close")#Set each button variable equal to the button it refers to
    no_close_button = 0
    no_close_button = button(window, no_close_button, 160,160,180,180, "No close")
    if button_check(window) == close_button:    #check which button variable is called
        print "Close!"
    elif button_check(window) == no_close_button:
        print "No close"

    

    
    #close_button.undraw() The issue with this approach is the text does not get undrawn. 
    button_undraw(close_button)#undraw desired buttons
    window.getMouse()
    button_undraw(button_list)
    window.getMouse
    window.close()


    #Running into errors still
    #For some reason the remaining list is not undrawing and the no close button has to be clicked twice to return its value
if __name__ == '__main__':
    test()       
