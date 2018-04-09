# * 匹配0次或者无限多次
# + 匹配1次或者无限多次
# ? 匹配0次或者1次

import re

a = 'pytho0python1pythonn2'

# r = re.findall('python*', a)  # ['pytho', 'python', 'pythonn']
# r = re.findall('python+', a)  # ['python', 'pythonn']
# r = re.findall('python?', a)  # ['pytho', 'python', 'python']
# r = re.findall('python{1,2}', a)  # ['python', 'pythonn']
r = re.findall('python{1,2}?', a)  # ['python', 'python']
print(r)
