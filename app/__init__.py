# -*- coding: utf-8 -*-
"""
Author:duan
Date: 2019/7/8 20:25
"""
from flask_sqlalchemy import SQLAlchemy
from flask import Flask


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/models05'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY'] = 'guess string'
app.debug = True
db = SQLAlchemy(app)
