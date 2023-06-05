#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/6/5 14:49
# @Author   : FengYun
# @File     : 通过深度获取json对象结果.py
# @Software : PyCharm
def deep_get(d, keys, default=None):
    if isinstance(keys, str):
        keys = keys.split('.')
    assert type(keys) is list
    if d is None:
        return default
    if not keys:
        return d
    return deep_get(d.get(keys[0]), keys[1:], default)


print(deep_get({"a": {"b": {"c": "结果"}}}, keys="a.b.c", default="没找到结果"))
