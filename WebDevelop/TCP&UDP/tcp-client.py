#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket

# 连接到sina，GET出html并保存
def example1():
    # 创建socket对象
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 建立连接
    # For IP sockets, the address is a pair (host, port).
    s.connect(('www.sina.com.cn', 80))

    # 发送请求
    s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')

    # 接收数据
    buffer = []
    while True:
        # 每次最多接收1024字节
        data = s.recv(1024)
        if data:
            buffer.append(data)
        else:
            break

    received_data = b''.join(buffer)
    s.close()
    # 分离header和html本身
    header, html = received_data.split(b'\r\n\r\n', 1)
    print(header)
    # 将html写入文件
    with open('index.html', 'wb') as f:
        f.write(html)

# 用于与server的例子沟通

from multiprocessing import Process
import time

def example2(client_name):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('127.0.0.1', 9000))
    print(s.recv(1024))
    s.send(client_name) # 必须send bit，不能是str
    print(s.recv(1024))
    time.sleep(1)
    s.send(b'exit') # 发送exit指令让server退出while循环

clients = [b'Adam', b'Ben', b'Cathy', b'David', b'Eric', b'Frank']

for i in range(18):
    p = Process(target=example2, args=(clients[i % 6],))
    p.start()
    time.sleep(1)
