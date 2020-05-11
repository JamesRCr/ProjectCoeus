import timeit

def label(func):
    return func


test = label
helper = label


@test
def test_function(n):
    return n

print(test_function("Hello World"))


def timer(func):
    def inner(n):
        start = timeit.timeit()
        func(n)
        end = timeit.timeit()
        return f"{func.__name__}: {end-start}s"
    return inner


@timer
def test_function_2(n):
    return n*2

print(test_function_2(10))
