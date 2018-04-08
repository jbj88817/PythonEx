c = 10  # 全局变量


def demo():
    c = 50
    # 没有块级作用域
    for i in range(0, 9):
        a = 'a'
        c += 1
    print(a)
    print(c)


demo()
