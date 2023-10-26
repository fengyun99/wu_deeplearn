#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/9/10 20:00
# @Author   : FengYun
# @File     : bert使用.py
# @Software : PyCharm
# bert 最后生成词向量
from transformers import BertModel, BertTokenizer
import torch
from torch import nn

sentence = 'i like eating apples very much'


class Model(nn.Module):
    def __init__(self):
        super().__init__()
        self.embedder = BertModel.from_pretrained("bert-base-cased", output_hidden_states=True)
        self.tokenizer = BertTokenizer.from_pretrained("bert-base-cased")

    def forward(self, inputs):
        tokens = self.tokenizer.tokenize(inputs)
        print(tokens)
        tokens_id = self.tokenizer.convert_tokens_to_ids(tokens)
        print(tokens_id)
        tokens_id_tenser = torch.tensor(tokens_id).unsqueeze(0)  # 变成1*6数组
        outputs = self.embedder(tokens_id_tenser)
        print(outputs)
        # print(outputs[0].shape)


model = Model()
results = model(sentence)
