import time

def decorator(func):
  def wrapper(*args):
    print(time.time())
    func(*args)
  return wrapper

@decorator
def f4(name, age):
  print('this is a function -- ' + name + ' -- ' + age)

f4('dong', '13')

