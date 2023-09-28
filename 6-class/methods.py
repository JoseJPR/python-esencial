class Person:
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

    def setAge(self, age):
        self.age = age

    def increaseAge(self):
        self.age += 1

jhonDoe = Person('Jhon', 'Doe')
print(jhonDoe)
print(jhonDoe.firstName)
print(jhonDoe.lastName)
jhonDoe.setAge(5)
print(jhonDoe.age)
jhonDoe.increaseAge()
print(jhonDoe.age)