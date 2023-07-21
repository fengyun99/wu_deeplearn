#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/7/12 10:17
# @Author   : FengYun
# @File     : learn_trans01.py
# @Software : PyCharm
# 情感分类
from transformers import pipeline
import warnings
# 写在最前面
warnings.filterwarnings("ignore")
classifier = pipeline("sentiment-analysis")
print("单个输出")
print(classifier("We are very happy to show you the 🤗 Transformers library."))
print("多个输出")
print(classifier(["We are very happy to show you the 🤗 Transformers library.", "We hope you don't hate it."]))