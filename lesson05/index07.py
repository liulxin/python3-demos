list_x = [1, 2, 3, 4, 5]
list_y = [1, 2, 3, 4]

r = map(lambda x, y: x * x + y, list_x, list_y)

print(list(r))  # [2, 6, 12, 20]
