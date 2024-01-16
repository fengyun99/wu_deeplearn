#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/11/1 19:58
# @Author   : FengYun
# @File     : 队列的基本使用.py
# @Software : PyCharm
from multiprocessing import Queue

q = Queue(3)
q.put('消息 1')
q.put('消息 2')
print('消息队列是否已满：', q.full())
q.put('消息 3')
print('消息队列是否已满：', q.full())
# q.put('消息 4')因为消息队列已满，需要直接写入需要等待，如果超时会抛出异常，
# 所以写入时候需判断，消息队列是否已满
if not q.full():
    q.put('消息 4')
# 同理读取消息时，先判断消息队列是否为空，再读取
if not q.empty():
    for i in range(q.qsize()):
        print(q.get())
