"""参数
1. 必须参数
2. 关键词参数
3. 默认参数
4. 可变参数
"""


def add(x, y):
    res = x + y
    return res


# 关键词参数
c = add(y=3, x=2)
# 代码可读性
