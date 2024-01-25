#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Build a sample vectorDB
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import WebBaseLoader, TextLoader
from langchain_community.embeddings import HuggingFaceBgeEmbeddings
from langchain_community.embeddings.huggingface import DEFAULT_QUERY_BGE_INSTRUCTION_ZH
from langchain_community.vectorstores import Chroma
from langchain_core.prompts import PromptTemplate
from langchain_openai import OpenAIEmbeddings
from langchain.retrievers.multi_query import MultiQueryRetriever
from langchain_openai import ChatOpenAI
# Set logging for the queries
import logging
from utils.title_add import TitleAddRecursiveCharacterTextSplitter
# from dotenv import load_dotenv, find_dotenv
# _ = load_dotenv(find_dotenv())
import os
os.environ['OPENAI_BASE_URL'] = 'http://192.168.2.103:8001/v1'
os.environ['OPENAI_API_KEY'] = 'EMPTY'

CHINESE_DEFAULT_QUERY_PROMPT = PromptTemplate(
    input_variables=['query'],
    template="""你是一名中文AI助手。你的任务是根据用户给定的问题生成3个不同版本从向量数据库中检索相关文档的新问题。
    需要对用户的问题进行多视角分析，你的目标是帮助用户解决相似度搜索的限制。最后的答案用中文回答,将生成的问题用换行符分隔开。
    用户给定的最初问题{question}""",
)

# Load blog post
# loader = WebBaseLoader("https://lilianweng.github.io/posts/2023-06-23-agent/")
# data = loader.load()
loaders = [
    TextLoader("../data/2019保定年报.txt", encoding='utf-8'),
    TextLoader("../data/2020保定年报.txt", encoding='utf-8'),
    TextLoader("../data/2015北京年报.txt", encoding='utf-8'),
    TextLoader("../data/2016北京年报.txt", encoding='utf-8'),
    TextLoader("../data/2017北京年报.txt", encoding='utf-8'),
    TextLoader("../data/2018北京年报.txt", encoding='utf-8'),
    TextLoader("../data/2019北京年报.txt", encoding='utf-8'),
    TextLoader("../data/2020北京年报.txt", encoding='utf-8'),
    TextLoader("../data/2021北京年报.txt", encoding='utf-8'),
    TextLoader("../data/2022北京年报.txt", encoding='utf-8')
]
docs = []
for loader in loaders:
    docs.extend(loader.load())

# Split
text_splitter = TitleAddRecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
splits = text_splitter.split_documents(docs)  # 对象列表

# print(splits)

# VectorDB
# embedding = OpenAIEmbeddings()
model_name = "BAAI/bge-large-zh-v1.5"
model_kwargs = {"device": "cuda"}
# 调用cpu来进行运算向量
# model_kwargs = {"device": "cpu"}
encode_kwargs = {"normalize_embeddings": True}
embedding = HuggingFaceBgeEmbeddings(
    model_name=model_name, model_kwargs=model_kwargs, encode_kwargs=encode_kwargs,
    query_instruction=DEFAULT_QUERY_BGE_INSTRUCTION_ZH
)

vectordb = Chroma.from_documents(documents=splits, embedding=embedding)

question = "2019年保定市缴存业务的运行情况?"
llm = ChatOpenAI(temperature=0)

# 将问题多样化后再查询。
retriever_from_llm = MultiQueryRetriever.from_llm(
    retriever=vectordb.as_retriever(), llm=llm, prompt=CHINESE_DEFAULT_QUERY_PROMPT
)

logging.basicConfig()
logging.getLogger("langchain.retrievers.multi_query").setLevel(logging.INFO)

unique_docs = retriever_from_llm.get_relevant_documents(query=question)
print(len(unique_docs))
print(unique_docs)
