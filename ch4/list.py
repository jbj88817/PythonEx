print(["hello", "world", 1, 9, True, False])
print([["hello", "world", 1, 9, True, False], [5, 6, "cool"]])

print(["hello", "world", 1, 9, True, False][2])
print(["hello", "world", 1, 9, True, False][-1:])  # 返回的False 是列表，因为有冒号

print(["hello", "world", 1, 9, True, False] + ["cool"])

print(3 in [1, 2, 3, 4, 5, 6])
print(10 in [1, 2, 3, 4, 5, 6])
print(3 not in [1, 2, 3, 4, 5, 6])

print(len([1, 2, 3, 4, 5, 6]))
print(len("hello"))

print(max([1, 2, 3, 4, 5, 6]))
print(min([1, 2, 3, 4, 5, 6]))

print(max("hello world"))  # w
print(min("hello world"))  # 输出空格

# 输出asc11
print(ord('w'))  # 119
print(ord('d'))  # 100
print(ord(' '))  # 32
