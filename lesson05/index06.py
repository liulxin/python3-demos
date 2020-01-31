# map

list_x = [1,2,3,4,5]

def square(x):
  return x * x

# list_y = map(square, list_x)

list_y = map(lambda x: x * x, list_x)

print(list_y) # <map object at 0x101fcc4d0>

print(list(list_y)) # [1, 4, 9, 16, 25]
