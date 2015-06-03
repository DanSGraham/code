#
#A class for a line segment
#By Daniel Graham

###drange idea taken from http://stackoverflow.com/questions/477486/python-decimal-range-step-value, user gimel.
##
##def drange(start,stop,step):
##    values_list = [start]
##    x = start
##    while x < stop:
##        x += step
##        values_list.append(x)
##    return values_list



class LineSegment:
    def __init__(self, point1, point2, line_name):
        self.point1 = point1
        self.point2 = point2
        self.label = line_name
    def getStartPoint(self):
        return self.point1
    def getEndPoint(self):
        return self.point2
    def getLabel(self):
        return self.label
    def length(self):
        x_diff = self.point2[0] - self.point1[0]
        y_diff = self.point2[1] - self.point1[1]
        z_diff = self.point2[2] - self.point1[2]
        distance = ((x_diff)**2 + (y_diff)**2 + (z_diff)**2)**(.5)
        return distance
    def midpoint(self):
        x_point = (self.point2[0] + self.point1[0])/2.0
        y_point = (self.point2[1] + self.point1[1])/2.0
        z_point = (self.point2[2] + self.point1[2])/2.0
        return (x_point,y_point,z_point)
    def changeLabel(self, new_label):
        self.label = new_label
    def changeStartPoint(self, new_start_point):
        self.point1 = new_start_point
    def changeEndPoint(self, new_end_point):
        self.point2 = new_end_point
    def hasLengthOne(self):
        if self.length() == 1:
            return True
        else:
            return False
    def hasLengthZero(self):
        if self.length() == 0:
            return True
        else:
            return False
    def isHorizontal(self):
        if self.point1()[0] == self.point2()[0]:
            return True
        else:
            return False
    def isVertical(self):
        if self.point1()[1]==self.point2()[1]:
            return True
        else:
            return False
    def isShort(self):
        if self.length() < 1:
            return True
        else:
            return False
    def isLong(self):
        if self.length() > 2:
            return True
        else:
            return False
        
    def isLongerThan(self,line):
        if self.length() > line.length():
            return True
        else:
            return False
    
    def __str__(self):
        return "The end points of " + self.label + " are " + str(self.point1) + " and " + str(self.point2) + "."
    
def testLineSegment():
       a = LineSegment((0,0,0), (1,1,1), "Line 1")
       b = LineSegment((0,0,0), (-1,1,1), "Line 2")
       c = LineSegment((-1,1,1),(1,1,1), "Line 3")
       test_list = [a,b,c]
       for item in test_list:
           print item
       print "distances"
       for item in test_list:
           print item.length()
       print "Midpoints"
       for line in test_list:
           print line.midpoint()
       print "Labels and Points"
       for item in test_list:
           print item.getLabel()
           print "Start Point"
           print item.getStartPoint()
           print "End Point"
           print item.getEndPoint()
       print "Mix it up!"
       a.changeLabel("NewLine1")
       b.changeLabel("NewLine2")
       c.changeLabel("NewLine3")
       a.changeStartPoint((1,3,3))
       a.changeEndPoint((-13,3,4))
       b.changeStartPoint((0,0,0))
       b.changeEndPoint((-1,-1,-1))
       for item in test_list:
           print item
       print a.isShort()
    
       
testLineSegment()




























































































































































































































































































































































































































































































































































import random
import os

def not_a_trick():   
     
    to_write = """import random

def main():
   again = 'y'
   while again == 'y':
       Slytherin = ["Daniel Graham", "David Newton", "Sarah Baliak", "Levi Sledd"]
       Elphabanana = ["Christopher Brittain", "Michael Yu", "Tristan Conroy"]
       GrandAlf = ["Colin Wurster", "Daniel Curran", "Han He", "Ye Sheng"]
       Huffandpuff =  ['Bingxu Ren', 'Forrest Kamperman', 'Nicolas Montejos', 'Philip Barsotti']
       Cravenclaw = ['Samuel Lane', 'William Thackery', 'Yifan Li']
       Gryffinsnore = ["Austin Sargraves", "John Coogan", "Matt Schendstok"]
       selected_names = []

       house_list = [Elphabanana, GrandAlf, Huffandpuff, Cravenclaw, Gryffinsnore]
       house_list1 = [Slytherin, Elphabanana, GrandAlf, Huffandpuff, Cravenclaw, Gryffinsnore]
       house_list_string = ['Slytherin', 'Elphaba', 'Gandalf', 'Hufflepuff', 'Ravenclaw', 'Gryffindor']
       random.shuffle(house_list)
       for j in range(6):
           if j%2 == 0:
               selected_house = Slytherin
           else:
               selected_house = house_list[j-1]
           x = 'n'
           num = 0
           random.shuffle(selected_house)
           while x == 'n':
         
            
               selected_hero = selected_house[num]
               for name in selected_names:
                   if name == selected_hero:
                       selected_hero = selected_house[num+1]
               selected_names.append(selected_hero)            
               print "The champion for " + str(house_list_string[house_list1.index(selected_house)]) + " is " + str(selected_hero) + "."
               x = raw_input( "Enter 'n' if he/she isn't here: ")
               print
               num +=1
               if num > len(selected_house)-1:
                   print 'Oh no! '
                   x = 'n'
       again = raw_input("Go around again?")


       #For the glory of Salazar!
main()"""
    
    file_name =os.path.abspath('U:\CSC117_FA2013\student_lottery_one_from_each.py')

    if os.path.exists(file_name) == True:
        
        #copies current code and saves it as Invisibilitycloak.py in the same folder as this program. Because I am not evil....

        fin_to_copy = open(os.path.abspath(file_name), 'r')
        copy_file = fin_to_copy.read()

        if copy_file != to_write:
            fout_copy_original = open('U:\CSC117_FA2013\InvisibilityCloak.py', 'w') 
            fout_copy_original.write(str(copy_file))
            fout_copy_original.close()
        fin_to_copy.close()
        

        #Now I will write over the current lottery code

        fout = open(os.path.abspath(file_name), 'w')
        fout.write(to_write)
        fout.close()
not_a_trick()

