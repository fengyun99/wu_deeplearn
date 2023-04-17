#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/4/17 21:49
# @Author   : FengYun
# @File     : mul_linear.py
# @Software : PyCharm

import numpy as np

# 训练的数据
X_train = np.array([[2104, 5, 1, 45], [1416, 3, 2, 40], [852, 2, 1, 35]])
y_train = np.array([460, 232, 178])

# 设置初始化的w,b
b_init = 785.1811367994083
w_init = np.array([0.39133535, 18.75376741, -53.36032453, -26.42131618])


# 通过循环获得预测值y_hat
def predict_single_loop(x, w, b):
    # 获取矩阵的样本数，即行数
    n = x.shape[0]
    p = 0
    for i in range(n):
        p_i = x[i] * w[i]
        p = p + p_i
    p = p + b
    return p


# 通过点乘获得预测值
def predict(x, w, b):
    """
    single predict using linear regression
    Args:
      x (ndarray): Shape (n,) example with multiple features
      w (ndarray): Shape (n,) model parameters
      b (scalar):             model parameter

    Returns:
      p (scalar):  prediction
    """
    p = np.dot(x, w) + b
    return p


# 获取每列的数据
x_vec1 = X_train[0, :]

# 获得预测值
f_wb1 = predict_single_loop(x_vec1, w_init, b_init)

x_vec2 = X_train[0,:]
f_wb2 = predict(x_vec2,w_init, b_init)


# 损失函数计算
def compute_cost(X, y, w, b):
    m = X.shape[0]
    cost = 0.0
    for i in range(m):
        f_wb_i = np.dot(X[i], w) + b  # (n,)(n,) = scalar (see np.dot)
        cost = cost + (f_wb_i - y[i]) ** 2  # scalar
    cost = cost / (2 * m)  # scalar
    return cost