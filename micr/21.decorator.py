def logger(func):
  def wrapper():
    print('---start---')
    func()
    print('---end---')
  return wrapper

@logger
def func():
  print('this is func')

func()