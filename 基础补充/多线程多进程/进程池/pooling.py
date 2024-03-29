#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/11/1 19:15
# @Author   : FengYun
# @File     : pooling.py
# @Software : PyCharm
# 操作多个文件目录或者远控多台主机时，并行操作可以节约时间。
# 非阻塞
import multiprocessing
import time


def func(msg):
    print("start:", msg)
    time.sleep(5)  # 太小没效果太大也看不出
    print("end：", msg)


if __name__ == "__main__":
    pool = multiprocessing.Pool(processes=3)
    for i in range(5):
        msg = "hello %d" % (i)
        # 维持执行的进程总数为 processes，当一个进程执行完毕后会添加新的进程进去
        pool.apply_async(func, (msg,))
    pool.close()  # 进程池关闭之后不再接收新的请求
    # 调用 join 之前，先调用 close 函数，否则会出错。
    # 执行完 close 后不会有新的进程加入到 pool,join 函数等待所有子进程结束
    pool.join()
