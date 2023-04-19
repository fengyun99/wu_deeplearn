#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/4/19 13:31
# @Author   : FengYun
# @File     : use_modle2vec.py
# @Software : PyCharm
from transformers import AutoTokenizer, AutoModel
from argparse import Namespace
import numpy as np
import pandas as pd
'''
后续，对长文本按句子分割，然后将长文本用循环存储到csv文件当中
'''

model = "silk-road/luotuo-bert"
text = "我爱你"
text01 = '''南郑县气象局2016年7月22日14时22分发布雷电黄色预警信号:预计未来六小时我县境内将会出现雷电活动,并伴有短时强降水、大风、冰雹等强对流性天气。请注意防范。'''
tokenizer = AutoTokenizer.from_pretrained(model)
model_args = Namespace(do_mlm=None, pooler_type="cls", temp=0.05, mlp_only_train=False, init_embeddings_model=None)
model = AutoModel.from_pretrained(model, trust_remote_code=True, model_args=model_args)
inputs = tokenizer(text01, padding=True, truncation=True, return_tensors="pt", max_length=128)
embed = np.array(model(**inputs, output_hidden_states=True, return_dict=True, sent_emb=True).pooler_output.detach().numpy()[0])
np.set_printoptions(threshold=np.inf)
# 创建数据
data = {'sentence': [text01], 'embed': [embed.tolist()]}
# 创建DataFrame
df = pd.DataFrame(data)
# 保存为csv文件
df.to_csv('data.csv', index=False)



