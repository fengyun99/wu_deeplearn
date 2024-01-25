#!/usr/bin/env python
# -*- coding: utf-8 -*-
import copy
import os
from typing import Any, List, Optional

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain_core.documents import Document


class TitleAddRecursiveCharacterTextSplitter(RecursiveCharacterTextSplitter):
    def __init__(self, **kwargs: Any):
        super().__init__(**kwargs)

    def create_documents(
            self, texts: List[str], metadatas: Optional[List[dict]] = None
    ) -> List[Document]:
        """Create documents from a list of texts."""
        _metadatas = metadatas or [{}] * len(texts)
        documents = []
        for i, text in enumerate(texts):
            index = -1
            filename = os.path.basename(_metadatas[i]['source']).split('.')[0]
            for chunk in self.split_text(text):
                metadata = copy.deepcopy(_metadatas[i])
                if self._add_start_index:
                    index = text.find(chunk, index + 1)
                    metadata["start_index"] = index
                new_doc = Document(
                    page_content=(chunk + f"\n来源:{filename}"),
                    metadata=metadata)
                documents.append(new_doc)
        return documents


if __name__ == '__main__':
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

    text_splitter = TitleAddRecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    a = text_splitter.split_documents(docs)
    print(a)
