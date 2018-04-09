def f1():
    a = 10

    def f2():
        # a 被认为是一个局部变量
        a = 20  # 有这个就不会是闭包
        return a

    return f2


f = f1()
print(f)
print(f.__closure__)
