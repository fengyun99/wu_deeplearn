#!/usr/bin/env python
# -*- coding: utf-8 -*-
# torch的学习
import torch
from torch.utils.data import Dataset


# 继承data加载数据
class MyDataSet(Dataset):
    def __init__(self, examples):
        self.examples = examples

    def __len__(self):
        return len(self.examples)  # 返回数据集长度

    def __getitem__(self, index):
        example = self.examples[index]
        s1 = example[0]  # 当前数据中的第一个句子
        s2 = example[1]  # 当前数据中的第二个句子
        l1 = len(s1)  # 第一个句子的长度
        l2 = len(s2)  # 第二个句子的长度
        return s1, l1, s2, l2, index


if __name__ == '__main__':
    train_set = '这是一句话'
    batch_size = 2
    data_workers = 2
    train_dataset = MyDataSet(train_set)

    train_data_loader = torch.utils.data.DataLoader(
        train_dataset,
        batch_size=batch_size,
        shuffle=True,  # 是否打乱顺序
        num_workers=data_workers,  # 工作进程数
        # collate_fn=the_collate_fn,
    )
