#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/11/1 19:34
# @Author   : FengYun
# @File     : 多进程数据不共享.py
# @Software : PyCharm
from multiprocessing import Process

num = 1


def work1():
    global num
    num += 5
    print('子进程 1 运行，num:', num)


def work2():
    global num
    num += 10
    print('子进程 2 运行，num：', num)


if __name__ == '__main__':
    print('父进程开始运行')
    p1 = Process(target=work1)
    p2 = Process(target=work2)
    p1.start()
    p2.start()
    p1.join()
    p2.join()
