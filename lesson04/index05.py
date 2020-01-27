# 数量

import re

s = 'python 111java445php'

res = re.findall('[a-z]{3,6}', s)

print(res) # ['python', 'java', 'php']
