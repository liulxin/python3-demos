import re

s = 'pytho0pythonn1pythonnn2'

# * 匹配 0 次或无限次
# + 一次 或 无限次
# ? 0 或 1 次

res = re.findall('python*', s)

print(res) # ['pytho', 'pythonn', 'pythonnn']

res2 = re.findall('python+', s)

print(res2) # ['pythonn', 'pythonnn']

res3 = re.findall('python?', s)

print(res3) # ['pytho', 'python', 'python']