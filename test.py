
def label(func):
    return func


test = label


@test
def test_function(n):
    return n


print(test_function("Hello World"))
