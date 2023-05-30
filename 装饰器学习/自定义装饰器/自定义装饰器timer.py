#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/5/29 13:58
# @Author   : FengYun
# @File     : 自定义装饰器timer.py
# @Software : PyCharm
import time
from functools import wraps


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execute_time = end_time - start_time
        return result, execute_time

    return wrapper
