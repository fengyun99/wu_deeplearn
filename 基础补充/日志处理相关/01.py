#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2024/1/16 17:09
# @Author   : FengYun
# @File     : 01.py
# @Software : PyCharm
import logging

# 创建第一个日志记录器
logger1 = logging.getLogger('logger1')
logger1.setLevel(logging.INFO)

# 创建第二个日志记录器
logger2 = logging.getLogger('logger2')
logger2.setLevel(logging.DEBUG)

# 创建处理程序和格式化程序
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# 为第一个记录器添加处理程序和格式化程序
file_handler1 = logging.FileHandler('logger1.log')
file_handler1.setFormatter(formatter)
logger1.addHandler(file_handler1)

# 为第二个记录器添加处理程序和格式化程序
file_handler2 = logging.FileHandler('logger2.log')
file_handler2.setFormatter(formatter)
logger2.addHandler(file_handler2)

# 记录日志信息
logger1.info('This is logger1')
logger2.debug('This is logger2')