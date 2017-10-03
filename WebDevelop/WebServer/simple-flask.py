#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/')
def home():
    return '<h1>Hello World</h1>'

app.run(host='127.0.0.1', port=8888)