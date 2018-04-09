# 正则表达式
import re

a = 'C|C++|Java|C#|Python|JavaScript'

print(a.index('Python'))  # 可以用 >-1 判断里面有没有这个元素
print('Python' in a)

r = re.findall('Python', a)
if len(r) > 0:
    print('include')
print(r)


