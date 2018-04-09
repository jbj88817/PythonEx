# 装饰器接受参数

import time

def decorator(func):
    def wrapper(*args):
        print(time.time())
        func(*args)

    return wrapper


@decorator
def f1(func_name):
    print('This is a function1 ' + func_name)


@decorator
def f2(func_name, name2):
    print('This is a function2 ' + func_name + name2)


f1('test func')
f2('1 ', '2')
# f = decorator(f1)
# f()
