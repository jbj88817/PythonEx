# 第三个参数的匹配模式

import re

a = 'PythonC#\nJavaPHP'

r = re.findall('c#.{1}', a, re.I | re.S)  # re.I是说忽略大小写，re.S是说.可以匹配任意字符
print(r)
