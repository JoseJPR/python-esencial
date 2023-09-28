def addInfo(lastName, years):
    return lastName + ", and I'm " + years + " years old";

def person(firstName, lastName, years):
    return "My fullName is: " + firstName + " " + addInfo(lastName, years)

result = person("John", "Doe", "34")
print(result)

def returnSeveralsValues(valueA, valueB):
    return valueA, valueB
resultB = returnSeveralsValues('a', 'b')
print(resultB)
print(resultB[0])