from enum import Enum
from enum import IntEnum,unique # 强制 int

class Vip(Enum):
  YELLOW = 1
  GREEN = 2
  BLANK = 3
  RED = 4

@unique
class VipInt(IntEnum):
  YELLOW = 1
  # YELLOW_Alias = 1
  GREEN = 2
  BLANK = 3
  RED = 4

res = Vip.YELLOW == 1

print(res) # False

print(Vip(1)) # Vip.YELLOW