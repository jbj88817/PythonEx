# 函数式编程
# 闭包 = 函数+环境变量

# python一切皆对象
# 函数当作另外一个函数传递到别的函数的参数里


def curve_pre():
    a = 25

    def curve(x):
        return a * x * x

    return curve


f = curve_pre()
print(f(2))

a = 10
print(f(2))  # 还是一个结果，因为会取闭包中的环境变量
print(f.__closure__[0])
print(f.__closure__[0].cell_contents)
