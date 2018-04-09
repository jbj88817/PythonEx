# 装饰器接受关键字参数

import time


def decorator(func):
    def wrapper(*args, **kw):
        print(time.time())
        func(*args, **kw)  # 所有参数都适用

    return wrapper


@decorator
def f3(func_name1, func_name2, **kw):
    print('This is a function2 ' + func_name1)
    print('This is a function2 ' + func_name2)
    print(kw)


f3('test1', 'test2', a=1, b=2, c='123')
