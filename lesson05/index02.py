from enum import Enum

class Vip(Enum):
  YELLOW = 1
  GREEN = 2
  BLANK = 3
  RED = 4

res = Vip.YELLOW == 1

print(res) # False