#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/11/1 20:12
# @Author   : FengYun
# @File     : 线程传递参数.py
# @Software : PyCharm
import _thread
import time


def fun1(thread_name, delay):
    print('线程{0}开始运行 fun1'.format(thread_name))
    time.sleep(delay)
    print('线程{0}运行 fun1 结束'.format(thread_name))


def fun2(thread_name, delay):
    print('线程{0}开始运行 fun2'.format(thread_name))
    time.sleep(delay)
    print('线程{0}运行 fun2 结束'.format(thread_name))


if __name__ == '__main__':
    print('开始运行')
    # 启动一个线程运行函数 fun1
    _thread.start_new_thread(fun1, ('thread-1', 4))
    # 启动一个线程运行函数 fun2
    _thread.start_new_thread(fun2, ('thread-2', 2))
    time.sleep(6)
