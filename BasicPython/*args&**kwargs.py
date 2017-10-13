# 1. 函数的参数为可变的
# *args会接收所有非键值对参数，组成一个list
# **kwargs会接收所有的键值对，组成一个dict
# 注意如果直接传一个list给*args，会把一整个list对象看成一个元素加入到args中，要拆开则要传入*list
# 比如itertools中的products，product(a, b, c)表示计算三个list a, b, c的叉乘，若有d = [a, b, c]，要传入d则为*d

def foo1(*args, **kwargs):
    print('args = ', args)
    print('kwargs = ', kwargs)
    print('---------------------------------------')

# 1.1 考虑传入tuple与dict
foo1(1, 2, 3, 4)                    # args = (1, 2, 3, 4)   kwargs = {}
foo1(a=1,b=2,c=3)                   # args = ()             kwargs = {'a': 1, 'b': 2, 'c': 3}
foo1(1, 2, 3, 4, a=1, b=2, c=3)     # args = (1, 2, 3, 4)   kwargs = {'a': 1, 'b': 2, 'c': 3}
foo1('a', 1, None, a=1, b='2', c=3) # args = ('a', 1, None) kwargs = {'a': 1, 'b': '2', 'c': 3}

# 1.2 函数的参数为可变的，传入可变参数
c = (1, 2, 3, 4)
d = {'a': 1, 'b': 2, 'c': 3}
foo1(c)     # args =  ((1, 2, 3, 4),)   kwargs =  {}
foo1(*c)    # args =  (1, 2, 3, 4)      kwargs =  {}
foo1(*d)    # args =  ('a', 'b', 'c')   kwargs =  {}
foo1(**d)   # args =  ()                kwargs =  {'a': 1, 'b': 2, 'c': 3}



# 2. 函数的参数为不可变的，传入可变参数
# *args把传入的args这个list拆开称一个一个parameter带入，参数个数不同则报错
# *kwargs，即*作用于dict，则会把dict的所有key视为一个list，然后同上
# **kwargs把kwargs这个dict拆开称一个一个键值对，传给与方法定义的parameter名称对应的，参数个数不同或者不匹配都报错
def foo2(first, second, third):
    print ('First argument: ', first)
    print ('Second argument: ', second)
    print ('Third argument: ', third)

# Use *args
args = [1, 2, 3]
foo2(*args)

# Use **kwargs
kwargs = {'first': 1, 'second': 2, 'third': 3}

foo2(*kwargs)  # results:  # First argument:  second   # Second argument:  first   # Third argument:  third
foo2(**kwargs) # results:  # First argument:  1    # Second argument:  2   # Third argument:  3

kwargs2 = {'first': 1, 'second': 2, 'third': 3, 'fouth': 4}

# foo2(*kwargs2)  # foo2() takes 3 positional arguments but 4 were given
# foo2(**kwargs2) # foo2() got an unexpected keyword argument 'fouth'

