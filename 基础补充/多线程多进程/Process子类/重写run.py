#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/10/31 19:21
# @Author   : FengYun
# @File     : 重写run.py
# @Software : PyCharm
# 导入模块
from multiprocessing import Process
import time


# 定义线程类
class ClockProcess(Process):
    def __init__(self, interval):
        Process.__init__(self)
        self.interval = interval

    def run(self):
        print('子进程开始执行的时间:{}'.format(time.ctime()))
        time.sleep(self.interval)
        print('子进程结束的时间:{}'.format(time.ctime()))


if __name__ == '__main__':
    # 创建进程
    p = ClockProcess(2)
    # 启动进程
    p.start()
    p.join()
    print('主进程结束')
