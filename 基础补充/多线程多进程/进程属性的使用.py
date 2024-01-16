#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/10/31 19:14
# @Author   : FengYun
# @File     : 进程属性的使用.py
# @Software : PyCharm
# 导入模块
import multiprocessing
import time


# 定义进程执行函数
def clock(interval):
    for i in range(5):
        print('当前时间为{0}：'.format(time.ctime()))
        time.sleep(interval)


if __name__ == '__main__':
    # 创建进程
    p = multiprocessing.Process(target=clock, args=(1,))
    # 启动进程
    p.start()
    p.join()
    # 获取进程的 ID
    print('p.id:', p.pid)
    # 获取进程的名称
    print('p.name:', p.name)
    # 判断进程是否运行
    print('p.is_alive:', p.is_alive())
