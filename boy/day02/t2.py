# name = input('please enter your name')
# age = input('please enter your age')
# job = input('please enter your job')
#
# # 格式化输出 % 占位符 s -> str d i r
# msg = '''
# -------------- info of %s ---------------
# Name : %s
# Age: %s
# job: %s
# -------------- end ------------------
# ''' % (name,name,age,job)
#
# print(msg)

# -------------- info of dong ---------------
# Name : dong
# Age: 18
# job: it
# -------------- end ------------------

# %% 代表普通%
inf = 'name: %s , age: %s, job: 1%%' % ('dong', 18)
print(inf)  # name: dong , age: 18, job: 1%

# format
print('{} {}'.format('hello', 'world'))  # 不带字段
# hello world
print('{0} {1}'.format('hello', 'world'))  # 带数字编号
# hello world
print('{0} {1} {0}'.format('hello', 'world'))  # 打乱顺序
# hello world hello
print('{1} {1} {0}'.format('hello', 'world'))
# world world hello
print('{a} {tom} {a}'.format(tom='hello', a='world'))  # 带关键字
# world hello world
