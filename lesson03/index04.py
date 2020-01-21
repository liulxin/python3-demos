class Student():
  sum = 0
  def __init__(self,name,age):
    self.name = name
    self.age = age
    self.__score = 0
    self.__class__.sum += 1

  def do_homework(self):
    print(self.name + '--' + str(self.age) + '  is doing homework')
