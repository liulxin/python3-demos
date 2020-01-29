from enum import Enum

class Vip(Enum):
  YELLOW = 1
  GREEN = 2
  BLANK = 3
  RED = 4

print(Vip.YELLOW) # Vip.YELLOW

print(type(Vip.YELLOW)) # <enum 'Vip'>

print(Vip.YELLOW.name) # YELLOW

print(Vip.YELLOW.value) # 1

for v in Vip:
  print(v)
  # Vip.YELLOW
  # Vip.GREEN
  # Vip.BLANK
  # Vip.RED