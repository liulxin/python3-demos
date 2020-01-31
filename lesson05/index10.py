# 装饰器

import time

def f1():
  print(time.time()) # 1580464825.2168288  unix 时间戳
  print('this is a func')

f1()

# ````
def f2():
  print('this is a function')

def print_cur_time(func):
  print(time.time())
  func()

print_cur_time(f2)
# ````

def decorator(func):
  def wrapper():
    print(time.time())
    func()
  return wrapper

# def f3():
#   print('this is a function')

# decorator(f3)()

@decorator
def f4():
  print('this is a function')

f4()