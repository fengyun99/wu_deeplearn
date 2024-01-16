#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/11/1 20:40
# @Author   : FengYun
# @File     : 处理死锁，线程同步.py
# @Software : PyCharm
import time
from threading import Thread, Lock
import threading

lock1 = Lock()
lock2 = Lock()
lock3 = Lock()
lock2.acquire()
lock3.acquire()


class Task1(Thread):
    def run(self):
        while True:
            if lock1.acquire():
                print('...task1...')
                time.sleep(1)
                lock2.release()


class Task2(Thread):
    def run(self):
        while True:
            if lock2.acquire():
                print('...task2...')
                time.sleep(1)
                lock3.release()


class Task3(Thread):
    def run(self):
        while True:
            if lock3.acquire():
                print('...task3...')
                time.sleep(1)
                lock1.release()


if __name__ == '__main__':
    t1 = Task1()
    t2 = Task2()
    t3 = Task3()
    t1.start()
    t2.start()
    t3.start()
