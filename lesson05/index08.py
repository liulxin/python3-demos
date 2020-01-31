# reduce

from functools import reduce

list_x = [1, 2, 3, 4, 5]

r = reduce(lambda x, y: x + y, list_x)
r1 = reduce(lambda x, y: x + y, list_x, 12)

print(r) # 15
print(r1) # 27
