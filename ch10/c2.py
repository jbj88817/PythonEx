# 正则表达式
import re

a = 'C0C++4Java5C#9Python5JavaScript'

# 找数字
r = re.findall('\d', a)
print(r)  # ['0', '4', '5', '9', '5']
