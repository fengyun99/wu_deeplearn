#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/11/2 22:49
# @Author   : FengYun
# @File     : app.py
# @Software : PyCharm
# 启动博客
import flask
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return flask.render_template('index.html')
