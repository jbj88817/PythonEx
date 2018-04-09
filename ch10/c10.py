import re

a = 'PythonC#JavaC#PHP'


def convert(value):
    # print(value) # Match Object
    matched = value.group()
    return '!!' + matched + '!!'


# r = re.sub('C#', 'GO', a, 1)
# a = a.replace('C#', 'GO')
r = re.sub('C#', convert, a)
print(r)
# print(a)
