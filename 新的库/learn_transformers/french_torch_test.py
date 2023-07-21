#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/7/12 14:41
# @Author   : FengYun
# @File     : french_torch_test.py
# @Software : PyCharm
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline
# 模型名称
model_name = "nlptown/bert-base-multilingual-uncased-sentiment"
# 加载模型
model = AutoModelForSequenceClassification.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)
# 加载管道，类型，模型，分词器
classifier = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)
print(classifier("Nous sommes très heureux de vous présenter la bibliothèque 🤗 Transformers."))