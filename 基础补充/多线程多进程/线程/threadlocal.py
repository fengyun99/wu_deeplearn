#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/11/1 20:53
# @Author   : FengYun
# @File     : threadlocal.py
# @Software : PyCharm
import threading

# 创建全局 ThreadLocal 对象:
local = threading.local()


def process_student():
    # 获取当前线程关联的 name:
    student_name = local.name
    print('线程名：%s 学生姓名:%s' % (threading.current_thread().name, student_name))


def process_thread(name):
    # 绑定 ThreadLocal 的 name:
    local.name = name
    process_student()


t1 = threading.Thread(target=process_thread, args=('张三',), name='Thread-A')
t2 = threading.Thread(target=process_thread, args=('李四',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()
