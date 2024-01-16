#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/11/1 20:32
# @Author   : FengYun
# @File     : 线程互斥锁.py
# @Software : PyCharm
import time
from threading import Thread, Lock

# 定义全局变量 num
num = 0
# 创建一把互斥锁
mutex = Lock()


def t1():
    global num
    '''在两个线程中都调用上锁的方法，则这两个线程就会抢着上锁，
    如果有 1 方成功上锁，那么导致另外一方会堵塞（一直等待）直到这个锁被解开
    '''
    mutex.acquire()  # 上锁
    for i in range(10000000):
        num += 1
    mutex.release()
    print('test1 输出 num:', num)


def t2():
    global num
    mutex.acquire()  # 上锁
    for i in range(10000000):
        num += 1
    mutex.release()
    print('test2 输出 num:', num)


if __name__ == '__main__':
    t1 = Thread(target=t1)
    t2 = Thread(target=t2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
