#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/8/8 17:08
# @Author   : FengYun
# @File     : excel2xml.py
# @Software : PyCharm
import openpyxl
import xml.etree.ElementTree as ET


def load_excel(excel_file_path, sheet_name):
    _list = []
    # 打开工作簿
    workbook = openpyxl.load_workbook(excel_file_path)

    # 选择工作表
    sheet = workbook[sheet_name]

    # 遍历工作表的每一行
    for row in sheet.iter_rows(values_only=True):
        _list.append(row)

    return _list


def data_set(data_list, data_type):
    if data_type == 'dict':
        dict_data = {}
        for data in data_list:
            dict_data[str(data[0])] = list(data[1:]) if len(data[1:]) != 1 else str(data[1])
        return dict_data
    elif data_type == 'list':
        list_data = []
        for data in data_list:
            list_data.append(list(data))
        return list_data


def data2excel(data, element_name, comment,output_name):
    # 创建根元素
    root = ET.Element("root")

    # 创建子元素
    element1 = ET.SubElement(root, element_name)
    text = f'\n<!--\n\t{comment}\n-->\n'
    if isinstance(data,dict):
        text += '{\n'
        for k,v in data.items():
            text += f'\t"{k}" : "{v}"\n'
        text += '}\n'
        element1.text = text
    elif isinstance(data,list):
        text += '[\n'
        for i in data:
            text += f'{str(i)}\n'
        text += ']\n'
        element1.text = text

    # 创建XML树
    tree = ET.ElementTree(root)

    # 将XML保存到文件
    xml_file_path = output_name
    tree.write(xml_file_path, encoding="UTF-8", xml_declaration=True)

    # # 使用minidom对XML进行格式化
    # dom = minidom.parse(xml_file_path)
    # with open(xml_file_path, "w", encoding="utf-8") as f:
    #     # 添加XML声明
    #     f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    #     f.write(dom.toprettyxml(indent=""))


if __name__ == '__main__':
    # 读取Excel文件
    excel_file_path = '../12/numbers.xlsx'  # 替换为您的Excel文件路径
    sheet_name = 'Sheet'  # 替换为您要读取的工作表名称
    data_type = 'list'
    data_list = load_excel(excel_file_path, sheet_name)
    res = data_set(data_list, data_type)
    data2excel(res, 'numbers', '数字信息',"numbers.xml")
