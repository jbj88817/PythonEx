students = {
    'haha': 18,
    'bojie': 20,
    'xiao': 22
}

# b = [key for key, value in students.items()]
b = {value: key for key, value in students.items()}
print(b)

b = (key for key, value in students.items())
for x in b:
    print(x)
