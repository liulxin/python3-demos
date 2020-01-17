# Number 整型：int 浮点型：float 复数：complex 
# bool:布尔类型(py 中布尔值属于整数的子类型)
print(type(1))
print(type(1.1))
print(type(1 + 1))
print(type(1 - 1))
print(type(1 + 1.1))
print(type(1 * 1))
print(type(1 / 1))  # <class 'float'>     /  会转为浮点型
print(type(1 // 1))  # <class 'int'>    //   会保留整数部分，转为整型


# 0b 为前缀代表 2 进制
# 0o 为前缀代表 8 进制
# 0x 为前缀代表 16 进制
print(0b10) # 2
print(0o10) # 8
print(0x10) # 16

# 进制转换
# bin() => 转 2 进制
# int() => 转 10 进制
# hex() => 转 16 进制
# oct() => 转 8 进制
print(bin(10)) # 0b1010
print(int(0b10)) # 2
print(hex(10)) # 0xa
print(oct(10)) # 0o12

# bool
print(type(True)) # <class 'bool'>
print(type(False)) # <class 'bool'>
print(int(True)) # 1 
print(int(False)) # 0
print(bool(1)) # True  非0均代表真
print(bool(0)) # False
print(bool([1,2])) # True
print(bool([])) # False
print(bool({1, 2})) # True
print(bool({})) # False
print(bool(None)) # False

# complex
# 复数中用j表示
print(10j) # 10j