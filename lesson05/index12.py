import time


def decorator(func):
    def wrapper(*args, **kw):
        print(time.time())
        func(*args, **kw)
    return wrapper


@decorator
def f4(name, age, **kw):
    print('this is a function -- ' + name + ' -- ' + age)
    print(kw)


f4('dong', '13', a=1, b=2)
