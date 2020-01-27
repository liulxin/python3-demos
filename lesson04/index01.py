import re

a = 'C|C++|Java|C#|Python|JavaScript'

res = re.findall('Python', a)

# print(res) # ['Python']

if len(res) > 0:
  print('Python')