#!/usr/bin/env python
# encoding: utf-8

from . import app,db,lm
from .models import User

from flask import request, render_template

@lm.user_loader
def user_loader(username):
    if username not in users:
        return
    user = User()
    user.username = username
@lm.request_loader
def request_loader(request):
    username =  request.getjson()

@app.route("/login" methods=["GET","POST"])
def login():
    if request.methods = "POST":
        username =  request.get_json()['username']
        password =  request.get_json()['password']




#app.run(host="0.0.0.0",debug=True)
