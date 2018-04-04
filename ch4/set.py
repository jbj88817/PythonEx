print(type({1, 2, 3, 4, 5}))

print({1, 1, 2, 2, 3, 3, 4, 5})  # set 不重复

print(len({1, 2, 3}))

print(1 in {1, 3, 2})
print(1 not in {1, 3, 2})

print({1, 2, 3, 4, 5, 6} - {3, 4})  # 求集合差集 输出{1, 2, 5, 6}
print({1, 2, 3, 4, 5, 6} & {3, 4})  # 求集合交集 输出{3, 4}
print({1, 2, 3, 4, 5, 6} | {3, 4, 7})  # 求集合的合集 输出{1, 2, 3, 4, 5, 6, 7}

# empty set
set()
print(type(set()))  # <class 'set'>
