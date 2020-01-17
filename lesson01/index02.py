# str  '' ,  "" ,   ''' '''

print(type('1'))  # str
print('let\'s go')  # let's go
print('''
  hello
  python
''')


'''
  转义字符 \n \' \t \r
    - 特殊字符
    - 无法'看见'的字符
    - 与语言本身语法有冲突的字符
'''
print('hello  \n world') 
# hello
#  world
print('hello  \\n world') # hello  \n world
print('c:\\northwind\\northwest') # c:\northwind\northwest

# 字符串运算符
# r/R 表示原始字符串
print(r'c:\northwind\northwest') # c:\northwind\northwest
# + 字符串拼接
print('hello' + 'world') # helloworld
# * 重复输出
print('hello' * 2) # hellohello
# [] 索引获取字符串中字符
print('hello'[0]) # h
print('hello'[-1]) # o
print('hello'[0:2]) # he
print('hello world'[6:]) # world
print('hello world'[:-5]) # hello 
print('hello world'[-5:]) # world 
# in 是否包含 not in 是否不包含
print('h' in 'hello') # True
print('h' not in 'hello') # False