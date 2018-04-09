# 概括字符集

import re

# \d \D
# \w \W 单词字符
# \s 空白字符 \S
# . 匹配除换行符之外其他所有字符

a = 'python 1111\tjav\ra&678\nphp'

# r = re.findall('\d', a)
# r = re.findall('[0-9]', a)
# r = re.findall('[^0-9]', a)
# r = re.findall('\w', a)
# r = re.findall('[A-Za-z0-9]', a)
# r = re.findall('[\W]', a)
r = re.findall('[\s]', a)
print(r)
