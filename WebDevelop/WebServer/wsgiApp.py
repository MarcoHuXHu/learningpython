#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# web application部分
def application(environment, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    body = '<h1>Hello, %s!</h1>' % (environment['PATH_INFO'][1:] or 'World')
    return [body.encode('utf-8')]
