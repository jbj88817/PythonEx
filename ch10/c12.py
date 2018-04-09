# 分组 可以用于爬虫
import re

a = 'life is short, i use python'

r = re.search('life(.*)python', a)
print(r.group(1))

r = re.findall('life(.*)python', a)
print(r)

a = 'life is short, i use python, i love python'

r = re.search('life(.*)python(.*)python', a)
print(r.group(0, 1, 2))
print(r.groups())  # 只返回分组
