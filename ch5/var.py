# 注意区分值类型和引用类型
# int str tuple 不可变 值类型
# list set dict 可变 引用类型
a = 1
b = a
a = 3
print(b)  # 1

# 注意！！！
a = [1, 2, 3, 4, 5]
b = a
a[0] = '1'
print(a)  # ['1', 2, 3, 4, 5]
print(b)  # 注意 b的值也改变了 ['1', 2, 3, 4, 5]

# 函数变量名不要赋值，否则没法用，就会报错 比如type

b = 'hello'
print(id(b))
b = b + 'python'
print(id(b))  # 因为str是不可变，所以这个id，也就是内存地址改变了
