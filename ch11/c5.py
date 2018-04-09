# 重点理解的闭包

def f1():
    a = 10

    def f2():
        # a此时被Python认为是一个局部的变量
        a = 20
        print(a)  # 20

    print(a)  # 10
    f2()
    print(a)  # 10


f1()
