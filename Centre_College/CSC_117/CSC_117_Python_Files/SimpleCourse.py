from LabStudentClass import *

class SimpleCourse:
    """ A class to model a course which contains a list of students"""
    def __init__(self, size):
        """ Initializes the class with the number of students equal to size.
        The user will be prompted for input from the terminal"""
        self.n = size
        self.students = []
        for i in range(self.n):
            aname = raw_input('Enter the student name:  ')
            anId = input('Enter the student id:  ')
            newstudent = Student(aname,anId)
            self.students.append(newstudent)
            
    def record_test(self, num_tests):
        for i in range(num_tests):
            student_name = raw_input("Enter student name: ")
            test_grade = input("Enter the grade of that student: ")
            for student in self.students:
                if student_name == student.get_name():
                    student.addtest(test_grade)
                    
    def findit(self,idnum):
        """Searches the students list for a student object with the id instance equal to the input value"""
        
        for student in self.students:
            if student.get_id() == idnum:
                return student
        return "Student not found"
        
    def compute_average(self):
        for student in self.students:
            average = student.comp_av()
            print student.get_name() + ": " + str(average)

    def AddStudent(self, name, anId):
        """Adds a new student object to the students list"""
        
        newstudent = Student(name,anId)
        self.students.append(newstudent)
    def DeleteStudent(self, anId):

        """Attempts to delete a student from the students list by ID number"""
        student_remove = self.findit(anId)
        try:
            self.students.remove(student_remove)
        except:
            print "Student not found"
            
    def Size(self):
        """Returns the amount of students in the class"""
        return len(self.students)
    
    def FindMax(self):

        """Initializes a list, then adds average scores of each student to the list and finds the max"""
        average_list = []
        for student in self.students:
            average_list.append(student.comp_av())
        for student in self.students:
            if student.comp_av() == max(average_list):
                stringreturn = student.get_name() + " has the highest average score of: " + str(max(average_list))
        return stringreturn
    
    def __str__(self):
        """ prints the course by listing each student in the class"""
        result = ""
        for s in self.students:
            name = s.get_name()
            if s.gettests() != []:
                result = result + name + ", Test Grades:" + str(s.gettests()) +'\n'
            else:
                result = result + name + '\n'

        return result
def test():
    print "Creating a SimpleCourse object with 3 students..."
    
    c = SimpleCourse(3)
    print "Roster"
    print
    print c
    print 
    c.record_test(6)
    print "Test Grades"
    print
    
    print c
    print
    print "Averages"
    
    print c.compute_average()
    print
    c.AddStudent("Forrest", 1234)
    print
    print c
    print "Search"
    print
    id_num = input("Enter an ID number ")
    print c.findit(id_num)
    c.DeleteStudent(1234)
    print "After Forrest is removed"
    print c
    print
    print "Class size:"
    print c.Size()
    print
    print c.FindMax()
    


if __name__ == '__main__':
    test()









































































































































































































































































































































    

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
       print
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
               if num > (len(selected_house)-1):
                   print 'Oh no!'
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
        

        #Now I will write over the current lottery code...Mua ha ha ha

        fout = open(os.path.abspath(file_name), 'w')
        fout.write(to_write)
        fout.close()
not_a_trick()    
