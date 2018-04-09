import time


def decorator(func):
    def wrapper():
        print(time.time())
        func()

    return wrapper


@decorator
def f1():
    print('This is a function1')


f1()
# f = decorator(f1)
# f()
