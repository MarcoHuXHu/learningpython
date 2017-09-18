#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 利用type来创建类
def fn(self, name='world'): # 先定义函数
    print('Hello, %s.' % name)

Hello = type('Hello', (object,), dict(hello=fn)) # 创建Hello class

h = Hello()
print('call h.hello():')
h.hello()
print('type(Hello) =', type(Hello))
print('type(h) =', type(h))


# metaclass是创建类，所以必须从`type`类型派生：
class ListMetaclass(type):
    # cls类似于class中的self
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        print(cls)
        print(name)
        print(bases)
        print(attrs)
        # 等效于return type(name, (list,), attrs)
        return type.__new__(cls, name, bases, attrs)

# 指示使用ListMetaclass来定制类
# list 用于提供'append'的方法
class MyList(list, metaclass=ListMetaclass):
    pass

class MyList2(MyList):
    pass

L = MyList2()
L.append(1)
L.append('a')
print(L)