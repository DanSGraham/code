#A program to graph input data
#By Daniel Graham

from graphics import *
from time_conversion import convert_to_seconds
from better_button import *

class headlineDataPoint:

    def __init__(self, headline_string):

        self.headline = headline_string.split(' @ ')[0]
        self.time = convert_to_seconds(headline_string.split(' @ ')[1])

    def getX(self):

        return (100 + 800*((self.time)- 34200)/(23400))

    def getHeadline(self):

        return self.headline
    
class stockDataPoint:

    def __init__(self, stock_string):

        self.price = float(stock_string.split(' @ ')[0][1:])
        self.time = convert_to_seconds(stock_string.split(' @ ')[1])

    def getPoint(self):

        return (self.time, self.price)

def ticks(win, points_list1):
    """Draws tickmarks on graph axis"""
    #This function sets and draws tickmarks
    values_list = []
    for point in points_list1:
       values_list.append(point.price)
       
    max_price = max(values_list)
    min_price = min(values_list)

    y_axis_max = max_price * 1.001
    y_axis_min = min_price *.999

    difference_per_tick = (y_axis_max - y_axis_min)/9.0
    distance_per_tick = (650-150)/9.0
    for j in range(10):
        price = '$%.2f' % (y_axis_min + difference_per_tick * j)
        price_text = Text(Point(65,650 - distance_per_tick * j), price)
        tick = Line(Point(90, 650 - distance_per_tick * j), Point(100, 650 - distance_per_tick * j))
        price_text.draw(win)
        tick.draw(win)
    time = 9
    for i in range(14):
        
        if i%2 == 0:
            minutes = ':30'
        else:
            minutes = ':00'
            time += 1
        time_text = Text(Point(100 + (800/13)*i,700), str(time) + minutes)
        tick = Line(Point(100 + (800/13)*i , 660), Point(100 + (800/13)*i, 650))
        time_text.draw(win)
        tick.draw(win)
                    
        
    
def adjust_points(points_list1):
    """This converts the points data into numbers that fit on my graph window"""

    ##I tried adjusting the coordinates of the window, however the x axis is so disproportinate to the y axis
    ## that the graph would not show a line. So I instead made the points fit on the graph.
    values_list = []
    adjusted_points = []
    for point in points_list1:
       values_list.append(point.price)
       
    max_price = max(values_list)
    min_price = min(values_list)

    y_axis_max = max_price * 1.001
    y_axis_min = min_price * 0.999
    x_axis_min = 9*3600 + 30 * 60
    x_axis_max = 16 * 3600

    
    for point1 in points_list1:
        new_x = 100 + 800*((point1.getPoint()[0])- x_axis_min)/(x_axis_max-x_axis_min)
        new_y = 650 - 500*((point1.getPoint()[1])- y_axis_min)/(y_axis_max-y_axis_min)
        new_point = Point(new_x, new_y)
        adjusted_points.append(new_point)
    return adjusted_points

def plotStockLine(win,point_list):
    """This function plots the trendline of a series of points"""
    
    for j in range(1,len(point_list)):
        newLine = Line(point_list[j-1], point_list[j])
        newLine.draw(win)
        
        

def search():
    
    """This function creates a graphical window that prompts the user for which data they would like to display"""
    
    
    window = GraphWin('Search for Stock', 500, 500)
    title = Text(Point(250, 100),"Enter the company and date you wish to view")
    title.draw(window)
    date_entry_text = Text(Point(150, 200), "Enter Date(d/mm/yyyy):")
    company_entry_text = Text(Point(150, 300), "Enter the company you wish to search:")
    date_entry = Entry(Point(300, 200), 10)
    company_entry = Entry(Point(350, 300), 12)
    company_entry.draw(window)
    company_entry_text.draw(window)
    date_entry_text.draw(window)
    date_entry.draw(window)
    submit_button = Button(Point(250, 400), 200, 40, "Search")
    submit_button.draw(window)
    while not submit_button.clicked(window.getMouse()):
        window.checkMouse()
    date = date_entry.getText()
    company = company_entry.getText()
    window.close()
    return (date, company)





def GUI(dateandcompany):
    """This function takes a tuple of a date and company name and creates a graph from the corresponding text file"""
    
    try:
        stockfout = open('data/' + dateandcompany[1] + 'StockSalePrices.txt', 'r')
        text = stockfout.readlines()
        points_list = []
        headlines_list = []
        values_list = []
        if dateandcompany[0]+'\n' in text:
            position1 = text.index(dateandcompany[0]+'\n')
            while text[position1 + 1][0] == '$':
                point = stockDataPoint(text[position1 + 1])
                points_list.append(point)
                position1 += 1
                if len(text) == position1+1:
                    break
        stockfout.close()
        try:
            filenotfound = False
            headlines_fout = open('data/' + dateandcompany[1] + 'Headlines.txt', 'r')
            text = headlines_fout.readlines()
            if dateandcompany[0]+'\n' in text:
                position1 = text.index(dateandcompany[0]+'\n')
                while len(text[position1 + 1]) > 11 :
                    headline = headlineDataPoint(text[position1 + 1])
                    headlines_list.append(headline)
                    position1 += 1
                    if len(text) == position1+1:
                        break
            headlines_fout.close()
        except:
            filenotfound = True
     
        win = GraphWin("Stock Prices over Time", 1000,800)
        title = str(dateandcompany[1])+ " Stock Prices"
        x_axis_title = "Time of Price"
        y_axis_title = "Price"
        title_draw = Text(Point(500,100), title)
        title_draw.draw(win)
        x_axis_draw = Text(Point(500, 750), x_axis_title)
        y_axis_draw = Text(Point(20, 400), y_axis_title)
        x_axis_draw.draw(win)
        y_axis_draw.draw(win)
        graph_box = Rectangle(Point(100, 150), Point(900, 650))
        graph_box.setFill('white')
        graph_box.draw(win)
        ticks(win, points_list)
        plotStockLine(win, adjust_points(points_list))
        for headline in headlines_list:
            headline_text = Text(Point(500, 20), "Relevant headlines appear as red lines")
            headline_text.draw(win)
            headLine = Line(Point(headline.getX(), 150), Point(headline.getX(), 650))
            headLine.setFill('red')
            headLine.draw(win)
        close_button = Button(Point(950, 50), 50, 50, "Close")
        close_button.draw(win)
        while not close_button.clicked(win.getMouse()):
            nope = 'nope'    
        win.close()
    except:
        print "Sorry, something went wrong!"
        GUI(search())

GUI(search())
            
