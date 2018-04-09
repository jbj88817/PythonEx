# 枚举

from enum import Enum
from enum import IntEnum, unique


class VIP(Enum):
    YELLOW = 1
    YELLOW_AlIAS = 1  # 可以是取数值相等，意义是别名
    GREEN = 2
    BLACK = 3
    RED = 4


print(VIP.BLACK)
print(VIP.RED.value)
print(VIP.GREEN.name)
print(type(VIP.BLACK))  # <enum 'VIP'>
print(type(VIP.GREEN.name))  # <class 'str'>
print(VIP['GREEN'])  # VIP.GREEN
# VIP.YELLOW = 6  # 报错 原因是不能更改枚举值

print('~~~~~~~~~~~~~')
for v in VIP:
    print(v)

print('~~~~~~~~~~~~~')
# 可以等值比较，不能大小比较
res = VIP.BLACK == VIP.GREEN
print(res)
res = VIP.RED is VIP.BLACK
print(res)

print('~~~~~~~~~~~~~')
a = 1
print(VIP(a))  # VIP.YELLOW


@unique  # 有这个value不能相同
# 这个class里面必须是int
class VIP1(IntEnum):
    GOOD = 1
    YEAH = 2

# 枚举类型是单例模式
