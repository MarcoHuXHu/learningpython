#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
from selectors import DefaultSelector, EVENT_READ, EVENT_WRITE
import time

start = time.time()
selector = DefaultSelector()
urls = ['www.google.com', 'www.sina.com', 'www.baidu.com', 'www.sohu.com']

class Crawler(object):
    def __init__(self, url):
        self.url = url
        self.sock = None
        self.response = b''

    def fetch(self):
        self.sock = socket.socket()
        self.sock.setblocking(False)
        try:
            self.sock.connect((self.url, 80))
        except BlockingIOError:
            pass
        # fileno是socket返回的file descriptor，EVENT_WRITE也是socket返回连接成功的事件
        selector.register(self.sock.fileno(), EVENT_WRITE, self.connected)

    # key和mask用来识别回调的是那个函数
    def connected(self, key, mask):
        selector.unregister(key.fd)
        get = 'GET / HTTP/1.1\r\nHost: {0}\r\nConnection: close\r\n\r\n'.format(self.url)
        self.sock.send(get.encode('ascii'))
        print("Connected and send request to %s at %s" % (self.url, time.time()-start))
        selector.register(key.fd, EVENT_READ, self.read_response)

    def read_response(self, key, mask):
        chunk = self.sock.recv(4096)
        if chunk:
            self.response += chunk
        else:
            print('Done with %s at %s' % (self.url, time.time()-start))
            selector.unregister(key.fd)
            urls.remove(self.url)

# Event Loop
def loop():
    while urls:
        # 阻塞直到有事件发生
        events = selector.select()
        for event_key, event_mask in events:
            callback = event_key.data
            callback(event_key, event_mask)

if __name__ == '__main__':
    import time
    start = time.time()
    for url in urls:
        crawler = Crawler(url)
        crawler.fetch()
    print(time.time() - start)
    loop()
    print(time.time()-start)
