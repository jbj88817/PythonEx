# 装饰器 / 注解

import time


def f1():
    print('This is a function1')


def f2():
    print('This is a function2')


def print_current_time(func):
    print(time.time())
    func()


print_current_time(f1)
print_current_time(f2)
