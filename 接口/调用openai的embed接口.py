#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/8/31 09:33
# @Author   : FengYun
# @File     : 调用openai的embed接口.py
# @Software : PyCharm
import os
import openai
openai.api_key = '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'
out= openai.Embedding.create(
  model="text-embedding-ada-002",
  input="测试数据"
)
print(out)