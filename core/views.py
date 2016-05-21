#!/usr/bin/env python
# encoding: utf-8

from . import app,db,lm
from flask.ext.login import flask_login
from .models import User

from flask import request, render_template, jsonfy

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
    if request.method  == "POST":
        username =  request.get_json()['username']
        password =  request.get_json()['password']
        if password = users[username]['pw']:
            user          = User()
            user.username = username
            flask_login.login_user(user)
            return jsonfy(
                {"status":"success",
                 "message":"login success"
            })
        else:
            return jsonfy({
                "status":"false",
                "message":"The password is wrong"
            })
    if request.method == "GET":
        return render_template("login.html")
@app.rout("/logout")
def logout():
    flask_login.logout_user()
    return jsonfy({
        "status":"success",
        "message":"logout success"
    })


#app.run(host="0.0.0.0",debug=True)
