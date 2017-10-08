#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
from selectors import DefaultSelector, EVENT_READ, EVENT_WRITE
import time

start = time.time()
selector = DefaultSelector()
urls = ['www.google.com', 'www.sina.com', 'www.baidu.com', 'www.sohu.com']
#urls = ['www.google.com']


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
    yield f
    selector.unregister(sock.fileno())


def read_response(sock):
    f = Future()

    def on_read_response():
        f.setResult(sock.recv(4096))

    selector.register(sock.fileno(), EVENT_READ, on_read_response)
    chunk = yield f
    selector.unregister(sock.fileno())


# 重构Crawler
class Crawler(object):
    def __init__(self, url):
        self.url = url
        self.response = b''



    def fetch(self):
        get = 'GET / HTTP/1.1\r\nHost: {0}\r\nConnection: close\r\n\r\n'.format(self.url)
        sock.send(get.encode('ascii'))
        print("Connected and send request to %s at %s" % (self.url, time.time() - start))

        while True:


            if chunk:
                self.response += chunk
            else:
                print('Done with %s at %s' % (self.url, time.time() - start))
                urls.remove(self.url)
                break


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
