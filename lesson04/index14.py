import re

s = 'life is short, i use python'

res = re.search('life(.*)python', s)

print(res) # <re.Match object; span=(0, 27), match='life is short, i use python'>

print(res.group()) # life is short, i use python
print(res.group(0)) # life is short, i use python --> 0 代表完整匹配结果
print(res.group(1)) #  is short, i use 

print(res.groups()) # (' is short, i use ',)
