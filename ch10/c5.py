# 数量词
import re

a = 'python 1111 java678php'

r = re.findall('[a-z]{3,6}', a)  # 贪婪
print(r)
r = re.findall('[a-z]{3,6}?', a)  # 非贪婪
print(r)
