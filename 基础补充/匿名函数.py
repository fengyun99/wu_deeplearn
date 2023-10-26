#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/10/22 16:41
# @Author   : FengYun
# @File     : 匿名函数.py
# @Software : PyCharm
sum = lambda a, b: a + b  # 参数:表达式
print(sum(1, 2))


def fun(a, b, opt):
    print(a)
    print(b)
    print(opt(a, b))


fun(1, 2, lambda a, b: a + b)

stus = [
    {"name": "zhangsan", "age": 18},
    {"name": "lisi", "age": 19},
    {"name": "wangwu", "age": 17}
]
# 按age或者name排序
stus.sort(key=lambda x: x['name'])
print(stus)
stus.sort(key=lambda x: x['age'])
print(stus)
