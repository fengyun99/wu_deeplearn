#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/10/22 16:16
# @Author   : FengYun
# @File     : 参数.py
# @Software : PyCharm
def fun(a, b, *args, **kwargs):
    print(a)
    print(b)
    print(args)
    for k, v in kwargs.items():
        print(str(k) + '=' + str(v))


if __name__ == '__main__':
    fun(1, 2, 3, 4, 5, m=6, n=7, p=8)