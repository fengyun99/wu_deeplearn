#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/10/31 19:17
# @Author   : FengYun
# @File     : 创建函数并作为多进程.py
# @Software : PyCharm
# 导入模块
import multiprocessing
import time


# 创建进程调用函数
def work1(interval):
    print('work1')
    time.sleep(interval)
    print('end work1')


def work2(interval):
    print('work2')
    time.sleep(interval)
    print('end work2')


def work3(interval):
    print('work3')
    time.sleep(interval)
    print('end work3')


if __name__ == '__main__':
    # 创建进程对象，运行顺序不一定顺序进行
    p1 = multiprocessing.Process(target=work1, args=(4,))
    p2 = multiprocessing.Process(target=work2, args=(3,))
    p3 = multiprocessing.Process(target=work3, args=(2,))
    # 启动进程
    p1.start()
    p2.start()
    p3.start()
    p1.join()
    p2.join()
    p3.join()
    print('主进程结束')
