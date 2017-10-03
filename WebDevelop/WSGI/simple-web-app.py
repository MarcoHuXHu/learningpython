def application(environment, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    body = '<h1>Hello, %s!</h1>' % (environment['PATH_INFO'][1:] or 'World')
    return [body.encode('utf-8')]

from wsgiref.simple_server import make_server

httpserver = make_server('', 8000, application)
print('Serving HTTP on port 8000...')
httpserver.serve_forever()
