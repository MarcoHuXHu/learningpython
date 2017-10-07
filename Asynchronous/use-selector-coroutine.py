#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
from selectors import DefaultSelector, EVENT_READ, EVENT_WRITE
import time

start = time.time()
selector = DefaultSelector()
urls = ['www.google.com', 'www.sina.com', 'www.baidu.com', 'www.sohu.com']


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


class Crawler(object):
    def __init__(self, url):
        self.url = url
        self.response = b''

    def fetch(self):
        sock = socket.socket()
        sock.setblocking(False)
        try:
            sock.connect((self.url, 80))
        except BlockingIOError:
            pass

        # 给connected注册回调
        f1 = Future()
        def on_connected():
            f1.setResult(None)

        selector.register(sock.fileno(), EVENT_WRITE, on_connected)
        yield f1

        # 相当于connected方法
        selector.unregister(sock.fileno())
        get = 'GET / HTTP/1.1\r\nHost: {0}\r\nConnection: close\r\n\r\n'.format(self.url)
        sock.send(get.encode('ascii'))
        print("Connected and send request to %s at %s" % (self.url, time.time() - start))

        while True:
            f2 = Future()

            def on_read_response():
                f2.setResult(sock.recv(4096))

            selector.register(sock.fileno(), EVENT_READ, on_read_response)
            chunk = yield f2
            selector.unregister(sock.fileno())
            if chunk:
                self.response += chunk
            else:
                print('Done with %s at %s' % (self.url, time.time() - start))
                urls.remove(self.url)
                break


class Task(object):
    def __init__(self, coroutine):
        self.coroutine = coroutine
        f = Future()
        f.setResult(None)
        self.step(f)

    def step(self, future):
        try:
            # send会进入到coroutine执行, 即fetch, 直到下次yield
            # next_future 为yield返回的对象
            next_future = self.coroutine.send(future.result)
        except StopIteration:
            return
        next_future.addDoneCallback(self.step)

# Event Loop
def loop():
    while urls:
        # 阻塞直到有事件发生
        events = selector.select()
        for event_key, event_mask in events:
            callback = event_key.data
            callback()

if __name__ == '__main__':
    import time
    start = time.time()
    for url in urls:
        crawler = Crawler(url)
        Task(crawler.fetch())
    print(time.time() - start)
    loop()
    print(time.time()-start)
