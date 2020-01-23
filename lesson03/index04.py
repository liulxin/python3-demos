from index06 import People


class Student(People):

    def __init__(self, school, name, age):
        self.school = school

        # People.__init__(self, name, age)
        super(Student, self).__init__(name, age)

    def do_homework(self):
        # super(Student, self).do_homework()
        print(self.name + '--' + str(self.age) + '  is doing homework')
