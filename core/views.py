#!/usr/bin/env python
# encoding: utf-8

from . import app


@app.route('/')
def index():
    return "hello world"
#app.run(host="0.0.0.0",debug=True)
