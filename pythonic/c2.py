# 列表推导式
# set, tuple, dict也可以被推导

a = [1, 2, 3, 4, 5, 6, 7, 8]

# b = [i ** 3 for i in a]
b = [i ** 3 for i in a if i >= 5]
print(b)
