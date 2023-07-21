#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/7/12 14:43
# @Author   : FengYun
# @File     : french_tf_test.py
# @Software : PyCharm
from transformers import AutoTokenizer, TFAutoModelForSequenceClassification
model_name = "nlptown/bert-base-multilingual-uncased-sentiment"
model = TFAutoModelForSequenceClassification.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)