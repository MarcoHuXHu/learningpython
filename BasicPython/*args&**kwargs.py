# 1. 函数的参数为可变的

def foo1(*args, **kwargs):
    print('args = ', args)
    print('kwargs = ', kwargs)
    print('---------------------------------------')

# 1.1 考虑传入参数的可变性
c = (1, 2, 3, 4)
d = {'a': 1, 'b': 2, 'c': 3}
foo1(c)
foo1(*c) # 比如itertools中的products，product(a, b, c)表示计算三个list a, b, c的叉乘，若有d = [a, b, c]，要传入d则为*d
foo1(*d)
foo1(**d)

# 1.2 考虑传入tuple与dict
foo1(1, 2, 3, 4)
foo1(a=1,b=2,c=3)
foo1(1, 2, 3, 4, a=1, b=2, c=3)
foo1('a', 1, None, a=1, b='2', c=3)

def foo2(first, second, third):
    print ('First argument: ', first)
    print ('Second argument: ', second)
    print ('Third argument: ', third)

# 2. 函数的参数为不可变的，传入可变参数
# Use *args
args = [1, 2, 3]
foo2(*args)

# Use **kwargs
kwargs = {'first': 1, 'second': 2, 'third': 3}

foo2(*kwargs)  # results:  # First argument:  second   # Second argument:  first   # Third argument:  third
foo2(**kwargs) # results:  # First argument:  1    # Second argument:  2   # Third argument:  3
