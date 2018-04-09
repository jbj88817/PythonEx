# 实例方法 类方法 静态方法


class Student:
    name = ''
    age = 0
    sum = 0
    __score = 0  # 私有的

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__score = 59
        self.__class__.sum += 1  # 实例方法里调用类变量

    def do_homework(self):
        print(self.name + ' is doing homework')

    @classmethod
    def plus_sum(cls):
        cls.sum += 1
        print(cls.sum)

    @staticmethod
    def add(x, y):
        print('This is a static method')
        print(Student.sum)  # 访问类变量
        return x + y


st1 = Student('haha', 18)
st2 = Student('lihai', 20)
Student.plus_sum()  # 用类调用类方法
st1.add(1, 2)
Student.add(1, 2)

st1.__score = -1  # 这种是动态添加了一个新的变量，并不是原class里面的
print(st1.__score)  # 上面添加过了，这里能访问
print(st1.__dict__)  # {'name': 'haha', 'age': 18, '_Student__score': 59, '__score': -1}

print(st1._Student__score)
st1._Student__score = 60  # 居然能更改私有变量...
print(st1._Student__score)
