# 继承
from ch9.c6 import Human


class Student(Human):
    # sum = 0
    def __init__(self, school, name, age):
        # self.__score = 0
        # self.__class__.sum += 1  # 实例方法里调用类变量
        self.school = school
        # Human.__init__(self, name, age)
        super(Student, self).__init__(name, age)

    def do_homework(self):
        super(Student, self).do_homework()
        print('homework')


st1 = Student('Wenquan', 'haha', 18)
Student.do_homework(st1)  # 可以这么玩儿，但是当然不建议
# Student.do_homework('')  # 还可以这么玩儿，可能会报错，但是当然不建议
print(st1.sum)
print(Student.sum)
print(st1.name)
print(st1.age)
print(st1.school)
# st1.get_name()
