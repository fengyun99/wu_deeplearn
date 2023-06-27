#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/6/17 15:01
# @Author   : FengYun
# @File     : 第二章编程.py
# @Software : PyCharm
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
# 加载糖尿病数据集
diabetes = datasets.load_diabetes()
# print(diabetes)
# 只使用一个特征
diabetes_X = diabetes.data[:, np.newaxis, 2]
# print(diabetes_X)
# 将数据集分为训练集和测试集
diabetes_X_train = diabetes_X[:-20]
diabetes_X_test = diabetes_X[-20:]

# 将结果分为数据集和测试集
diabetes_Y_train = diabetes.target[:-20]
diabetes_Y_test = diabetes.target[-20:]

# 创建线性回归对象
regr = linear_model.LinearRegression()

# 使用训练集训练模型
regr.fit(diabetes_X_train, diabetes_Y_train)

# 系数
print("Coefficients: \n", regr.coef_)

# 平方误差
print("Residual sum of squares: %.2f" % np.mean((regr.predict(diabetes_X_test) - diabetes_Y_test) ** 2))

# 方差得分
print("Variance score: %.2f" % regr.score(diabetes_X_test, diabetes_Y_test))

# plt输出
plt.scatter(diabetes_X_test, diabetes_Y_test, color='black')
plt.plot(diabetes_X_test, regr.predict(diabetes_X_test), color='blue', linewidth=3)
plt.xticks(())
plt.yticks(())
plt.show()