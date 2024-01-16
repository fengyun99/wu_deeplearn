#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/11/1 20:21
# @Author   : FengYun
# @File     : 继承threading创建线程.py
# @Software : PyCharm
import threading
import time


def fun1(delay):
    print('线程{0}开始运行 fun1'.format(threading.current_thread().getName()))
    time.sleep(delay)
    print('线程{0}运行 fun1 结束'.format(threading.current_thread().getName()))


def fun2(delay):
    print('线程{0}开始运行 fun2'.format(threading.current_thread().getName()))
    time.sleep(2)
    print('线程{0}运行 fun2 结束'.format(threading.current_thread().getName()))


# 创建线程类继承 threading.Thread
class MyThread(threading.Thread):
    # 重写父类的构造方法，其中 func 是线程函数，args 是传入线程的参数,name 是线程名
    def __init__(self, func, name, args):
        super().__init__(target=func, name=name, args=args)

    # 重写父类的 run()方法
    def run(self):
        self._target(*self._args)


if __name__ == '__main__':
    print('开始运行')
    # 创建线程
    t1 = MyThread(fun1, 'thread-1', (2,))
    t2 = MyThread(fun2, 'thread-2', (4,))
    t1.start()
    t2.start()
