#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 利用contextlib，使得函数可以使用with的形式，而非try...finally

# 方法1：通过__enter__和__exit__这两个方法实现上下文管理
# 注意：__exit__方法只起到finally的作用，即无论是否出错都会执行其中的语句，然而并没有catch的作用因此执行完__exit__之后还是会抛出的
class MyClass(object):

    def __init__(self, number):
        print('init')
        self.number = number

    def __enter__(self):
        print('enter')
        return self # return self是必须的

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print('Error')
        else:
            print('Exit with no error')

    def calc(self):
        print(10/self.number)


def example1():
    with MyClass(0) as myClass:
         myClass.calc()

# 方法二：使用contextlib中的@contextmanager：
# @contextmanager这个decorator接受一个generator，用yield语句把with ... as var把变量输出出去，然后，with语句就可以正常地工作了：

from contextlib import contextmanager

@contextmanager
def create_dict():
    print('contextmanager enter')
    dic = dict()
    dic['a'] = 1
    yield(dic)
    print('contextmanager exit')


def example2():
    with create_dict() as d:
        d['b'] = '2'
        print(d)
        print(d['c'])

# 代码的执行顺序是：
# with语句首先执行yield之前的语句
# yield调用会执行with语句内部的所有语句
# 但是这里不能起到__exit__的作用，即出现异常，yield后的语句便不会执行了
# 解决方法为：

@contextmanager
def closing(thing):
    try:
        print('closing enter')
        yield thing
    finally:
        print('closing exit')
        # thing.close()

# try&catch与with的区别体现在这里：
'''
try:
    f = open("")
except:
    pass
finally:
    f.close()
'''
# 这里并不能关闭f，因为f在try...catch的区块内，finally并不能引用到f
# 要想处理这种情况，必须在外面在加一层try...catch
# 因此with的好处不在于处理异常，而在于当open的时候就异常了也可以finally close


def example3():
    with closing(dict) as d:
        d['e'] = 5
        print(d['f]'])
        print('end') # 并不会执行，因为上一句已经抛出异常了

example1()
example2()
example3()