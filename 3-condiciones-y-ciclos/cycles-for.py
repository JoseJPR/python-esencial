for letter in 'hello':
    print(letter)

languages = ["javascript", "python"]
for language in languages:
    print(language)

cars = ["golf", "porsche"]
for car in cars:
    print(car)
    if car == "golf":
        break

bikes = ["triumph", "yamaha"]
for bike in bikes:
    if bike == "triumph":
        continue
    print(bike)

numbers = range(1, 5)
for number in numbers:
    print(number)