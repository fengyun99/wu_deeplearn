#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/9/10 18:00
# @Author   : FengYun
# @File     : 神经语言模型.py
# @Software : PyCharm
import torch
from hanlp.components.amr.seq2seq import optim
from torch import nn
from torch import optim
from torch.autograd import Variable

dtype = torch.FloatTensor

sentences = ['i like dog', 'i love coffee', 'i hate milk', 'i like nlp']

word_list = ' '.join(sentences).split()
word_list = list(set(word_list))

word_dict = {w: i for i, w in enumerate(word_list)}
number_dict = {i: w for i, w in enumerate(word_list)}

n_calss = len(word_list)
m = 2
n_step = 2
n_hidden = 2


def make_batch(sentences):
    input_batch = []
    target_batch = []

    for s in sentences:
        word = s.split()
        input = [word_dict[n] for n in word[:-1]]
        target = word_dict[word[-1]]
        # print(input)
        # print(target)
        input_batch.append(input)
        target_batch.append(target)
    return input_batch, target_batch


class NNLM(nn.Module):
    def __init__(self):
        super(NNLM, self).__init__()
        self.embed = nn.Embedding(n_calss, m)
        self.W = nn.Parameter(torch.randn(n_step * m, n_hidden).type(dtype))
        self.d = nn.Parameter(torch.randn(n_hidden).type(dtype))
        self.U = nn.Parameter(torch.randn(n_hidden, n_calss).type(dtype))
        self.b = nn.Parameter(torch.randn(n_calss).type(dtype))

    def forward(self, x):
        x = self.embed(x)  # 4 * 2 * 2 四句子每句两个词
        x = x.view(-1, n_step * m)
        tanh = torch.tanh(self.d + torch.mm(x, self.W))
        output = self.b + torch.mm(tanh, self.U)
        return output


model = NNLM()

criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

input_batch, target_batch = make_batch(sentences)
input_batch = Variable(torch.LongTensor(input_batch))
target_batch = Variable(torch.LongTensor(target_batch))

for epoch in range(5000):
    optimizer.zero_grad()

    output = model(input_batch)

    loss = criterion(output, target_batch)  # 交叉熵损失函数

    if (epoch + 1) % 1000 == 0:
        print('epoch:', epoch + 1, f"cost={loss.item()}")

    loss.backward()
    optimizer.step()

predict = model(input_batch).data.max(1, keepdim=True)[1]
