#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/9/10 20:47
# @Author   : FengYun
# @File     : MLP使用.py
# @Software : PyCharm
# 多层感知机
import torch
from torch import nn
import torch.nn.functional as F

x_input = torch.randn(2, 3, 10)  # 输入10


# print(x_input)


class MLP(nn.Module):
    def __init__(self, input_dim, hidden_dim, output_dim):
        super(MLP, self).__init__()
        self.fc1 = nn.Linear(input_dim, hidden_dim)
        self.fc2 = nn.Linear(hidden_dim, output_dim)

    def forward(self, inputs):
        intermediate = F.relu(self.fc1(inputs))
        outputs = self.fc2(intermediate)
        # 概率分布
        outputs = F.softmax(outputs, dim=2)

        return outputs


model = MLP(10, 20, 5)
x_output = model(x_input)
print(x_output)  # 输出5
