import re

a = 'C1C++2Java3C#4Python5JavaScript6'

res = re.findall('\d', a)

print(res) # ['1', '2', '3', '4', '5', '6']

# 'python' 普通字符  '\d' 元字符