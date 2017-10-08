#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 将连接，读取数据的代码单独拿出来，作为一个独立的协程

import socket
from selectors import DefaultSelector, EVENT_READ, EVENT_WRITE
import time

start = time.time()
selector = DefaultSelector()
urls = ['www.google.com', 'www.sina.com', 'www.baidu.com', 'www.sohu.com']
#urls = ['www.google.com']

# 协程：异步建立连接，对于多个url可以同时建立连接而不用等上一个url连接完成了在开始下一个url的建立，且哪个url连接好了就开始GET数据
def connect(sock, address):
    sock.setblocking(False)
    try:
        sock.connect(address)
    except BlockingIOError:
        pass

    f = Future()

    def on_connected():
        f.setResult(None)

    selector.register(sock.fileno(), EVENT_WRITE, on_connected)
    yield from f # 必须给Future加入__iter__这里才可以用yield from，否则只能用yield，在read_one_response中同理
    selector.unregister(sock.fileno())


# 协程：异步读取一次数据（4096字节）
def read_one_response(sock):
    f = Future()

    def on_read_response():
        f.setResult(sock.recv(4096))

    selector.register(sock.fileno(), EVENT_READ, on_read_response)
    chunk = yield f # 必须给Future加入__iter__这里才可以用yield from，否则只能用yield，在on_connected中同理
    selector.unregister(sock.fileno())
    return chunk


# 协程：异步不断调用read_one_response，直到读取完整个response
def read_all(sock):
    response = []
    chunk = yield from read_one_response(sock)
    while chunk:
        response.append(chunk)
        chunk = yield from read_one_response(sock)
    return b''.join(response)


# 重构Crawler
class Crawler(object):
    def __init__(self, url):
        self.url = url
        self.response = b''

    def fetch(self):
        sock = socket.socket()
        yield from connect(sock, (self.url, 80))
        print("Connected and send request to %s at %s" % (self.url, time.time() - start))

        get = 'GET / HTTP/1.1\r\nHost: {0}\r\nConnection: close\r\n\r\n'.format(self.url)
        sock.send(get.encode('ascii'))

        self.response = yield from read_all(sock)
        print('Done with %s at %s, length=%s' % (self.url, time.time() - start, len(self.response)))

        urls.remove(self.url)


# 关于event loop，Future以及Task对象的说明，详见use-selector-coroutine
def loop():
    while urls:
        events = selector.select()
        for event_key, event_mask in events:
            callback = event_key.data
            callback()


class Future(object):
    def __init__(self):
        self.result = None
        self.callbacks = []

    def addDoneCallback(self, fn):
        self.callbacks.append(fn)

    def setResult(self, result):
        self.result = result
        for fn in self.callbacks:
            fn(self)

    # yield可以直接作用于普通Python对象（原本的Future里面没有yield，不是Iterator）而yield from却不行，
    # 以及Future和Task都不是协程，只是用于管理协程，协程是指
    # 所以我们对Future还要进一步改造，把它变成一个iterable对象就可以了。
    def __iter__(self):
        yield self
        return self.result


class Task(object):
    def __init__(self, coroutine):
        self.coroutine = coroutine
        f = Future()
        f.setResult(None)
        self.step(f)

    def step(self, future):
        try:
            next_future = self.coroutine.send(future.result)
        except StopIteration:
            return
        next_future.addDoneCallback(self.step)


if __name__ == '__main__':
    import time
    start = time.time()
    for url in urls:
        crawler = Crawler(url)
        Task(crawler.fetch())
    print(time.time() - start)
    loop()
    print(time.time()-start)
