# 局部变量变成全局变量

def demo():
    global c
    c = 2


demo()
print(c)
