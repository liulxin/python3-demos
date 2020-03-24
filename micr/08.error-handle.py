x = 42
y = 0

# print()
# print(x / y)
# print()

print()
try:
  print(x / y)
except ZeroDivisionError as e:
  print('not allowed divide by zero')
else:
  print('something else went wrong')
finally:
  print('finally')
print()