#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import time

def tcp_link(sock, address):
    print('Accept new connection from %s:%s...' % address)
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed.' % address)


# 创建socket对象
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# bind监听端口
s.bind(('127.0.0.1', 9000))

s.listen(4) # 最大连接数
print('Waiting Connection...')

while True:
    sock, address = s.accept() # accept在此会阻塞，直到有新的连接


