#!/usr/bin/env python
# encoding: utf-8

from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
import flask.ext.login as flask_login

lm = flask_login.LoginManager()
basedir = os.path.abspath(os.path.dirname(__file__))
db_dir  = os.path.join(basedir,db)
sqlite_dir = "sqlite:////" + db_dir
app.config["SQLALCHEMY_DATABASE_URL"] = 'sqlite:////'
app = Flask(__name__)
db = SQLAlchemy(app)
lm.init_app(app)
import core.models
import core.views
