# 可变参数


def demo(*param):
    print(param)
    print(type(param))


demo(1, 2, 3, 4, 5)

a = (1, 2, 3, 4)
demo(a)  # ((1, 2, 3, 4),)
demo(*a)  # (1, 2, 3, 4) 加星号是说我传的这个元祖不要成为二维元祖


def demo1(param1, *param, param2='2'):
    print(param1)
    print(param)
    print(param2)


demo1('a', 1, 2, 3, param2='param')
