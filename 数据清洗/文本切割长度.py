#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/8/4 14:07
# @Author   : FengYun
# @File     : 文本切割长度.py
# @Software : PyCharm
def split_text_by_sentence(text, max_length):
    """
    将文本按照句子分割，并在拼接句子时避免超过指定的最大长度，并在分割后的文本段末尾加上句号，
    除了最后一个分割后的文本段，最后一个分割后的文本段不加句号。

    参数:
    text (str): 需要分割的文本
    max_length (int): 每个分割后的字段的最大长度

    返回:
    List[str]: 分割后的文本段列表
    """
    # 用于存储分割后的文本段的列表
    segmented_text = []

    # 分割句子
    sentences = text.split("。")

    # 用于临时存储当前段落
    current_segment = ""

    for i, sentence in enumerate(sentences):
        # 尝试将句子拼接到当前段落
        if len(current_segment) + len(sentence) + 1 <= max_length:  # +1 用于考虑句号的长度
            if current_segment:
                current_segment += "。"  # 拼接句号
            current_segment += sentence
        else:
            if current_segment:
                segmented_text.append(current_segment + "。")  # 在段落末尾添加句号
            current_segment = sentence

    # 处理最后一个段落
    if current_segment:
        if i == len(sentences) - 1:
            segmented_text.append(current_segment)  # 不添加句号
        else:
            segmented_text.append(current_segment + "。")  # 在段落末尾添加句号

    return segmented_text

# 测试例子
text_to_split = "这是一段很长的文本，用于测试拼接句子的算法。第一句。第二句。第三句。" * 50  # 这里假设文本很长
max_length = 786
segments = split_text_by_sentence(text_to_split, max_length)
print(segments[2])

