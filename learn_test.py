#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/4/19 10:30
# @Author   : FengYun
# @File     : learn_test.py
# @Software : PyCharm
import numpy as np
import pandas as pd
arr = np.array([[1,2,3,4],[5,6,7,8]])
X,Y = np.split(arr,2,axis=1)
print(X.flatten())
print(Y.flatten())

# 创建数据
data = {'text': ['这是第一条文本', '这是第二条文本', '这是第三条文本'], 'label': [0, 1, 0]}

# 创建DataFrame
df = pd.DataFrame(data)

# 保存为csv文件
df.to_csv('data.csv', index=False)