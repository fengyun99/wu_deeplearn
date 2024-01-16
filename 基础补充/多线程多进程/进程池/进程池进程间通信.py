#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/11/1 20:03
# @Author   : FengYun
# @File     : 进程池进程间通信.py
# @Software : PyCharm
from multiprocessing import Manager, Pool
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
    q = Manager().Queue()
    # 创建进程池
    p = Pool(3)
    # 使用阻塞模式创建进程
    p.apply(write, (q,))
    p.apply(read, (q,))
    p.close()
    p.join()
