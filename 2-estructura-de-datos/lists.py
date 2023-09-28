exampleA = ['a', 0, 1.2, True, 'b']
print(exampleA)
print(exampleA[0])
print(len(exampleA))
print(exampleA[0:3])

exampleA[0] = 'aa'

print(exampleA)

exampleA.append('other')

print(exampleA)

exampleB = ['python', 'js']

exampleA.extend(exampleB)
print(exampleA)