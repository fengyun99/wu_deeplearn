#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/9/10 21:03
# @Author   : FengYun
# @File     : RNN模型.py
# @Software : PyCharm
# RNNCell
import torch
from torch import nn

x_input = torch.randn(2, 3, 10)


class RNN(nn.Module):
    def __init__(self, input_size, hidden_size, batch_first=False):
        super(RNN, self).__init__()
        self.rnn_cell = nn.RNNCell(input_size, hidden_size)

        self.batch_first = batch_first
        self.hidden_size = hidden_size

    def _init_hidden(self, batch_size):
        return torch.zeros(batch_size, self.hidden_size)

    def forward(self, inputs, init_hidden=None):
        if self.batch_first:
            batch_size, seq_size, fear_size = inputs.size()
            inputs = inputs.permute(1, 0, 2)

        else:
            seq_size, batch_size, feat_size = inputs.size()

        hiddens = []

        if init_hidden is None:
            init_hidden = self._init_hidden(batch_size)
            init_hidden = init_hidden.to(inputs.device)  # 放在什么设备上

        hidden_t = init_hidden

        for t in range(seq_size):
            hidden_t = self.rnn_cell(inputs[t], hidden_t)
            hiddens.append(hidden_t)

        hiddens = torch.stack(hiddens)

        if self.batch_first:
            hiddens = hiddens.permute(1, 0, 2)

        return hiddens


model = RNN(10, 15, batch_first=True)

outputs = model(x_input)
print(outputs.shape)
