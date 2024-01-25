#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2024/1/9 11:41
# @Author   : FengYun
# @File     : use.py
# @Software : PyCharm
import os

os.environ["CUDA_VISIBLE_DEVICES"] = "0"
from llama_index import VectorStoreIndex, SimpleDirectoryReader
from llama_index import ServiceContext
from llama_index import LLMPredictor
import torch
from llama_index.llms import HuggingFaceLLM
from llama_index.prompts.prompts import SimpleInputPrompt
import torch
from transformers import pipeline
from typing import Optional, List, Mapping, Any

from llama_index import ServiceContext, SimpleDirectoryReader, SummaryIndex
from llama_index.callbacks import CallbackManager
from llama_index.llms import (
    CustomLLM,
    CompletionResponse,
    CompletionResponseGen,
    LLMMetadata,
)
from llama_index.llms.base import llm_completion_callback
from transformers import AutoModelForCausalLM, AutoTokenizer
from transformers.generation import GenerationConfig

# set context window size
context_window = 2048
# set number of output tokens
num_output = 256

# store the pipeline/model outside of the LLM class to avoid memory issues
model_name = "qwen7bchat"

tokenizer = AutoTokenizer.from_pretrained(f"Qwen-7B-Chat", trust_remote_code=True)
# model = AutoModel.from_pretrained("Qwen-7B-Chat", trust_remote_code=True, device='cuda')
model = AutoModelForCausalLM.from_pretrained(f"Qwen-7B-Chat", device_map="auto", trust_remote_code=True,
                                             bf16=True).eval()

# model = model.eval()
model.generation_config = GenerationConfig.from_pretrained(f"Qwen-7B-Chat", trust_remote_code=True)


class OurLLM(CustomLLM):
    @property
    def metadata(self) -> LLMMetadata:
        """Get LLM metadata."""
        return LLMMetadata(
            context_window=context_window,
            num_output=num_output,
            model_name=model_name,
        )

    @llm_completion_callback()
    def complete(self, prompt: str, **kwargs: Any) -> CompletionResponse:
        prompt_length = len(prompt)

        # only return newly generated tokens
        text, _ = model.chat(tokenizer, prompt, history=[])
        return CompletionResponse(text=text)

    @llm_completion_callback()
    def stream_complete(
            self, prompt: str, **kwargs: Any
    ) -> CompletionResponseGen:
        raise NotImplementedError()


def main():
    llm = OurLLM()
    service_context = ServiceContext.from_defaults(llm=llm, embed_model="local:m3e-base")

    documents = SimpleDirectoryReader("./data").load_data()

    index = VectorStoreIndex.from_documents(documents, service_context=service_context)

    query_engine = index.as_query_engine()
    response = query_engine.query("请问是什么")
    print(response)


if __name__ == "__main__":
    main()