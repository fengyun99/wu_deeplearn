#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/12/29 15:33
# @Author   : FengYun
# @File     : parallel_request.py
# @Software : PyCharm
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv, find_dotenv
from langchain_core.runnables import RunnablePassthrough

# 加载环境
_ = load_dotenv(find_dotenv())

prompt = ChatPromptTemplate.from_template("Tell me a short joke about {topic}")
model = ChatOpenAI(model="gpt-3.5-turbo")
output_parser = StrOutputParser()

chain = {"topic": RunnablePassthrough()} | prompt | model | output_parser

print(chain.batch(["ice cream", "spaghetti", "dumplings"]))