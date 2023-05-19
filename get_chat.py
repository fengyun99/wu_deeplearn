#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/5/8 15:16
# @Author   : FengYun
# @File     : get_chat.py
# @Software : PyCharm
from fastapi import FastAPI
from pydantic import BaseModel
from argparse import Namespace
import numpy as np
from transformers import AutoTokenizer, AutoModel
import uvicorn
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


# 定义向量请求体的内容
class Embed_Param(BaseModel):
    # 输入的文本
    input: str
    # 设置模型
    model: str = "silk-road/luotuo-bert"


# 定义对话请求体的内容
class Chat_Param(BaseModel):
    # 输入检索的文本内容
    text: str
    # 输入对应的问题
    question: str
    # 预设
    preset: str = r'''根据下面文本和问题，归纳总结出答案，答案用一两句话展示，只归纳总结文本中提到的内容，不要修改文本的内容，不要添加额外的内容。\n\n文本：\n'''
    # 历史上文
    history: list = []
    # 最长token
    max_length: int = 2048
    # top_p
    top_p: int = 0.7
    # temperature
    temperature: int = 0.95


app = FastAPI()


# 向量接口入口
@app.post("/api/embeddings/")
async def text2embedding(param: Embed_Param):
    # 模型
    use_model = "/home/ubuntu/model/" + param.model.split("/")[-1]
    print(use_model)
    # 分词器
    tokenizer = AutoTokenizer.from_pretrained(use_model)
    # 设置参数，调用模型预训练
    model_args = Namespace(do_mlm=None, pooler_type="cls", temp=0.05, mlp_only_train=False, init_embeddings_model=None)
    model = AutoModel.from_pretrained(use_model, trust_remote_code=True, model_args=model_args)
    # 输入文本分词
    inputs = tokenizer(param.input, padding=True, truncation=True, return_tensors="pt", max_length=512)
    # 生成转换后的向量
    embed = np.array(
        model(**inputs, output_hidden_states=True, return_dict=True, sent_emb=True).pooler_output.detach().numpy()[0])
    np.set_printoptions(threshold=np.inf)
    result = {"data": [{"content": param.input, "embedding": embed.tolist()}], "model": param.model,
              "length": str(len(embed))}
    return result


# 模型调用接口入口
@app.post("/api/chat")
async def glm_chat(param: Chat_Param):
    # 启动ui界面情况下，获取返回的结果
    glm_api = "http://192.168.2.103:6006"
    data = param.preset + param.text + r"\n\n问题：\n" + param.question
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    web = Chrome(options=options)
    web.get(glm_api)
    web.find_element(By.XPATH, r'//*[@id="component-6"]/label/textarea').send_keys(data, Keys.ENTER)
    web.find_element(By.XPATH, r'//*[@id="component-9"]').click()
    time.sleep(10)
    msg = web.find_element(By.XPATH, r'//*[@id="component-2"]/div[2]/div/div[2]').text
    web.close()
    result = {"input": [{"question": param.question, "text": param.text}], "response": msg}
    return result



if __name__ == '__main__':
    uvicorn.run('get_chat:app', host="0.0.0.0", port=8000, reload=True)
