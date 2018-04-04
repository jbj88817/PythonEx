# 定义一个元组
tuple1 = ()
tuple1 = tuple({1, 2, 3, 4, 5, '6'})
tuple1 = (1, 2, '3', 4, '5')
# 定义了一个元组之后就无法再添加或修改元组中的元素,但是可以重新赋值
print(tuple1[0])  # 元组的元素都有确定的顺序。元组的索引也是以0为基点的
print(tuple1[-1])  # 负的索引从元组的尾部开始计数
print(tuple1[1:3])  # 元组也可以进行切片操作。对元组切片可以得到新的元组。
# 可以使用 in 运算符检查某元素是否存在于元组中。
print(1 in tuple1)  # True
# 使用for in 进行遍历元组
for item in tuple1:
    print(item)

print(type((1)))
print(type((1,)))
print(type(()))
