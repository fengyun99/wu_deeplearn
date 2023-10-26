#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/10/22 16:20
# @Author   : FengYun
# @File     : 自增.py
# @Software : PyCharm
# Python中函数参数是引用传递（注意不是值传递）。对于不可变类型，因变量不能修改，所以运算不会影响到
# 变量自身；而对于可变类型来说，函数体中的运算有可能会更改传入的参数变量。
import anyio.abc


def selfAdd(a):
    a += a


def selfAdd2(a):
    # 局部变量?
    a = a + a

def selfAddReturn(a):
    a += a
    return a


a_int = 1
selfAdd(a_int)
print(a_int)
a_list = [1, 2]
selfAdd(a_list)
print(a_list)
b = selfAddReturn(a_int)
print(a_int)
print(b)

a_int = 1
a_list = [1, 2]
selfAdd2(a_int)
print(a_int)
selfAdd2(a_list)
print(a_list)
