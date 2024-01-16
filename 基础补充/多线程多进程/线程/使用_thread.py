#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/11/1 20:09
# @Author   : FengYun
# @File     : 使用_thread.py
# @Software : PyCharm
import _thread
import time


def fun1():
    print('开始运行 fun1')
    time.sleep(4)
    print('运行 fun1 结束')


def fun2():
    print('开始运行 fun2')
    time.sleep(2)
    print('运行 fun2 结束')


if __name__ == '__main__':
    print('开始运行')
    # 启动一个线程运行函数 fun1
    _thread.start_new_thread(fun1, ())
    # 启动一个线程运行函数 fun2
    _thread.start_new_thread(fun2, ())
    time.sleep(6)
