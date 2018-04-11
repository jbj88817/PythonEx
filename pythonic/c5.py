# 生成器
# print 0~10000

def gen(max):
    n = 0
    while n <= max:
        # print(n)
        n += 1
        yield n


g = gen(10000)
for i in g:
    print(i)
