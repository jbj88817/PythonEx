# 字符串、列表、元祖比较大小，会重头一个一个char比较，发现不一样的，比较asc11，然后返回结果
print('acb' < 'ada')  # True
print([1, 2, 3] < [2, 3, 4])  # True
