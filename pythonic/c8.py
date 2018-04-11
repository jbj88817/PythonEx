# 装饰品的副作用

import time
from functools import wraps


def decorator(func):
    @wraps(func)
    def wrapper():
        print(time.time())
        func()

    return wrapper


@decorator
def f1():
    """
    This is f1
    """

    print(f1.__name__)  # 有了装饰器，函数名就要改变, 解决方法是加上warps


f1()
