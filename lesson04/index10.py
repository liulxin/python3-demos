import re

lang = 'pythonC#\njavaPhp'

res = re.findall('c#.{1}', lang, re.I)
res2 = re.findall('c#.{1}', lang, re.I | re.S)

# re.I 忽略大小写
# re.S 在此匹配模式下 . 可以匹配换行符以内的任意字符

print(res) # []

print(res2) # ['C#\n']