from functools import reduce

list_x = ['1', '2', '3', '4', '5']
# 连续计算，连续调用lambda
r = reduce(lambda x, y: x + y, list_x, 'aaa')
print(r)

# (((1 + 2) + 3) + 4) + 5
