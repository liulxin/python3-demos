import re

# re.match 从头开始，不满足就返回 None
# re.search 从头开始，返回第一个满足条件的结果

s = 'A8C3721D86'

res = re.match('\d', s)
print(res) # None

res2 = re.search('\d', s)
print(res2) # <re.Match object; span=(1, 2), match='8'>
