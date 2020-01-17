# 变量

A = [1, 2, 3, 4]
B = [1, 2]

print(A * 3 + B + A)  # [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 1, 2, 3, 4]


# 变量命名规则
'''
首字符不能为数字
字母、数字、下划线 组合
不可为保留关键字 （if and import 等）
区分大小写
'''
_name = 'liuli'

# 1name = 'liuli'


a = 1
b = a
a = 3
print(b)  # 1

arr_a = [1, 2, 3]
arr_b = arr_a
arr_a[0] = 3
print(arr_b)  # [3, 2, 3]


# 值类型(不可改变): int str tuple
# 引用类型(可变): set list dict

b_ = 'hello'
print(id(b_))  # 9559584

b_ = b_ + 'py'
print(id(b_))  # 9452832

a_ = [1, 2]
print(id(a_))  # 47070344
a_[0] = 2
print(id(a_))  # 47070344


c = (1, 2, 3)
# c[0] = 2 typeError

a_.append(3)
print(a_)
# c.append(4) typeError
