# if elif else

'''
a = input('please enter you num ')

b = int(a)

if b > 1:
    print('> 1')
elif b > 0:
    print('0 < x < 1')
else:
    print('not 0 < x < 1')
'''

code = 'qwer'
username = input('please enter your name')
password = input('please enter your password')
your_code = input('please enter your code')

if your_code == code:
  if username == 'dong' and password == 'wud':
    print('登陆成功')
  else:
    print('失败')
else:
  print('验证码错误')

