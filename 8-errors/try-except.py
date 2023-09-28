def validate_with_exception_error(x):
    if x < 1:
        raise Exception("The number must be greater than one")
    else:
        return x

try:
    result = validate_with_exception_error(0.1)
    print(result)
except Exception as err:
    print(err)

print("--------------------")

def validate_with_assertion_error(x):
    assert x > 1, "The number must be greater than one"
    return x

try:
    result = validate_with_assertion_error(1)
    print(result)
except AssertionError as err:
    print(err)