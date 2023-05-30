#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/5/29 14:03
# @Author   : FengYun
# @File     : test_timer.py
# @Software : PyCharm
import time

from 装饰器学习.自定义装饰器.自定义装饰器timer import timer


@timer
def my_function():
    time.sleep(2)
    return "Done"


res = my_function()
# 返回元组
print(res)
