class Student():
    # 类变量
    # name = ''
    sum = 0
    age = 0

    def __init__(self, name, age):
        # 实例变量
        self.name = name
        self.age = age
        self.__score = 0
        # print(name) # xiaoming
        # print(age)  # 18
        print(Student.age)
        print(self.__class__.age)
        self.__class__.sum += 1
        print('当前学生总数为：' + str(self.__class__.sum))

    def say(self):
        print('my name is ' + self.name + 'my age is ' + str(self.age))
        self.__score = 10
        self.__dohomework()

    # 类方法 cls -- 同时可以被实例和类调用
    @classmethod
    def plus_sum(cls):
        print(cls.sum)

    # 静态方法 -- 同时可以被实例和类调用
    @staticmethod
    def add(x, y):
        print(Student.sum + x + y)

    def __dohomework(self):
      print('homework')

# 公开的 public
# 私有的 private 加 __ 设置为私有
# 方法私有化后，外部访问会报错，而属性却没有，原因是：由于python语言特性，其实是动态添加了一个新的属性

