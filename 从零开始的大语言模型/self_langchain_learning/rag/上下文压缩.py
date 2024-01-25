#!/usr/bin/env python
# -*- coding: utf-8 -*-

from langchain.text_splitter import CharacterTextSplitter, RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import FAISS
# from langchain_community.vectorstores import ElasticsearchStore
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv, find_dotenv
from langchain.retrievers import ContextualCompressionRetriever
from langchain.retrievers.document_compressors import LLMChainExtractor
from langchain_openai import OpenAI
from langchain.retrievers.document_compressors import LLMChainFilter

_ = load_dotenv(find_dotenv())


# Helper function for printing docs


def pretty_print_docs(docs):
    print(
        f"\n{'-' * 100}\n".join(
            [f"Document {i + 1}:\n\n" + d.page_content for i, d in enumerate(docs)]
        )
    )


documents = TextLoader("../data/2019保定年报.txt", encoding='utf-8').load()
text_splitter = CharacterTextSplitter(separator="\n", chunk_size=500, chunk_overlap=0)
# text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=0)
texts = text_splitter.split_documents(documents)
retriever = FAISS.from_documents(texts, OpenAIEmbeddings()).as_retriever()

# docs = retriever.get_relevant_documents(
#     "2019年保定市缴存业务的运行情况?"
# )
llm = OpenAI(temperature=0)

# 慢，额外总结了一次
# compressor = LLMChainExtractor.from_llm(llm)
# compression_retriever = ContextualCompressionRetriever(
#     base_compressor=compressor, base_retriever=retriever
# )

# compressed_docs = compression_retriever.get_relevant_documents(
#     "2019年保定市缴存业务的运行情况?"
# )
# pretty_print_docs(compressed_docs)

# 慢，额外处理了一次
# _filter = LLMChainFilter.from_llm(llm)
# compression_retriever = ContextualCompressionRetriever(
#     base_compressor=_filter, base_retriever=retriever
# )
#
# compressed_docs = compression_retriever.get_relevant_documents(
#     "2019年保定市缴存业务的运行情况?"
# )
# pretty_print_docs(compressed_docs)

from langchain.retrievers.document_compressors import EmbeddingsFilter
from langchain_openai import OpenAIEmbeddings

embeddings = OpenAIEmbeddings()
embeddings_filter = EmbeddingsFilter(embeddings=embeddings, similarity_threshold=0.76)
compression_retriever = ContextualCompressionRetriever(
    base_compressor=embeddings_filter, base_retriever=retriever
)

compressed_docs = compression_retriever.get_relevant_documents(
    "2019年保定市缴存业务的运行情况?"
)
pretty_print_docs(compressed_docs)

