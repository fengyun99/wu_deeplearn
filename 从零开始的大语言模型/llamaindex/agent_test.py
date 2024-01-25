#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2024/1/5 16:55
# @Author   : FengYun
# @File     : agent_test.py
# @Software : PyCharm
import json
from typing import Sequence, List

from llama_index.llms import OpenAI, ChatMessage
from llama_index.tools import BaseTool, FunctionTool
from openai.types.chat import ChatCompletionMessageToolCall
import nest_asyncio
import os
from llama_index.agent import OpenAIAgent
from llama_index.llms import OpenAI

os.environ["OPENAI_API_KEY"] = "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"
nest_asyncio.apply()


def multiply(a: int, b: int) -> int:
    """Multiple two integers and returns the result integer"""
    return a * b


def add(a: int, b: int) -> int:
    """Add two integers and returns the result integer"""
    return a + b


add_tool = FunctionTool.from_defaults(fn=add)

multiply_tool = FunctionTool.from_defaults(fn=multiply)

llm = OpenAI(model="gpt-3.5-turbo-0613")
agent = OpenAIAgent.from_tools(
    [multiply_tool, add_tool], llm=llm, verbose=True
)

# 自定义agent的流程
# class YourOpenAIAgent:
#     def __init__(
#             self,
#             tools: Sequence[BaseTool] = [],
#             llm: OpenAI = OpenAI(temperature=0, model="gpt-3.5-turbo-0613"),
#             chat_history: List[ChatMessage] = [],
#     ) -> None:
#         self._llm = llm
#         self._tools = {tool.metadata.name: tool for tool in tools}
#         self._chat_history = chat_history
#
#     def reset(self) -> None:
#         self._chat_history = []
#
#     def chat(self, message: str) -> str:
#         chat_history = self._chat_history
#         chat_history.append(ChatMessage(role="user", content=message))
#         tools = [
#             tool.metadata.to_openai_tool() for _, tool in self._tools.items()
#         ]
#
#         ai_message = self._llm.chat(chat_history, tools=tools).message
#         additional_kwargs = ai_message.additional_kwargs
#         chat_history.append(ai_message)
#
#         tool_calls = additional_kwargs.get("tool_calls", None)
#         # print(tool_calls)
#         # parallel function calling is now supported
#         if tool_calls is not None:
#             for tool_call in tool_calls:
#                 function_message = self._call_function(tool_call)
#                 chat_history.append(function_message)
#                 ai_message = self._llm.chat(chat_history).message
#                 chat_history.append(ai_message)
#
#         return ai_message.content
#
#     def _call_function(self, tool_call: ChatCompletionMessageToolCall) -> ChatMessage:
#         id_ = tool_call.id
#         function_call = tool_call.function
#         tool = self._tools[function_call.name]
#         output = tool(**json.loads(function_call.arguments))
#         return ChatMessage(
#             name=function_call.name,
#             content=str(output),
#             role="tool",
#             additional_kwargs={
#                 "tool_call_id": id_,
#                 "name": function_call.name,
#             },
#         )


if __name__ == '__main__':
    # agent = YourOpenAIAgent(tools=[multiply_tool, add_tool])
    # # print(agent.chat("Hi"))
    # # print(agent.chat("What is 2123 * 215123"))
    # print(agent.chat("999 + 123的答案是多少?"))
    response = agent.chat("What is (121 * 3) + 42?")
    print(str(response))
