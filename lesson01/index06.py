# dict 字典 {key: value} key不可重复

print(type({'name': 'python'})) # <class 'dict'>

# value：str int float list tuple set dict
print({'name': (1,2,3)})

# key： 不可变性  int float str tuple
print({(1,2): 'python'}) # 元组可以作key
print({1.2: 'a'})
# print({[1,2]: 1}) TypeError