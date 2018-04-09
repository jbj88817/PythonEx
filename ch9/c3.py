class Student:
    name = ''
    age = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def do_homework(self):
        print(self.name + ' is doing homework')


st = Student('Bojie', 18)
st.do_homework()
print(st.__dict__) # 打印实例里的变量
