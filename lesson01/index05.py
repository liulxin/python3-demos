# str list tuple 都是序列

# 集合 set （无序、不重复）

print(type({1,3,4})) # <class 'set'>

print({1,1,2,2,3}) # {1, 2, 3}

print(len({1,2,3})) # 3
print(1 in {1,2,3}) # True
print(1 not in {1,2,3}) # False

# - 求两个集合的差集
print({1,2,3,4,5} - {4,5,6}) # {1, 2, 3}

# & 求两个集合的交集
print({1,2,3} & {1}) # {1}

# | 求两个集合的并集
print({1, 2, 3} | {2, 5}) # {1, 2, 3, 5}



print(type({})) # <class 'dict'> 字典

# 定义空的集合
print(type(set())) # <class 'set'>