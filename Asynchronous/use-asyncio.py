import asyncio
import threading

@asyncio.coroutine
def hello():
    # 由打印的当前线程名称可以看出，两个coroutine是由同一个线程并发执行的
    # I/O操作是并行的，但是管理和调度I/O操作的协程是由一个线程完成的其并发的
    print("Hello world! from %s" % threading.currentThread())
    # 异步调用asyncio.sleep(1):
    r = yield from asyncio.sleep(1)
    print("Hello again! from %s" % threading.currentThread())

def example1():
    # 获取EventLoop:
    loop = asyncio.get_event_loop()
    # 执行coroutine
    loop.run_until_complete(asyncio.wait([hello(), hello()]))
    print("Bye")
    loop.close()


import time

@asyncio.coroutine
def Crawler1(url):
    # 注意，调用的方法如果带有@coroutine装饰，调用的时候自然要用yield from
    reader, writer = yield from asyncio.open_connection(url, 80)
    get = 'GET / HTTP/1.1\r\nHost: {0}\r\nConnection: close\r\n\r\n'.format(url)
    writer.write(get.encode('ascii'))
    yield from writer.drain()
    lines = []
    while True:
        line = yield from reader.readline()
        if line:
            lines.append(line)
        else:
            response = b''.join(lines)
            print('Done with %s at %s Length is %s' % (url, time.time()-start, len(response)))
            writer.close()
            return response

# 利用async和await来代替@asyncio.coroutine和yield from
# await 相当于 yield from
# async with ... as ...: 相当于 with (yield from ...) as ...:
async def Crawler2(url):
    reader, writer = await asyncio.open_connection(url, 80)
    get = 'GET / HTTP/1.1\r\nHost: {0}\r\nConnection: close\r\n\r\n'.format(url)
    writer.write(get.encode('ascii'))
    await writer.drain()
    lines = []
    while True:
        line = await reader.readline()
        if line:
            lines.append(line)
        else:
            response = b''.join(lines)
            print('Done with %s at %s Length is %s' % (url, time.time() - start, len(response)))
            writer.close()
            return response


def example2():
    urls = ['www.google.com', 'www.sina.com', 'www.baidu.com', 'www.sohu.com']
    tasks = []
    for url in urls:
        tasks.append(Crawler2(url))
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()

start = time.time()
example2()
