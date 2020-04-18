# 1 ～ 100 所有的数字

"""
count = 1
while count <= 100:
    print(count)
    count = count + 1
"""

# 1 + 2 + ... + 100

"""
sum = 1
i = 2
while i <= 100:
    sum = sum + i
    i = i + 1
print(sum) # 5050
"""

# break 循环中遇到break 直接退出循环
# continue 跳出本次循环，继续下次循环
# while else -> 如何被break打断，则不执行else语句

i = 0
while i < 101:
    if i % 2 == 0:
        print(i)
    i = i + 1
    if i < 96:
        continue
    print('this is continue')
    # if i > 97:
        # break
else:
    print(i) # 101
