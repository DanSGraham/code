#
#A program to create an employee class
#By Daniel Graham

class Employee:
    def __init__(self, employee_name, hourly_rate, department_key):
        self.name = employee_name
        self.payrate = hourly_rate
        self.department = department_key
        self.sexual_harrassment = "No" # I would hope you did not hire someone who sexually harrassed another employee
    def getHourlyRate(self):
        return self.payrate
    
    def changeHourlyRate(self, new_rate):
        self.payrate = new_rate
        
    def getName(self):
        return self.name

    def changeName(self, new_name):
        self.name = new_name

    def getDepartment(self):
        return self.department

    def setDepartment(self, new_department):
        self.department = new_department

    def sexualHarrassment(self,has_harrassed):
        self.sexual_harrassment = has_harrassed

    def calc_pay(self, hours):
        return (self.payrate) * float(hours)

    def __str__(self):
        if self.sexual_harrassment != 'No':
            return self.name + "'s contract has been terminated due to sexual harrassment charges."
        else:
            return self.name + " has an hourly rate of $%0.2f and works in department " %self.payrate +self.department+"."
def main():
    ford_prefect = Employee('Ford Prefect', 9.50, 'H')
    zaphod_beeblebrox = Employee("Zaphod Beeblebrox", 8.50, 'G')
    tricia_mcmillan = Employee("Tricia McMillan", 7.50, 'G')
    sirius_black = Employee("Sirius Black", 9.00 , 'H')
    bilbo_baggins = Employee("Bilbo Baggins", 8.50, 'G')
    elizabeth_montgomery = Employee("Elizabeth Montgomery", 8.00, 'G')
    emp_list = [ford_prefect, zaphod_beeblebrox, tricia_mcmillan, sirius_black, bilbo_baggins, elizabeth_montgomery]
    print sirius_black
    sirius_black.setDepartment('G')
    print sirius_black
    print
    print elizabeth_montgomery
    elizabeth_montgomery.changeHourlyRate(8.50)
    print elizabeth_montgomery
    print
    print "Bilbo would earn $%0.2f in 40 hours." %(bilbo_baggins.calc_pay(40))
    print
    zaphod_beeblebrox.sexualHarrassment("Yes")
    for employee in emp_list:
        print employee


if __name__ == '__main__':
    main()
    
    
        
