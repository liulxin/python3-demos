# 边界匹配

import re

qq = '12902001'

qq1 = '123456789'

res = re.findall('^\d{4,8}$', qq)

res2 = re.findall('^\d{4,8}$', qq1)

print(res) # ['12902001']

print(res2) # []