import ch7.t.c9

print('name:' + (__name__ or 'No name'))  # name:__main__
print('package:' + (__package__ or 'no package'))
print('doc:' + (__doc__ or 'No doc'))
print('file:' + __file__)
