#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2023/7/3 17:33
# @Author   : FengYun
# @File     : run_md_read.py
# @Software : PyCharm
from util.dataset_processing_md import *
output_dict1 = output_data_dict("data/original_file/docs/ejx4core/guide/core.md")
file_store(output_dict1, "out.txt")
output_dict2 = output_data_dict("data/original_file/docs/ejx4core/guide/iohttp.md")
file_store(output_dict2, "out.txt")
output_dict3 = output_data_dict("data/original_file/docs/ejx4core/guide/ioscene.md")
file_store(output_dict3, "out.txt")
output_dict4 = output_data_dict("data/original_file/docs/ejx4core/guide/queue.md")
file_store(output_dict4, "out.txt")
output_dict5 = output_data_dict("data/original_file/docs/ejx4core/guide/route.md")
file_store(output_dict5, "out.txt")
output_dict6 = output_data_dict("data/original_file/docs/ejx4core/guide/uibackend.md")
file_store(output_dict6, "out.txt")
output_dict7 = output_data_dict("data/original_file/docs/ejx4core/guide/uidesign.md")
file_store(output_dict7, "out.txt")
output_dict8 = output_data_dict("data/original_file/docs/ejx4core/guide/uifeature.md")
file_store(output_dict8, "out.txt")
output_dict9 = output_data_dict("data/original_file/docs/ejx4core/guide/uiprocess.md")
file_store(output_dict9, "out.txt")
output_dict10 = output_data_dict("data/original_file/docs/ejx4core/guide/vmqueue.md")
file_store(output_dict10, "out.txt")