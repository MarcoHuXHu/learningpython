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


with MyClass(0) as myClass:
     myClass.calc()
