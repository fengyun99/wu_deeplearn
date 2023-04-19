#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/4/17 21:49
# @Author   : FengYun
# @File     : mul_linear.py
# @Software : PyCharm
import copy
import math

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
    # 获取数据量
    m = X.shape[0]
    cost = 0.0
    for i in range(m):
        f_wb_i = np.dot(X[i], w) + b  # (n,)(n,) = scalar (see np.dot)
        cost = cost + (f_wb_i - y[i]) ** 2  # scalar
    cost = cost / (2 * m)  # scalar
    return cost


# 测试损失函数
cost = compute_cost(X_train, y_train, w_init, b_init)
print(f'Cost at optimal w : {cost}')


# 计算梯度
def compute_gradient(X, y, w, b):
    m, n = X.shape  # m是样本数量，n是特征数量
    dj_dw = np.zeros((n,))
    dj_db = 0.

    for i in range(m):
        # 预测和真实值的偏差量
        err = (np.dot(X[i], w) + b) - y[i]
        for j in range(n):
            # 计算w的梯度
            dj_dw[j] = dj_dw[j] + err * X[i, j]
        # 计算b的梯度
        dj_db = dj_db + err
    dj_dw = dj_dw / m
    dj_db = dj_db / m

    return dj_db, dj_dw


# 梯度下降---设置α
def gradient_descent(X, y, w_in, b_in, cost_function, gradient_function, alpha, num_iters):
    J_history = []
    w = copy.deepcopy(w_in)  # 深拷贝，避免操作影响原数组
    b = b_in

    for i in range(num_iters):

        # 计算梯度，更新梯度
        dj_db, dj_dw = gradient_function(X, y, w, b)  ##None

        # Update Parameters using w, b, alpha and gradient
        w = w - alpha * dj_dw  ##None
        b = b - alpha * dj_db  ##None

        # Save cost J at each iteration
        if i < 100000:  # prevent resource exhaustion
            J_history.append(cost_function(X, y, w, b))

        # Print cost every at intervals 10 times or as many iterations if < 10
        if i % math.ceil(num_iters / 10) == 0:
            print(f"Iteration {i:4d}: Cost {J_history[-1]:8.2f}   ")

    return w, b, J_history  # return final w,b and J history for graphing