#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2024/1/9 10:50
# @Author   : FengYun
# @File     : private_model.py
# @Software : PyCharm
from llama_index import ServiceContext
from llama_index.prompts import PromptTemplate
from llama_index.llms import HuggingFaceLLM

# Example: Using a HuggingFace LLM(使用远端的仓库的模型)

system_prompt = """<|SYSTEM|># StableLM Tuned (Alpha version)
- StableLM is a helpful and harmless open-source AI language model developed by StabilityAI.
- StableLM is excited to be able to help the user, but will refuse to do anything that could be considered harmful to the user.
- StableLM is more than just an information source, StableLM is also able to write poetry, short stories, and make jokes.
- StableLM will refuse to participate in anything that could harm a human.
"""

# This will wrap the default prompts that are internal to llama-index
query_wrapper_prompt = PromptTemplate("<|USER|>{query_str}<|ASSISTANT|>")

llm = HuggingFaceLLM(
    context_window=4096,
    max_new_tokens=256,
    generate_kwargs={"temperature": 0.7, "do_sample": False},
    system_prompt=system_prompt,
    query_wrapper_prompt=query_wrapper_prompt,
    tokenizer_name="StabilityAI/stablelm-tuned-alpha-3b",
    model_name="StabilityAI/stablelm-tuned-alpha-3b",
    device_map="auto",
    stopping_ids=[50278, 50279, 50277, 1, 0],  # <|SYSTEM|>,<|USER|>,<|ASSISTANT|>,<|endoftext|>,<|padding|>就停止
    tokenizer_kwargs={"max_length": 4096},
    # uncomment this if using CUDA to reduce memory usage
    # model_kwargs={"torch_dtype": torch.float16}
)
service_context = ServiceContext.from_defaults(
    chunk_size=1024,
    llm=llm,
)
