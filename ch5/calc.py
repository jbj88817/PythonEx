# 字符串、列表、元祖比较大小，会重头一个一个char比较，发现不一样的，比较asc11，然后返回结果
print('acb' < 'ada')  # True
print([1, 2, 3] < [2, 3, 4])  # True
print({1, 2, 3} < {1, 2, 4})

a = 1
b = 2
# 判断值
print(a == b)
# 判断id 身份 内存地址
print(a is b)
# 判断类型
print(isinstance(a, str))
print(isinstance(a, (str, int, float)))

# >>> []>{}
# True
# >>> []>set()
# False
# >>> set()>'1'
# False
# >>> 1>1.0
# False
# >>> 1>=1.0
# True
# >>> '1'>1.0
# True
# >>> set()>1.0
# True
# >>> [1]>[2]
# False
# >>> [1]>[0]
# True

# CPython implementation detail: Objects of different types except
#  numbers are ordered by their type names; objects of the same types that
#  don’t support proper comparison are ordered by their address.
