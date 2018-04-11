# None != 空列表等等

a = []
if not a:
    print('T')
else:
    print('F')

if a is None:
    print('T')
else:
    print('F')