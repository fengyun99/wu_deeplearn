#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2024/1/3 17:11
# @Author   : FengYun
# @File     : test.py
# @Software : PyCharm
from langchain.prompts import ChatPromptTemplate
from langchain_community.chat_models import ChatOpenAI
from dotenv import load_dotenv, find_dotenv
# 加载环境
_ = load_dotenv(find_dotenv())

model = ChatOpenAI()
prompt = ChatPromptTemplate.from_template("tell me a joke about {topic}")
chain = prompt | model

print(chain.input_schema.schema())
print(prompt.input_schema.schema())
print(model.input_schema.schema())