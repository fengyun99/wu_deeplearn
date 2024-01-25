#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2024/1/5 11:50
# @Author   : FengYun
# @File     : starter.py
# @Software : PyCharm
import os.path
from llama_index import (
    VectorStoreIndex,
    SimpleDirectoryReader,
    StorageContext,
    load_index_from_storage,
)
import os

os.environ["OPENAI_API_KEY"] = "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"

# check if storage already exists
PERSIST_DIR = "./storage"
if not os.path.exists(PERSIST_DIR):
    # load the documents and create the index
    documents = SimpleDirectoryReader("data").load_data()
    index = VectorStoreIndex.from_documents(documents)
    # store it for later
    index.storage_context.persist(persist_dir=PERSIST_DIR)
else:
    # load the existing index
    storage_context = StorageContext.from_defaults(persist_dir=PERSIST_DIR)
    index = load_index_from_storage(storage_context)

# either way we can now query the index
query_engine = index.as_query_engine()
response = query_engine.query("What did the author do growing up?")
print(response)
