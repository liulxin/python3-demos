# 贪婪
# 非贪婪 数量词后 + ?

import re

s = 'python 111java445php'

res = re.findall('[a-z]{3,6}', s)

res2 = re.findall('[a-z]{3,6}?', s)

print(res)  # ['python', 'java', 'php']

print(res2)  # ['pyt', 'hon', 'jav', 'php']
