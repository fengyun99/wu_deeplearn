#!/usr/bin/env python
# -*- coding: utf-8 -*-
import copy
import os
import re
from typing import Optional, List, Any, overload

from langchain.text_splitter import TextSplitter, _split_text_with_regex
from langchain_community.document_loaders import TextLoader
from abc import ABC, abstractmethod
from typing import Iterable
from langchain_core.documents import Document

# 抽象类继承抽象类
class TextTitleSplitter(TextSplitter, ABC):
    def __init__(self, **kwargs: Any):
        super().__init__(**kwargs)

    @abstractmethod
    def split_text(self, text: str, filename: str = None) -> List[str]:
        """Split text into multiple components."""

    def create_documents(
            self, texts: List[str], metadatas: Optional[List[dict]] = None
    ) -> List[Document]:
        """Create documents from a list of texts."""
        _metadatas = metadatas or [{}] * len(texts)
        documents = []
        for i, text in enumerate(texts):
            index = -1
            source: str = os.path.basename(_metadatas[i]['source'])
            filename = source.split('.')[0]
            for chunk in self.split_text(text, filename):
                metadata = copy.deepcopy(_metadatas[i])
                if self._add_start_index:
                    index = text.find(chunk, index + 1)
                    metadata["start_index"] = index
                new_doc = Document(page_content=chunk, metadata=metadata)
                documents.append(new_doc)
        return documents

# 有问题
class RecursiveCharacterTitleTextSplitter(TextTitleSplitter):
    """Splitting text by recursively look at characters.
    And add a title to the chunks
    Recursively tries to split by different characters to find one
    that works.
    """

    def __init__(
            self,
            separators: Optional[List[str]] = None,
            keep_separator: bool = True,
            is_separator_regex: bool = False,
            **kwargs: Any,
    ) -> None:
        """Create a new TextSplitter.
        Args:
            separators(分隔符): A list of common separator
            keep_separator(保留分隔符): Whether to keep the separator in the chunks
            is_separator_regex(分隔符是否为正则表达式): Separator is or not regex
        """
        super().__init__(keep_separator=keep_separator, **kwargs)
        self._separators = separators or ["\n\n", "\n", " ", ""]
        self._is_separator_regex = is_separator_regex

    def _split_text(self, text: str, filename: str, separators: List[str]) -> List[str]:
        """Split incoming text and return chunks."""
        final_chunks = []
        # Get appropriate separator to use
        separator = separators[-1]
        new_separators = []
        for i, _s in enumerate(separators):
            # re.escape()用于转义正则中的特殊字符，使其能够被当作普通字符进行匹配
            _separator = _s if self._is_separator_regex else re.escape(_s)
            if _s == "":
                separator = _s
                break
            if re.search(_separator, text):  # if you find separator in text is true
                separator = _s
                new_separators = separators[i + 1:]
                break

        _separator = separator if self._is_separator_regex else re.escape(separator)
        # \n\n或者\n或者" "(前面按照分隔符分割) 或者最后为""(按照字分割)
        splits = _split_text_with_regex(text, _separator, self._keep_separator)

        # Now go merging things, recursively splitting longer texts. 现在开始合并，递归地拆分较长的文本。
        _good_splits = []
        _separator = "" if self._keep_separator else separator
        for s in splits:
            if self._length_function(s) < self._chunk_size:
                _good_splits.append(s)  # 如果小于chunk_size，则直接加入_good_splits
            else:
                if _good_splits:  # 如果_good_splits不为空，则合并_good_splits
                    _good_splits.append(f'\n来源:{filename}')
                    merged_text = self._merge_splits(_good_splits, _separator)
                    final_chunks.extend(merged_text)
                    _good_splits = []
                if not new_separators:  # 分隔符全部取出后，说明没有新的分隔符，将剩下文本直接加入final_chunks
                    final_chunks.append(s + f'\n来源:{filename}')
                else:
                    other_info = self._split_text(s, filename, new_separators)  # 递归分割
                    final_chunks.extend(other_info)
        if _good_splits:
            _good_splits.append(f'\n来源:{filename}')
            merged_text = self._merge_splits(_good_splits, _separator)
            final_chunks.extend(merged_text)
        return final_chunks

    def split_text(self, text: str, filename: str = None) -> List[str]:
        return self._split_text(text, filename, self._separators)
