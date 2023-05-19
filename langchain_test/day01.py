#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/5/10 09:51
# @Author   : FengYun
# @File     : day01.py
# @Software : PyCharm
import os
import datetime
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.llms import OpenAI
from langchain.agents import AgentType

os.environ["OPENAI_API_KEY"] = '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'
os.environ["SERPAPI_API_KEY"] = 'e5c5471b199a145db984e7a4bf094efb95fe0e1e9d5bb18f4597a1ac1b42a8ec'

# 加载 OpenAI 模型
llm = OpenAI(temperature=0, max_tokens=2048)

# 加载 serpapi 工具
tools = load_tools(["serpapi"])

# 如果搜索完想在计算一下可以这么写
# tools = load_tools(['serpapi', 'llm-math'], llm=llm)

# 如果搜索完想再让他再用python的print做点简单的计算，可以这样写
# tools=load_tools(["serpapi","python_repl"])

# 工具加载后都需要初始化，verbose 参数为 True，会打印全部的执行详情
agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

# 运行 agent
agent.run("今天的日期是，历史上今天发生的事情有哪些？")
