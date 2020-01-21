from index02 import Student

student = Student('xiaoming', 18)
student1 = Student('xiaoming1', 18)
student2 = Student('xiaoming2', 18)
student.say()
# student.__dohomework() # AttributeError: 'Student' object has no attribute '__dohomework'
# print(student.__score) # AttributeError: 'Student' object has no attribute '__score'
print(student._Student__score) # 私有变量 其实是被更换了名字 加了 _Student
student.__score = -1 # 等于新增了一个属性
print(student.__score) 

print(student.name)

# print(Student.name)

print(student.__dict__)  # {'name': 'xiaoming', 'age': 18}
print(Student.__dict__)  # {'__module__': 'index02', '__init__': <function Student.__init__ at 0x0079C610>, 'say': <function Student.say at 0x0079C658>, '__dict__': <attribute '__dict__' of 'Student' objects>, '__weakref__': <attribute '__weakref__' of 'Student' objects>, '__doc__': None}

# 类方法调用
Student.plus_sum()
student.plus_sum()

# 静态方法调用
student.add(1, 32)
Student.add(1, 32)
