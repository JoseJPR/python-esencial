language = {
    "name": "phyton",
    "creator": "bla bla bla"
}

for key in language:
    print("key", key)
    print("value", language[key])

print("---------------")

for item in language.items():
    print("item", item)
    print("key", item[0])
    print("value", item[1])

print("---------------")

for key, value in language.items():
    print(key, value)