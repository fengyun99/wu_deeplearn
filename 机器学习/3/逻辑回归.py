#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/6/17 15:33
# @Author   : FengYun
# @File     : 逻辑回归.py
# @Software : PyCharm
from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize
from matplotlib.font_manager import FontProperties

# 解决windows环境下画图汉字乱码问题
font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=14)


# 定义逻辑回归算法函数
def LogisticRegression():
    data = loadtxtAndcsv_data("data2.txt", ", ", np.float64)
    X = data[:, 0:-1]
    y = data[:, -1]

    plot_data(X, y)  # 画图

    X = mapFeature(X[:, 0], X[:, 1])  # 映射为多项式
    initial_theta = np.zeros((X.shape[1], 1))  # 初始化theta
    initial_lambda = 0.1  # 初始化正则化系数， 一般取0.01, 0.1, 1 ....

    J = costFunction(initial_theta, X, y, initial_lambda)  # 计算一下给定初始化的theta和lambda求出的代价J
    print(J)  # 输出计算的值
    # result = optimize.fmin(costFunction, initial_theta, args=(X, y, initial_lambda)) # 直接使用最小化的方法，效果不好
    '''调用SciPy中的优化算法fmin_bfgs(拟牛顿法Broyden-Fletcher-Goldfarb-Shanno)
    - costFunction 是自己实现的一个求代价的函数
    - initial_theta 表示初始化的值
    - fprime 指定costFunction的梯度
    - args 是其预测参数，以元组的形式传入，最后会将最小化costFunction的theta返回
    '''
    result = optimize.fmin_bfgs(costFunction, initial_theta, fprime=gradient, args=(X, y, initial_lambda))
    p = predict(X, result)  # 预测
    print(u'在训练集上的准确度为%f%%' % np.mean(np.float64(p == y) * 100))  # 与真实值比较，p==y返回True，转为float
    X = data[:, 0:-1]
    y = data[:, -1]
    plotDecisionBoundary(result, X, y)  # 画决策边界


# 加载txt和csv文件
def loadtxtAndcsv_data(filename, split, dataType):
    return np.loadtxt(filename, delimiter=split, dtype=dataType)


# 加载npy文件
def loadnpy_data(fileName):
    return np.load(fileName)


# 显示二维图形
def plot_data(X, y):
    pos = np.where(y == 1)
    neg = np.where(y == 0)
    # 作图
    plt.figure(figsize=(15, 12))
    plt.plot(X[pos, 0], X[pos, 1], 'ro')  # red o
    plt.plot(X[neg, 0], X[neg, 1], 'bo')  # blue o
    plt.title(u"两个类别数点图", fontproperties=font)
    plt.show()


# 映射为多项式
def mapFeature(X1, X2):
    degree = 2  # 映射的最高次方
    out = np.ones((X1.shape[0], 1))  # 映射后的结果数组（取代x）
    '''
    这里degree=2为例，映射为1,x1,x2,x1^2,X1,X2,X2^2
    '''
    for i in np.arange(1, degree + 1):
        for j in range(i + 1):
            temp = X1 ** (i - j) * (X2 ** j)
            out = np.hstack((out, temp.reshape(-1, 1)))
    return out


# 代价函数
def costFunction(initial_theta, X, y, initial_lambda):
    m = len(y)
    J = 0

    h = sigmoid(np.dot(X, initial_theta))  # 计算h(z)
    theta = initial_theta.copy()  # 因为正则化j=1从1开始，不包含0，所以复制一份，前theta(0)为0
    theta[0] = 0
    temp = np.dot(np.transpose(theta), theta)
    J = (-np.dot(np.transpose(y), np.log(h)) - np.dot(np.transpose(1 - y), np.log(h)) - np.dot(np.transpose(1 - y),
                                                                                               np.log(
                                                                                                   1 - h)) + temp * initial_lambda / 2) / m
    return J

# 计算梯度
def gradient(initial_theta, X, y, initial_lambda):
    m = len(y)
    grad = np.zeros((initial_theta.shape[0]))

    h = sigmoid(np.dot(X, initial_theta)) # 计算h(z)
    theta = initial_theta.copy()
    theta[0] = 0
    grad = np.dot(np.transpose(X), h-y)/m + initial_lambda/m*theta # 正则化的梯度
    return grad

def sigmoid(z):
    h = np.zeros(len(z), 1) # 初始化，与z的长度一致
    h = 1.0/(1.0+np.exp(-z))
    return h

# 画决策边界
def plotDecisionBoundary(theta, X, y):
    pos = np.where(y == 1) #找到y==1的坐标
    neg = np.where(y == 0) #找到y==0的坐标
    # 作图
    plt.figure(figsize=(15, 12))
    plt.plot(X[pos, 0], X[pos, 1], 'ro')  # red o
    plt.plot(X[neg, 0], X[neg, 1], 'bo')  # blue o
    plt.title(u"两个类别数点图", fontproperties=font)
    # u = np.linspace(30, 100, 100)
    # v = np.linspace(30, 100, 100)
    u = np.linspace(-1, 1.5, 50) # 根据具体数据调整
    v = np.linspace(-1, 1.5, 50)
    z = np.zeros((len(u), len(v)))
    for i in range(len(u)):
        for j in range(len(v)):
            z[i, j] = np.dot(mapFeature(u[i].reshape(1, -1), v[j].reshape(1, -1)), theta) # 计算对应的值，需要map
    z = np.transpose(z)
    plt.contour(u, v, z, [0, 0.01], linewidth=2.0) # 画等高线，范围在[0, 0.01], 即计时为决策边界
    # plt.legend()
    plt.show()

# 预测
def predict(X, theta):
    m = X.shape[0]
    p = np.zeros((m, 1))
    p = sigmoid(np.dot(X, theta))  # 预测的结果，概率
    for i in range(m):
        if p[i] > 0.5:
            p[i] = 1
        else:
            p[i] = 0
    return p

# 测试逻辑回归
def testLogisticRegression():
    LogisticRegression()

if __name__ == '__main__':
    testLogisticRegression()
