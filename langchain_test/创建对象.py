#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/8/29 09:54
# @Author   : FengYun
# @File     : 创建对象.py
# @Software : PyCharm
from typing import List

from pydantic import BaseModel


class OpenAiMessage(BaseModel):
    role: str = "user"
    content: str = "hello"


class OpenAiChatMsgIn(BaseModel):
    model: str = "aaa"
    messages: List[OpenAiMessage]
    temperature: float = 0.7
    n: int = 1
    max_tokens: int = 1024
    stop: List[str] = []
    stream: bool = False
    presence_penalty: int = 0
    frequency_penalty: int = 0


