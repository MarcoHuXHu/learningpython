#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
from selectors import DefaultSelector, EVENT_READ, EVENT_WRITE
import time

start = time.time()
selector = DefaultSelector()
urls = ['www.google.com', 'www.sina.com', 'www.baidu.com', 'www.sohu.com']
#urls = ['www.google.com']


# 未来对象(Future)，异步调用执行完的时候，就把结果放在它里面。模拟asyncio中futures部分
class Future(object):
    def __init__(self):
        self.result = None
        self.callbacks = []

    def addDoneCallback(self, fn):
        self.callbacks.append(fn)

    # 设置结果的时候执行所有回调，其中有一个回调是下一步的step()
    def setResult(self, result):
        self.result = result
        for fn in self.callbacks:
            # print(fn) # 这里我们发现Future对象的所有callbacks，其实都是Task.step()方法
            fn(self)


# 任务对象(Task)，用来管理生成器的状态，恢复生成器的执行。模拟asyncio中tasks部分
# 初始化时传入被管理的、待执行的协程coroutine
# 一个Task对应一个coroutine，管理其所有回调和结果
class Task(object):
    def __init__(self, coroutine):
        self.coroutine = coroutine
        f = Future()
        f.setResult(None)
        # step()方法，在初始化的时候就会执行一遍。调用send()方法发送None对协程进行初始化
        self.step(f)

    def step(self, future):
        try:
            # send会进入到coroutine执行, 即fetch, 直到下次yield
            # 从send的进入点直到yield即为本次要异步执行的操作，直到yield退回到此处
            # 直到下一次step()运行。下一次step会在什么情况运行呢？
            # 即事件循环loop中接收到异步执行完毕的事件，调用callback()，callback(on_connected, on_read_response)里面
            # future.setResult执行所有callbacks，其中有step()
            # next_future 为yield返回的对象
            next_future = self.coroutine.send(future.result)
            # send()完成之后，得到了下一次的future
        except StopIteration:
            return
        # 然后给下一次的future添加step()回调。callbacks这个list里面无论如何都会有一个step()，使得Task一步一步执行下去
        next_future.addDoneCallback(self.step)


# Event Loop
def loop():
    while urls:
        # 阻塞直到有事件发生
        events = selector.select()
        for event_key, event_mask in events:
            callback = event_key.data
            callback()
            # 这里的callback（on_connected和on_read_response）不再关心业务逻辑，反正callback已经和future对象关联起来了，
            # 具体下一步怎么执行由future以及管理该future的task决定


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
        # 开始建立连接后，就通过yield返回
        # 当连接建成后，事件循环会从此处重入，事件循环只负责调用callback（on_connected），
        # 其中的setResult最后会调用Task.step，其中的next_future = self.coroutine.send(future.result)
        # 会使得协程重新进入这里

        # 相当于connected方法
        selector.unregister(sock.fileno())
        get = 'GET / HTTP/1.1\r\nHost: {0}\r\nConnection: close\r\n\r\n'.format(self.url)
        sock.send(get.encode('ascii'))
        print("Connected and send request to %s at %s" % (self.url, time.time() - start))

        # 因为response每次只接收4096字节，故而可能需要多次接收才能完成，因此将接收的部分装在while循环中
        while True:
            f2 = Future()

            def on_read_response():
                f2.setResult(sock.recv(4096))

            selector.register(sock.fileno(), EVENT_READ, on_read_response)
            # 注册一个接收到数据的read事件就yield退出，直到收到该事件由此重入
            chunk = yield f2
            selector.unregister(sock.fileno())
            if chunk:
                self.response += chunk
            else:
                print('Done with %s at %s, length=%s' % (self.url, time.time() - start, len(self.response)))
                urls.remove(self.url)
                break


if __name__ == '__main__':
    import time
    start = time.time()
    for url in urls:
        crawler = Crawler(url)
        Task(crawler.fetch())
    print(time.time() - start)
    loop()
    print(time.time()-start)
