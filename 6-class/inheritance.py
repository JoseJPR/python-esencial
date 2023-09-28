class Person:
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

    def setAge(self, age):
        self.age = age

    def increaseAge(self):
        self.age += 1

class Employe(Person, object):
    def __init__(self, firstName, lastName, totalHoursWorked):
        super(Employe, self).__init__(firstName, lastName)
    
        self.totalHoursWorked = totalHoursWorked
        
    def setJob(self, jobName):
        self.jobName = jobName

    def increaseHoursWorked(self):
        self.totalHoursWorked += 1

johnDoe = Employe('John', 'Doe', 8)
johnDoe.setAge(50)
johnDoe.setJob('Dev')
print(johnDoe.jobName)
print(johnDoe.age)
print(johnDoe.totalHoursWorked)
johnDoe.increaseHoursWorked()
print(johnDoe.totalHoursWorked)