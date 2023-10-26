#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/8/30 13:36
# @Author   : FengYun
# @File     : list2tree.py
# @Software : PyCharm
"""
列表转树函数
关键字：id、parent_id、children
"""


def list2tree(data: list) -> list:
    # 转成ID为Key的字典
    mapping: dict = dict(zip([i['id'] for i in data], data))

    # 树容器
    container: list = []

    for d in data:
        # 如果找不到父级项，则是根节点
        parent: dict = mapping.get(d['parent_id'])
        if parent is None:
            container.append(d)
        else:
            children: list = parent.get('children')
            if not children:
                children = []
            children.append(d)
            parent.update({'children': children})
    return container


if __name__ == '__main__':
    data: list = [
        {'id': 1, 'parent_id': 0, 'name': '用户管理', 'url': 'https://www.baidu.com'},
        {'id': 2, 'parent_id': 0, 'name': '菜单管理', 'url': 'https://www.baidu.com'},
        {'id': 3, 'parent_id': 1, 'name': '新增用户', 'url': 'https://www.baidu.com'},
        {'id': 4, 'parent_id': 1, 'name': '删除用户', 'url': 'https://www.baidu.com'},
        {'id': 5, 'parent_id': 2, 'name': '新增菜单', 'url': 'https://www.baidu.com'},
        {'id': 6, 'parent_id': 2, 'name': '删除菜单', 'url': 'https://www.baidu.com'},
    ]

    # 打印验证一下
    for i in list2tree(data):
        print(i)