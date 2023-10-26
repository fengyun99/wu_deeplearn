#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/8/28 14:21
# @Author   : FengYun
# @File     : use_hunmanprompt.py
# @Software : PyCharm
from langchain.prompts import HumanMessagePromptTemplate, ChatPromptTemplate

human_prompt = "{input}"
human_message_template = HumanMessagePromptTemplate.from_template(human_prompt)
print(human_message_template)
chat_prompt = ChatPromptTemplate.from_messages(
    [("human", "我们来玩成语接龙，我先来，生龙活虎"),
     ("ai", "虎头虎脑"),
     ("human", "{input}")])
print(chat_prompt)