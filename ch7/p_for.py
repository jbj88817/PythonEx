a = [['apple', 'orange', 'banana', 'grape'], (1, 2, 3)]
for x in a:
    for y in x:
        print(y)
else:
    print('EOF')

b = [1, 2, 3]
for x in b:
    if x == 2:
        break
    print(x)
else:
    print('EOF')  # 如果是break了，不会执行这句



