#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/10/28 22:03
# @Author   : FengYun
# @File     : 3.8多进程共享内存.py
# @Software : PyCharm
from multiprocessing import Process
from multiprocessing import shared_memory

share_nums = shared_memory.ShareableList(range(5))


def do_work1(nums):
    for i in range(5):
        nums[i] += 10
    print('do_work1 nums = %s' % nums)


def do_work2(nums):
    print('do_work2 nums = %s' % nums)


if __name__ == '__main__':
    p1 = Process(target=do_work1, args=(share_nums,))
    # 处理五个进程
    p1.start()
    p1.join()
    p2 = Process(target=do_work2, args=(share_nums,))
    p2.start()
