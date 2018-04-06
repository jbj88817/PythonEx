for x in range(0, 10, 2):
    print(x, end=' | ')

print('\n')

for x in range(10, 0, -2):
    print(x, end=' | ')

print('\n')

a = [1, 2, 3, 4, 5, 6, 7, 8]
# print out 1, 3, 5, 7

# Method 1
for i in range(0, len(a), 2):
    print(a[i], end=' | ')

print('\n')

# Method 2
b = a[0:len(a):2]
print(b)  # [1, 3, 5, 7]
