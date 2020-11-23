import functools

def print_function_name(func):
    @functools.wraps(func)  # An issue should be raised here
    def logging(*args, **kwargs):
        print(func.__name__ + " was called")
        return func(*args, **kwargs)
    return logging


def wraps(func):
    def wrap(*args, **kwargs):
        print("Not functool's wrap")
        return func(*args, **kwargs)

    return wrap


@wraps  # No issue here. This is fine.
def foo(x):
    print(x)


foo("DeepSource")
