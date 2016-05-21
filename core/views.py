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
@app.route('/account/<username>',methods=["GET","POST","DELETE","PUT"])
@flask_login.login_required
def account(username):
    usernames = [user.name for user in db.User.query.all()]
    if request.method == "POST":
        data = request.get_json()
        if data['name'] not in usernames:
            age       = data['profile']['age']
            sex       = data['profile']['sex']
            interests = data['profile']['interests']
            exiting = ""
            for item in interests:
                exiting + str(interests[item])
            user = User(username=data['name'],password=data['password'],interests=exiting,age=age,sex=sex)
            db.session.add(user)
            db.session.commit()
            return jsonfy({
                "status":"success",
                "message":"Creat Account Success"
            })
        else:
            return jsonfy({
                "status":"false",
                "message":"The account already exists"
            })
    elif request.method == "DELETE":
        data = request.get_json()
        if data['name'] in username:
            user = db.User.query.filter_by(username=data['name'])
            db.session.delete(user)
            db.session.commit()
            return jsonfy({
                "status":"success",
                "message":"Delete the user success"
            })
        else:
            return jsonfy({
                "status":"false",
                "message":"The account didn't exist"
            })
#app.run(host="0.0.0.0",debug=True)
