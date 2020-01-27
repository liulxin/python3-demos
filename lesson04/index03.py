# 字符集
import re

s = 'abc, acc, adc, aec, afc, ahc'

# [] 或关系
# [^] 非关系
# [a-c] a到c ==> [abc]
res = re.findall('a[cf]c', s)

res2 = re.findall('a[^cf]c', s)

res3 = re.findall('a[a-c]c', s)

print(res) # ['acc', 'afc']

print(res2) # ['abc', 'adc', 'aec', 'ahc']

print(res3) # ['abc', 'acc']