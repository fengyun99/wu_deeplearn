#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2024/1/5 14:41
# @Author   : FengYun
# @File     : a.py
# @Software : PyCharm
from llama_index import VectorStoreIndex, SimpleDirectoryReader
import os

os.environ["OPENAI_API_KEY"] = "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"
documents = SimpleDirectoryReader("data").load_data()
index = VectorStoreIndex.from_documents(documents)
query_engine = index.as_chat_engine()
response = query_engine.chat("What did the author do growing up?")
print(response)

response = query_engine.chat("Oh interesting, tell me more.")
print(response)