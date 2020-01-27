# 组

import re

s = 'PythonPythonPythonPython'

res = re.findall('(Python){3}', s)

print(res) # ['Python']