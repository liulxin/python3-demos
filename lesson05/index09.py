# filter

list_x = [1,2,3,4]

r = filter(lambda x: x > 2, list_x)

print(r) # <filter object at 0x106389fd0>

print(list(r)) # [3, 4]