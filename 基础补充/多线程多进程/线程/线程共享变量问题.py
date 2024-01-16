#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/11/1 20:28
# @Author   : FengYun
# @File     : 线程共享变量问题.py
# @Software : PyCharm
import time
from threading import *

# 定义全局变量 num
num = 0


def t1():
    global num
    for i in range(1000000):
        num += 1
    print('test1 输出 num:', num)


def t2():
    global num
    for i in range(1000000):
        num += 1
    print('test2 输出 num:', num)


if __name__ == '__main__':
    t1 = Thread(target=t1)
    t2 = Thread(target=t2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
