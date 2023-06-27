#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/6/5 19:07
# @Author   : FengYun
# @File     : test.py
# @Software : PyCharm
import numpy as np
x = np.arange(0., 10., 0.2)
print(x)
m = len(x)  # 训练数据点数目
print(m)
x0 = np.full(m, 1.0)
print(x0)
input_data = np.vstack([x0, x]).T
print(input_data)
print(input_data.shape)
# print(np.random.seed(0))
q = np.random.randn(2)
print(q)
print(q.shape)
print(np.dot(np.random.randn(2), input_data[0]))