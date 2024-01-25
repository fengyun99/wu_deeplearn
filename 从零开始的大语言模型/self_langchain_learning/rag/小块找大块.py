#!/usr/bin/env python
# -*- coding: utf-8 -*-
from langchain.retrievers import ParentDocumentRetriever
from langchain.storage import InMemoryStore
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain_community.embeddings.huggingface import DEFAULT_QUERY_BGE_INSTRUCTION_ZH
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_community.embeddings import HuggingFaceBgeEmbeddings
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())

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

print(docs)
model_name = "BAAI/bge-large-zh-v1.5"
model_kwargs = {"device": "cuda"}
# 调用cpu来进行运算向量
# model_kwargs = {"device": "cpu"}
encode_kwargs = {"normalize_embeddings": True}
hf = HuggingFaceBgeEmbeddings(
    model_name=model_name, model_kwargs=model_kwargs, encode_kwargs=encode_kwargs,
    query_instruction=DEFAULT_QUERY_BGE_INSTRUCTION_ZH
)

# This text splitter is used to create the parent documents
parent_splitter = RecursiveCharacterTextSplitter(chunk_size=1000)
# This text splitter is used to create the child documents
# It should create documents smaller than the parent
child_splitter = RecursiveCharacterTextSplitter(chunk_size=300)
# The vectorstore to use to index the child chunks
vectorstore = Chroma(
    collection_name="parents", embedding_function=hf
)
# The storage layer for the parent documents
store = InMemoryStore()

retriever = ParentDocumentRetriever(
    vectorstore=vectorstore,
    docstore=store,
    child_splitter=child_splitter,
    parent_splitter=parent_splitter,  # 返回原来全部文档，不需要此字段
)

retriever.add_documents(docs)

if __name__ == '__main__':
    # 只能扩充信息，不能够精确信息内容。
    import time
    start = time.time()
    sub_docs = vectorstore.similarity_search("2018年新开户单位")
    print(sub_docs[0].page_content)  # 2019年北京
    # print('*' * 20)
    # print(sub_docs[1].page_content)  # 无关信息
    # print('*' * 20)
    # print(sub_docs[2].page_content)  # 2019年北京第二段
    # print('*' * 20)
    # print(sub_docs[3].page_content)  # 2019年保定
    print('===========================')
    retrieved_docs = retriever.get_relevant_documents("2018年新开户单位")
    print(retrieved_docs[0].page_content)
    # print('*' * 20)
    # print(retrieved_docs[1].page_content)
    # print('*' * 20)
    # print(retrieved_docs[2].page_content)
    # print('*' * 20)
    # print(retrieved_docs[3].page_content)
    print(time.time() - start)
