class Person:
    pass

jhonDoe = Person()
print(type(jhonDoe))

otherPerson = Person()
print(type(otherPerson))

print(jhonDoe == otherPerson)

class Car:
    def __init__(self):
        print('Hi from constructor')

carA = Car()
