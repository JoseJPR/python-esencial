class Person:
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

jhonDoe = Person('Jhon', 'Doe')
print(jhonDoe)
print(jhonDoe.firstName)
print(jhonDoe.lastName)