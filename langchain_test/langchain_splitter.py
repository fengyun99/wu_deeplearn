#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/5/10 10:34
# @Author   : FengYun
# @File     : langchain_splitter.py
# @Software : PyCharm
import json

from langchain.text_splitter import RecursiveCharacterTextSplitter

with open("data/data.txt", "r", encoding="utf-8") as f:
    content = f.read()

# 构造分词器
text_splitter = RecursiveCharacterTextSplitter(
    # Set a really small chunk size, just to show.
    chunk_size=50,
    chunk_overlap=20,
    length_function=len,
)

texts = text_splitter.create_documents([content])
print(texts[0])
print(texts[1])
# 判断文段是否是连续的内容
if json.loads(texts[0].json())["page_content"][-20:] == json.loads(texts[1].json())["page_content"][:20]:
    print(json.loads(texts[0].json())["page_content"] + json.loads(texts[1].json())["page_content"][:20])
