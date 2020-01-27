# \d \D 

# \w 元字符用于查找单词字符。单词字符包括：a-z、A-Z、0-9，以及下划线, 包含 _ (下划线) 字符

# \s 空白字符: 空格符 制表符 回车符 换行符 垂直换行符 换页符

# . 除换行符以外所有的字符

import re

s = 'python 23\tjava\njs\r32&php'

res = re.findall('\d', s)

res2 = re.findall('[0-9]', s)

res3 = re.findall('\w', s)

res4 = re.findall('\s', s)

print(res) # ['2', '3', '3', '2']

print(res2) # ['2', '3', '3', '2']

print(res3) # ['p', 'y', 't', 'h', 'o', 'n', '2', '3', 'j', 'a', 'v', 'a', 'j', 's', '3', '2', 'p', 'h', 'p']

print(res4) # [' ', '\t', '\n', '\r']
