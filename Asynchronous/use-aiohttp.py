import time
import aiohttp, asyncio

async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get('http://{0}'.format(url)) as response:
            response = await response.read()
            print('Done with %s at %s Length is %s' % (url, time.time() - start, len(response)))

start = time.time()

def Crawler():
    urls = ['www.google.com', 'www.sina.com', 'www.baidu.com', 'www.sohu.com']
    tasks = []
    for url in urls:
        tasks.append(fetch(url))
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()


import asyncio

from aiohttp import web

async def index(request):
    return web.Response(body=b'<h1>Index</h1>', content_type='text/html')

async def hello(request):
    text = '<h1>hello, %s!</h1>' % request.match_info['name']
    return web.Response(body=text.encode('utf-8'), content_type='text/html')

async def init(loop):
    app = web.Application()
    app.router.add_route('GET', '/', index)
    app.router.add_route('GET', '/hello/{name}', hello)
    srv = await loop.create_server(app.make_handler(), '127.0.0.1', 8000)
    print('Server started at http://127.0.0.1:8000...')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()