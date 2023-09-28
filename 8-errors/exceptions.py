def validate(x):
    if x < 1:
        raise Exception("The number must be greater than one")
    else:
        print(x)

validate(0.1)