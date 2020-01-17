# 算术运算符
print(3 - 1)
print(3 + 1)
print(3 * 2)
print(3 / 2)
print(3 // 2)
print(5 % 2)
print(5 ** 2)  # 25


# 赋值运算符
c = 1
c += 2
print(c)  # 3
c -= 1
print(c)  # 2
c *= 4
print(c)  # 8
c //= 2
print(c)  # 4
c **= 2
print(c)  # 16
c %= 3
print(c)  # 1


# 关系运算符
print(1 == 1) # True
print(1 != 2) # True
print(2 > 1) # True
print(1 < 2) # True
print(2 >= 2) # True
print(1 <= 0) # False

d = 1
d += d >= 0
print(d) # 2  (1 += (d >= 0)) => (1 += True) => (1 += 1)

# 逻辑运算符 (并不一定返回bool类型)
print(True and True) # True
print(True and False) # False
print(True or False) # True
print(not False) # True
print(1 and 1) # 1
print( 'he' and 'hd') # he
print('he' or 'hd') # he
print(0 or 0) # 0
print(not 'a') # False
print(1 and 0) # 0
print(0 and 1) # 0
# and 中如果第一个值为真，会继续后续判断，返回第二个值；如果第一个值为假，就不会继续后续判断， 直接进行返回第一个值

# 成员运算符

# 身份运算符

# 位运算符
