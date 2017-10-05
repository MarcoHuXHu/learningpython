#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# “子程序就是协程的一种特例。”
# 协程看上去也是子程序，但执行过程中，在子程序内部可中断，然后转而执行别的子程序，在适当的时候再返回来接着执行。

# Python对协程的支持是通过generator实现的。
# 但是Python的yield不但可以返回一个值，它还可以接收调用者发出的参数。

def consumer():
    r = ''
    while True:
        n = yield r
        # producer每次send或者next，consumer都会从yield后面开始
        # 如果是send，则n会接收send过来的数据，如果是next，则n为None
        # consumer会一直执行到下一个yield或者return，
        # 如果是yield，则producer中r = c.send(n)的r会接收到yield的值，如果是return，则会StopIteration
        if not n:
            n = yield 'Send' # 这里也要给n赋值，否则下一次producer调用send时，从此处进入，n会接收不到send过来的数据
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'



def producer():
    c = consumer() # 这里只是构造一个生成器
    c.send(None)   # 从此处开始执行consumer中的代码，直到遇到yield，本例中此处返回来一个空的str
    # 其实next(c)和c.send(None)是等价的
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send([n, n*2])
        print('[PRODUCER] Consumer return: %s' % r)
        print(next(c))
    c.close()

producer()