class Student:
    """A class to model a student with name, id and list of test grades"""
    def __init__(self, name, id):
        """initializes the name and id number; sets list of grades to []"""
        self.s_name = name
        self.ident = id
        self.tests=[]
  
    def get_name(self):
        """ returns the student name"""
        return self.s_name
    def get_id(self):
        return self.ident
    def addtest(self,t):
        """adds a grade to the list of test grades """
        self.tests.append(t)

    def gettests(self):
        return self.tests
    
    def __str__(self):
        """returns the student name and the current list of grades"""
        return self.s_name + ", Test Grades:" + str(self.tests) + "  " 

    def comp_av(self):
        """returns the average of the current set of grades or 'no grades'
        if appropriate"""
        if len(self.tests) > 0:
            sum = 0.0
            for item in self.tests:
                sum = sum + item
            average = float(sum)/len(self.tests)
            return average
        else:
            return "no grades"


