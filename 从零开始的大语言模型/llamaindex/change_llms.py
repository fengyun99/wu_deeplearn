#!/usr/bin/env python
# -*- coding: utf-8 -*-
from llama_index import set_global_tokenizer

# tiktoken
import tiktoken

set_global_tokenizer(tiktoken.encoding_for_model("gpt-3.5-turbo").encode)

# huggingface
from transformers import AutoTokenizer

set_global_tokenizer(
    AutoTokenizer.from_pretrained("HuggingFaceH4/zephyr-7b-beta").encode
)
