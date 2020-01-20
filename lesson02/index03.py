'''
表达式(Expression)是运算符(operator)和操作数(operand)所构成的序列
'''

print(1 + 2 * 3)  # 7
print(1 or 2 and 3)  # 1  --> 1 or (2 and 3) --> 1 or 3 --> 1

# not > and > or
# 算术 > 比较 > 逻辑

'''
条件控制 循环控制 分支
if esle for while 
'''

mood = False
if mood:
    print('go left')
else:
    print('go right')1


ACCOUNT = 'dongliuli'
PASSWORD = '123456'

print('please input accout')
user_account = input()

print('please input password')
user_password = input()


if ACCOUNT == user_account and PASSWORD == user_password:
    print('success')
else:
    print('fail')