#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2024/1/10 11:19
# @Author   : FengYun
# @File     : llama_use.py
# @Software : PyCharm
from typing import List

from llama_index.llms.llama_api import LlamaAPI
from llama_index.program import OpenAIPydanticProgram
from pydantic import BaseModel
from llama_index.llms.openai_utils import to_openai_tool
import os

os.environ["OPENAI_API_KEY"] = "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"

api_key = "LL-lhIaip4ZCl2m4wfdpwdOAAJIOnH84bTAzIjwEQXrsJm98GoehVvsKyD3l6ZcJpMu"


# llm = LlamaAPI(api_key=api_key)
# resp = llm.complete("Paul Graham is ")
# print(resp)

# class Song(BaseModel):
# #     """A song with name and artist"""
# #
# #     name: str
# #     artist: str
# #
# #
# # song_fn = to_openai_tool(Song)  # json格式错误?
# #
# # llm = LlamaAPI(api_key=api_key)
# # response = llm.complete("Generate a song", functions=[song_fn])
# # print(response)
# # function_call = response.additional_kwargs["function_call"]
# # print(function_call)


class Song(BaseModel):
    """Data model for a song."""

    title: str
    length_mins: int


class Album(BaseModel):
    """Data model for an album."""

    name: str
    artist: str
    songs: List[Song]


prompt_template_str = """\
Extract album and songs from the text provided.
For each song, make sure to specify the title and the length_mins.
{text}
"""

llm = LlamaAPI(api_key=api_key, temperature=0.0)

program = OpenAIPydanticProgram.from_defaults(
    output_cls=Album,
    llm=llm,
    prompt_template_str=prompt_template_str,
    verbose=True,
)

output = program(
    text="""
"Echoes of Eternity" is a compelling and thought-provoking album, skillfully crafted by the renowned artist, Seraphina Rivers. \
This captivating musical collection takes listeners on an introspective journey, delving into the depths of the human experience \
and the vastness of the universe. With her mesmerizing vocals and poignant songwriting, Seraphina Rivers infuses each track with \
raw emotion and a sense of cosmic wonder. The album features several standout songs, including the hauntingly beautiful "Stardust \
Serenade," a celestial ballad that lasts for six minutes, carrying listeners through a celestial dreamscape. "Eclipse of the Soul" \
captivates with its enchanting melodies and spans over eight minutes, inviting introspection and contemplation. Another gem, "Infinity \
Embrace," unfolds like a cosmic odyssey, lasting nearly ten minutes, drawing listeners deeper into its ethereal atmosphere. "Echoes of Eternity" \
is a masterful testament to Seraphina Rivers' artistic prowess, leaving an enduring impact on all who embark on this musical voyage through \
time and space.
"""
)
print(output)
