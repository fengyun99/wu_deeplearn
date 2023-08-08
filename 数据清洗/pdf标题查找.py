#!/usr/bin/env python
# -*- coding: utf-8 -*-
import PyPDF2
import re

'''
问题：无关信息页码读取拼接到程序当中会导致不稳定的提取内容
混乱的表格数据？处理，子标题下内容过长如何程序连续拼接询问?
'''
MAX_LENGTH = 1024


def is_contain_chinese(check_str):
    """
    判断字符串中是否包含中文
    :param check_str: {str} 需要检测的字符串
    :return: {bool} 包含返回True， 不包含返回False
    """
    for ch in check_str:
        if u'\u4e00' <= ch <= u'\u9fff':
            return True
    return False


def is_catalogue(check_str):
    """
    判断字符串中是否包含中文
    :param check_str: {str} 需要检测的字符串
    :return: {bool} 包含返回True， 不包含返回False
    """
    count = 0
    for ch in check_str:
        if ch == '.':
            count += 1
    if count > 30:
        return True
    return False


def remove_numeric_markers(text):
    pattern = r'-\d+-'
    return re.sub(pattern, '', text)


def remove_number_chinese(text):
    pattern = r'^\d第[一二三四五六七八九十][章|条]'
    if re.match(pattern, text):
        remove_pattern = r'^\d'
        return re.sub(remove_pattern, '', text)


# 读取pdf文档
def get_pdf_text(pdf_path, start_page=0, stop_page=None):  # start_page，pdf从第几页开始加载,stop_page，pdf从第几页结束加载
    temp_lines = []
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        # 初始化结束页面为最后一页
        length = len(reader.pages)
        # 判断是否传入结束参数
        if stop_page is not None:
            length = stop_page

        for page_num in range(start_page, length):
            page = reader.pages[page_num]
            text = page.extract_text()
            print(text)
            # 包含多个.的内容是目录跳过
            if text == '':
                continue
            if is_catalogue(text):
                continue

            temp_lines.extend(['' if len(t) < 4 and not is_contain_chinese(t) else remove_numeric_markers(t) for t in
                               text.split('\n')])

    # print(temp_lines)
    pdf_content = '\n'.join(temp_lines)
    return pdf_content


# 正则去除当行数字，去除当前行不带中文的内容，剔除带点的内容，剔除前缀是数字不带汉字？


# 正则表达式用于检查行中是否包含1. 2. 1.1.标识
def is_valid_digital_line(line, use_punctuation=True, limit=True):
    pattern = r'\d+[\.^\d]*'
    if not re.match(pattern, line):
        return False

    # 是否限制长度
    if limit:
        # 检查长度是否小于10个字符
        if len(line) >= 20:
            return False

    # 是否采用标题不含标点风格切割
    if use_punctuation:
        # 检查是否包含标点符号
        if any(char in line for char in ['。', '，', '！', '？', '：', '；', '、']):
            return False

    return True


# 通过1. 1.1. 1.1.1. 格式获取标题
def extract_text_digital_title_line(text: str, use_punctuation=True, limit=True):
    valid_lines = []
    lines = text.split('\n')
    for line in lines:
        if is_valid_digital_line(line.strip(), use_punctuation, limit):
            valid_lines.append(line.strip())
    return [lines, valid_lines]


# 正则表达式用于检查行中是否包含"第一章"、"第一条"等标识
def is_valid_chinese_all_line(line):
    pattern = r'第[一二三四五六七八九十]+(章|条)'

    if not re.match(pattern, line):
        return False
    return True


# 提取出具体的标题，第*条开头
def is_regulations_in_line(text):
    match_list = []
    pattern = r'第[一二三四五六七八九十]+条[（(].+?[)）]'
    matches = re.findall(pattern, text)

    for match in matches:
        match_list.append(match)

    if match_list:
        return match_list


# 提取出所有按第*章|条的内容信息
def extract_text_chinese_title_line(text: str):
    valid_lines = []
    out_list = []
    lines = text.split('\n')
    for line in lines:
        line = line.strip()
        if is_valid_chinese_all_line(line):
            valid_lines.append(line)
        for vline in valid_lines:
            if is_regulations_in_line(vline) is not None:
                out_list.append(is_regulations_in_line(vline)[0])
            else:
                out_list.append(vline)
    return [lines, out_list]


# 标题中含有顿号
def is_comma_title(line):
    pattern = r'[一二三四五六七八九十]|[0-9]+、.+?'

    if not re.match(pattern, line):
        return False

    # 检查长度是否小于10个字符
    if len(line) >= 20:
        return False

    # 检查是否包含标点符号
    if any(char in line for char in ['。', '，', '！', '？', '：', '；']):
        return False

    return True


# 一、1、等类型标题
def extract_text_comma_title(text: str):
    valid_lines = []
    lines = text.split('\n')

    for line in lines:
        line = line.strip()

        if is_comma_title(line):
            valid_lines.append(line)
    return [lines, valid_lines]


# 只包含一、二、类型的句子，非标题类型
def is_chinese_comma_content(line):
    pattern = r'[一二三四五六七八九十]+、.+?'

    if not re.match(pattern, line):
        return False
    return True


def extract_text_chinese_comma_sentence(text: str):
    valid_lines = []
    lines = text.split('\n')

    for line in lines:
        line = line.strip()

        if is_chinese_comma_content(line):
            valid_lines.append(line)

    return [lines, valid_lines]


# 根据标题数组拼接数据
def split_list_by_delimiters(data_list, delimiters, mode):
    sublists = []
    current_sublist = []

    for item in data_list:
        if any(item.startswith(delimiter) for delimiter in delimiters):
            if current_sublist:
                sublists.append(current_sublist)
                current_sublist = []
            # Add a newline character before the delimiter if it exists in data_list
            if mode != "chinese_chapter" and mode != "ch_sentence":
                if item in data_list:
                    item = item + '\n'
        current_sublist.append(item)

    if current_sublist:
        sublists.append(current_sublist)

    # Concatenate sublists with length <= 2 to the next list's beginning
    new_sublists = []
    for i, sublist in enumerate(sublists):
        if i < len(sublists) - 1 and len(sublist) <= 2:
            sublists[i + 1] = sublist + sublists[i + 1]
        else:
            new_sublists.append(sublist)

    return new_sublists


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


#
def result_spilt_data(pdf_file_path, mode, start=0, stop=None, has_attached_table=False, use_punctuation=True,
                      limit=True):
    global valid_lines
    res = []
    # 使用示例：从第二页开始提取内容,提取数字标题
    pdf_content = get_pdf_text(pdf_file_path, start, stop)
    if mode == "digital":
        valid_lines = extract_text_digital_title_line(pdf_content, use_punctuation, limit)
    elif mode == "chinese_chapter":
        valid_lines = extract_text_chinese_title_line(pdf_content)
    elif mode == "ch_num_comma":
        valid_lines = extract_text_comma_title(pdf_content)
    elif mode == "ch_sentence":
        valid_lines = extract_text_chinese_comma_sentence(pdf_content)

    if has_attached_table:
        valid_lines[1].append("附表")
    for data in split_list_by_delimiters(valid_lines[0], valid_lines[1], mode):
        data_res = ''.join(data)
        if len(data_res) > MAX_LENGTH:
            res.extend(split_text_by_sentence(data_res, MAX_LENGTH))
            continue
        res.append(data_res)
    # print(valid_lines[1])
    return res


if __name__ == '__main__':
    get_pdf_text(r'G:\test\满足规则一：JGJT 388-2016 住房公积金信息系统技术规范.pdf')
