from functools import wraps


def add(a, b):
    return a + b


def print_function_name(func):
    @wraps(func)
    def logging(*args, **kwargs):
        print(func.__name__ + " was called")
        return func(*args, **kwargs)

    return logging


@print_function_name
def square(x):
    return x * x


def nested_function(a, b, c):
    def print_function_name(func):
        @wraps(func)
        def logging(*args, **kwargs):
            print(func.__name__ + " was called")
            return func(*args, **kwargs)

        return logging

    @print_function_name
    def multiply(a, b):
        return a * b

    return multiply(a / 2, b * 4) + c


class MyClass:
    def print_function_name(func):
        @wraps(func)
        def logging(*args, **kwargs):
            print(func.__name__ + " was called")
            return func(*args, **kwargs)

        return logging

    def divide(self, a, b):
        return a / b

    @print_function_name
    def power(self, a, b):
        return a ** b


if __name__ == "__main__":
    print(square(4))
    print(add(2, 3))
    print(nested_function(2, 3, 4))
    obj = MyClass()
    print(obj.divide(10, 2))
    print(obj.power(2, 4))
