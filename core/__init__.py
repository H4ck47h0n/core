#!/usr/bin/env python
# encoding: utf-8

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app.config["SQLALCHEMY_DATABASE_URL"] = 'sqlite:////'
app = Flask(__name__)
db = SQLAlchemy(app)
import core.models
import core.views
