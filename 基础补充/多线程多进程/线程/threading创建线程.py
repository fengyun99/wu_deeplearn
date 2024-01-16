#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/11/1 20:19
# @Author   : FengYun
# @File     : threading创建线程.py
# @Software : PyCharm
import threading
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
    # 创建线程
    t1 = threading.Thread(target=fun1, args=('thread-1', 2))
    t2 = threading.Thread(target=fun2, args=('thread-2', 4))
    t1.start()
    t2.start()
