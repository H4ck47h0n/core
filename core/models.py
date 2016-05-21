#!/usr/bin/env python
 from core import app,db

 class User(db.Model):
     id = db.Column(db.Interger, primary_key=True)
     username  = db.Column(db.String(120),unique=True)
     phone_num = db.Column(db.String(120),unique=True)
     password  = db.Column(db.String(120))
     like      = db.Column(db.String(1200))
     dislike   = db.Column(db.String(1200))
     exiting   = db.Column(db.String)
     def __init__(self,username,password,exiting):
         self.username  =  username
         self.password  =  password
         self.exiting   =  exiting
     def __repr__(self):
         return "<ACCOUNT NAME IS %r>"%self.username
