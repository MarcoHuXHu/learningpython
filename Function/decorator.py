import functools

# decorator without argument
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

# decorator with argument
def info(text):
    def decorator(func):
        # 使用装饰器修饰过的函数func（下面例子的f3），实际上是一个decorator函数返回的“闭包”对象wrapper
        # 所以要用functools模块的wraps装饰器，更正函数名
        # 不然函数名，即__name__为wrapper
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)

        return wrapper
    return decorator

##### decorator without argument
@log
def f1():
    print('f1')

def f2():
    print('f2')

# 使用decorator
f1()
# 不使用decorator的等效用法
f2 = log(f2)
f2()


##### decorator with argument
@info('execute f3')
def f3():
    print('f3')

def f4():
    print('f4')

# 使用decorator
f3()
# 不使用decorator的等效用法
temp = info('execute f4')
f4 = temp(f4)
f4()


###### @functools.wraps(func)的作用
print(f1.__name__) # wrapper
print(f2.__name__) # wrapper
print(f3.__name__) # f3
print(f4.__name__) # f4
