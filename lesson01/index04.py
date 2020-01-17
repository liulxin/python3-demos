# 元组

print((1, 2, 3, 4))

# 元组只有一个元素时需要加逗号

print(type((1,2))) # <class 'tuple'>
print(type(('hello'))) # <class 'str'>
print(type(('hello',))) # <class 'tuple'>
print(type((2,))) # <class 'tuple'>
print(type((2))) # <class 'int'>
print(type(())) # <class 'tuple'>

print(('香蕉', '苹果', '橘子')[0]) # 香蕉
print(('香蕉', '苹果', '橘子')[0:2]) # ('香蕉', '苹果')
print(('香蕉', '苹果', '橘子') + ('柚子',)) # ('香蕉', '苹果', '橘子', '柚子') 
print(('香蕉', '苹果', '橘子') * 2) # ('香蕉', '苹果', '橘子', '香蕉', '苹果', '橘子')


print(len((1,2,3))) # 3
print(max((1,2,3))) # 3 
print(min((1,2,3))) # 1
print(max('helloworld')) # w

# ord
# Return the Unicode code point for a one-character string
print(ord('w')) # 119
