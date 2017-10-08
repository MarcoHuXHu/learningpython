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


