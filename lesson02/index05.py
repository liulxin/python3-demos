print('please input a value')
a = int(input())

if a == 1:
    print('apple')
elif a == 2:
    print('banner')
elif a == 3:
    print('orange')
else:
    print('shopping')


CON = 0
while CON < 4:
    CON += 1
    print('i am con')
else:
    print('CON end')


arr = ['dong', 'liuli', 'wudi', 'tar']
for item in arr:
    print(item)

arr_se = [['dong', 'liuli', 'wudi', 'tar'], (1, 2, 3)]
for x in arr_se:
    if x[2] == 'wudi':
        break
    for y in x:
        print(y, end='-')
else:
    print('this is for else')
# for else 正常循环完毕 会执行else 中的逻辑,但是如果中间被break打断循环就不会执行else

# 0 -- 9  (10 代表 10个偏移  2 代表步长,即间隔多少)
for x in range(0, 10, 2):
    print(x)

for x in range(10, 0, -2):
    print(x)


a = [1,2,3,4,5,6,7,8,9]

for i in range(0, len(a), 2):
  print(a[i], end = '|')

b = a[0:len(a):2]
print(b)