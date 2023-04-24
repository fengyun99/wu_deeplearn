#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/4/24 16:45
# @Author   : FengYun
# @File     : fastapi_example.py
# @Software : PyCharm
from typing import Union
from fastapi import FastAPI
from transformers import AutoTokenizer, AutoModel
from argparse import Namespace
import numpy as np
import pandas as pd

app = FastAPI()


@app.get("/input")
def read_root(input_str: str):
    model = "silk-road/luotuo-bert"
    tokenizer = AutoTokenizer.from_pretrained(model)
    model_args = Namespace(do_mlm=None, pooler_type="cls", temp=0.05, mlp_only_train=False, init_embeddings_model=None)
    model = AutoModel.from_pretrained(model, trust_remote_code=True, model_args=model_args)
    inputs = tokenizer(input_str, padding=True, truncation=True, return_tensors="pt", max_length=512)

    embed = np.array(
        model(**inputs, output_hidden_states=True, return_dict=True, sent_emb=True).pooler_output.detach().numpy()[0])
    np.set_printoptions(threshold=np.inf)
    return {input_str: str(embed),"lenght":str(len(embed))}
