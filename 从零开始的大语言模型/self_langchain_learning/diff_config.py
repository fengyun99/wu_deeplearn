#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/12/29 15:56
# @Author   : FengYun
# @File     : diff_config.py
# @Software : PyCharm
from langchain_community.chat_models import ChatOpenAI, ChatAnthropic
from langchain_community.llms import OpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import ConfigurableField, RunnablePassthrough
from dotenv import load_dotenv, find_dotenv
# 加载环境
_ = load_dotenv(find_dotenv())

# 三种模型
model = ChatOpenAI(model="gpt-3.5-turbo")
llm = OpenAI(model="gpt-3.5-turbo-instruct")
# anthropic = ChatAnthropic(model="claude-2")

prompt = ChatPromptTemplate.from_template(
    "Tell me a short joke about {topic}"
)
output_parser = StrOutputParser()


configurable_model = model.configurable_alternatives(
    ConfigurableField(id="model"),
    default_key="chat_openai",
    openai=llm,
    # anthropic=anthropic,
)
configurable_chain = (
    {"topic": RunnablePassthrough()}
    | prompt
    | configurable_model
    | output_parser
)

print(configurable_chain.invoke(
    "ice cream",
    config={"model": "openai"}
))
# stream = configurable_chain.stream(
#     "ice cream",
#     config={"model": "anthropic"}
# )
# for chunk in stream:
#     print(chunk, end="", flush=True)

print(configurable_chain.batch(["ice cream", "spaghetti", "dumplings"]))

# await configurable_chain.ainvoke("ice cream")