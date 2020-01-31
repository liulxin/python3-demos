def add(x,y):
  return x + y

add(1,2)

# 匿名函数

f = lambda x,y: x + y
f(1,2)

# 三元表达式

# x > y ? x : y

x = 1
y = 3
r = x if x > y else y

print(r) # 3