#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/4/19 13:31
# @Author   : FengYun
# @File     : use_modle2vec.py
# @Software : PyCharm
import csv

from transformers import AutoTokenizer, AutoModel
from argparse import Namespace
import numpy as np
import pandas as pd
'''
后续，对长文本按句子分割，然后将长文本用循环存储到csv文件当中
'''
text = []
model = "silk-road/luotuo-bert"
with open('data.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        text.append(line)

tokenizer = AutoTokenizer.from_pretrained(model)
model_args = Namespace(do_mlm=None, pooler_type="cls", temp=0.05, mlp_only_train=False, init_embeddings_model=None)
model = AutoModel.from_pretrained(model, trust_remote_code=True, model_args=model_args)
inputs = tokenizer(text[0], padding=True, truncation=True, return_tensors="pt", max_length=512)

embed = np.array(model(**inputs, output_hidden_states=True, return_dict=True, sent_emb=True).pooler_output.detach().numpy()[0])
np.set_printoptions(threshold=np.inf)
# 创建数据
data = {'sentence': text[0], 'embed': [embed.tolist()]}
# 创建DataFrame
df = pd.DataFrame(data)
# 保存为csv文件,数据添加""
df.to_csv('data.csv', index=False)