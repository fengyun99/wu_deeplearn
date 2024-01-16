#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/11/1 19:59
# @Author   : FengYun
# @File     : 队列实现进程间的通信.py
# @Software : PyCharm
from multiprocessing import *
import time


def write(q):
    # 将列表中的元素写入队列中
    for i in ["a", "b", "c"]:
        print('开始写入值%s' % i)
        q.put(i)
        time.sleep(1)


# 读取
def read(q):
    print('开始读取')
    while True:
        if not q.empty():
            print('读取到:', q.get())
            time.sleep(1)
        else:
            break


if __name__ == '__main__':
    # 创建队列
    q = Queue()
    # 创建写入进程
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动进程
    pw.start()
    pw.join()
    pr.start()
    pr.join()
