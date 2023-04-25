#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/4/24 16:45
# @Author   : FengYun
# @File     : fastapi_example.py
# @Software : PyCharm
from fastapi import FastAPI
from pydantic import BaseModel
from transformers import AutoTokenizer, AutoModel
from argparse import Namespace
import numpy as np
import uvicorn
from enum import Enum


# 定义枚举的参数
class Model(Enum):
    LUOTUO_BERT = "silk-road/luotuo-bert"


# 定义请求体的内容
class Param(BaseModel):
    input: str
    # 设置模型
    model: str = Model.LUOTUO_BERT


app = FastAPI()


@app.post("/api/embeddings/")
async def read_root(param: Param):
    # 分词器
    tokenizer = AutoTokenizer.from_pretrained(param.model)  # "/model/ + param.model将所有模型放置位置"
    # 设置参数，调用模型预训练
    model_args = Namespace(do_mlm=None, pooler_type="cls", temp=0.05, mlp_only_train=False, init_embeddings_model=None)
    model = AutoModel.from_pretrained(param.model, trust_remote_code=True, model_args=model_args)
    # 输入文本分词
    inputs = tokenizer(param.input, padding=True, truncation=True, return_tensors="pt", max_length=512)
    # 生成转换后的向量
    embed = np.array(
        model(**inputs, output_hidden_states=True, return_dict=True, sent_emb=True).pooler_output.detach().numpy()[0])
    np.set_printoptions(threshold=np.inf)
    return {"data": [{"content": param.input, "embedding": embed.tolist()}], "model": param.model, "length": str(len(embed))}


if __name__ == '__main__':
    uvicorn.run('fastapi_example:app', reload=True)
