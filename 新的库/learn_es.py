#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List

from elasticsearch import Elasticsearch as ES
import warnings

warnings.filterwarnings("ignore")

es = ES(hosts='http://127.0.0.1:9000')


def create_index(file_name):
    index_name = f'data_{file_name}'
    # 创建索引
    request_body = {
        'mappings': {
            'properties': {
                'name': {
                    'type': 'text'
                },
                'index': {
                    'type': 'integer'
                },
                'message': {
                    'type': 'text'
                },
            }
        }
    }
    es.indices.create(index=index_name, body=request_body, ignore=400)


def insert_data(file_name, data: List[dict]):
    index_name = f'data_{file_name}'
    # 插入数据
    for line in data:
        es.index(index=index_name, id=line['index'], body=line)


def query_all_data():
    index_name = 'data_*'
    # 想查询全部数据即可修改上述查询语句为：
    query = {"query": {"match_all": {}}}
    response = es.search(index=index_name, body=query)
    return response


def query_data(words_list: list, top_k: int, score: float = 0.0):  # words_list: nlp分词后列表
    index_name = f'data_*'
    query_list = []
    for value in words_list:
        query_list.append({"match_phrase": {"message": value}})
    # 想查询全部数据即可修改上述查询语句为：
    query = {"query": {"bool": {"should": query_list}}}
    response = es.search(index=index_name, body=query)['hits']['hits']
    return [i for i in response[:top_k] if i['_score'] > score]


def delete_index(file_name):
    # 删除索引
    index_name = f'data_{file_name}'
    es.indices.delete(index=index_name)
    return {"msg": "delete success", "status": 200}


# 函数已废弃
def delete_file_name(index_name, name):
    es.delete_by_query(index=index_name, body={"query": {"match": {"name": name}}})


# if __name__ == '__main__':
    # data01 = [{"name": "t.docx", "index": 1, "message": "正文内容01"},
    #           {"name": "t.docx", "index": 2, "message": "正文内容02"}]
    # data02 = [{"name": "a.docx", "index": 1, "message": "文章的内容01"},
    #           {"name": "a.docx", "index": 2, "message": "文章的内容02"},
    #           {"name": "a.docx", "index": 3, "message": "文章的内容03"}]
    # filename1 = data01[0]['name']
    # index_name1 = f'{filename1}'
    # create_index(index_name1)
    # insert_data(index_name1, data01)
    # filename2 = data02[0]['name']
    # index_name2 = f'{filename2}'
    # insert_data(index_name2, data02)
    # print(query_all_data())
    # print('------------------------------------------')
    # print(query_data(["正文", "01"], 1000, 0.1))