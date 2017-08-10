# decorator without argument
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

# decorator with argument
def info(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log
def f1():
    print('2015-3-25')

@info('execute hahaha')
def f2():
    print('2015-3-25')